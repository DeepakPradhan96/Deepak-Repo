import xlrd


#we need to crete a object of workbook
wk=xlrd.open_workbook('D:\Selenium With Python\Xlrd.xls')

#found no of sheet
print(wk.nsheets)
#work on sheet
#we=wk.sheet_by_index(0)
ws=wk.sheet_by_name('Sheet1')
print(ws.nrows)
print(ws.ncols)
print(ws.number)

#work on cell

wc=ws.cell(1,0)#(row'colm)
print(wc.value)