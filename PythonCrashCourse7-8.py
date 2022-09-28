#PythonCrashCourse7-4

sandwich_orders = ["Tuna deluxe", "Falafel pita", "Chicken fajita", "Breakfast bagel"]
finished_sandwiches = []

for i in sandwich_orders:
    print("Your '" + i + "' order has been placed :)")
    finished_sandwiches.append(sandwich_orders) #moving sandwiches from "ordered" state to "finished" state
finish_the_sandwich = sandwich_orders.pop() #deleting the items from the "ordered" state

for n in finished_sandwiches:
    print("Your ", end='')
    print(n, end='')
    print(" order is finished!")
