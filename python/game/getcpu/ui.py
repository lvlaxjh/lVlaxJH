import wmi
import platform
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
import win32api, win32con
import psutil
import datetime
import _thread

getX = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
getY = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
c = wmi.WMI()


def getcpu():
    tmpdict = {}
    tmpdict["CpuCores"] = 0
    for cpu in c.Win32_Processor():
        tmpdict["cpuid"] = cpu.ProcessorId.strip()
        tmpdict["CpuType"] = cpu.Name
        tmpdict['systemName'] = cpu.SystemName
        try:
            tmpdict["CpuCores"] = cpu.NumberOfCores
        except:
            tmpdict["CpuCores"] += 1
        tmpdict["CpuClock"] = cpu.MaxClockSpeed
        tmpdict['DataWidth'] = cpu.DataWidth
    cpustr = ''
    for i in tmpdict:
        cpustr = cpustr + str(i) + ':' + str(tmpdict[i]) + '\n'
    # print(cpustr)
    return cpustr


def getboard():
    boards = []
    # print len(c.Win32_BaseBoard()):
    for board_id in c.Win32_BaseBoard():
        tmpmsg = {}
        tmpmsg['UUID'] = board_id.qualifiers['UUID'][1:-1]  # 主板UUID,有的主板这部分信息取到为空值，ffffff-ffffff这样的
        tmpmsg['SerialNumber'] = board_id.SerialNumber  # 主板序列号
        tmpmsg['Manufacturer'] = board_id.Manufacturer  # 主板生产品牌厂家
        tmpmsg['Product'] = board_id.Product  # 主板型号
        boards.append(tmpmsg)
    strboaed = ''
    for i in boards:
        for n in i:
            strboaed = strboaed + str(n) + ':' + str(i[n]) + '\n'
    return strboaed


def getBIOS():
    bioss = []
    for bios_id in c.Win32_BIOS():
        tmpmsg = {}
        tmpmsg['BiosCharacteristics'] = bios_id.BiosCharacteristics  # BIOS特征码
        tmpmsg['version'] = bios_id.Version  # BIOS版本
        tmpmsg['Manufacturer'] = bios_id.Manufacturer.strip()  # BIOS固件生产厂家
        tmpmsg['ReleaseDate'] = bios_id.ReleaseDate  # BIOS释放日期
        tmpmsg['SMBIOSBIOSVersion'] = bios_id.SMBIOSBIOSVersion  # 系统管理规范版本
        bioss.append(tmpmsg)
    strbios = ''
    for i in bioss:
        for n in i:
            strbios = strbios + str(n) + ':' + str(i[n]) + '\n'
    return strbios


def getDisk():
    disks = []
    for disk in c.Win32_DiskDrive():
        # print disk.__dict__
        tmpmsg = {}
        tmpmsg['SerialNumber'] = disk.SerialNumber.strip()
        tmpmsg['DeviceID'] = disk.DeviceID
        tmpmsg['Caption'] = disk.Caption
        tmpmsg['Size'] = disk.Size
        tmpmsg['UUID'] = disk.qualifiers['UUID'][1:-1]
        disks.append(tmpmsg)
    strdisk = ''
    for i in disks:
        for n in i:
            strdisk = strdisk + str(n) + ':' + str(i[n]) + '\n'
    return strdisk


def getMemory():
    memorys = []
    for mem in c.Win32_PhysicalMemory():
        tmpmsg = {}
        tmpmsg['UUID'] = mem.qualifiers['UUID'][1:-1]
        tmpmsg['BankLabel'] = mem.BankLabel
        tmpmsg['SerialNumber'] = mem.SerialNumber.strip()
        tmpmsg['ConfiguredClockSpeed'] = mem.ConfiguredClockSpeed
        tmpmsg['Capacity'] = mem.Capacity
        tmpmsg['ConfiguredVoltage'] = mem.ConfiguredVoltage
        memorys.append(tmpmsg)
    strmem = ''
    for i in memorys:
        for n in i:
            strmem = strmem + str(n) + ':' + str(i[n]) + '\n'
    return strmem


def getcpuandmemstate(interval=1):
    phymem = psutil.virtual_memory()
    mempercent=str(phymem.percent)+'%'
    memuse=str(int(phymem.used / 1024 / 1024)) + "M"
    memtotal=str(int(phymem.total / 1024 / 1024)) + "M"
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    allstr=nowTime + '\n' + "CPU usage rate:" +'\n'+ str(psutil.cpu_percent(interval)) + "%" + '\n' +'Memory usage rate:'+'\n'+ mempercent +'-'+memuse+'/'+memtotal+ '\n'
    return allstr


def getp():
    while (True):
        p = []
        for zz in c.Win32_Process():
            cap = zz.Caption
            p.append(cap)
        Number_of_processes = len(p)
        return str(len(p))


def getsf():
    sf = []
    for zz in c.Win32_Product():
        cap = zz.Caption
        sf.append(cap)
    return len(sf)


class WinForm(QWidget):
    def __init__(self, parent=None):
        strsize = 12
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('getInformation')
        desktop = QApplication.desktop()
        rect = desktop.availableGeometry()  # 获取屏幕尺寸
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置无边框
        self.setGeometry(rect)  # 设置全屏
        self.move(0, 0)  # 左上角
        self.lable1 = QLabel(self)  # cpu+主板+bios+磁盘+内存

        self.lable6 = QLabel(self)  # cpu+内存使用率

        self.lable1.setStyleSheet("color:lightgreen")
        self.lable6.setStyleSheet("color:green")

        self.lable1.setFont(QFont("Microsoft YaHei", 11, QFont.Bold))
        self.lable6.setFont(QFont("Microsoft YaHei", 15, QFont.Bold))

        self.lable1.setAlignment(Qt.AlignLeft)
        self.lable6.setAlignment(Qt.AlignLeft)

        layout = QGridLayout(self)
        all_str = ''
        all_str = 'CPU information:' + '\n' + getcpu()+'\n'+'BIOS information:'+'\n'+getBIOS()+'\n'+'Motherboard information:'+'\n'+getboard()+'\n'+'Disk information:'+'\n'+getDisk()+'\n'+'Memory information:'+'\n'+getMemory()
        self.lable1.setText(all_str)
        self.lable6.setText(getcpuandmemstate())
        layout.addWidget(self.lable1, 0, 0)
        layout.addWidget(self.lable6, 0, 1)

        self.btnStart = QRadioButton()
        # self.btnStart.setStyleSheet("QPushButton{background-color:green}")
        # self.btnStart.resize(100,100)
        # self.btnStart.move(1500,500)
        layout.addWidget(self.btnStart)
        self.btnStart.clicked.connect(self.slotAdd)
        self.setLayout(layout)
        # self.lable1.move(10,10)
        # self.lable6.move(getX/2+10,10)

    def slotAdd(self):
        a = 1
        while (True):
            a+=1
            if a%2!=0:
                self.lable6.setStyleSheet("color:green")
            elif a%2==0:
                self.lable6.setStyleSheet("color:lightgreen")
            if a==1000000:
                a=0
            self.lable6.setText(getcpuandmemstate())
            QApplication.processEvents()
            # time.sleep(1)

    def paintEvent(self, event):
        painter = QPainter(self)
        # 设置背景颜色
        painter.setBrush(Qt.black)
        painter.drawRect(self.rect())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = WinForm()
    form.showMaximized()
    sys.exit(app.exec_())
