from qgis.core import *
from qgis.gui import *
from PyQt5.QtCore import QSettings, QTranslator, QVersionNumber, QCoreApplication, Qt, QObject, pyqtSignal
from PyQt5.QtGui import QColor


class PolygonMapTool(QgsMapToolEmitPoint):
    """

    """
    endSelection = QtCore.pyqtSignal()

    # def __init__(self, canvas,layerNames,selectPoints=True):
    def __init__(self, canvas):
        self.canvas = canvas
        # self.layerNames = layerNames
        # self.selectPoints = selectPoints
        self.wktGeomery = None
        QgsMapToolEmitPoint.__init__(self, self.canvas)
        self.rubberBand = QgsRubberBand(self.canvas, True)
        self.rubberBand.setColor(Qt.red)
        rFillColor = QColor(254, 178, 76, 63)
        self.rubberBand.setFillColor(rFillColor)
        self.rubberBand.setWidth(1)
        # self.marker = QgsVertexMarker(self.canvas)
        # self.marker.setColor(Qt.red)
        # self.marker.setIconSize(3)
        # self.marker.setIconType(QgsVertexMarker.ICON_BOX)
        # self.marker.setPenWidth(1)
        self.reset()

    def getWktGeomeetry(self):
        return self.wktGeomery

    def reset(self):
        self.isEmittingPoint = False
        self.point = None
        self.pointMove = None
        self.points = []
        self.rubberBand.reset(True)

    def canvasPressEvent(self, e):
        if e.button() == Qt.RightButton:
            self.selection()
        if e.button() == Qt.LeftButton:
            self.point = self.toMapCoordinates(e.pos())
            self.pointMove = self.toMapCoordinates(e.pos())
            self.points.append(QgsPointXY(self.point))
            self.isEmittingPoint = True
            # self.marker.setCenter(QgsPointXY(self.point))
            self.showPol()

    def canvasMoveEvent(self, e):
        if not self.isEmittingPoint:
            return
        else:
            self.pointMove = self.toMapCoordinates(e.pos())
            self.isEmittingPoint = True
            self.showPol()

    def showPol(self):
        self.rubberBand.reset(QgsWkbTypes.PolygonGeometry)
        for point in self.points:
            self.rubberBand.addPoint(point, False)
            self.rubberBand.shape()
        self.rubberBand.addPoint(self.pointMove, True)
        self.rubberBand.show()

    def showPolMove(self):
        self.rubberBand.reset(QgsWkbTypes.PolygonGeometry)
        for point in self.points:
            self.rubberBand.addPoint(point, True)
            self.rubberBand.shape()
        self.rubberBand.show()

    def selection(self):
        geom_selection = self.rubberBand.asGeometry()
        # self.wktGeomery = None
        self.wktGeomery = geom_selection.asWkt()
        self.endSelection.emit()
        # if not self.selectPoints:
        #     self.wktGeomery = geom_selection.asWkt()
        #     self.endSelection.emit()
        #     return
        # layers = self.canvas.layers()
        # for layer in layers:
        #     layerName = layer.name()
        #     if not layerName in self.layerNames:
        #         continue
        #     if layer.type() == QgsMapLayer.VectorLayer:
        #         features_bb = layer.getFeatures(QgsFeatureRequest().setFilterRect(geom_selection.boundingBox()))
        #         for feature in features_bb:
        #             if feature.geometry().within(geom_selection):
        #                 layer.select(feature.id())
        self.rubberBand.hide()
        self.rubberBand.reset(QgsWkbTypes.PolygonGeometry)
        self.reset()

    def deactivate(self):
        self.canvas.scene().removeItem(self.rubberBand)
        #self.canvas.scene().removeItem(self.marker)
        super(PolygonMapTool, self).deactivate()

        # self.emit(SIGNAL("deactivated()"))
