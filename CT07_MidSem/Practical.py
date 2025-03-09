import random
health = 100;

battles = []
print(f"Hero starts on his adventure with Health: ", health)
while health > 0:
    damage = random.randint(1,15)
    health -= damage
    print("After finishing monsters, his health is now", health)
    i += 1
    
