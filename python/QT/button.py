from PyQt5.QtWidgets import QMainWindow,QHBoxLayout,QPushButton,QApplication,QWidget
import sys

class WinForm(QMainWindow):
    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.setWindowTitle("test")
        self.button1=QPushButton('111')
        self.button1.clicked.connect(self.onButtonClick)
        layout=QHBoxLayout()
        layout.addWidget(self.button1)
        main_frame=QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)


    def onButtonClick(self):
        sender=self.sender()
        print('11')
        qApp=QApplication.instance()
        qApp=quit()

if __name__ =="__main__":
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())