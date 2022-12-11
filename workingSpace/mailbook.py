import csv

mailbook = []

f = open("mail_book.csv",'r')
rdr = csv.reader(f)
for row in rdr:
    mailbook.append(row)
f.close

while True:
    a = input().strip()
    for i in mailbook:
            if a == "":
                print("[{}] {} {}".format(i[0], i[1], i[2])) 
            elif a in i[0] or a in i[1] or a in i[2]:
                print("[{}] {} {}".format(i[0], i[1], i[2]))
