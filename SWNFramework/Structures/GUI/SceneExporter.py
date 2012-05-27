from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtSvg import *

import os
import string

def exportSceneToPng(scene, filename, resizeFactor = 1.0):
    """
    Salva il contenuto di una GraphicsScene su PNG
    """
    pixmap = QPixmap(scene.sceneRect().width()*resizeFactor, 
                     scene.sceneRect().height() * resizeFactor )
    painter = QPainter(pixmap)
    scene.render(painter)
    painter.end()
    pixmap.save(filename)
    
def exportSceneToQImage(scene, resizeFactor = 1.0):
    """
    Salva il contenuto di una GraphicsScene su QImage
    """
    height = scene.sceneRect().height()*resizeFactor
    width = scene.sceneRect().width()*resizeFactor
    
    image = QImage(width, height,QImage.Format_ARGB32)    
    painter = QPainter(image)
    scene.render(painter)
    painter.end()
    return image

def exportSceneToQPicture(scene, resizeFactor = 1.0):
    """
    Salva il contenuto di una GraphicsScene su QImage
    """
    height = scene.sceneRect().height()*resizeFactor
    width = scene.sceneRect().width()*resizeFactor
    
    picture = QPicture()
    painter = QPainter()
    painter.begin(picture)
    scene.render(painter)
    painter.end()
    return picture


def exportSceneToClipboard(scene, resizeFactor = 1.0):
    """
    Copia la mappa esagonale nella clipboard
    """
    image = exportSceneToQImage(scene, resizeFactor)
    clipboard = QApplication.clipboard()
    clipboard.setImage(image)


def exportSceneToSvg(scene, filename, resolution = 72):
    """
    Salva il contenuto di una GraphicsScene su SVG
    """
    generator = QSvgGenerator()
    generator.setResolution(resolution)
    generator.setSize(QSize(scene.sceneRect().width(), 
                     scene.sceneRect().height()))
    generator.setFileName(filename)
    painter = QPainter(generator)
    scene.render(painter)
    painter.end()

def exportSceneToPdf(scene, filename, resolution = 96):
    printer = QPrinter(QPrinter.HighResolution)
    printer.setResolution(96)
    rect = scene.sceneRect()
    w = rect.width() 
    h = rect.height() 
    printer.setPaperSize(QSizeF(210,297), QPrinter.Millimeter)
    printer.setFullPage(True)
    printer.setOutputFileName(filename)
    painter = QPainter(printer)
    printer.setOutputFormat(QPrinter.PdfFormat)
    printer.setPageMargins(10,10,-10,-10, QPrinter.DevicePixel)
    rect_paper = printer.paperRect().adjusted(76,76,-76,-76)
    scene.render(painter,rect_paper,rect,Qt.KeepAspectRatio)
    c_transparent = QColor(0,0,0,0)
    b_transparent = QBrush(c_transparent)
    c_border = QColor(0,0,0,128)
    p_border = QPen(c_border)
    p_border.setStyle(Qt.DotLine)
    painter.setPen(p_border)
    painter.setBrush(b_transparent)
    rect_paper = rect_paper.adjusted(-38,-38,38,38)
    painter.drawRect(rect_paper)
    painter.end()

def exportSectorToHtml(scene, sector, filename):
    try:
        file_path = string.replace(filename, ".html", "_dir")
        file_name = os.path.join (file_path ,"index.html")
        img_name = os.path.join (file_path ,sector.name + ".svg")
        os.mkdir(file_path)
        exportSceneToSvg(scene, img_name)
        html = sector.str_html()
        
        html = """
        <html>
            <head><title>%s</title>
            <style>
            BODY, P, UL LI, DT, DD, DL, TD , TH {
            font-family: droid sans, corbel, verdana, sans-serif;
            font-size: 11pt;
            }
            </style>
            </head>
            <body>
            <div style='text-align:center;'>
            <img src="%s.svg" alt="sector %s">
            </div>
            <hr />
            %s
            </body>
        </html>
        """ % (sector.name, sector.name, sector.name, html)
        with open (file_name, "w") as f:
            f.write(html)
        
    except Exception as err:
        print err
        print "Error writing file "
        pass