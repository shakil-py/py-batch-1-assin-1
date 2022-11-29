# a=int(input())
list_1 = []
for i in range(10):
    a =input()
    
    if a not in list_1:
        list_1.append(a)


    else:
        print("duplicate")

print(list_1)
