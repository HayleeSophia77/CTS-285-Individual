"""
Datamon

A math problem helper that helps students, teachers and parents
make math fun.

Haylee Kaheel Teresa Aryan James
"""

from AnswerChecker import run_math_quiz
from memorybank import memory_bank
from ElectroFlash import electro_flash

def menu():
    print("\n" + "=" * 10 + " Menu " + "=" * 10)
    print("1) Answer Checker")
    print("2) Memory Bank")
    print("3) Electro Flash")
    print("4) Exit")
    print("=" * 30)

def main():
    choice = ""
    while choice != "4":
        menu()
        choice = input("Which one will you choose? ")

        if choice == "1":
            print("\n--- Starting Answer Checker ---\n")
            run_math_quiz()
        elif choice == "2":
            print("\n--- Starting Memory Bank ---\n")
            memory_bank()
        elif choice == "3":
            print("\n--- Starting Electro Flash ---\n")
            electro_flash()
        elif choice == "4":
            print("Exit Program: Goodbye!")
        else:
            print("Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
