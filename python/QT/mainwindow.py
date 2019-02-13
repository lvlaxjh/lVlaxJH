import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import win32api,win32con
getX=win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
getY=win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setFixedSize(400,200)
        self.status=self.statusBar()
        self.status.showMessage("状态栏",5000)
        self.setPosition()
        self.x=self.width()
        self.y=self.height()
        self.pos1=self.pos()
        print(self.x,self.y,self.pos1)
    def setPosition(self):
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        # self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
        self.move(0,0)


if __name__=="__main__":
    app=QApplication(sys.argv)
    form=MainWindow()
    form.show()
    sys.exit(app.exec_())