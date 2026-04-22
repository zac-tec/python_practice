"""
QUESTION 3: Student Grade Classifier
You have a dictionary of students and their marks.
Task: Create a new dictionary called 'status'. 
- If the mark is 50 or above, the value should be "Pass". 
- If it is below 50, the value should be "Fail".
Challenge: Try using a dictionary comprehension.

Input:
results = {"Arjun": 85, "Sita": 42, "Varun": 91, "Deepa": 55}

Expected Output:
{'Arjun': 'Pass', 'Sita': 'Fail', 'Varun': 'Pass', 'Deepa': 'Pass'}
"""

# Write your code below:
names=input("enter the names of student:")
names=names.split()
marks=input("enter the marks of student:")
marks=marks.split()
# result=dict.fromkeys(names,marks)
# print(result)
result = {names[i]: int(marks[i]) for i,j in enumerate(names)}
status={}
for i,j in result.items():
    if j >= 50:
        status[i]="pass"
    else:
        status[i]="fail"  

for i,j in result.items():
    print(f"{i}: {j}")
    
for i,j in status.items():
    print(f"{i}: {j}")         