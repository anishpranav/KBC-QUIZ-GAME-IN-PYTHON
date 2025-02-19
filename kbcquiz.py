#import random and time module 
import random 
import time 

#print * 80 times 
for i in range(80): 
    print("*", end="") 
    time.sleep(0) 
print() 

print("\t\t\t        Welcome to Kaun Banega Crorepati  ") 

for i in range(80): 
    print("*", end="") 
    time.sleep(0) 
print() 

a = input("\tEnter Your Name - ") 

for i in range(80): 
    print("*", end="") 
    time.sleep(0) 
print() 

print("\n\t\tOK ", a, " Let's Start The Game") 
time.sleep(1) 

questions = [
    "Who is The Prime Minister of India",
    "In Which Country Area 51 is Located",
    "Which one is the largest Continent in the world",
    "What is the Latest Version of Windows Since 2019",
    "Which One of These Is not a Software Company",
    "How Many MB Makes 1 GB",
    "Facebook Was Firstly Developed By",
    "Founder of Apple is",
    "___ is one of The Founder of Google",
    "BIGG BOSS season 13 Starts in __ & ends in __",
    "Apple's Laptop is Also Known as",
    "First Apple Computer is Known as",
    "Joystick is used For",
    "_____ is used to Encrypt Drives in Computer"
]

answer = [
    "Narendra Modi", "United States", "Asia", "Windows 10", "Honda",
    "1024", "Mark Zuckenberg", "Steve Jobs", "Larry Page",
    "2019 - 2020", "Macbook", "Mactonish", "Playing Games", "Bitlocker"
]

wronganswers = [
    ["Amit Shah", "Aditya Nath Yogi", "Azhar Ansari"],
    ["India", "Africa", "Iraq"],
    ["South Africa", "North America", "Europe"],
    ["Windows 7", "Windows 8", "Windows 11"],
    ["Oracle", "Microsoft", "Google"],
    ["10024", "1004", "2024"],
    ["Bill Gates", "Larry Page", "Azhar Ansari"],
    ["Azhar Ansari", "Charles Babbage", "Sundar Pichai"],
    ["Larry Hensberg", "Sunder Pichai", "Bill Gates"],
    ["2020 - 2021", "Not Starts Now", "2018 - 2019"],
    ["ThinBook", "Notebook", "ChromeBook"],
    ["Apple v.1", "Apple Computer", "Appbook"],
    ["Giving output command", "Shutting down Computer", "Log off Computer"],
    ["KeyGuard", "Windows Secure", "No Software like this"]
]

attempquestion = []
count = 1
amount = 0

while True:
    while True:
        selectquestion = random.choice(questions)
        if selectquestion in attempquestion:
            pass
        else:
            attempquestion.append(selectquestion)
            questionindex = questions.index(selectquestion)
            correctanswer = answer[questionindex]
            break

    optionslist = []
    inoptionlist = []
    optioncount = 1

    while optioncount < 4:
        optionselection = random.choice(wronganswers[questionindex])
        if optionselection not in inoptionlist:
            optionslist.append(optionselection)
            inoptionlist.append(optionselection)
            optioncount += 1

    optionslist.append(correctanswer)
    alreadydisplay = []
    optiontodisplay = []

    for _ in range(4):
        while True:
            choice = random.choice(optionslist)
            if choice not in alreadydisplay:
                alreadydisplay.append(choice)
                optiontodisplay.append(choice)
                break

    right_answer = ""
    if correctanswer == optiontodisplay[0]:
        right_answer = "a"
    elif correctanswer == optiontodisplay[1]:
        right_answer = "b"
    elif correctanswer == optiontodisplay[2]:
        right_answer = "c"
    elif correctanswer == optiontodisplay[3]:
        right_answer = "d"

    print("-------------------------------------------------------------------")
    print("\t\t\tAmount Win - ", amount)
    print("-------------------------------------------------------------------")
    time.sleep(1)

    print("\n\t\tQuestion ", count, " on your Screen")
    print("-------------------------------------------------------------------")
    time.sleep(1)
    print("  |  Question - ", selectquestion)
    print("-------------------------------------------------------------------")
    time.sleep(1)

    print("\t|  A. ", optiontodisplay[0])
    time.sleep(1)
    print("\t|  B. ", optiontodisplay[1])
    time.sleep(1)
    print("\t|  C. ", optiontodisplay[2])
    time.sleep(1)
    print("\t|  D. ", optiontodisplay[3])

    useranswer = input("\t\tEnter Correct Option\t   or \t press Q to quit.\n\t\t\t...").lower()

    if useranswer == right_answer:
        amount_map = {1: 1000, 2: 2000, 3: 5000, 4: 10000, 5: 40000, 
                      6: 80000, 7: 160000, 8: 320000, 9: 640000, 10: 1500000}
        amount = amount_map.get(count, amount)

        if count == 10:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("***************************")
            print("\t\t\t \\\\\\\\\\ Congratulations! //////////")
            print("\t\t\t|||||||||| You Won The Game ||||||||||")
            print("***************************")
            print("\n\n\t\t You Won Rs. ", amount)
            print()
            break

        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("***************************")
        print("\t\t\t \\\\\\\\\\ Congratulations! //////////")
        print("\t\t\t|||||||||| Right Answer ||||||||||")
        print("***************************")
        count += 1
    elif useranswer == "q":
        print("\n\n\t\t You Won Rs. ", amount)
        break
    else:
        print("***************************")
        print("\t\t\tWrong Answer")
        print("***************************")
        print("\n\n\t\t \tYou Won Rs. ", amount)
        print("***************************")
        break
