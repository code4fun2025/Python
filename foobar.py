count = 5
num = 12
j = 2
while(j < 5):
    for i in range(j, 6):
        if(num - (1 + i + j - 2) > i):
            print(str(j - 1), str(i), str(num - (1+i)))
            count += 1
        else:
            break
    j += 1

# for i in range(3, 6):
#     if(num - (2 + i) > i):
#         print("2", str(i), str(num - (1+i)))
#         count += 1
#     else:
#         break

# for i in range(4, 6):
#     if(num - (3 + i) > i):
#         print("3", str(i), str(num - (1+i)))
#         count += 1
#     else:
#         break

print(count)