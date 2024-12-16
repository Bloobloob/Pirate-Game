import time

# Game Introduction
print("Ahoy captain! I see ye're ready for adventure!")
time.sleep(3)
print("Err, has no one told you the rules??? (y/n)")
played_before = input().lower()  # Convert input to lowercase for consistency.

# Initialize game state variables
life = True  # Track the player's life state
has_sword = False  # Track if the player has acquired a sword

# Game Loop
if played_before == "y":
    print("Yarrr, let's get started then... but you need to first pick a name...")
    name = input("What's your pirate name, Captain? ")
    print(f"Welcome aboard, Captain {name}!")
    
    while life:  # Keep looping as long as the player is alive
        # First Encounter
        print("\nThis sailor is demanding your money! What do you do, Captain?")
        print("1 - YOU KILL HIM")
        print("2 - You forgive him, renouncing worldly possessions. After all, what is money but a made-up idea?")
        print("3 - YOU SHOUT")
        q1 = input("Choose an action (1, 2, or 3): ")

        if q1 == "1":
            print("You attack the pirate, and he flees, leaving behind his sword. +1 sword!")
            has_sword = True
        elif q1 == "2":
            print("The sailor is moved by your generosity and offers you his eternal loyalty.")
            print("Congratulations, Captain! You gain a loyal crewmate.")
        elif q1 == "3":
            print("The pirate shoots you! You are dead.")
            life = False
            break
        else:
            print("RAWR!!! Invalid choice! The sailor stares at you in confusion.")
            continue

        # Second Encounter
        print("\nYou keep walking for three hours when you stumble upon a village.")
        time.sleep(3)
        print("Inside the village, you find a big temple with two ways to go:")
        print("1 - Left")
        print("2 - Right")
        print("3 - Death")
        q2 = input("Choose an action (1, 2, or 3): ")

        if q2 == "1":
            print("You find a zombie! OH MY GOD, WHAT? A ZOMBIE IN A PIRATE GAME?!")
            if has_sword:
                print("You take out your huge sword and kill the evil zombie.")
                time.sleep(3)
                print("+1 zombie innards!")
            else:
                print("The zombie attacks you! Without a sword, you cannot escape.")
                print("Surprisingly, the zombie turns you into one of them... but you don't die?")
                print("Okay... yay, zombie pirate!")
        elif q2 == "2":
            print("You walk into a long, long, long, long hallway...")
            time.sleep(3)
            print("And it keeps going...")
            print("And going...")
            time.sleep(2)
            print("Finally, you find a treasure chest!")
        elif q2 == "3":
            print("You chose death! Glitter and roses shower over you as you perish.")
            life = False
        else:
            print("RAWR!!! Invalid choice! The mysterious forces of the temple stare at you in confusion.")

        # Final Scene
        if life:
            print("\nOn the other side of the temple, you find yourself on a desolate beach...")
            print("With giant crabs. So very big crabs. Scary!")
        else:
            print("You have met your end. Yippieee!")

    print("\nGame Over. Thank you for playing!")
else:
    print("Go to pirate hell!")  # Playful pirate tone

