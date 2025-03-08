# # # # print("Hello from lesson 3")

# # i = 1

# # while i < 3:
# #     1 = input ("How many colors are in the rainbow")
# #     if 1 == 7:
# #         print("Correct")
# #         2 = input("How much is 4 + 4")
# #     else:
# #         print("Incorrect")
# #     if 2 == 8:
# #         print("Correct")
# #         3 = input ("How much is 2 + 2")
# #     else:
# #         print("Incorrect")
# #     if 3 == 4:
# #         print("Correct you finished the test")
# #         break
# #     else:
# #         print("Incorrect")

# score = 0
# answer = input("What is the color of the orange")
# while(answer != "orange"):
#     print("Wrong answer try again noob")
#     answer = input("What is the color of the orange")

# print("Correct")
# score = score + 1

# answer = input("What is the color of the sun")
# while(answer != "white"):
#     print("Wrong answer try again noob")
#     answer = input("What is the color of the sun")

# print("Correct")
# score = score + 1

# answer = input("What is the color of an apple")
# while(answer != "red"):
#     print("Wrong answer try again noob")
#     answer = input("What is the color of an apple")

# print("Correct")
# score = score + 1

# import time

# time = int(input("How many minutes do you want to study for?"))
# time = time * 60

# while ( time != 0):
#     print ("seconds")
#     time = time - 1
#     time.sleep(1)

# print("You suck at maths! A- HAIYAAA")

import time

study_time = int(input("How many minutes do you want to study for? "))
study_time = study_time * 60  # convert to seconds

while study_time != 0:
    print(f"{study_time} seconds remaining")
    study_time -= 1  # decrement time by 1 second
    time.sleep(1)  # wait for 1 second

print("Time's up! You've finished studying.")

