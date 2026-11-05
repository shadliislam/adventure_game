# adventure_game.py
# A text-based adventure game where the player searches for a legendary treasure.

def forest_path():
    print("\nYou enter the dark forest.")
    print("You see a river and a tall tree.")
    choice = input("Do you want to follow the river or climb the tree? ").lower()

    if choice == "follow the river" or choice == "river":
        print("\nYou follow the river and discover an ancient bridge.")
        print("Crossing the bridge leads you to the legendary treasure!")
        print("🎉 Congratulations! You found the treasure and won the game! 🎉")
    elif choice == "climb the tree" or choice == "tree":
        print("\nYou climb the tree and spot a path.")
        print("Unfortunately, you lose your footing and fall.")
        print("💀 Game Over!")
    else:
        print("\nInvalid choice. You become lost in the forest.")
        print("💀 Game Over!")


def cave_path():
    print("\nYou enter the mysterious cave.")
    choice = input("Do you light a torch or proceed in the dark? ").lower()

    if choice == "light a torch" or choice == "torch":
        print("\nThe torch reveals hidden markings on the wall.")
        print("Following the markings, you discover the legendary treasure!")
        print("🎉 Congratulations! You found the treasure and won the game! 🎉")
    elif choice == "proceed in the dark" or choice == "dark":
        print("\nYou stumble in the darkness and fall into a deep pit.")
        print("💀 Game Over!")
    else:
        print("\nInvalid choice. You lose your way in the cave.")
        print("💀 Game Over!")


def start_game():
    print("======================================")
    print("    WELCOME TO THE ADVENTURE GAME")
    print("======================================")

    player_name = input("What is your name, explorer? ")

    print(f"\nWelcome, {player_name}!")
    print("Your quest is to find the legendary treasure.")
    print("Choose your path carefully.")

    choice = input(
        "\nDo you want to explore the forest or enter the cave? "
    ).lower()

    if choice == "forest":
        forest_path()
    elif choice == "cave":
        cave_path()
    else:
        print("\nThat is not a valid path.")
        print("💀 Game Over!")


def play_game():
    while True:
        start_game()

        restart = input("\nWould you like to play again? (yes/no): ").lower()

        if restart != "yes":
            print("\nThank you for playing. Goodbye!")
            break


# Start the game
play_game()