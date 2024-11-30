from DNAclass import DNA
from File_operations import File_operations
import os

class Interface1():
    """Interface of the DNA playground program"""

    def listing(self, file_op):
        """Obtain the listing of .dna present. Used by list, load and delete.\n
        Parameters: file class"""
        listing, dictionary = file_op.list_info()
        print("[Id]-Length,Sequence")
        for item in listing:
            print(item)
        

    def loading (self, file_op, number):
        """Load a DNA from the list.\n
        Parameters: file class, number to be loaded"""
        loop1 = True
        while loop1 == True:
            print("\nLet's load a DNA from the list.")
            self.listing(file_op)
            number = input("··· Enter the Id.number that you want to load: ")
            loaded = file_op.load(number)
            print("This is the sequence you want to load? ",loaded)
            choiceLOAD = input("Bring sequence to main menu (Y/n)? ")
            if choiceLOAD == "y" or choiceLOAD == "Y":
                loop1 = False
                return loaded
            
# Initializing variables of DNA and file classes:
    #file = ""
    #file_op = File_operations(file)

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

        while choice != "boletus" or "BOLETUS":
            print(menu)

            # Show current sequence under menu
            if sequence == None:    
                sequence = "*** No DNA on the plate yet ***"
                print(sequence)
                sequence = None
            else:
                print(f"You got a FRESH sequence: * {sequence} *")

            # Choices
            choice = input("\n\tWhat would you like to do? \n\t··· Provide the letter and leave it in my hands! > ")
            
            if choice == "B" or choice == "b": # Bake/CREATE
                loop = True
                while loop == True:
                    print ("\nLets create a new DNA chain!")
                    length = int(input("··· Enter the desired DNA sequence length: "))
                    seq = DNA("")
                    sequence = seq.create_seq(length)
                    print(f"Here is your freshly made DNA sequence! *** {sequence} ***")
                    choiceB = input("Do you like it? \nWould you like to bring it to the main menu (Y/n)?  ")
                    if choiceB == "y" or choiceB == "Y":
                        loop = False

            elif choice == "E" or choice == "e": # Extract/SAVE
                if sequence == None:
                    print("\nNothing to save! \nYou must bake/create(B) or take/load(T) a sequence...")
                    input("\tPress ENTER to confirm.")
                else:
                    print ("\nLet's freeze this DNA for later use.")
                    file = (input("··· Enter a file name: "))
                    file_op = File_operations(file)
                    file_op.save(DNA(sequence))
                    print(f"Your DNA sequence has just been saved to: {file_op.directory}/{file_op.file}")
                    input("""Nothing else to do here... \n\tPress ENTER to go back to the main menu.""")

            elif choice == "L" or choice == "l": # LIST
                print("\nThese are all the DNA sequences available at the moment:")
                self.listing(file_op)
                input("When you are ready press ENTER to back to the main menu.")

            elif choice == "T" or choice == "t": # Take/LOAD
                print("\nLet's load a DNA from the list:")
                self.listing(file_op)
                numberL = input("··· Enter the number of [Id] of the sequence that you want to load: ")
                loaded = file_op.load(numberL)
                print("This is the sequence you selected: ",loaded)
                choiceLOAD = input("Do you want to bring it to main menu (Y/n)? ")
                if choiceLOAD == "Y" or choiceLOAD == "y":
                    sequence = loaded

            elif choice == "U" or choice == "u": # Unwanted/DELETE
                raw_list, dictionary = file_op.list_info()
                if raw_list == []:
                    print("""\nNothing to delete! 
    You must bake/create(B) and establish/save(E) some sequence so you can delete it.""")
                    input("""Press ENTER to confirm.""")
                else:
                    loop = True
                    while loop == True:
                        print("\nLet's remove all those unwanted DNA's!") 
                        self.listing(file_op)
                        numberD = (input("··· Enter the [Id] of the sequence that you want to delete: "))
                        print(f"Are you sure that you want to get rid of sequence {file_op.load(numberD)}?")
                        makesure = input("(Y/n) ")
                        if makesure == "y" or makesure == "Y":
                            numberD = int(numberD)
                            filepath = file_op.delete(numberD)
                            if os.path.exists(filepath): 
                                os.remove(filepath)
                                print(f"File '{filepath}' deleted successfully.")
                            else: 
                                print(f"File '{filepath}' not found.")
                        choiceU = input("Would you like to continue throwing away unwanted DNA (Y/n)?  ")
                        if choiceU == "n" or choiceU == "N":
                            loop = False

            elif choice == "O" or choice == "o": # OPERATIONS
                print ("yeah!"*6)            

            elif choice == "S" or choice == "s": # Stop/EXIT
                break



    def operationsDNA(self):
        pass
    def file_operations (self):
        pass
    def errortackle (self):
        """Deal with errors"""
        pass

if __name__ == "__main__":
    mi_app = Interface1()
    mi_app.menu()


#### En la INTERFAZ ####
# Check if file already exists:
        #if os.path.exists(filepath):
         #   raiseError
