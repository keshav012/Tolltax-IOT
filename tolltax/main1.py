from ultra1 import *
from motar1 import *
from data1 import *
import rfid1 
import excelrd1

import time
while(1):
    dis_m=ultraa()
    if(dis_m>50):
        pass        
    if(dis_m<50):
        motarclock()
        time.sleep(4)
        motarstop()
        print("door is Locked")
        ch=int(input("choose\n1.Comming\n2.Going"))
        if(ch==1):
            data()
        if(ch==2):
            print("scan your RFID chip")
            rf=rfid1.rfidd()
            excelrd1.xlread(rf)
        motaranticlock()
        time.sleep(4)
        motarstop()
        print("door is UN-loked")
       
