#Types of list
#List with Integers
list_a = [1, 2, 3, 4, 5]
#list with int and string $ bool$a float
list_b = [1, "today", True, 3.89]
#list with a string
list_c = ["James", "Dan", "Ann"]
#a nested list
list_d = [1, 2, 3, [4, 5], 6, 7]
#void list
list_e = []

# print(list_a[0])
# print(list_d[4])
list_a[0] = 12
#print(list_a)
#insertion
#print(len(list_a))
list_a.insert(len(list_a), 6)
list_a.append(10)
print (list_a)
list_a.extend([8, 9])
list_a.pop(6)
del list_a[0]

for item in list_a:
    print(item)
    

