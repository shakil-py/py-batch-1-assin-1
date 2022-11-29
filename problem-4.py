list_1=[5,15,20,12,20,13,20,14,20]
print("frist list : ",list_1)
for i in range(len(list_1)):
    # if list_1[i]==20:
    #     list_1=list_1.remove(20)
    #     print(list_1)
    if 20 in list_1:
        list_1.remove(20)
print("After loop list : ",list_1)
