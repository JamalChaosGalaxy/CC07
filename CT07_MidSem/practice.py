Regiplate = input("What is your registration plate?")
Skibidi = Regiplate.split(",")

numbers = 0
aplha = 0
for letter in Skibidi:
    if letter.isdigit:
        numbers += 1
    if letter.isalpha:
        alpha += 1

if aplha > 4 or numbers > 4:
    print("Car registration is invalid")

