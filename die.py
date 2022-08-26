import random
again = True
while again:
     print(random.randint(1,6))
     another_roll = input("do you want to roll the dice again? (yes/no):")
     if another_roll.lower() == "yes":
        continue
     else:
        break


