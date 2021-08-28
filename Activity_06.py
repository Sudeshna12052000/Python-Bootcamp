my_list1 = input().split()
my_list1[::-1]
print("Reversed list = ",my_list1)
new_list1 = my_list1[0:3]
print("sliced list = ", new_list1)
my_list1[0] = 0
new_list1[0] = 0
my_list1[-1] = 0
new_list1[-1] = 0
print("replaced list-1 = ", my_list1)
print("replaced list-2 = ",new_list1)
