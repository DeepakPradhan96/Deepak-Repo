import openpyxl

wk=openpyxl.load_workbook('D:\\xls\\xlrd2.xlsx')
print(wk.sheetnames)
print('active sheet is:-' + wk.active.title)

#create obj of Any Sheet you Want To Work

sh=wk['Hellow']
print(sh.title)