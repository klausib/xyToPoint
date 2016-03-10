# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
import locale
import os
#import resources


#support for multiple languages
translator = QTranslator(QCoreApplication.instance())
localeCode = QLocale.system().name()
if localeCode:
    translator.load("xyToPoint_" + localeCode + ".qm",  os.path.dirname(__file__))
    QCoreApplication.instance().installTranslator(translator)

def name():
    return QCoreApplication.translate("init","xyToPoint Plugin")

def description():
    return QCoreApplication.translate("init","Creates a point layer based on tabular coordinate values")

def icon():
	return "xyToPoint.png"

def version():
    return "1.0.3"

def qgisMinimumVersion():
  return "2.4"

#def category():
#  return "Database"

def classFactory(iface):
    from xyToPointMain import xyToPoint
    return xyToPoint(iface)
