import os,sys
import wmi
import platform
import pynvml
# os.environ["CUDA_VISIBLE_DEVICES"] = "0"
c=wmi.WMI()

def getcpu():
    tmpdict={}
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
    print(tmpdict)
    return tmpdict

def getsf():
    sf=[]
    for zz in c.Win32_Product():
        cap = zz.Caption
        sf.append(cap)
    print(sf)
    return sf

def getp():
    p=[]
    for zz in c.Win32_Process():
        cap = zz.Caption
        p.append(cap)
    print(p)
    return p

def getboard():
    boards = []
    # print len(c.Win32_BaseBoard()):
    for board_id in c.Win32_BaseBoard():
        tmpmsg = {}
        tmpmsg['UUID'] = board_id.qualifiers['UUID'][1:-1]   #主板UUID,有的主板这部分信息取到为空值，ffffff-ffffff这样的
        tmpmsg['SerialNumber'] = board_id.SerialNumber                #主板序列号
        tmpmsg['Manufacturer'] = board_id.Manufacturer       #主板生产品牌厂家
        tmpmsg['Product'] = board_id.Product                 #主板型号
        boards.append(tmpmsg)
    print(boards)
    return boards
#BIOS
def getBIOS():
    bioss = []
    for bios_id in c.Win32_BIOS():
        tmpmsg = {}
        tmpmsg['BiosCharacteristics'] = bios_id.BiosCharacteristics   #BIOS特征码
        tmpmsg['version'] = bios_id.Version                           #BIOS版本
        tmpmsg['Manufacturer'] = bios_id.Manufacturer.strip()                 #BIOS固件生产厂家
        tmpmsg['ReleaseDate'] = bios_id.ReleaseDate                   #BIOS释放日期
        tmpmsg['SMBIOSBIOSVersion'] = bios_id.SMBIOSBIOSVersion       #系统管理规范版本
        bioss.append(tmpmsg)
    print(bioss)
    return bioss
#硬盘
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
    for d in disks:
        print(d)
    return disks
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
    for m in memorys:
        print(m)
    return memorys

getcpu()

getboard()
getBIOS()
getDisk()
getMemory()
getsf()
