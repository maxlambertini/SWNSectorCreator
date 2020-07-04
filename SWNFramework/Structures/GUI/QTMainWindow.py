from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import * 
from PySide2.QtPrintSupport import *
from SWNFramework.Structures.GUI import QTWidgets, SWNDialogs, SceneExporter
from SWNFramework.Structures.Tables import deserialize_sector
from SWNFramework.Structures.GUI.QTWidgets import SWNSystemEditor
import SWNFramework.Structures.GUI.SWNDialogs

class SWNMainWindow(QMainWindow):
    def __init__(self):
        super(SWNMainWindow, self).__init__()
        self.SWNView = QTWidgets.SWNGraphicsView(self)
        self.setCentralWidget(self.SWNView)
        
        self.defaultPrinter = QPrinter()
        
        self.__createActions()
        self.__createMenus()
        self.__createToolbars()
        self.__createStatusBar()
        self.__createDockWindows()
        
        self.SWNView.starSystemSelected.connect(self.handle_starSystemSelected)
        self.SWNView.starSystemChanged.connect(self.handle_starSystemSelected)
        self.SWNView.starSystemCreated.connect(self.handle_starSystemSelected)
        self.SWNView

        self.filename = None
        self.dirty = False        
        self.resize(QSize(800,600))
        self.setWindowTitle("Stars Without Numbers Sector Creator")
        self.setUnifiedTitleAndToolBarOnMac(True)

    def __makeAction (self, icon, text, s_shortcut, status_tip, ev_triggered):
        act = QAction(icon,text,self)
        if (s_shortcut is not None):
            act.setShortcut(s_shortcut)
        act.setStatusTip(status_tip)
        act.triggered.connect(ev_triggered)
        return act
        
    def __createActions(self):
        self.a_fileNewSector = self.__makeAction(QIcon(":/filenew.png"), "New Sector","Ctrl+N" ,
                                                 "Create a new Sector", self.handle_fileNewSector)
        self.a_fileOpenSector = self.__makeAction(QIcon(":/fileopen.png"), "Open Sector","Ctrl+O" ,
                                                 "Loads Sector", self.handle_fileOpenSector)
        self.a_fileSaveSector = self.__makeAction(QIcon(":/filesave.png"), "Save Sector", "Ctrl+S",
                                                 "Save a Sector", self.handle_fileSaveSector)
        self.a_fileSaveAsSector = self.__makeAction(QIcon(":/filesaveas.png"), "Save As...", "Ctrl+Shift+S",
                                                 "Save a Sector with a new name", self.handle_fileSaveAsSector)
        self.a_filePrintSetup = self.__makeAction(QIcon(), "Print Preview", "Ctrl+Shift+P",
                                                 "Preview document printing", self.handle_filePageSetup)
        self.a_filePrintSector = self.__makeAction(QIcon(":/fileprint.png"), "Print Sector", "Ctrl+P",
                                                 "Print the sector", self.handle_filePrintSector)
        self.a_fileQuit = self.__makeAction(QIcon(":/exit.png"), "Quit", "Ctrl+Q",
                                                 "Exit the program", self.close)
        
        self.a_fileExportExportToPng = self.__makeAction(QIcon(":/export_png.png"), "Export as Png", "Alt+Shift+B", 
                                                               "Export as Png",
                                                               self.handle_fileExportExportToPng)
        self.a_fileExportExportToPdf = self.__makeAction(QIcon(":/filetype_pdf.png"), "Export as Pdf", "Alt+Shift+P", 
                                                               "Export as Pdf",
                                                               self.handle_fileExportExportToPdf)
        self.a_fileExportExportToSvg = self.__makeAction(QIcon(":/export_svg.png"), "Export as Svg", "Alt+Shift+S", 
                                                               "Export as Svg",
                                                               self.handle_fileExportExportToSvg)
        self.a_fileExportExportToHtml = self.__makeAction(QIcon(":/filetype_html.png"), "Export as Html", "Alt+Shift+H", 
                                                               "Export as Html file",
                                                               self.handle_fileExportExportToHtml)
        
        #-------------------------#
        self.a_editCut = self.__makeAction(QIcon(":/editcut.png"), "Cut","Ctrl+X" ,
                                                 "Create a new Sector", self.handle_editCut)
        self.a_editCopy = self.__makeAction(QIcon(":/editcopy.png"), "Copy","Ctrl+C" ,
                                                 "Create a new Sector", self.handle_editCopy)
        self.a_editPaste = self.__makeAction(QIcon(":/editpaste.png"), "Paste","Ctrl+V" ,
                                                 "Create a new Sector", self.handle_editPaste)
        self.a_editPreferences = self.__makeAction(QIcon(":/editpreferences.png"), "Preferences","Ctrl+," ,
                                                 "Setup the program", self.handle_editPreferences)
        #-------------------------#
        self.a_helpHelp = self.__makeAction(QIcon(":/help_help.png"), "Help",None ,
                                                 "Create a new Sector", self.handle_helpHelp)
        self.a_helpAbout = self.__makeAction(QIcon(":/help_about.png"), "About",None ,
                                                 "Create a new Sector", self.handle_helpAbout)
        self.a_helpAboutQt = self.__makeAction(QIcon(":/help_aboutqt.png"), "About Qt",None ,
                                                 "Create a new Sector", self.handle_helpAboutQt)
        
        #-------------------------#
        self.a_systemAddNew = self.__makeAction(QIcon(":/system_add.png"), "Add New System","Ins" ,
                                                 "Adds a new system", self.handle_systemAddNewSystem)
        self.a_systemChangeSystem = self.__makeAction(QIcon(":/system_change.png"), "Change System Data","Shift+Ins" ,
                                                 "Changes extant system data", self.handle_systemChangeSystem)
        self.a_systemDeleteSysten = self.__makeAction(QIcon(":/system_help.png"), "Delete System","Del" ,
                                                 "Deletes current system", self.handle_systemDeleteSystem)
        self.a_systemConnectSystems = self.__makeAction(QIcon(":/system_help.png"), "Connect Systems","Shift+C" ,
                                                 "Connects two systems", self.handle_systemConnectSystems)
        pass
    
    def __createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.a_fileNewSector)
        self.fileMenu.addAction(self.a_fileOpenSector)
        self.fileMenu.addAction(self.a_fileSaveSector)
        self.fileMenu.addAction(self.a_fileSaveAsSector)
        self.fileMenu.addSeparator()
        
        self.exportMenu =  self.fileMenu.addMenu("Export")
        self.exportMenu.addAction(self.a_fileExportExportToPdf)
        self.exportMenu.addAction(self.a_fileExportExportToPng)
        self.exportMenu.addAction(self.a_fileExportExportToSvg)
        self.exportMenu.addSeparator()
        self.exportMenu.addAction(self.a_fileExportExportToHtml)
        
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.a_filePrintSector)
        self.fileMenu.addAction(self.a_filePrintSetup)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.a_fileQuit)
        
        self.editMenu = self.menuBar().addMenu("&Edit")
        self.editMenu.addAction(self.a_editCut)
        self.editMenu.addAction(self.a_editCopy)
        self.editMenu.addAction(self.a_editPaste)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.a_editPreferences)
        
        self.systemsMenu = self.menuBar().addMenu("&Systems")
        self.systemsMenu.addAction(self.a_systemAddNew)
        self.systemsMenu.addAction(self.a_systemChangeSystem)
        self.systemsMenu.addAction(self.a_systemConnectSystems)
        self.systemsMenu.addSeparator()
        self.systemsMenu.addAction(self.a_systemDeleteSysten)
        
        self.helpPenu = self.menuBar().addMenu("&Help")
        self.helpPenu.addAction(self.a_helpHelp)
        self.helpPenu.addSeparator()
        self.helpPenu.addAction(self.a_helpAbout)
        self.helpPenu.addAction(self.a_helpAboutQt)
    
    def __createToolbars(self):
        self.fileToolbar = self.addToolBar("File")
        self.fileToolbar.addAction(self.a_fileNewSector)
        self.fileToolbar.addAction(self.a_fileOpenSector)
        self.fileToolbar.addAction(self.a_fileSaveSector)
        self.fileToolbar.addAction(self.a_filePrintSector)
        self.fileToolbar.addAction(self.a_fileQuit)
        self.fileToolbar.addSeparator()
        self.fileToolbar.addAction(self.a_editCut)
        self.fileToolbar.addAction(self.a_editCopy)
        self.fileToolbar.addAction(self.a_editPaste)

        self.ctlToolbar = QToolBar("Tools")
        self.addToolBar(Qt.BottomToolBarArea,self.ctlToolbar)
        self.spinZoom = QSlider(Qt.Horizontal)
        self.spinZoom.resize(200,self.spinZoom.height())
        self.spinZoom.setMaximum(200)
        self.spinZoom.setMinimum(5)
        self.spinZoom.setValue(100)
        self.spinZoom.valueChanged.connect(self.handle_spinValueChanged)
        lbl = QLabel("Zoom: ")
        self.ctlToolbar.addWidget(lbl)
        self.ctlToolbar.addWidget(self.spinZoom)
        self.ctlToolbar.setAllowedAreas(Qt.BottomToolBarArea)
        self.ctlToolbar.setMovable(False)
        
        self.nameToolbar = QToolBar("SectorName")
        self.addToolBar(Qt.TopToolBarArea, self.nameToolbar)
        self.txtSectorName = QLineEdit()
        self.txtSectorName.editingFinished.connect(self.handle_txtSectorNameEditingFinished)
        self.txtSectorName.resize(150, self.txtSectorName.height())
        lbl = QLabel("Sector Name: ")
        self.nameToolbar.addWidget(lbl)
        self.nameToolbar.addWidget(self.txtSectorName)
        self.ctlToolbar.setAllowedAreas(Qt.TopToolBarArea)
        
        
    
    def __createStatusBar(self):
        self.statusBar().showMessage("Ready to go!")
    
    def __createDockWindows(self):
        self.swnEditWindow = QDockWidget("System Editor",self)
        self.swnEditWindow.setFeatures(QDockWidget.AllDockWidgetFeatures)
        self.swnEditWindow.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.systemInfo = SWNSystemEditor()
        self.sectorInfo = QTextEdit()
        self.systemInfo.tabs.addTab(self.sectorInfo,"Textual Info")
        self.systemInfo.sectorChanged.connect(self.handle_sectorChanged)
        self.swnEditWindow.setWidget(self.systemInfo)
        self.addDockWidget(Qt.RightDockWidgetArea,self.swnEditWindow)
                
        
        pass
    
    def handle_sectorChanged(self,system):
        self.SWNView.repaint()
    
    #---------------------------------------------------------
    # Event handling starts here
    #---------------------------------------------------------
    
    def handle_txtSectorNameEditingFinished(self):
        self.sector.name = self.txtSectorName.text()
        self.SWNView.set_sector(self.sector)
    
    def closeEvent(self,event):
        try:
            if self.maybe_save():
                pass
            else:
                event.ignore()
        except:
            print ("Error saving, forcing close")
            pass
    
    def handle_fileNewSector(self):
        try:
            if self.maybe_save():
                self.SWNView.create_new_sector()
                self.sector = self.SWNView.sector
                self.dirty = True
                self.filename = None
                self.txtSectorName.setText(self.sector.name)
        except:
            print ("Error...")
            self.SWNView.create_new_sector()
            self.sector = self.SWNView.sector
            self.txtSectorName.setText(self.sector.name)
            self.dirty = True
            self.filename = None
            pass
    
    def handle_fileOpenSector(self):
        try:
            if self.maybe_save():
                (filename, mask) = QFileDialog.getOpenFileName(self,
                                                   "Load Sector",
                                                   "./",
                                                   "SWN Sector files (*.swnsector)")
                if filename is not None or filename != "":
                    print ("Load Sector  from ", filename)
                    self.sector = deserialize_sector(filename)
                    self.txtSectorName.setText(self.sector.name)
                    print (str(self.sector))
                    self.SWNView.set_sector(self.sector)
                    self.filename = filename
        except:
            pass

    def maybe_save(self):
        if self.dirty:
            res = QMessageBox.question(self,
                                       "Stars Without Number Sector Editor - Unsaved changes",
                                       "Save unsaved changes?",
                                       QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if res == QMessageBox.Cancel:
                return False
            elif res == QMessageBox.Yes:
                self.handle_fileSaveSector()
        return True

    def handle_fileSaveSector(self):
        if self.filename != None:
            self.SWNView.sector.save_sector(self.filename)
        else:
            self.handle_fileSaveAsSector()
        self.dirty = False
    
    def handle_fileSaveAsSector(self):
        (filename, mask) = QFileDialog.getSaveFileName(self,
                                           "Save Sector",
                                           "./" + self.SWNView.sector.name+".swnsector",
                                           "SWN Sector files (*.swnsector)")
        if filename != "" or filename is not None:
            print (filename)
            self.SWNView.sector.save_sector(filename)
            self.dirty =False
            print ("Saved Sector on ", filename)
            self.filename = filename
            return True
        else:
            return False

    def handle_filePrintSector(self):
        printer = self.defaultPrinter
        print_dialog = QPrintDialog(printer)
        if print_dialog.exec_() == QDialog.Accepted:
            self.SWNView.exportToOpenOffice(printer)
        pass
    
    def handle_filePageSetup(self):
        if self.defaultPrinter == None:
            self.defaultPrinter = QPrinter()
        ps = QPrintPreviewDialog(self.defaultPrinter)
        ps.paintRequested.connect(self.handle_printPreview)
        ps.exec_()
        
    def handle_printPreview(self,printer):        
        self.SWNView.exportToOpenOffice(printer)
    
    def handle_fileExportExportToPdf(self):
        (filename, mask) = QFileDialog.getSaveFileName(self,
                                           "Save as PDF",
                                           "./" + self.SWNView.sector.name+".pdf",
                                           "PDF files (*.pdf)")
        if filename != "" or filename is not None:
            SceneExporter.exportSceneToPdf(self.SWNView.scene, filename)
    
    def handle_fileExportExportToPng(self):
        (filename, mask) = QFileDialog.getSaveFileName(self,
                                           "Save as PNG",
                                           "./" + self.SWNView.sector.name+".png",
                                           "PNG files (*.png)")
        if filename != "" or filename is not None:
            SceneExporter.exportSceneToPng(self.SWNView.scene, filename,2.0)
    
    def handle_fileExportExportToSvg(self):
        (filename, mask) = QFileDialog.getSaveFileName(self,
                                           "Save as SVG",
                                           "./" + self.SWNView.sector.name+".svg",
                                           "SVG inkscape files (*.svg)")
        if filename != "" or filename is not None:
            SceneExporter.exportSceneToSvg(self.SWNView.scene, filename)
    
    def handle_fileExportExportToHtml(self):
        (filename, mask) = QFileDialog.getSaveFileName(self,
                                           "Save as HTML",
                                           "./" + self.SWNView.sector.name+".html",
                                           "HTML web page (*.html)")
        if filename != "" or filename is not None:
            SceneExporter.exportSectorToHtml(self.SWNView.scene, self.SWNView.sector, filename)
            pass
    
    def handle_filePrintSetup(self):
        pass

    def handle_editCut(self):
        pass
    
    def handle_editCopy(self):
        SceneExporter.exportSceneToClipboard(self.SWNView.scene, 1.0)
        pass
    
    def handle_editPaste(self):
        pass
    
    def handle_editPreferences(self):
        pass
    
    def handle_helpHelp(self):
        pass
    
    def handle_helpAbout(self):
        res = SWNDialogs.Question("Le ore del mattino hanno sempre l'oro in bocca", "Ore")
        print (res)
        pass
    
    def handle_helpAboutQt(self):
        
        QApplication.aboutQt()
        
    def handle_systemAddNewSystem(self):
        self.dirty = True
        self.SWNView.add_new_system()
        pass
    
    def handle_systemChangeSystem(self):
        self.dirty = True
        self.SWNView.change_system()
        pass
    
    def handle_systemDeleteSystem(self):
        self.dirty = True
        self.SWNView.remove_system()
        pass
    
    def handle_systemConnectSystems(self):
        sel_items = self.SWNView.scene.selectedItems()
        if sel_items is None:
            print ("No items selected")
        else:
            print ("You selected ", len(sel_items), " items")
            if len(sel_items) == 2:
                item_1 = sel_items[0]
                item_2 = sel_items[1]
                if item_1.starSystem is not None and item_2.starSystem is not None:
                    self.SWNView.add_line_item(item_1, item_2)
                    pass
        pass
    
    def handle_starSystemSelected(self,item,system):
        item.setSelected(True)
        if system != None:
            self.systemInfo.set_swn_system(system)
            self.sectorInfo.setHtml(system.str_html())
        
    def handle_spinValueChanged(self,value):
        factor = float(value) / 100.0
        matrix = self.SWNView.matrix()
        matrix.reset()
        matrix.scale(factor, factor)
        self.SWNView.setMatrix(matrix)
    

