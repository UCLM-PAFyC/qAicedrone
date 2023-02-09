# -*- coding: utf-8 -*-
"""
/***************************************************************************
 qAicedroneDockWidget
                                 A QGIS plugin
 A plugin for AICEDRONE project
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-06-13
        git sha              : $Format:%H$
        copyright            : (C) 2019 by David Hernandez Lopez, Universidad de Castilla-La Mancha
        email                : david.hernandez@uclm.es
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

# dhl
import sys,os
from osgeo import osr
from decimal import Decimal
from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, QFileInfo, QDir, QObject
from PyQt5.QtWidgets import QMessageBox,QFileDialog,QTabWidget,QInputDialog,QLineEdit
from PyQt5.QtWidgets import QDockWidget
from qgis.core import QgsApplication, QgsDataSourceUri,QgsProject, QgsCoordinateReferenceSystem
# pluginsPath = QFileInfo(QgsApplication.qgisUserDatabaseFilePath()).path()
# pluginPath = os.path.dirname(os.path.realpath(__file__))
# pluginPath = os.path.join(pluginsPath, pluginPath)
# libCppPath = os.path.join(pluginPath, 'libCpp')
# existsPluginPath = QDir(libCppPath).exists()
# sys.path.append(pluginPath)
# sys.path.append(libCppPath)
# os.environ["PATH"] += os.pathsep + libCppPath
# from libCpp.libPyModelManagementTools import IPyModelManagementToolsProject
from .multipleFileSelectorDialog.multiple_file_selector_dialog import * #panel nueva camara
# from .reports.Report import *
# import MMTDefinitions
from . import MMTDefinitions
#  dhl

import os

from math import floor
import re

from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSignal

from qgis import utils

from qgis.core import Qgis
qgis_version_number_str = Qgis.QGIS_VERSION.split('-')[0]
qgis_version_first_number = int(qgis_version_number_str.split('.')[0])
qgis_version_second_number = int(qgis_version_number_str.split('.')[1])
qgis_version_third_number = int(qgis_version_number_str.split('.')[2])
qgis_version_second_number_change_buffer_parameters = 20

from osgeo import osr
projVersionMajor = osr.GetPROJVersionMajor()

FORM_CLASS = None

# if projVersionMajor < 8:
#     FORM_CLASS, _ = uic.loadUiType(os.path.join(
#         os.path.dirname(__file__), 'model_management_tools_dockwidget_base_old_osgeo.ui'))
# else:
#     FORM_CLASS, _ = uic.loadUiType(os.path.join(
#         os.path.dirname(__file__), 'model_management_tools_dockwidget_base.ui'))
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'qAicedrone_dockwidget_base.ui'))

class qAicedroneDockWidget(QtWidgets.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self,
                 iface,
                 projVersionMajor,
                 pluginPath,
                 libCppPath,
                 currentPluginName,
                 settings,
                 iPyProject,
                 parent=None):
        """Constructor."""
        super(qAicedroneDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://doc.qt.io/qt-5/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setWindowTitle(MMTDefinitions.CONST_PROGRAM_NAME)
        self.iface = iface
        self.projVersionMajor = projVersionMajor
        self.path_plugin = pluginPath
        self.path_libCpp = libCppPath
        self.current_plugin_name = currentPluginName
        self.settings = settings
        self.iPyProject = iPyProject
        self.isModelManagementPlugin = False
        self.plugin_name = None
        self.referenceLayer = None
        if self.current_plugin_name == MMTDefinitions.CONST_SETTINGS_PLUGIN_NAME:
            self.isModelManagementPlugin = True
            self.plugin_name = MMTDefinitions.CONST_SETTINGS_PLUGIN_NAME
        self.setupUi(self)
        # self.pluginPointCloudToolsInstance = None
        # self.pluginPointCloudToolsInstance = utils.plugins['point_cloud_tools']
        self.pluginPhotogrammetryToolsInstance = utils.plugins['photogrammetry_tools']
        # self.initialize()

        #### depuracion report
        # report = Report(self.iface,self.path_plugin)
        # reportType = 'PhHotspot'
        # reportSucess, strError = report.initialize(reportType)
        # if not reportSucess:
        #     msgBox = QMessageBox(self)
        #     msgBox.setIcon(QMessageBox.Information)
        #     msgBox.setWindowTitle(self.windowTitle)
        #     msgBox.setText(strError)
        #     msgBox.exec_()
        #     return

        ####
