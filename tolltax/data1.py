from xlutils.copy import copy
import rfid1
from xlrd import open_workbook
rbook=open_workbook("Excel_WB.xls")
rsheet=rbook.sheet_by_index(0)
r=rsheet.nrows
c=rsheet.ncols
cbook=copy(rbook)
csheet=cbook.get_sheet(0)
def data():
    vechicle=int(input("enter type of viechicles\n1.car\n2.truck\n3.bus"))
    if(vechicle==1):
        amt=60
    if(vechicle==2):
        amt=80
    if(vechicle==3):
        amt=100
    print("amount to paid is ",amt)
    name=input("enter name")
    print("scan rfid")
    for i in range(r,r+1):
        for j in range(c):
            if(j==0):
                n=name
            if(j==1):
                n=amt
            if(j==2):
                n=rfid1.rfidd()
            csheet.write(i,j,n)
    cbook.save("Excel_WB.xls")


