import csv

# 1. 读取csv的第一种方式
with open("stock.csv","r",encoding='gbk') as fp:
    reader = csv.reader(fp)
    titles = next(reader)
    print(titles)
    print("="*30)
    for row in reader:
        print(row[1],row[3])


# 2. 读取csv的第二种方式
with open("stock.csv","r",encoding='gbk') as fp:
    reader = csv.DictReader(fp)
    for row in reader:
        secId = row['secID']
        secShortName = row['secShortName']
        print(secId,secShortName)