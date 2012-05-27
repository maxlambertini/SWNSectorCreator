from PySide.QtCore import *
from PySide.QtGui import *
from SWNFramework.Structures.Tables import StarSystem, get_tags
from SWNFramework.Structures import Tables
from SWNFramework.Structures.GUI import QTGraphicsItems, SWNDialogs,\
    SceneExporter
import sys
import SWNFramework
import SWNFramework.Structures.GUI.SWNDialogs
import SWNFramework.Structures.GUI.SceneExporter 
from SWNFramework.Structures.GUI.QTGraphicsItems import LinkLineItem

class SWNSystemEditor(QWidget):
    
    sectorChanged = Signal(object)
    
    def __init__(self,Parent=None):
        super(SWNSystemEditor,self).__init__(Parent)
        self.txtSectorName = QLineEdit()
        self.lblAtmosphere= QLabel()
        self.lblBiosphere= QLabel()
        self.lblTemperature = QLabel()
        self.lblTechnology = QLabel()
        self.lblPopulation = QLabel()
        self.lblPopulationQty = QLabel()
        self.tagViewer0 = SWNTagViewer()
        self.tagViewer1 = SWNTagViewer()
        
        self.tabs =  QTabWidget()
        self.pageInfo = QWidget()
        
        self.system = None
        
        grid = QGridLayout()
        
        self.txtSectorName.setSizePolicy(QSizePolicy (QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.txtSectorName.setMinimumSize(QSize(300,25))
        self.lblAtmosphere.setSizePolicy(QSizePolicy (QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.lblBiosphere.setSizePolicy(QSizePolicy (QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.lblPopulation.setSizePolicy(QSizePolicy (QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.lblPopulationQty.setSizePolicy(QSizePolicy (QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.lblTechnology.setSizePolicy(QSizePolicy (QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.lblTemperature.setSizePolicy(QSizePolicy (QSizePolicy.Expanding, QSizePolicy.Fixed))
        
        lbl = QLabel("System Name")
        lbl.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)        
        grid.addWidget(lbl, 0,0,Qt.AlignRight)
        grid.addWidget(self.txtSectorName, 0,1,Qt.AlignLeft)

        lbl = QLabel("Atmosphere")
        lbl.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)        
        grid.addWidget(lbl, 1,0,Qt.AlignRight)
        grid.addWidget(self.lblAtmosphere, 1,1,Qt.AlignLeft)
       
        lbl = QLabel("Biosphere")
        lbl.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)        
        grid.addWidget(lbl,2,0,Qt.AlignRight)
        grid.addWidget(self.lblBiosphere, 2,1,Qt.AlignLeft)

        lbl = QLabel("Temperature")
        lbl.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)                
        grid.addWidget(lbl, 3,0,Qt.AlignRight)
        grid.addWidget(self.lblTemperature, 3,1,Qt.AlignLeft)
        
        lbl = QLabel("Technology")
        lbl.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)        
        grid.addWidget(lbl, 4,0,Qt.AlignRight)
        grid.addWidget(self.lblTechnology, 4,1,Qt.AlignLeft)
        
        lbl = QLabel("Population")
        lbl.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)        
        grid.addWidget(lbl , 5,0,Qt.AlignRight)
        grid.addWidget(self.lblPopulation, 5,1,Qt.AlignLeft)
        
        lbl = QLabel("Quantity")
        lbl.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)        
        grid.addWidget(lbl, 6,0,Qt.AlignRight)
        grid.addWidget(self.lblPopulationQty, 6,1,Qt.AlignLeft)
    
        grid.setRowStretch(0,0)
        grid.setRowStretch(1,0)
        grid.setRowStretch(2,0)
        grid.setRowStretch(3,0)
        grid.setRowStretch(4,0)
        grid.setRowStretch(5,0)
        grid.setRowStretch(6,0)
        grid.setRowStretch(7,0)
        grid.setRowStretch(8,1)
        
        grid.setColumnStretch(0,0)
        grid.setColumnStretch(0,1)
    
        self.pageInfo.setLayout(grid)
        self.btnConfirm = QPushButton("Confirm changes")
        self.btnConfirm.clicked.connect(self.btnConfirm_clicked)
        grid.addWidget(self.btnConfirm,7,0)

        self.btnChangePhysical = QPushButton("Create New Data")
        self.btnChangePhysical.clicked.connect(self.btnChangePhysical_clicked)
        grid.addWidget(self.btnChangePhysical,7,1)

        self.tabs.addTab(self.pageInfo,"Info")
        self.tabs.addTab(self.tagViewer0,"Tag 1")
        self.tabs.addTab(self.tagViewer1,"Tag 2")

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        
        self.setLayout(layout)
        
    def btnChangePhysical_clicked(self):
        if self.system == None:
            return
        self.system.initialize_simple_data(self.txtSectorName.text())
        self.set_swn_system(self.system)
        self.sectorChanged.emit(self.system)
        pass
        
    def btnConfirm_clicked(self):
        if self.system == None:
            return
        self.system.name = self.txtSectorName.text()
        self.sectorChanged.emit(self.system)
        pass
    
    def set_swn_system(self,system):
        if system == None:
            return 
        self.system = system
        self.txtSectorName.setText(system.name)
        self.lblAtmosphere.setText(system.atmosphere["Description"])
        self.lblBiosphere.setText(system.biosphere["Description"])
        self.lblTemperature.setText(system.temperature["Description"])
        self.lblTechnology.setText(system.tech["Description"])
        self.lblPopulation.setText(system.population["Description"])
        self.lblPopulationQty.setText("{:,}".format(system.population["Population"]))
        self.tagViewer0.fill_with_tag(system, system.tags[0], 0)
        self.tagViewer1.fill_with_tag(system, system.tags[1], 1)
        self.tabs.setTabText(1, system.tags[0]["name"])
        self.tabs.setTabText(2, system.tags[1]["name"])

        
class SWNTagViewer(QWidget):
    
    tagUpdated = Signal(object,object,int)
    
    def __init__ (self,Parent=None):
        super(SWNTagViewer,self).__init__(Parent)
        self.tag = None
        self.lblTagName = QLabel(self)
        self.lblTagName.setSizePolicy(QSizePolicy (QSizePolicy.Preferred, QSizePolicy.Fixed))
        self.lblTagName.setMinimumSize(QSize(300,25))
        self.lblTagDesc = QTextEdit(self)
        self.lblTagDesc.setSizePolicy(QSizePolicy (QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.lblTagDesc.setMinimumSize(QSize(300,25))
        self.lblTagEnemies = QTextEdit(self)
        self.lblTagEnemies.setMinimumSize(QSize(300,25))
        self.lblTagEnemies.setSizePolicy(QSizePolicy (QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.lblTagFriends = QTextEdit(self)
        self.lblTagFriends.setMinimumSize(QSize(300,25))
        self.lblTagFriends.setSizePolicy(QSizePolicy (QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.lblTagComplications = QTextEdit(self)
        self.lblTagComplications.setMinimumSize(QSize(300,25))
        self.lblTagComplications.setSizePolicy(QSizePolicy (QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.lblTagThings = QTextEdit(self)
        self.lblTagThings.setMinimumSize(QSize(300,25))
        self.lblTagThings.setSizePolicy(QSizePolicy (QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.lblTagPlaces = QTextEdit(self)
        self.lblTagPlaces.setMinimumSize(QSize(300,25))
        self.lblTagPlaces.setSizePolicy(QSizePolicy (QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.starSystem = None
        self.tag = None
        self.idx_tag = -1
        self.btnCommit = QPushButton("Confirm changes",self)
        self.btnCommit.clicked.connect(self.btnCommit_clicked)
        
        self.tabs = QTabWidget(self)
        
        grid = QGridLayout()
        grid.addWidget(QLabel("Tag Name"),0,0, Qt.AlignRight)
        grid.addWidget(self.lblTagName,0,1, Qt.AlignLeft)
        grid.addWidget(QLabel("Description"),1,0, Qt.AlignRight)
        grid.addWidget(self.lblTagDesc,1,1, Qt.AlignLeft)
        
        w1 = QWidget(self)
        w1.setLayout(grid)
        
        self.tabs.addTab(w1, "Basic Info")
        
        grid = QGridLayout()
        grid.addWidget(QLabel("Enemies"),0,0, Qt.AlignRight)
        grid.addWidget(self.lblTagEnemies,0,1, Qt.AlignLeft)
        grid.addWidget(QLabel("Friends"),1,0, Qt.AlignRight)
        grid.addWidget(self.lblTagFriends,1,1, Qt.AlignLeft)
        
        w1 = QWidget(self)
        w1.setLayout(grid)
        self.tabs.addTab(w1, "People")
        
        grid = QGridLayout()
        grid.addWidget(QLabel("Places"),0,0, Qt.AlignRight)
        grid.addWidget(self.lblTagPlaces,0,1, Qt.AlignLeft)
        grid.addWidget(QLabel("Things"),1,0, Qt.AlignRight)
        grid.addWidget(self.lblTagThings,1,1, Qt.AlignLeft)
        grid.addWidget(QLabel("Complications"),2,0, Qt.AlignRight)
        grid.addWidget(self.lblTagComplications,2,1, Qt.AlignLeft)
        
        w1 = QWidget(self)
        w1.setLayout(grid)
        self.tabs.addTab(w1, "Other")
        
        lv = QVBoxLayout()
        lv.addWidget(self.tabs)
        lv.addWidget(self.btnCommit)
    
        self.setLayout(lv)
        
    def btnCommit_clicked(self):
        if (self.starSystem != None and self.idx != -1 and self.tag != None):
            new_tag = self.get_new_tag()
            self.starSystem.tags[self.idx] = new_tag
            self.tag = self.starSystem.tags[self.idx] 
            self.tagUpdated.emit(self.starSystem, self.tag,self.idx)
        pass


    def fill_with_tag (self,m_starSystem, m_tag, m_idx):
        self.starSystem = m_starSystem
        self.idx = m_idx
        self.tag = m_tag
        self.lblTagName.setText(m_tag['name'])
        self.lblTagDesc.setText(m_tag["description"])
        self.lblTagEnemies.setText(m_tag["enemies"])
        self.lblTagFriends.setText(m_tag["friends"])
        self.lblTagPlaces.setText(m_tag["places"])
        self.lblTagThings.setText(m_tag["things"])
        self.lblTagComplications.setText(m_tag["complications"])

    def get_new_tag(self):
        new_tag = {}
        new_tag_data = { 
                        'name' : self.lblTagName.text(),
                        'description' : self.lblTagDesc.toPlainText(),
                        'enemies' : self.lblTagEnemies.toPlainText(),
                        'friends' : self.lblTagFriends.toPlainText(),
                        'complications' :self.lblTagComplications.toPlainText(),
                        'things' :self.lblTagThings.toPlainText(),
                        'places' :self.lblTagPlaces.toPlainText()                     
                        }
        return new_tag_data
    
    def newTag(self):
        self.tag = get_tags()[0]


class SWNGraphicsScene(QGraphicsScene):
    """
    QGraphicsScene subclass to handle correctly item selection
    """
    
    itemSelected = Signal(object, object)
    
    def __init__ (self):
        super (SWNGraphicsScene,self).__init__()
        self.setBackgroundBrush(QBrush(Qt.white))
    
    def sceneHandleSelectedItem(self, item, system):
        self.itemSelected.emit(item, system)
        
    def exportToPng(self,filename):
        SceneExporter.exportSceneToPng(self, filename)
        
    def exportToSvg(self,filename):
        SceneExporter.exportSceneToSvg(self, filename)
        
        

class SWNGraphicsView(QGraphicsView):
    """
    Graphics View Customizzata per 
    - Antialiasing
    - Rubberband Dragmode
    """
    starSystemSelected = Signal(object,object)
    starSystemChanged = Signal(object,object)
    starSystemCreated = Signal(object,object)
    starSystemDeleted = Signal(object)
    
    def __init__(self,parent=None):
        super(SWNGraphicsView,self).__init__(parent)
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.TextAntialiasing)
        self.sector = None
        self.radius = 80
        
        self.scene = SWNGraphicsScene()
        self.scene.itemSelected.connect (self.handle_item_clicked)
        self.setScene(self.scene)
        
        self.current_selected_item= None
        self.current_system = None
        self.items = {}
    
    def handle_item_clicked(self,item, system):
        self.current_selected_item = item
        self.current_system = system
        self.starSystemSelected.emit(item,system)
        
    def change_system(self):
        if (self.current_system != None):
            if SWNDialogs.Question("Do you want to reinitialize system data?"):
                print "Current System is " + self.current_system.name
                self.current_system.initialize_data()
                self.repaint()
                self.starSystemChanged.emit(self.current_selected_item,self.current_system)
            
    
        
    def wheelEvent(self,event):
        """
        Gestiamo l'evento della rotellina
        """
        self.factor = 1.41 ** (event.delta() / 240.0)
        self.scale(self.factor,self.factor)

    def set_sector(self,new_sector):
        self.sector = new_sector
        self.update_widget_view()

    def create_new_sector(self):
        self.sector = Tables.Sector()
        self.sector.name = Tables.get_place()
        self.update_widget_view()

    def add_new_system(self):
        if (self.current_selected_item != None):            
            coord = self.current_selected_item.coord
            if coord in self.items.keys():                
                item = self.items[coord]
                can_create = True
                if item.starSystem != None:
                    can_create = SWNDialogs.Question("There is already a system defined in this hex.\nWant to overwrite it?")
                if can_create :
                    my_sys = self.sector.add_new_system(coord)
                    item.starSystem = my_sys
                    self.current_selected_item = item            
                    self.starSystemCreated.emit(self.current_selected_item, self.current_selected_item.starSystem)
                    viewport = self.viewport()
                    viewport.update()

    def remove_system(self):
        if (self.current_selected_item != None):
            coord = self.current_selected_item.coord
            if coord in self.items.keys():                
                item = self.items[coord]
                if item.starSystem != None:
                    can_remove = SWNDialogs.Question("Do you really want to remove this system?")
                    if can_remove:
                        self.sector.remove_system(coord)        
                        item.starSystem = None            
                        viewport = self.viewport()
                        viewport.update()
            #self.starSystemDeleted(self.current_selected_item)
        
    def update_widget_view(self, p_coord =None):
                
        self.scene.clear()
        self.current_selected_item = None
        self.items = {}
        
        dx = self.radius*1.5
        dy = self.radius * 1.732
        dy2 = self.radius * .866
        
        sector_name = self.sector.name + " sector"
        font = QFont("Corbel")
        font.setBold(True)
        font.setPointSizeF(40)
        font_metrics = QFontMetricsF(font)
        height = font_metrics.height()
        t_item = QGraphicsTextItem(sector_name)
        self.scene.addItem(t_item)
        t_item.setFont(font)
        t_item.setPos(QPointF(-self.radius,- (dy2)))
        
        for y in range(0,10):
            for x in range(0,8):
                coord = (x,y)
                xc = x *dx
                yc = (height * 1.2) + y *dy
                if x % 2 == 1:
                    yc += dy2
                position = QPointF(xc,yc)
                system = None
                if coord in self.sector.systems.keys():
                    system = self.sector.systems[coord]
                item = QTGraphicsItems.HexItem(position, self.scene, self.radius,system,coord)
                self.items[coord] = item
                if (coord == p_coord):
                    self.current_selected_item = item


    def add_line_item (self,item_1,item_2):
        line_item = LinkLineItem(self.sector, item_1, item_2)
        self.scene.addItem(line_item)
        
        
    def exportToOpenOffice(self,printer):
        
        px = QPrinter()
        p_rect = printer.pageRect()
        left = top = right = bottom = 0
        (left,top,right,bottom) = printer.getPageMargins(QPrinter.DevicePixel)
        
        s_rect = self.scene.sceneRect()
        ratio = 0.75* (p_rect.width() - (left+right)) / s_rect.width()
        
        print "Ratio is ", ratio
        
        m_doc = QTextDocument()
        m_cur = QTextCursor(m_doc)
        picture = SceneExporter.exportSceneToQImage(self.scene,ratio)
        m_cur.movePosition( QTextCursor.End )
        
        m_cur.insertBlock()
        m_cur.insertImage(picture)
        m_cur.movePosition( QTextCursor.End )
        m_cur.insertBlock()
        m_cur.insertBlock()
        m_cur.insertHtml(self.sector.str_html())
        
        m_doc.print_(printer)
        
            
        
