import sys
import time

def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def main_menu():
    print("Welcome to the Adventure Game!")
    print("1. New Game")
    print("2. Load Game")
    print("3. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        start_new_game()
    elif choice == '2':
        load_game()
    elif choice == '3':
        print("Thank you for playing!")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def start_new_game():
    print_slow("Creating your character...")
    name = input("Enter your character's name: ")
    print(f"Welcome, {name}! Your journey begins now.")

    character = {
        "name": name,
        "health": 100,
        "inventory": ["Bag","Bottle","Knife","Torch","Match-box"],
    }

    first_scene(character)

def load_game():
    print("Feature under development. Please start a new game.")
    main_menu()

def first_scene(character):
    print_slow("You find yourself in a dense forest, surrounded by towering trees and the sound of rustling leaves.")
    print("1. Explore the forest")
    print("2. Follow the sound of water")

    choice = input("Enter your choice: ")
    if choice == '1':
        explore_forest(character)
    elif choice == '2':
        follow_water(character)
    else:
        print("Invalid choice. Please try again.")
        first_scene(character)

def explore_forest(character):
    print_slow("You venture deeper into the forest and come across a strange glowing object.")
    print("1. Pick it up")
    print("2. Ignore it")

    choice = input("Enter your choice: ")
    if choice == '1':
        character["inventory"].append("Glowing Stone")
        print("You picked up the Glowing Stone. It feels warm in your hand.")
        hidden_cave(character)
    elif choice == '2':
        print("You decide to leave the object and move on.")
        mysterious_hut(character)
    else:
        print("Invalid choice. Please try again.")
        explore_forest(character)

def follow_water(character):
    print_slow("You follow the sound of water and find a crystal-clear stream.")
    print("1. Drink from the stream")
    print("2. Search around the stream")

    choice = input("Enter your choice: ")
    if choice == '1':
        print("You feel refreshed as you drink the cool water. Your health improves.")
        character["health"] += 10
        hidden_cave(character)
    elif choice == '2':
        print("You find a hidden pouch containing a map and some gold coins.")
        character["inventory"].extend(["Map", "Gold Coins"])
        mysterious_hut(character)
    else:
        print("Invalid choice. Please try again.")
        follow_water(character)

def hidden_cave(character):
    print_slow("You discover a hidden cave behind some bushes. Inside, there is a treasure chest.")
    print("1. Open the chest")
    print("2. Leave the cave")

    choice = input("Enter your choice: ")
    if choice == '1':
        print("The chest contains a magical sword. You take it.")
        character["inventory"].append("Magical Sword")
        next_action(character)
    elif choice == '2':
        print("You decide to leave the cave and continue your journey.")
        next_action(character)
    else:
        print("Invalid choice. Please try again.")
        hidden_cave(character)

def mysterious_hut(character):
    print_slow("You come across a mysterious hut.\nA wise old man greets you.")
    print("1. Talk to the old man")
    print("2. Ignore the hut and move on")

    choice = input("Enter your choice: ")
    if choice == '1':
        print_slow("The old man gives you a riddle to solve.")
        solve_riddle(character)
    elif choice == '2':
        print_slow("You decide to continue your journey.")
        next_action(character)
    else:
        print("Invalid choice. Please try again.")
        mysterious_hut(character)

def solve_riddle(character):
    print("Riddle: What has to be broken before you can use it?")
    answer = input("Your answer: ").strip().lower()
    if answer == "egg":
        print_slow("Correct! The old man gives you a healing potion.")
        character["inventory"].append("Healing Potion")
        next_action(character)
    else:
        print_slow("Incorrect. The old man shakes his head.")
        next_action(character)

def next_action(character):
    print_slow("What would you like to do next?")
    print("1. Check inventory")
    print("2. Continue your journey")

    choice = input("Enter your choice: ")
    if choice == '1':
        print_slow(f"Inventory: {character['inventory']}")
        next_action(character)
    elif choice == '2':
        print_slow("Your journey continues...")
        print_slow("To be continued...")
    else:
        print("Invalid choice. Please try again.")
        next_action(character)

if __name__ == "__main__":
    main_menu()
