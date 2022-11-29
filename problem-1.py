###################################################################
## Take input 2 int list and Concatinate two list index wise ##
###################################################################


my_input_1 = input("Please input list-1 number useing ',' :")
my_input_2 = input("Please input list-2 number useing ',' :")

list_1 = my_input_1.split(",")
list_2 = my_input_2.split(",")

for i in range(len(list_1)):
    list = int(list_2[i])+int(list_1[i])
    print(list)

