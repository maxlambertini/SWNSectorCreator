from PySide2.QtGui import QColor, QBrush, QPen
from PySide2.QtCore import Qt

# print "Initializing Color"

colorHexLine        = QColor(Qt.green)
colorHexBrush       = QColor(192,255,192)
colorHexRoute       = QColor(255,192,0)
colorHexRoute.setAlpha(128)
colorHexRouteSel    = QColor(192,128,0)
colorHexRouteSel.setAlpha(128)


penLine             = QPen(colorHexLine)
penLine.setWidthF(2.0)
penRoute            = QPen(colorHexRoute)
penRoute.setWidthF(12.0)
penRouteSel         = QPen(colorHexRouteSel)
penRouteSel.setWidthF(12.0)

brushHex            = QBrush(colorHexBrush) 
