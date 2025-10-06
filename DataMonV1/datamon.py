# -*- coding: utf-8 -*-
"""
Datamon

A math problem helper that helps students, teachers and parents
make math fun.

Haylee Kaheel Teresa Aryan James
Created on Wed Sep 10 13:38:34 2025

@author: thear
"""

def menu():
    """
    Displays the menu options.

    Returns
    -------
    None

    """
    print()
    print("=" * 10 + "Menu" + "=" * 10)
    print('1) Answer Checker! ')
    print("2) Memory Bank!")
    print("3) Electro Flash!")
    print("4) Exit")
    print("=" * 24)

def main():
    """
    Main function to handle the menu and the users options.

    Returns
    -------
    None.
    """
    try:
        choice = 0
        

        while choice != "4":
           
            menu()
            
            choice = input("Which one will you choose? ")

            # evaluates the value of choice
            if choice == "1":
                print("option 1: Answer checker.")
                

            elif choice == "2":
                print("\nOption 2: Memory Bank.")
                

            elif choice == "3":
                print("\nOption 3: Electro Flash. ")
               

            
            elif choice == "4":
                # exits program
                print("Exit Program: GoodBye!")
            else:
                print("\nPlease include an option between 1 and 4!")

    except FileNotFoundError as err:
        print(f"Error: File not found - {err}")
    except ValueError as err:
        print(f"Error: Invalid value - {err}")


if __name__ == "__main__":
    main()




