"""
QUESTION 4: Nested List Flattener
You are given a list that contains other lists.
Task: Use nested loops to "flatten" this into a single list.
Do not use external libraries like numpy or itertools.

Input:
nested_list = [[1, 2], [3, 4], [5, 6]]

Expected Output:
[1, 2, 3, 4, 5, 6]
split function is only work for strings so that convert the last single string into numericals

"""

# Write your code below:
# # print("enter the nested list:")
# nested_list=input()
# nested_list=nested_list.split()
# print(nested_list)
# for i in range(len(nested_list)):
#     nested_list[i]=nested_list[i].split(",")
# print(nested_list) 

input_list=input("enter the nested list:")
input_list=input_list.split()
print(input_list)
nested_list=[]
for i in input_list:
    nested_list.append(i.split(","))
print(nested_list)

flat_list=[]
for i in nested_list:
    for j in i:
        flat_list.append(j)
print(flat_list)

num_list=[]
for i in flat_list:
    num_list.append(int(i))
print(num_list)