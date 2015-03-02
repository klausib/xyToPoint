# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Mon Mar 02 14:45:24 2015
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
        frmMainWindow.resize(241, 525)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
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
        self.btnRefresh.setGeometry(QtCore.QRect(70, 420, 91, 41))
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
        self.groupBox_4.setGeometry(QtCore.QRect(10, 250, 221, 151))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.btnRun = QtGui.QPushButton(self.groupBox_4)
        self.btnRun.setGeometry(QtCore.QRect(30, 100, 151, 41))
        self.btnRun.setObjectName(_fromUtf8("btnRun"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 30, 191, 51))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.txtName = QtGui.QLineEdit(self.groupBox_5)
        self.txtName.setGeometry(QtCore.QRect(10, 20, 171, 20))
        self.txtName.setObjectName(_fromUtf8("txtName"))
        self.progressBar = QtGui.QProgressBar(frmMainWindow)
        self.progressBar.setGeometry(QtCore.QRect(10, 490, 221, 23))
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty(_fromUtf8("value"), 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))

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

import resources_rc
