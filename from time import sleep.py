from time import sleep
from math import *
import random
import string

print("This project is a multitasking toolbox")

tool = input("Pick what you want: 1- Basic Calculator, 2- Mad Libs Games, 3- Currency Converter, 4- Number Guessing Game, 5- Unit Converter, 6- To-Do List, 7- Rock Paper Scissors, 8- Password Generator, 9- Quiz Game: ")

if tool == "1":
    operand = input("Ok.. cool! Pick a function: 1- Addition, 2- Subtraction, 3- Multiplication, 4- Division, 5- Exponentiation: ")
    
    if operand in ["1", "2", "3", "4", "5"]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        match operand:
            case "1":
                print("The answer is " + str(num1 + num2))
            case "2":
                print("The answer is " + str(num1 - num2))
            case "3":
                print("The answer is " + str(num1 * num2))
            case "4":
                print("The answer is " + str(num1 / num2))
            case "5":
                print("The answer is " + str(num1 ** num2))
    else:
        print("Invalid bro")

elif tool == "2":
    print("That'll certainly be fun... however, remember to be respectful, and these Mad Libs are not mine; I got them from the internet.")
    madlibsno = input("Which Mad Libs game do you want to play? 1- Jungle Adventure: ")
    match madlibsno:
        case "1":
            w1 = input("Type an adjective: ")
            w2 = input("Type a plural noun: ")
            w3 = input("Type a plural noun: ")
            w4 = input("Type a noun: ")
            w5 = input("Type an adjective: ")
            w6 = input("Type an animal sound: ")
            w7 = input("Type a name of a person: ")
            w8 = input("Type an adjective: ")
            w9 = input("Type an animal: ")
            w10 = input("Type a plural noun: ")
            w11 = input("Type a name of a person: ")
            w12 = input("Type an adjective: ")
            w13 = input("Type an adjective: ")
            w14 = input("Type an animal: ")
            w15 = input("Type a food item: ")
            w16 = input("Type a food item: ")
            w17 = input("Type an adjective: ")
            w18 = input("Type an adjective: ")
            w19 = input("Type an adjective: ")
            w20 = input("Type an adjective: ")
            w21 = input("Type a name of a person: ")
            w22 = input("Type a verb: ")
            w23 = input("Type an adjective: ")
            w24 = input("Type an animal: ")
            w25 = input("Type a name of a person: ")
            w26 = input("Type a plural noun: ")
            w27 = input("Type a plural noun: ")
            w28 = input("Type an adjective: ")
            w29 = input("Type a name of a person: ")
            w30 = input("Type a noun: ")
            w31 = input("Type an adjective: ")

            print(f"One sunny morning, a group of {w1} adventurers set off on a journey into the wild, untamed Amazon jungle. They packed {w2}, {w3}, and a giant {w4}, just in case they encountered a {w5} problem. As they walked through the dense jungle, they suddenly heard a loud {w6}. What was that?! yelled {w7}, looking around nervously. Out of the trees, a massive {w8} {w9} appeared, covered in {w10}. 'This is it!' screamed {w11}, 'We’re gonna get {w12}!' But just then, a {w13} {w14} swooped down and stole their last bag of {w15}! 'No! Not the {w16}!' cried the group. 'We’ll never survive the jungle without it!' They quickly followed the {w17} creature into the jungle, which led them to a {w18} waterfall. Beneath the water, they saw something shiny, a {w19} treasure chest! 'It’s the legendary {w20} treasure!' shouted {w21}. 'Let’s open it!' But as they touched the chest, the ground began to {w22}, and a giant {w23} {w24} burst from the earth! 'RUN!' yelled {w25}. The group sprinted through the jungle, dodging {w26} and {w27}, until they reached the safety of a {w28} treehouse. Panting and out of breath, {w29} wiped their brow and sighed, 'Well, at least we still have our {w30}... and our {w31} sense of adventure.'")
        case _:
            print('Invalid Mad Libs game selected.')

elif tool == "3":
    print("You chose the currency converter. Please note: to use this tool, you need to first specify how 1 of the first currency equals the second (i.e., 1 currency one = x currency two).")
    confac = input("Input the conversion factor (x): ")
    money = input("Now type how many of the first currency you want converted: ")
    print(f"This is equal to {float(confac) * float(money)}")

elif tool == "4":
    number = random.randint(1, 100)
    attempts = 0
    print("You chose the number guessing game.")
    print("I'm thinking of a number between 1 and 100.")
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < number:
            print("Too low... Try again bro...")
        elif guess > number:
            print("Too high... Try again.")
        else:
            print(f"Congrats! You guessed it in {attempts} attempts. NOT BAD!")
            break

elif tool == "5":
    print("You chose the unit converter. Options: 1- Kilometers to Miles, 2- Celsius to Fahrenheit, 3- Kilograms to Pounds.")
    choice = input("Pick a conversion (1-3): ")
    if choice == "1":
        km = float(input("Enter distance in kilometers: "))
        miles = km * 0.621371
        print(f"{km} kilometers is {miles} miles.")
    elif choice == "2":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit.")
    elif choice == "3":
        kgs = float(input("Enter weight in kilograms: "))
        pounds = kgs * 2.20462
        print(f"{kgs} kilograms is {pounds} pounds.")
    else:
        print("Sorry, invalid choice. Please rerun the app.")

elif tool == "6":
    tasks = []
    print("Welcome to the To-Do List!")

    while True:
        print("\n1. Add Task, 2. View Tasks, 3. Delete Task, 4. Exit")
        taskpick = input("Pick an option: ")
        if taskpick == "1":
            newtask = input("Enter a task: ")
            tasks.append(newtask)
            print(f"Task '{newtask}' added.")
        elif taskpick == "2":
            if tasks:
                print("Your tasks: ")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks yet.")
        elif taskpick == "3":
            if tasks:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Task '{removed_task}' deleted.")
                else:
                    print("Invalid task number.")
            else:
                print("No tasks to delete.")
        elif taskpick == "4":
            print("Goodbye!!!!")
            break
        else:
            print("Invalid choice.")

elif tool == "7":
    rpc = ["rock", "paper", "scissors"]
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors) or 'quit': ").lower()
        if user_choice == "quit":
            print("Thanks for playing!")
            break
        if user_choice not in rpc:
            print("Invalid choice. Try again.")
            continue
        computer_choice = random.choice(rpc)
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

elif tool == "8":
    print("You chose the password generator.")
    length = int(input("Enter the length of the password: "))
    include_symbols = input("Include symbols? (y/n): ").lower() == "y"
    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Your password is: {password}")

elif tool == "9":
    questions = [
        {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin"], "answer": "Paris"},
        {"question": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
        {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter"], "answer": "Mars"}
    ]
    score = 0
    print("You chose the quiz game. Welcome!")
    for q in questions:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")
        user_answer = input("Enter your answer (1-3): ")
        if q["options"][int(user_answer) - 1] == q["answer"]:
            print("That's right!")
            score += 1
        else:
            print("Incorrect!")
    print(f"\nYour final score is {score}/{len(questions)}.")

else:
    print("Invalid tool selected.")
