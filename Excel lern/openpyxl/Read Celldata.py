import openpyxl

wk=openpyxl.load_workbook('D:\\xls\\xlrd2.xlsx')
sh=wk['Sheet1']

rows=sh.max_row
coulms=sh.max_column

print('total rows:-'+ str (rows))
print('total no of colmns:-'+str (coulms))

for i in range(1,rows+1):
    for j in range(1,coulms+1):
        cv=sh.cell(i,j)
        print(cv.value)

c1=sh.cell(column=2,row=1)
print(c1.value)

#print(c1.row)
#print(c1.column)

for r in sh['A1':'c5']:
  for c in r :
     print(c.value)