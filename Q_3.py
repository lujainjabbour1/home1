import json
name = input("ادخل اسمك : ")
co = 0
LL = 0
with open('data.json') as jsonfile:
    data = json.load(jsonfile)
    for M in data:
        print(M)
        ANS = input()
        if ANS == data[j]:
            co += 1
        LL += 1

resultFile = open("lujain.txt", "w")
resultFile.write("your name is: "+name+"\n")
resultFile.write("and your a result is: " + str(co)+"/" + str(LL))
