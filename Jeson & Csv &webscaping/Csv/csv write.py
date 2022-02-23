import csv

f=open('D:\\Csv.csv','w')

write=csv.writer(f)

write.writerow(['id','pass','slno'])
write.writerow(['hello',256,45])
write.writerow(['hello1',286,5])
write.writerow(['hello2',25,45])
write.writerow([1,2])