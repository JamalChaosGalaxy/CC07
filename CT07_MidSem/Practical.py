import random
health = 100;

print(f"Hero starts on his adventure with Health: ", health)
while health > 0:
    damage = random.randint(1,15)
    health -= damage
    print("After finishing monsters, his health is now", health)

