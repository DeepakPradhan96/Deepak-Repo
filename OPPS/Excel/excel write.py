import  xlwt
 #obj of workbook
wk=xlwt.Workbook()
ws=wk.add_sheet('Testing')

ws.write(0,0,'testing')
ws.write(0,1,'test data')

#save Workbook

wk.save('D:\\xls\Testing1.xls')