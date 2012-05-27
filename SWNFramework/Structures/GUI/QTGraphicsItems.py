from PySide.QtGui import *
from PySide.QtCore import *
from SWNFramework.Structures.Tables import StarSystem
import SWNConstants

from math import *

colors = [QColor(96,0,255),
          QColor(0,128,255),
          QColor(0,192,255),
          QColor(0,255,255),
          QColor(0,255,192),
          QColor(0,255,128),
          QColor(0,255,64),
          QColor(0,255,0),
          QColor(128,255,0),
          QColor(255,255,0),
          QColor(255,128,0),
          QColor(255,0,0)
         ]

def populationToColor(pop):
    try:
        n = int(log10(pop))
        #print "log is: ",n
        if n < 0:
            n = 0
        if n > 11:
            n = 11
        return colors[n]
    except:
        return QColor(192,192,255)
    
class LinkLineItem(QGraphicsItem):
    
    def __init__ (self, sector, item_1,item_2):
        super (LinkLineItem,self).__init__()
        self.setFlags(QGraphicsItem.ItemIsFocusable) 
        self.pos_1 = item_1.pos()
        self.pos_2 = item_2.pos()
        self.setZValue(min (item_1.zValue(), item_2.zValue()) - 200)
        
        min_x, min_y = min(self.pos_1.x(),self.pos_2.x() ),min(self.pos_1.y(),self.pos_2.y() )
        max_x, max_y = max(self.pos_1.x(),self.pos_2.x() ),max(self.pos_1.y(),self.pos_2.y() )
        r_width, r_height = abs(self.pos_1.x()-self.pos_2.x() ),abs(self.pos_1.y()-self.pos_2.y() )
        
        self.d_pos_x = r_width / 2.0
        self.d_pos_y = r_height / 2.0
        
        pos = QPointF( (self.pos_1.x()+self.pos_2.x())/2.0,(self.pos_1.y()+self.pos_2.y())/2.0)
        self.setPos(pos)
        self.rect = QRectF(-r_width/2.0,-r_height/2.0,r_width,r_height)
        
        pos_key = [item_1.starSystem.coords, item_2.starSystem.coords]
        pos_key.sort()
        
        p_key = ( pos_key[0], pos_key[1])
        if not p_key in sector.links.keys():
            sector.links[p_key]  = self
            print sector.links
        
        self.penRoute = SWNConstants.penRoute
        self.penRouteSel = SWNConstants.penRouteSel
        pass
    
    def boundingRect(self):
        print "returning ", self.rect
        return self.rect
    
    def paint (self,painter,option,widget):
        if (option.state & QStyle.State_Selected):
            painter.setPen(self.penRouteSel)
        else:
            painter.setPen(self.penRoute)
        painter.drawLine(self.mapFromScene(self.pos_1), self.mapFromScene(self.pos_2))
            

class HexItem(QGraphicsItem):
    """
    Questa classe rappresenta un esagono nella sector map.
    Ad esso posso associarci uno Star System. Inoltre quando ci clicco
    sopra emetto un evento. 
    """
    
    
    def __init__(self,position, scene, radius=50, star_system = None, coord = None):
        "HexItem (pos, scene, radius, star_system)"
        super(HexItem,self).__init__()
        self.setFlags(QGraphicsItem.ItemIsSelectable | 
                      QGraphicsItem.ItemIsFocusable)
        self.rect= QRectF(-radius, -radius *.866, 2*radius, radius*1.732)
        self.setPos(position)
        self.radius = radius
        scene.clearSelection()
        scene.addItem(self)
        self.starSystem = star_system
        self.coord = coord
        
    def boundingRect(self):
        return self.rect.adjusted(-2,-2,2,2)
    
    def paint(self,painter,option,widget):
        path = QPainterPath()
        rect = self.rect
        dx = rect.width() / 4
        dy = rect.height() / 2
        
        path = QPainterPath()
        pen4 =QPen()
        pen4.setColor(Qt.green)
        if (option.state & QStyle.State_Selected):
            pen4.setColor(Qt.blue)
            pen4.setWidthF(5.5)
        painter.setPen(pen4)
        
        self.__draw_hex(path, rect, dx, dy)
        r_text_2 = QRectF (self.rect.left()+dx,
                           self.rect.top() + 6,
                           self.rect.width()-(dx*2),
                           20) 

        painter.drawPath(path)


        if self.starSystem != None:
            self.__draw_star_system(painter)

        font_coord = QFont("Corbel",10, QFont.Bold)
        pen_green = QPen(Qt.gray)
        pen_green.setWidthF(1.1)
        brush_green = QBrush(Qt.gray)
        painter.setBrush(brush_green)
        painter.setPen(pen_green)
        painter.setFont(font_coord)
        text_option = QTextOption(Qt.AlignCenter)
        painter.drawText(r_text_2, str(self.coord),text_option)
        
        
    def __draw_star_system(self,painter):
        star_radius = self.radius/2
        gray1 = QColor(192,192,192)
        gray2 = QColor(128,128,128)
        black = Qt.black
        
        brush = QBrush()
        brush.setColor(gray1)
        brush_black = QBrush()
        brush_black.setColor(black)
        pen = QPen()
        pen.setColor(gray2)
        pen.setWidthF(3.0)
        
        font = QFont("Corbel",12, QFont.Bold)
        
        ell_rect = QRectF(self.rect.left()+self.rect.width() *.5 - self.rect.height() *.25,
                          self.rect.top() + self.rect.height() *.25,
                          self.rect.height() *.5, self.rect.height() * .5) 
        
        #print "pop is: ", self.starSystem.population["Population"]
        a_pop = int(self.starSystem.population["Population"])
        color_pop = populationToColor(a_pop)
        painter.setBrush(QBrush(color_pop))
        painter.setPen(pen)
        painter.drawEllipse(ell_rect)
        
        painter.setBrush(brush_black)
        painter.setFont(font)
        
        text_option = QTextOption(Qt.AlignCenter)
        r_text = QRectF (self.rect.left(), 
                           self.rect.top()+ self.rect.height() * .75,
                           self.rect.width(),
                           self.rect.height() * .25)
        painter.drawText(r_text, self.starSystem.name, text_option)
        
    def __draw_hex(self, path, rect, dx, dy):
        path.moveTo( rect.left(), rect.top()+dy)
        path.lineTo(rect.left()+dx,rect.top()+ dy *2) 
        path.lineTo(3*dx+rect.left(),rect.top()+ dy *2)
        path.lineTo(4*dx+rect.left(),rect.top()+ dy)
        path.lineTo(3*dx+rect.left(),rect.top())
        path.lineTo(dx+rect.left(),rect.top()) 
        path.lineTo(rect.left(), rect.top()+dy)

    def mouseReleaseEvent(self,event):
        super(HexItem,self).mouseReleaseEvent(event)
        if (self.isSelected()):
            scene = self.scene()
            try:
                self.scene().sceneHandleSelectedItem(self,self.starSystem)
            except AttributeError:
                # scene isn't subclassed and doesn't contain any
                # callback 
                pass
