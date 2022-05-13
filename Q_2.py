dec = int(input('Enter dec number: '))
num_Binary = []
while dec > 0:
    b = dec % 2
    dec = int(dec / 2)
    num_Binary.append(b)
num_Binary.reverse()
print(num_Binary)



