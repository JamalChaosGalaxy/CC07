# print("Hello from lesson 4")

# solarsystem = [
#     "Mercury",
#     "Venus",
#     "Earth",
#     "Mars",
#     "Jupiter",
#     "Saturn",
#     "Uranus",
#     "Neptune"
# ]

# print(solarsystem[3])
# solarsystem[3] = "Skibidi"
# print(solarsystem[3])
# print(len(solarsystem))

# solarsystem.insert(3, "hi")
# solarsystem.append("end")

# solarsystem.insert(3, "lalaland")
# solarsystem.append("Pluto")

# # solarsystem.pop(5)
# # del(solarsystem[5])

# for counter in range(len(solarsystem)):
#     print(solarsystem[counter])

#     if counter == 2:
#         print("this is my home")
#     if counter == 4:
#         print("conquered this")
#     if counter == 3:
#         print("created this")

# countries = []
# i = 0

# while True:
#     country = input("What is a country you would like to visit?")

#     if country == "End":
#         break

#     countries.append(country)
#     i += 1 

# for country in countries:
#         print(f"I would like to visit {country}")

menu = []
i = 0

while True:
    food = input("What would you like to add to the menu?")
    if food == "end":
        break

    menu.append(food)
    i += 1 

for food in menu:
        print(f"I would like to add {food} to the menu!")

chad = input("What would you like to it")

# i = 0

while True:
    for i in range(len(menu)):
        if chad == menu[i]:
            print ("Yes, we do have it, please take a seat.")

        else:
            i += 1
        if i == len(menu):
             print

    print("Sorry we dont have it")

    if chad == "end":
        print ("Ok, we will get you order ready for you, please take a seat.")
        break

