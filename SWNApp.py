from PySide.QtCore import *
from PySide.QtGui import *
from SWNFramework.Structures.GUI.QTMainWindow import SWNMainWindow

if __name__ == '__main__':

    import sys
    import res

    app = QApplication(sys.argv)
    css = QFile(":/style.qss")
    css.open(QFile.ReadOnly)
    app.setWindowIcon(QIcon(":/icon.png"))
    #app.setStyleSheet(str(css.readAll()))
    css.close()
    print QDir.currentPath()
    print QDir.homePath()    
    
    mainWin = SWNMainWindow()
    
    mainWin.show()
    sys.exit(app.exec_())