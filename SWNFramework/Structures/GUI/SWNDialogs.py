from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

def Question(text,title="", parent =None) :
    res = QMessageBox.question(parent, title, text,
                               QMessageBox.Yes, QMessageBox.No)  == QMessageBox.Yes
    #print res
    return res

def Error(text, title="",parent = None):
    QMessageBox.critical(parent,title,text)
    
def Warning(text = None,title = "",parent = None):
    QMessageBox.warning(parent,title,text)
    
