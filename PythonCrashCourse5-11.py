#PythonCrashCourse5-11

numbers = list(range(1, 10)) #creating the list

for i in numbers: #looping through the numbers and defining what should happen to the first three numbers
    if i == 1:
        print(i, end='')
        print("st")
    elif i == 2:
        print(i, end='')
        print("nd")
    elif i == 3:
        print(i, end='')
        print("rd")
    else:
        print(i, end='')
        print("th")
