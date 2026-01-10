"""
POS System Startup Script
Allows user to choose between CLI or GUI version
"""

import sys


def show_menu():
    """Display startup menu"""
    print("=" * 50)
    print("          Point of Sale System (POS)")
    print("=" * 50)
    print("Please select startup mode:")
    print("1. Graphical Interface (GUI) - Recommended")
    print("2. Command Line Interface (CLI)")
    print("0. Exit")
    print("=" * 50)


def main():
    """Main function"""
    while True:
        show_menu()
        choice = input("Please enter option (0-2): ").strip()
        
        if choice == "1":
            print("\nStarting graphical interface...")
            try:
                from main_gui import main
                main()
                break
            except ImportError as e:
                print(f"Error: Cannot import GUI module - {e}")
                print("Please ensure Tkinter is installed")
                input("\nPress Enter to continue...")
            except Exception as e:
                print(f"Error: {e}")
                input("\nPress Enter to continue...")
        
        elif choice == "2":
            print("\nStarting command line interface...")
            try:
                from main import main
                main()
                break
            except Exception as e:
                print(f"Error: {e}")
                input("\nPress Enter to continue...")
        
        elif choice == "0":
            print("\nGoodbye!")
            sys.exit(0)
        
        else:
            print("\nInvalid choice, please try again")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
