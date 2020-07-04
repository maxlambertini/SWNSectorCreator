from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from SWNFramework.Structures.GUI.QTMainWindow import SWNMainWindow

if __name__ == '__main__':

    import sys
    import res
    print ("init app")
    app = QApplication(sys.argv)
    print ("qss")
    css = QFile(":/style.qss")
    print ("open qss")
    css.open(QFile.ReadOnly)
    print ("icon")
    app.setWindowIcon(QIcon(":/icon.png"))
    
    #app.setStyleSheet(str(css.readAll()))
    css.close()
    print (QDir.currentPath())
    print (QDir.homePath()    )
    
    mainWin = SWNMainWindow()
    
    mainWin.show()
    sys.exit(app.exec_())
