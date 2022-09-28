#PythonCrashCourse4-9

#making a list with numbers 1-10
listOne = list(range(1, 11))
#making a second one that "cubes" all the numbers in the first one using list comprehension
listTwo = [i**3 for i in listOne]
#printing the new second list
print(listTwo)
