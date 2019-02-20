# -*- coding: utf-8 -*-

from qgis.PyQt import *
import locale
import os
#import resources


#support for multiple languages
translator = QtCore.QTranslator(QtCore.QCoreApplication.instance())
localeCode = QtCore.QLocale.system().name()
if localeCode:
    translator.load("xyToPoint_" + localeCode + ".qm",  os.path.dirname(__file__))
    QtCore.QCoreApplication.instance().installTranslator(translator)

def name():
    return QtCore.QCoreApplication.translate("init","xyToPoint Plugin")

def description():
    return QtCore.QCoreApplication.translate("init","Creates a point layer based on tabular coordinate values")

def icon():
	return "xyToPoint.png"

def version():
    return "2.0"

def qgisMinimumVersion():
  return "3.0"

#def category():
#  return "Database"

def classFactory(iface):
    from .xyToPointMain import xyToPoint
    return xyToPoint(iface)
