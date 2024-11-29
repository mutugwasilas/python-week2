"""question 1"""
my_list = []

print(my_list)

"""question 2"""
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

"""question 3"""
my_list.insert(1,15)
print(my_list)

"""question 4"""
list = [50, 60, 70]
my_list.extend(list)
print(my_list)

"""question5"""
del my_list[-1]
print(my_list)

"""question 6"""
my_list.sort()
print("sorted list:", my_list)

index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)