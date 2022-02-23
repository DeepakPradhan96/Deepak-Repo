import xlrd


#we need to crete a object of workbook
wk=xlrd.open_workbook('D:\Selenium With Python\Xlrd.xls')

ws=wk.sheet_by_name('Sheet1')
r=ws.nrows
c=ws.ncols

for i in range(0,r):
    for j in range (0,c):
        wc=ws.cell(i,j)
        print(wc.value)