import sys
from PyQt5.QtWidgets import *
import time
# class WinForm(QWidget):
# #     def __init__(self,parent=None):
# #         super(WinForm,self).__init__(parent)
# #         self.setWindowTitle("test")
# #         self.lable1=QLabel(self)
# #         self.lable1.setText("1111")
# #         self.changelabe()
# #         print(self.lable1.text())
# #     def changelabe(self):
# #         for i in range(10):
# #             self.lable1.setText(str(i))
# #             QApplication.processEvents()
# #             # time.sleep(1)
# #
# #
# # app=QApplication(sys.argv)
# # win=WinForm()
# # win.show()
# # sys.exit(app.exec_())
class WinForm(QWidget):
    def __init__(self, parent = None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('实时刷新页面例子')
        # self.listFile = QListWidget()
        self.lable1 = QLabel(self)
        self.btnStart = QPushButton('开始')
        layout = QGridLayout(self)
        layout.addWidget(self.lable1, 0, 0, 1, 2)
        layout.addWidget(self.btnStart, 1, 1)
        self.btnStart.clicked.connect(self.slotAdd)
        self.setLayout(layout)

    def slotAdd(self):
        for n in range(10):
            str_n = 'file index {0}'.format(n)
            # self.listFile.addItem(str_n)\
            self.lable1.setText(str_n)
            QApplication.processEvents()
            time.sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())