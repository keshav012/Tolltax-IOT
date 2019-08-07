from xlrd import open_workbook
rbook=open_workbook("Excel_WB.xls")
rsheet=rbook.sheet_by_name("sheet1")
r=rsheet.nrows
c=2
def xlread(str):
    for i in range(r):
        val=rsheet.cell(i,c).value
        if(str==val):
            name=rsheet.cell(i,1)
            vechicle=rsheet.cell(i,2)
            print(name,vechicle)
           


