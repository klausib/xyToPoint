# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui, QtXml
from qgis.gui import *
from qgis.core import *
from qgis.analysis import *


import resources, math, copy, string, os

from mainWindow import *




class xyToPoint( QtGui.QWidget): # Inherits QWidget to install an Event filter
    def __init__(self,iface):

        QtGui.QWidget.__init__(self)

        #----------------------------------------------------------------------
        #instance variables

        #Reference to the QGIS Interface
        self.iface = iface
        self.mc = self.iface.mapCanvas()    #Map Canvas variable
        self.layer = QgsVectorLayer()

##        self.maptool = QgsMapTool(self.mc)     #force a variable type
##        self.grafArea = QgsDistanceArea()
##        self.DialogDock = QtGui.QDockWidget()
        self.Dialog = QtGui.QDialog()
        self.Dialog = None
##        self.cpoint = QgsPoint()
##        self.cpoint_list = []

        self.layerliste=[]

        #-----------------------------------------------------------------------

    ##############################################
    #initialize the connection with the QGIS GUI
    ##############################################
    def initGui(self):

        # action for starting the plugin
        self.xyToPoint = QtGui.QAction( QtGui.QIcon(":/plugins/xyToPoint/xyToPoint.png"),  QtCore.QCoreApplication.translate("xyToPointMain", "Create Point Layer from XY Attribute Values"),  self.iface.mainWindow() )
        QtCore.QObject.connect(self.xyToPoint, QtCore.SIGNAL("triggered()"), self.showMainWindow)

        # toolbar button and menue item
        self.iface.addToolBarIcon( self.xyToPoint )
        self.iface.addPluginToVectorMenu(QtCore.QCoreApplication.translate("xyToPointMain",  "Create Point Layer from XY Attribute Values"),  self.xyToPoint)

        # connect project read/write signals to class methods (XML read/write) of the plugin
        QtCore.QObject.connect(QgsProject.instance(),  QtCore.SIGNAL("readProject(const QDomDocument&)"),  self.readXML)
        QtCore.QObject.connect(QgsProject.instance(),  QtCore.SIGNAL("writeProject(QDomDocument&)"),  self.writeXML)
        #----------------------------------------------------------------------


    #############################################
    #start the Plugin
    #############################################
    def showMainWindow(self):


        # GUI object
        self.Dialog = xyToPointDialog(self.iface.mainWindow())

        self.akt_layer()
        self.Dialog.show()

        # Event Filtering for the Plugin Window
        self.Dialog.installEventFilter(self)

        # Connect Buttons and Combo Boxes to methods
        QtCore.QObject.connect(self.Dialog.cmbLayer, QtCore.SIGNAL("currentIndexChanged (int)"), self.akt_attr)
        QtCore.QObject.connect(self.Dialog.btnRun, QtCore.SIGNAL("clicked()"), self.create_layer)
        QtCore.QObject.connect(self.Dialog.btnRefresh, QtCore.SIGNAL("clicked()"), self.trigger_update)

        # Initialize the Combo Box with Field Names of the first Layer in the QGIS Legend
        self.akt_attr(self.Dialog.cmbLayer.currentIndex())


        # emits a layer add event
        QtCore.QObject.connect( QgsMapLayerRegistry.instance(), QtCore.SIGNAL("layersAdded (QList< QgsMapLayer * > )"), self.add_layer)
        # emits a layer remove event
        QtCore.QObject.connect( QgsMapLayerRegistry.instance(), QtCore.SIGNAL("layersRemoved (QStringList )"), self.akt_layer)

        self.Dialog.progressBar.setRange(0,1)   # kind of initialization to prevent oscillation of the bar

    #########################################
    #Add loaded Layers to the Combo Box
    #########################################
    def akt_layer(self, layer = None):

        leginterface = self.iface.legendInterface()


        self.Dialog.cmbLayer.clear()
        for lyr_tmp in leginterface.layers():
            self.Dialog.cmbLayer.addItem(lyr_tmp.name(),lyr_tmp)    #Layername and Ref. to the Layerobject are added together

    ###################################################################
    #Add new loaded Layers to the Combo Box while the Plugin is active
    ###################################################################
    def add_layer(self, lyr_list):


        for lyr in lyr_list:
            self.Dialog.cmbLayer.addItem(lyr.name(),lyr)    #Layername and Ref. to the Layerobject are added together


    ######################################################
    #Add X and Y Column Names to the X/Y Field Combo Boxes
    ######################################################
    def akt_attr(self,iti):

        self.Dialog.cmbX.clear()
        self.Dialog.cmbY.clear()

        # if none, return: This happens, when a layer is removed from the legend
        # no good but an easy way to prevent an error..
        if  self.Dialog.cmbLayer.itemData(iti) is None:
            return

        lyr_prov = self.Dialog.cmbLayer.itemData(iti).dataProvider()
        for field in lyr_prov.fields():
            self.Dialog.cmbX.addItem(field.name())
            self.Dialog.cmbY.addItem(field.name())

        # Optional Layername
        self.Dialog.txtName.setText(self.Dialog.cmbLayer.itemText(self.Dialog.cmbLayer.currentIndex()) + '_pt')


    ##########################
    # deactivating the plugin
    ##########################
    def unload(self):


        QtCore.QObject.disconnect(QgsProject.instance(),  QtCore.SIGNAL("readProject(const QDomDocument&)"),  self.readXML)
        QtCore.QObject.disconnect(QgsProject.instance(),  QtCore.SIGNAL("writeProject(QDomDocument&)"),  self.writeXML)

        #first delete the Widget Object
        #self.Dialog = None

        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&xyToPoint", self.xyToPoint)
        self.iface.removeToolBarIcon(self.xyToPoint)



    ##############################################################
    # Event filter for the Plugin GUI. We only catch the Close Event
    ##############################################################
    def eventFilter(self,affe,event):

        if not event == None:

            if event.type() == QtCore.QEvent.Close: # close event

                 # disconnect everything
                QtCore.QObject.disconnect(self.Dialog.cmbLayer, QtCore.SIGNAL("currentIndexChanged (int)"), self.akt_attr)
                QtCore.QObject.disconnect(self.Dialog.btnRun, QtCore.SIGNAL("clicked()"), self.create_layer)
                QtCore.QObject.disconnect(self.Dialog.btnRefresh, QtCore.SIGNAL("clicked()"), self.trigger_update)
                #QtCore.QObject.disconnect(QgsProject.instance(),  QtCore.SIGNAL("readProject(const QDomDocument&)"),  self.readXML)
                #QtCore.QObject.disconnect(QgsProject.instance(),  QtCore.SIGNAL("writeProject(QDomDocument&)"),  self.writeXML)
                QtCore.QObject.disconnect( QgsMapLayerRegistry.instance(), QtCore.SIGNAL("layersAdded (QList< QgsMapLayer * > )"), self.add_layer)


                #clear up
                #self.Dialog.removeEventFilter(self)
                #self.Dialog = None  # delete
                return True
            else:   # everything else
                return False


    #################################################################################
    # read the "join Information" (Table - Point Layer) out of the xyToPoints XML
    # and start recalculateing the point memory layers (described by the XML content)
    # this method is a slot which is executed, whenever an QGIS Project File is read
    #################################################################################
    def readXML(self, domnode = None):

        currentProjectPath = QgsProject.instance().fileName()
        d = QtXml.QDomDocument()


        #try to load the matching xyToPoint XML
        try:
            file = open((currentProjectPath).replace('.qgs','') + "_xyToPoint.xml","r")
            xml = file.read()

            d.setContent(xml)   # d contains the whole XML
            file.close()
            Flagge = True

        except IOError: # if nothing found
            return  # do nothing!!


        #evaluate the XML
        #and load the contained information
        join = d.elementsByTagName("join")

        i = 0
        #QtGui.QMessageBox.critical(None, "Neu geordnet !!",str(range(join.length())))


        di_cl = False   # update is called interactively
        if self.Dialog is None:
            # update ist called by loading a QGIS Project
            self.showMainWindow()   # to show the progress bar!
            di_cl = True

        for i in range(join.length()):

            quell_id = join.item(i).namedItem("QuelllayerID").firstChild().toText().data()
            quell_name = join.item(i).namedItem("QuelllayerName").firstChild().toText().data()
            ziel_id = join.item(i).namedItem("ZiellayerID").firstChild().toText().data()
            ziel_name = join.item(i).namedItem("ZiellayerName").firstChild().toText().data()
            feldx = join.item(i).namedItem("FeldX").firstChild().toText().data()
            feldy = join.item(i).namedItem("FeldY").firstChild().toText().data()


            # verify the variables
            if not (quell_id == None or quell_name == None or ziel_id == None or ziel_name == None or feldx == None or feldy == None):

                # call the layer update methode
                self.update_layer(quell_id, quell_name,ziel_id, ziel_name, feldx, feldy)

                # reinitialize the layerlist
                lyr = memlyr()
                lyr.id_memlyr = ziel_id
                lyr.name_memlyr = ziel_name
                lyr.id_quelllyr = quell_id
                lyr.name_quelllyr = quell_name
                lyr.x_spalte = feldx
                lyr.y_spalte = feldy
                self.layerliste.append(lyr)

        self.iface.mapCanvas().refresh()


        if di_cl:
            # update ist called by loading a QGIS Project
            self.Dialog.close()



    ##################################################################################
    # write the "join Information" (Table - Point Layer) into the the xyToPoints XML
    # this method is a slot which is executed, whenever an QGIS Project File is saved
    ##################################################################################
    def writeXML(self, domnode = None):

        name = QgsProject.instance().fileName().replace('.qgs','') + "_xyToPoint.xml"
        d = QtXml.QDomDocument("xyToPoints")
        root = d.createElement("joins")
        d.appendChild(root)


        # create the XML content
        for k in self.layerliste:

            el = d.createElement("join")
            root.appendChild(el)

            tag = d.createElement("QuelllayerID")
            t = d.createTextNode(k.id_quelllyr)
            tag.appendChild(t)
            el.appendChild(tag)

            tag = d.createElement("QuelllayerName")
            t = d.createTextNode(k.name_quelllyr)
            tag.appendChild(t)
            el.appendChild(tag)

            tag = d.createElement("ZiellayerID")
            t = d.createTextNode(k.id_memlyr)
            tag.appendChild(t)
            el.appendChild(tag)

            tag = d.createElement("ZiellayerName")
            t = d.createTextNode(k.name_memlyr)
            tag.appendChild(t)
            el.appendChild(tag)

            tag = d.createElement("FeldX")
            t = d.createTextNode(k.x_spalte)
            tag.appendChild(t)
            el.appendChild(tag)

            tag = d.createElement("FeldY")
            t = d.createTextNode(k.y_spalte)
            tag.appendChild(t)
            el.appendChild(tag)




        # write the XML content into
        # the xyToPoint XML File
        ret = QtGui.QMessageBox.Yes
        if os.path.exists(name):
            ret = QtGui.QMessageBox.critical(None, "Hint", QtCore.QCoreApplication.translate("xyToPointMain","A xyToPoint XML already exists. Overwirte it?"),QtGui.QMessageBox.Yes | QtGui.QMessageBox.Cancel)

        if ret == QtGui.QMessageBox.Yes:
            try:
                file = open(name,"w")
                #raus = d.toString()
                raus = d.toByteArray()  # äöü
                file.write(raus)
                file.close()
            except IOError: #fail
                QtGui.QMessageBox.critical(None, "Error", QtCore.QCoreApplication.translate("xyToPointMain", "Unable to save the xyToPoint XML ") + currentProjectPath + QtCore.QCoreApplication.translate("xyToPointMain"," onto disk!"))




    ###############################################################################
    # create a point memory layer. calculate the coordinates according to the data
    # of the x and y fields of the source table
    ###############################################################################
    def create_layer(self,tabellenname = None,abfrage_where = None,Gemeindetext = ""):


        # the source table (layer) - a reference to the itemdata Attribute of the cmbLayer Combobox
        in_lyr = self.Dialog.cmbLayer.itemData(self.Dialog.cmbLayer.currentIndex())


        # fetch the layer name written to the text edit widget
        layername = self.Dialog.txtName.text()
        if layername == '':
            # if none, set the name
            layername = self.Dialog.cmbLayer.itemText(self.Dialog.cmbLayer.currentIndex()) + '_pt'

        # new memory layer
        yes = False
        geomType = 'Point' + '?crs=proj4:' + QgsProject.instance().readEntry("SpatialRefSys","/ProjectCRSProj4String")[0]
        epLayer = QgsVectorLayer(geomType, string.strip(layername), 'memory')
        QgsMapLayerRegistry.instance().addMapLayer(epLayer)


        # Add the fields of the source table
        feld = []
        feldnamen = self.Dialog.cmbLayer.itemData(self.Dialog.cmbLayer.currentIndex()).dataProvider().fields()    # the source field map

        epProvider = epLayer.dataProvider() # to add fields use the data provider object
        # create the field list
        for depp in range(feldnamen.count()):
            feld.append(feldnamen.at(depp)) # remember, feldnamen is a map type
        # and add it
        epProvider.addAttributes(feld)


        # start edit session
        epLayer.startEditing()


        # a progress bar is usefull...
        i = 0
        self.Dialog.progressBar.setRange(0,in_lyr.featureCount()-1)

        x_spalte = self.Dialog.cmbX.itemText(self.Dialog.cmbX.currentIndex())
        y_spalte = self.Dialog.cmbY.itemText(self.Dialog.cmbY.currentIndex())

        # QGIS Objects - necessery to create the point features
        ep_point = QgsPoint()
        ep_geom = QgsGeometry()
        ep_feature = QgsFeature()

        # loop through the source table
        for line in in_lyr.getFeatures():

            # short check if the fields contain numerical values
            try:
                # point geometry
                ep_point.setX(float(line.attribute(x_spalte)))
                ep_point.setY(float(line.attribute(y_spalte)))
            except:
                QtGui.QMessageBox.critical(None, 'Error',QtCore.QCoreApplication.translate("xyToPointMain", 'Please choose numerical Columns!'))
                QgsMapLayerRegistry.instance().removeMapLayer(epLayer.id())
                return
            # set feature geometry
            ep_feature.setGeometry(ep_geom.fromPoint(ep_point))

            self.Dialog.progressBar.setValue(i)

            # set feature attributes
            ep_feature.setAttributes(line.attributes())
            # and add them
            epLayer.addFeature(ep_feature)

            i = i + 1

        self.Dialog.progressBar.setRange(0,1)   # kind of reset to prevent oscillation of the bar

        epLayer.commitChanges() # write changes to the layer Object




        # keep track of what is connected! (for refresh/update, save and load)
        # write it to a list Object. See also in the following methods
        if epLayer.isValid():

            lyr = memlyr()  # a kind of struct
            lyr.id_memlyr = epLayer.id()
            lyr.name_memlyr = epLayer.name()
            lyr.id_quelllyr = in_lyr.id()
            lyr.name_quelllyr = in_lyr.name()
            lyr.x_spalte = x_spalte
            lyr.y_spalte = y_spalte

            self.layerliste.append(lyr)



    ##############################################################################
    # trigger interactively (refresh buttun) a update of all created point layers
    # as documented in the self.layerlist Variable
    # in case that the source tables have changed.
    ##############################################################################
    def trigger_update(self):

        # fetch the joins from the layerlist
         for element in self.layerliste:
            quell_id = element.id_quelllyr
            quell_name = element.name_quelllyr
            ziel_id = element.id_memlyr
            ziel_name = element.name_memlyr
            feldx = element.x_spalte
            feldy = element.y_spalte

            # and update all of the created point layers
            if not (quell_id == None or quell_name == None or ziel_id == None or ziel_name == None or feldx == None or feldy == None):
                self.update_layer(quell_id, quell_name,ziel_id, ziel_name, feldx, feldy)



    ############################################################################################
    # update a specific point memory layer. Recalculate the coordinates according to the
    #  (changed) data content of the x and y fields of the source table.
    #############################################################################################
    def update_layer(self, quell_id, quell_name, ziel_id, ziel_name, spalteX, spalteY):


        layerMap = QgsMapLayerRegistry.instance().mapLayers()

        # QGIS Objects - necessery to create the point features
        ep_point = QgsPoint()
        ep_geom = QgsGeometry()
        ep_feature = QgsFeature()
        epLayer =QgsVectorLayer()


        # check if the specified layer exists
        ok_1 = False
        ok_2 = False

        for vorhanden in QgsMapLayerRegistry.instance().mapLayers():    # dont use the self.mc.layers(): method
                                                                        # its not ready initialized when QGIS starts
                                                                        # use the QgsMapLayerRegistry.instance() Object instead!


            lyr = layerMap[vorhanden]
            if string.strip(lyr.id()) == string.strip(quell_id):  # Sourece Table Found
                ok_1 = True
                in_lyr = lyr
            if string.strip(lyr.id()) == string.strip(ziel_id):  # Target memory layer found
                ok_2 = True
                epLayer = lyr

        # if not found - exit
        if not (ok_1 and ok_2):
            QtGui.QMessageBox.critical(None, 'Warning',QtCore.QCoreApplication.translate("xyToPointMain", 'Layer not found'))
            return


        # Re-Add the fields of the source table
        feld = []
        feldnamen = in_lyr.dataProvider().fields()    # the source field map

        epProvider = epLayer.dataProvider() # to add fields use the data provider object
        # create the field list
        for depp in range(feldnamen.count()):
            feld.append(feldnamen.at(depp)) # remember, feldnamen is a map type
        # and add it
        epProvider.addAttributes(feld)
        epLayer.updateFields()



        # edit session starten
        epLayer.startEditing()
        # in case of an update, delete all existing features first
        epLayer.selectAll()
        epLayer.deleteSelectedFeatures()


        # a progress bar might be usefull...
        i = 0
        self.Dialog.progressBar.setRange(0,in_lyr.featureCount()-1)

         # loop through the source table
        for line in in_lyr.getFeatures():

            # short check if the fields contain numerical values
            try:
                # point geometry
                ep_point.setX(float(line.attribute(spalteX)))
                ep_point.setY(float(line.attribute(spalteY)))    #da ein tuple zurückgegeben wird
            except:
                QtGui.QMessageBox.critical(None, 'Error',QtCore.QCoreApplication.translate("xyToPointMain", 'Unable to Update'))
                QgsMapLayerRegistry.instance().removeMapLayer(epLayer.id())
                return

            # set feature geometry
            ep_feature.setGeometry(ep_geom.fromPoint(ep_point))         #da ein tuple zurückgegeben wird

            self.Dialog.progressBar.setValue(i)

            # set feature attributes
            ep_feature.setAttributes(line.attributes())   #Nun wird die Attribute Map aufs Feature gesetzt!

            # and add them
            epLayer.addFeature(ep_feature)

            i = i + 1

        self.Dialog.progressBar.setRange(0,1)   # kind of reset to prevent oscillation of the bar

        epLayer.commitChanges()# write changes to the layer Object





###############################################
# Dialog Widget Class
# inherits the QT Designer window definition
# and the QDialog definition
###############################################
class xyToPointDialog(QtGui.QDialog,Ui_frmMainWindow):
    def __init__(self,parent):

        QtGui.QDialog.__init__(self,parent) #parent keeps the dialog in front of the parent window (without locking it).
        #QtGui.QDialog.__init__(self)
        Ui_frmMainWindow.__init__(self)

        self.setupUi(self)  #creates the GUI specified with QT Designer

########################################
# A class for a special data container
# a kind of C struct
########################################
class memlyr():
    def init(self):
        self.name_memlyr = ''
        self.name_quelllyr = ''
        self.id_memlyr = ''
        self.id_quelllyr = ''
        self.x_spalte = ''
        self.y_spalte = ''
