from DNAclass import DNA
from File_operations import File_operations
from OperationsSubmenu import OperationsSubmenu
import os

class Interface:
    """Interface of the DNA playground program"""

    def __init__(self):
        self.file_op = File_operations()
        self.sequence = None
        self.is_sequence_saved = True  # Flag to track if the sequence has been saved

    def menu(self):
        """Main menu loop"""
        while True:
            self.display_menu()
            self.display_sequence()
            choice = input("··· Provide a letter from the menu! > ").strip().upper()
            if choice == "B":
                self.bake_dna()
            elif choice == "E":
                self.save_dna()
            elif choice == "L":
                self.list_dna()
            elif choice == "T":
                self.load_dna()
            elif choice == "U":
                self.delete_dna()
            elif choice == "O":
                self.open_DNAoperations_submenu()
            elif choice == "S":
                if not self.is_sequence_saved and self.sequence:
                    print("\nYou have an unsaved sequence on the plate!")
                    save_choice = input("Would you like to save it before exiting? (Y/n): ").strip().lower()
                    if save_choice == "y":
                        self.save_dna()
                    else:
                        print("Exiting without saving...")
                print("\nExiting the DNA playground. See you next time!")
                break
            else:
                input("Invalid choice. Please select a valid option.")

    def display_menu(self):
        """Display the main menu"""
        print("""
· · · · · · · · Welcome   to   the DNA playground · · · · · · · · ·
        ~ MENU ~
        --------
        B - Bake a fresh DNA            (Create DNA chain)
        O - Open to spice up your DNA!  (Operations with DNA)  
        L - List DNA stock              (List of all the DNA available)
        E - Establish DNA recipe        (Save DNA)
        T - Take DNA from freezer       (Load DNA)
        U - Unwanted DNA to discard     (Delete DNA)
        S - Stop cooking                (Exit)
-------------------------------------------------------------------""")

    def display_sequence(self):
        """Display the current DNA sequence"""
        if self.sequence:
            print(f"You got a FRESH sequence: * {self.sequence} *")
        else:
            print("*** No DNA on the plate yet ***")
        print("-------------------------------------------------------------------")
    
    def bake_dna(self):
        """Bake a fresh DNA sequence"""
        while True:
            try:
                length = int(input("··· Lets bake a DNA sequence! Enter the desired length: "))
                if length <= 0:
                    raise ValueError("The length must be a positive number.")
            except ValueError as e:
                print(f"Invalid input: {e}")
                continue

            seq = DNA("")
            self.sequence = seq.create_seq(length)
            self.is_sequence_saved = False  # Sequence modified
            print(f"""Here is your freshly made DNA sequence! 
            *** {self.sequence} ***""")
            input("Let's get it to the main menu!")
            break

    def save_dna(self):
        """Save the current DNA sequence to a file"""
        if not self.sequence:
            print("\nNothing to save! You must bake (B) or take (T) a sequence onto the plate...")
            input("Press ENTER to confirm.")
            return

        file_name = input("··· Let's establish this DNA. Enter a file name: ").strip()
        self.file_op = File_operations(file_name)
        self.file_op.save(DNA(self.sequence))
        print(f"Your DNA sequence has been saved to {self.file_op.directory}/{self.file_op.file}")
        self.is_sequence_saved = True
        input("Well done! Press ENTER to go back to the main menu.")

    def list_dna(self):
        """List all available DNA sequences"""
        raw_list, _, _ = self.file_op.list_info()
        if not raw_list:
            print("\nNothing here! You must bake (B) and establish (E) some DNA.")
            input("Press ENTER to confirm.")
            return False
        
        print("\nThese are all the DNA sequences available at the moment:")
        print("\t[Id] - Length, Sequence")
        print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for item in raw_list:
            print(f"\t{item}")
        input("Press ENTER to back to the main menu.")
        return True
    
    def load_dna(self):
        """Load a DNA sequence from the list"""
        if not self.list_dna():
            return
        while True:
            number = input("··· Enter the [Id] of the DNA to load: ").strip()
            valid_number = self.check_number(number)
            if valid_number is None:
                input("Please enter a number. Press ENTER.")
                continue

            loaded_sequence = self.file_op.load(valid_number)
            input(f"This is the sequence that we are taking: {loaded_sequence}")
            self.sequence = loaded_sequence
            break

    def delete_dna(self):
        """Delete a DNA sequence from the list"""
        if not self.list_dna():
            return
        while True:
            number = input("··· Enter the [Id] of the DNA to delete: ").strip()
            valid_number = self.check_number(number)
            if valid_number is None:
                input("Please enter a valid number. Press ENTER.")
                continue

            filepath = self.file_op.filedic.get(valid_number)
            if not filepath:
                input("Invalid ID. Please try again. Press ENTER.")
                continue

            print(f"Are you sure you want to delete the sequence {self.file_op.load(valid_number)}?")
            choice = input("(Y/n): ").strip().lower()
            if choice == "y" and os.path.exists(filepath):
                os.remove(filepath)
                print(f"File '{filepath}' deleted successfully.")
                input("Press ENTER to back to the main menu.")
            else:
                print("Deletion canceled.")
            break

    def open_DNAoperations_submenu(self):
        """Open the DNA operations submenu"""
        if not self.sequence:
            print("\nNo DNA loaded! Bake (B) or load (T) one first.")
            input("Press ENTER to return to the main menu.")
            return
        
        input("\nEmbarking onto DNA Operations... Press ENTER.")
        DNAoperations = OperationsSubmenu(self.sequence) 
        modified_sequence = DNAoperations.submenu()
        if modified_sequence:
            self.sequence = modified_sequence
            self.is_sequence_saved = False  # Sequence modified

    def check_number(self, number):
        """Validate a number input"""
        _, _, num = self.file_op.list_info()
        max_id = num - 1
        try:
            value = int(number)
            if value <= 0 or value > max_id:
                raise ValueError("The number is out of range.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")
            return None
        

if __name__ == "__main__":
    app = Interface()
    app.menu()
