# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Wed Mar 11 12:05:23 2015
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_frmMainWindow(object):
    def setupUi(self, frmMainWindow):
        frmMainWindow.setObjectName(_fromUtf8("frmMainWindow"))
        frmMainWindow.setWindowModality(QtCore.Qt.NonModal)
        frmMainWindow.resize(241, 646)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frmMainWindow.sizePolicy().hasHeightForWidth())
        frmMainWindow.setSizePolicy(sizePolicy)
        frmMainWindow.setMinimumSize(QtCore.QSize(200, 170))
        self.groupBox = QtGui.QGroupBox(frmMainWindow)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 221, 71))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.cmbLayer = QtGui.QComboBox(self.groupBox)
        self.cmbLayer.setGeometry(QtCore.QRect(10, 30, 191, 22))
        self.cmbLayer.setObjectName(_fromUtf8("cmbLayer"))
        self.btnRefresh = QtGui.QPushButton(frmMainWindow)
        self.btnRefresh.setGeometry(QtCore.QRect(70, 510, 91, 41))
        self.btnRefresh.setObjectName(_fromUtf8("btnRefresh"))
        self.groupBox_2 = QtGui.QGroupBox(frmMainWindow)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 90, 221, 71))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.cmbX = QtGui.QComboBox(self.groupBox_2)
        self.cmbX.setGeometry(QtCore.QRect(10, 30, 191, 22))
        self.cmbX.setObjectName(_fromUtf8("cmbX"))
        self.groupBox_3 = QtGui.QGroupBox(frmMainWindow)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 170, 221, 71))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.cmbY = QtGui.QComboBox(self.groupBox_3)
        self.cmbY.setGeometry(QtCore.QRect(10, 30, 191, 22))
        self.cmbY.setObjectName(_fromUtf8("cmbY"))
        self.groupBox_4 = QtGui.QGroupBox(frmMainWindow)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 250, 221, 251))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.btnRun = QtGui.QPushButton(self.groupBox_4)
        self.btnRun.setGeometry(QtCore.QRect(30, 200, 151, 41))
        self.btnRun.setObjectName(_fromUtf8("btnRun"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 30, 201, 61))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.txtName = QtGui.QLineEdit(self.groupBox_5)
        self.txtName.setGeometry(QtCore.QRect(10, 30, 171, 20))
        self.txtName.setObjectName(_fromUtf8("txtName"))
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 100, 201, 91))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.cmbLayerCRS = QtGui.QComboBox(self.groupBox_6)
        self.cmbLayerCRS.setEnabled(True)
        self.cmbLayerCRS.setGeometry(QtCore.QRect(10, 60, 171, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbLayerCRS.sizePolicy().hasHeightForWidth())
        self.cmbLayerCRS.setSizePolicy(sizePolicy)
        self.cmbLayerCRS.setObjectName(_fromUtf8("cmbLayerCRS"))
        self.rbProject = QtGui.QRadioButton(self.groupBox_6)
        self.rbProject.setGeometry(QtCore.QRect(10, 30, 101, 17))
        self.rbProject.setChecked(True)
        self.rbProject.setObjectName(_fromUtf8("rbProject"))
        self.buttonGroup = QtGui.QButtonGroup(frmMainWindow)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.rbProject)
        self.rbLayer = QtGui.QRadioButton(self.groupBox_6)
        self.rbLayer.setGeometry(QtCore.QRect(130, 30, 51, 17))
        self.rbLayer.setObjectName(_fromUtf8("rbLayer"))
        self.buttonGroup.addButton(self.rbLayer)
        self.progressBar = QtGui.QProgressBar(frmMainWindow)
        self.progressBar.setGeometry(QtCore.QRect(10, 560, 221, 23))
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty(_fromUtf8("value"), 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.btnClose = QtGui.QPushButton(frmMainWindow)
        self.btnClose.setGeometry(QtCore.QRect(70, 600, 91, 41))
        self.btnClose.setObjectName(_fromUtf8("btnClose"))

        self.retranslateUi(frmMainWindow)
        QtCore.QMetaObject.connectSlotsByName(frmMainWindow)

    def retranslateUi(self, frmMainWindow):
        frmMainWindow.setWindowTitle(QtGui.QApplication.translate("frmMainWindow", "xyToPoint", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("frmMainWindow", "Inputtable or Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRefresh.setText(QtGui.QApplication.translate("frmMainWindow", "Refresh All", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("frmMainWindow", "Column with X Coordinate Values", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("frmMainWindow", "Column withY Coordinate Values", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("frmMainWindow", "Calculated Memory-Pointlayer", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRun.setText(QtGui.QApplication.translate("frmMainWindow", "Create Point Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("frmMainWindow", "Layername (Input Optional)", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("frmMainWindow", "Define CRS (optional)", None, QtGui.QApplication.UnicodeUTF8))
        self.rbProject.setText(QtGui.QApplication.translate("frmMainWindow", "Project Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.rbLayer.setText(QtGui.QApplication.translate("frmMainWindow", "Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClose.setText(QtGui.QApplication.translate("frmMainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))

