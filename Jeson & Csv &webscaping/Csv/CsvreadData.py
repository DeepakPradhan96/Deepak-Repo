import csv

#open csv File
f=open("D:\\Csv.csv")

csv_data= csv.reader(f)
list1=list(csv_data)
print(list1)
print(len(list1))
for row in list1:
    l=len(row)
    for j in range(0,l):
        print(row[j])