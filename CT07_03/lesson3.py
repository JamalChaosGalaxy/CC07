# # print("Hello from lesson 3")
# # savings = 0

# # while savings < 100:
# #     daily_savings = float(input("how much did you save today?"))
# #     savings += daily_savings
# #     # savings = savings + daily_savings

# #     if savings >= 100:
# #         print("Congratulations you asian cheapskate you saved 100 dollars fuiyohh")
# #         break

# # while savings <= 100:
# #     daily_savings = float(input("how much did you save today?"))
# #     savings += daily_savings
# #     #  savings = savings + daily_savings

# # print("Congratulations you asian cheapskate you saved 100 dollars fuiyohh")

# import random

# total_Qns = 15
# lives = 3

# for i in range(total_Qns):
#     num1 = random.randint(2,20)
#     num2 = random.randint(2,20)
#     correct_ans = num1 * num2

#     while lives>0:
#         answer = int(input(f"what is {num1} x {num2} ?"))

#         if answer == correct_ans:
#             print(f"Correct!")
#             break;
#         else:
#             lives -= 1
#             print("Wrong try again")

#         if lives == 0:
#             print("Go and see MS Tan for Remedial!")

# if lives > 0:
#     print("Congrats you have completed the quiz!")

# line = "ROBLOX,USD,0,813345,4.5,Games"
# words = line.split(",")
# print(words[1])


import math

score = [90, 45, 56, 61, 79, 89, 92, 86, 74, 64, 59]

maximum = math.max(max)
minimum = math.min(min)