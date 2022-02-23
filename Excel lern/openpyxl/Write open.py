import openpyxl

wk=openpyxl.Workbook()
print(wk.active.title)
sh=wk.active
sh.title='testing'
print(sh)
sh['A4'].value='Deepak'

#New Sheet Create
wk.create_sheet(title='testing2')
sh1=wk['testing2']
sh1['A2'].value='rit'

wk.create_sheet(title='test3')
#remove sheet
wk.remove(wk['test3'])

wk.save('D:\\xls\\openpy.xlsx')

