list_1=[5,15,20,12,20,13,20,14,20]
# list_1.remove(7)

# list_2=list_1.sort()
# print(list_2)
# print(list_1)
for i in range(len(list_1)):
    if list_1[i]==20:
        list_1[i]=list_1.remove(7)
        print(list_1)
# list_2=set(list_1)
# print(list_2)
