print("Welcome to my computer quiz!")

playing = input("Are you ready to be tested on basic computer acronyms and definitions?")

if playing != "yes":
    quit()

print("Alright! Let's see how you will do :)")
score = 0

answer= input("1.What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Oops! You are wrong :<")

answer= input("2. What does GPU mean? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Oops! You are wrong :<")

answer= input("3.What is AI? ")
if answer.lower() == "artificial intelligence":
    print('Correct!')
    score += 1
else:
    print("Oops! You are wrong :<")

answer= input("4.What is RAM? ")
if answer.lower() == "Random Access Memory":
    print('Correct!')
    score += 1
else:
    print("Oops! You are wrong :<")

answer= input("5.What is ASCII ")
if answer.lower() == "american standard code for information interchange":
    print('Correct!')
    score += 1
else:
    print("Oops! You are wrong :<")

answer= input("6.What is ALU? ")
if answer.lower() == "arithmetic logic unit":
    print('Correct!')
    score += 1
else:
    print("Oops! You are wrong :<")

answer= input("7.What is USB ")
if answer.lower() == "universal serial bus":
    print('Correct!')
    score += 1
else:
    print("Oops! You are wrong :<")

answer= input("8.What is IoT? ")
if answer.lower() == "internet of things":
    print('Correct!')
    score += 1
else:
    print("Oops! You are wrong :<")

answer= input("9.What is HTML? ")
if answer.lower() == "hyper text markup language":
    print('Correct!')
    score += 1
else:
    print("Oops! You are wrong :<")

answer= input("10.What is BIOS? ")
if answer.lower() == "basic input-output services":
    print('Correct!')
    score += 1
else:
    print("Oops! You are wrong :<")

print("You got " + str(score) + " questions correct! ")
print("You got " + str((score /10)*100) + "%.")