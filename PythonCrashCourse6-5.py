#PythonCrashCourse6-5

riverDict = {   #creating a dictionary of some rivers and their corresponding countries
    "Yangtze":"China",
    "Mississippi":"USA",
    "Volga":"Russia"
}
print("")   #empty space
for key, value in riverDict.items():
    print("The ", end='')
    print(key, end='')
    print(" river is located in ", end='')
    print(value, end='')
    print(".\n")
