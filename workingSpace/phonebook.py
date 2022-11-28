import csv

phonebook = []

data = list()
f = open("phone_book.csv",'r')
rdr = csv.reader(f)
for row in rdr:
    data.append(row)
f.close

phonebook = data

while True:
    # 1. 검색, 2. 입력, 3. 삭제, 4. 전체 5. 종료

    num = input().strip()
    if num == "": continue

    if num == "1":# 검색
        a = input().strip()
        for i in phonebook:
            if a == "":
                print("[{}] {} {}".format(i[0], i[1], i[2])) 
            elif a in i[0] or a in i[1] or a in i[2]:
                print("[{}] {} {}".format(i[0], i[1], i[2]))

    elif num == "2":# 입력
        a = input("부서 입력: ").strip()
        b = input("이름 입력: ").strip()
        c = input("전화번호 입력: ").strip()
        if a == "" or b == "" or c == "":
            continue

        phonebook.append([a, b, c]) #부서,이름,전화번호
        print("{} {} {} 입력".format(a, b, c))

    elif num == "3":# 삭제
        a = input("삭제할 전화번호 입력: ").strip()
        if a == "":
            continue

        del_cnt = 0

        for i in phonebook:
            if i[2] == a:
                phonebook.remove([i[0], i[1], i[2]])
                del_cnt += 1

        if del_cnt > 0:
            print("{} 삭제".format(a))

    elif num == "4":# 전체
        print(phonebook)

    elif num == "5":# 종료
        break

