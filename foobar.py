count = 5
num = 12

for i in range(2, 6):
    if(num - (1 + i) > i):
        print("1", str(i), str(num - (1+i)))
        count += 1
    else:
        break


for i in range(3, 6):
    if(num - (2 + i) > i):
        print("2", str(i), str(num - (1+i)))
        count += 1
    else:
        break

for i in range(4, 6):
    if(num - (3 + i) > i):
        print("3", str(i), str(num - (1+i)))
        count += 1
    else:
        break

print(count)
