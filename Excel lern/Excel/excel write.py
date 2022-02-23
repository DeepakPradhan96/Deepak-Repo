import  xlwt
 #obj of workbook
wk=xlwt.Workbook()
ws=wk.add_sheet('Testing')

ws.write(0,0,'testing')
ws.write(0,1,'test data')

ws2=wk.add_sheet('test2')
ws2.write(0,0,'hu')
ws2.write(0,1,'dee')

#save Workbook

wk.save('D:\\xls\Testing1.xls')