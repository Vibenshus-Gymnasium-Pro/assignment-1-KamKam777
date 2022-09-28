#PythonCrashCourse5-10

#creating the lists, with "JoHn" at the end, to test upper- and lowercase checking
current_users = ["GamerBoy88", "PizzaDawg39846", "BigBro420", "HungryLizardHD", "NaMe5", "User190", "JoHn"]
new_users = ["UniqueNormie1", "GamerBoy88", "sicksti6", "NaMe5", "oddDude78", "JOHN"]

#converting both lists to all lowercase using list comprehension, to make the two lists even, when checking for availability
current_users_lower = [users.lower() for users in current_users]
new_users_lower = [users2.lower() for users2 in new_users]

#looping through the new users to check if they already exist, and giving a message based on the result
for user in new_users_lower:
    if user in current_users_lower:
        print("The username '" + user + "' is taken.")
    else:
        print("The username '" + user + "' is valid.")
