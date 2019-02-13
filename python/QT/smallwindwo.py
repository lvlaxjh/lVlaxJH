import sys
from PyQt5.QtWidgets import QApplication,QWidget

app=QApplication(sys.argv)
window=QWidget()
window.resize(400,200)
window.move(250,150)
window.setWindowTitle("11")
window.show()
sys.exit(app.exec_())