#PythonCrashCourse7-4

prompt = "\nEnter your preferred toppings, one at a time, and they'll be added to your pizza!: "
prompt += "\nEnter 'quit' to finish. "

addTopping = True #making a boolean that stays true until the user types 'quit'

while addTopping:
    userInput = input(prompt)
    if userInput == 'quit':
        addTopping = False
    else:
        print("")
        print("'" + userInput + "' will be added to your pizza!")
