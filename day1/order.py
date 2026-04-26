"""
QUESTION 2: The Duplicate Remover (Order Preserved)
Python's set() removes duplicates but loses the original order.
Task: Given a list of data, write a script that removes duplicates 
but keeps the original order of the first appearance of each element.

Input:
data = [1, 2, 2, 3, 4, 4, 5, 1]

Expected Output:
[1, 2, 3, 4, 5]
"""

# Write your code below:
data=input("enter the data;")
print(type(data))
data=data.split()
print(type(data))
unique =[]

data_set = set(data)
print(data_set)

# for i,j in enumerate(data_set):
#     print(i,j)

# for i in range (len(data_set)):
#     print(data_set[i])
    
# for index, element in enumerate(data_set):
#     print(index, element) 
# from rony
    
    
for i in data:
    if i not in unique:
        unique.append(i)
print(unique)   