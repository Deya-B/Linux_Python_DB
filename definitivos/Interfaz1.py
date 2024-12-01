from DNAclass import DNA
from File_operations import File_operations
import os

class Interface1():
    """Interface of the DNA playground program"""

    def listing(self, file_op):
        """Handling listing. Obtain the listing of .dna present. Used by list, load and delete.\n
        Parameters: file class"""
        raw_list,_,_ = file_op.list_info()
        if len(raw_list) == 0:
            print("""\nNothing here! 
    You must bake(B) and establish(E) some DNA so you can work with them.""")
            input("""Press ENTER to confirm.""")
            return False
        else:
            print("\t[Id]-Length,Sequence")
            for item in raw_list:
                print(f"\t{item}")
            
# MAIN PROGRAM:
    def menu(self, sequence = None, choice = "", file = None, file_op = File_operations()):
        """Display and control the menu"""
        print("""           
                · Welcome   to   the ·
        *********** DNA playground **************""")
        menu = ("""
                      ~ MENU ~
                
        B - Bake a fresh DNA            (Create DNA chain)
        O - Open to spice up your DNA!  (Operations with DNA)  
        L - List DNA stock              (List of all the DNA available)
        E - Establish DNA recipe        (Save DNA)
        T - Take DNA from freezer       (Load DNA)
        U - Unwanted DNA to discard     (Delete DNA)
        S - Stop cooking                (Exit)
                  """)
        
        while True:
            print(menu)

        # Show current sequence under menu
            if sequence == None:    
                sequence = "*** No DNA on the plate yet ***"
                print(sequence)
                sequence = None
            else:
                print(f"You got a FRESH sequence: * {sequence} *")

        # Choices
            choice = input("""\n\tWhat would you like to do? 
                ··· Provide the letter from the menu! > """).strip().upper()
            if choice not in "BOLETUS":
                print("Invalid character! Please enter a valid letter from the menu.")
                input("Press ENTER to go back to the DNA playground menu...")
                continue
        
        # Bake/CREATE
            if choice == "B":       
                loop = True
                while loop == True:
                    print ("\nLets create a new DNA chain!")

                    try:
                        length = int(input("··· Enter the desired DNA sequence length: "))
                        if length <= 0:
                            raise ValueError("C'mon! Give me a proper number for length.")
                    except ValueError as e:
                        print(f"Invalid input: {e}")
                        continue

                    seq = DNA("")
                    sequence = seq.create_seq(length)
                    print(f"Here is your freshly made DNA sequence! *** {sequence} ***")
                    choiceB = input("Do you like it? \nWould you like to bring it to the main menu (Y/n)?  ")
                    if choiceB == "y" or choiceB == "Y":
                        loop = False

        # Extract/SAVE
            elif choice == "E":     
                if sequence == None:
                    print("\nNothing to save! \nYou must bake(B) or take(T) a sequence onto the plate...")
                    input("\tPress ENTER to confirm.")
                else:
                    print ("\nLet's freeze this DNA for later use.")
                    file = (input("··· Enter a file name: "))
                    file_op = File_operations(file)
                    file_op.save(DNA(sequence))
                    print(f"Your DNA sequence has just been saved to {file_op.directory}/{file_op.file}")
                    input("""Well done!! \n\tPress ENTER to go back to the main menu.""")

        # LIST
            elif choice == "L":     
                print("\nThese are all the DNA sequences available at the moment:")
                checklist = self.listing(file_op)
                if checklist == False:
                    pass
                else:
                    input("When you are ready press ENTER to back to the main menu.")

        # Take/LOAD
            elif choice == "T":
                print("\n")
                checklist = self.listing(file_op)
                if checklist == False:
                    pass
                else:
                    loopload = True
                    while loopload:
                        print("\nLet's load a DNA from the list.")
                        numberL = input("··· Enter the number of [Id] of the DNA you want to load: ")
                        valid_number = self.check_number(numberL, file_op)

                        if valid_number is None:
                            input("Please enter a valid number. Press ENTER.")
                            continue
                        
                        # Load the DNA sequence
                        loaded = file_op.load(valid_number)
                        print("This is the sequence you want to load? ", loaded)

                        choiceLOAD = input("Exit to the playground (Y/n)? ")
                        if choiceLOAD == "y" or choiceLOAD == "Y":
                            loopload = False
                            sequence = loaded
                        else:
                            input("Sequence not loaded. Press ENTER to return to DNA listing.")

        # Unwanted/DELETE
            elif choice == "U":
                loopD = True
                while loopD:  
                    print("\nLet's remove all those unwanted DNA's!")
                    
                    # Make sure there are files to delete
                    print("Current DNA stock:")
                    checklist = self.listing(file_op)
                    if checklist == False:
                        break
                    
                    numberD = input("··· Enter the [Id] of the sequence that you want to delete: ")
                    # Check if the input is valid
                    valid_numberD = self.check_number(numberD, file_op)
                    if valid_numberD is None:
                        input("Please enter a valid number. Press ENTER.")
                        continue
                    numberD = int(numberD)
                    filepath = file_op.filedic.get(numberD)

                    # Confirm deletion
                    print(f"Are you sure you want to delete the sequence {file_op.load(numberD)} in file '{filepath}'?")
                    makesure = input("(Y/n) ")
                    if makesure == "y" or makesure == "Y":
                        if os.path.exists(filepath):
                            os.remove(filepath)
                            print(f"File '{filepath}' deleted successfully.")
                        else:
                            print("Deletion canceled.")
                            print(f"File '{filepath}' not foundor or already deleted.")

                    choiceD = input("Exit to the playground (Y/n)? ")
                    if choiceD == "y" or choiceD == "Y":
                        loopD = False

        # OPERATIONS
            elif choice == "O":     
                print ("yeah!"*6)

        # Stop/EXIT
            elif choice == "S" or choice == "BOLETUS":     
                print("\nExiting the DNA playground. See you next time!")
                break

    
    def check_number(self, number, file_op):
        """Handling possible number input errors"""
        _, _, num = file_op.list_info()
        number_of_samples = num - 1
        try:
            value = int(number)
            if value <= 0 or value > number_of_samples:
                raise ValueError("The number provided is not within the range of available samples.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")
            return None


if __name__ == "__main__":
    mi_app = Interface1()
    mi_app.menu()


#### En la INTERFAZ ####
# Check if file already exists:
        #if os.path.exists(filepath):
         #   raiseError


