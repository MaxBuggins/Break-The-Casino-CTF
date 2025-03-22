import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slot_animation():
    frames = [
        "╔══╗\n║  ║\n║  ║\n╚══╝",
        "╔══╗\n║│ ║\n║ │║\n╚══╝",
        "╔══╗\n║ │║\n║│ ║\n╚══╝"
    ]
    
    for _ in range(5):  # Spin the animation 5 times
        for frame in frames:
            clear_screen()
            print(frame)
            time.sleep(0.1)

def main_menu():
    clear_screen()
    print("Welcome to the Slot Machine Game!")
    while True:
        try:
            rows = int(input("Enter the number of rows: "))
            columns = int(input("Enter the number of columns: "))
            if rows > 0 and columns > 0:
                break
            else:
                print("Rows and columns must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return rows, columns

def generate_slot_machine(rows, columns):
    symbols = ['A', 'B', 'C', 'D', 'E']
    return [[random.choice(symbols) for _ in range(columns)] for _ in range(rows)]

def display_slot_machine(slot_machine):
    print("\n--- Slot Machine ---")
    for row in slot_machine:
        print(" | ".join(row))
    print("-------------------")

def check_jackpot(slot_machine):
    for row in slot_machine:
        if len(set(row)) == 1:  # All symbols in the row are the same
            return True
    return False

def main():
    rows, columns = main_menu()
    while True:
        slot_animation()  # Show spin animation
        clear_screen()  # Clear screen to display slot machine result cleanly
        
        slot_machine = generate_slot_machine(rows, columns)
        display_slot_machine(slot_machine)

        if check_jackpot(slot_machine):
            print("JACKPOT! 🎉")
        else:
            print("Try Again!")

        play_again = input("\nSpin again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
