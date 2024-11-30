from DNAclass import DNA
from File_operations import File_operations
import os

# Functions
def loading():
    loop1 = True
    while loop1 == True:
        print("\nLet's load a DNA from the list.")
        for item in listing:
            print(item)
        numberL = input("··· Enter the Id.number that you want to load: ")
        loaded = operation.load(numberL)
        print("This is the sequence you want to load? ",loaded)
        choiceLOAD = input("Bring sequence to main menu (Y/n)? ")
        if choiceLOAD == "y" or choiceLOAD == "Y":
            loop1 = False
    

# Initializing variables of DNA and file classes:
file = ""
operation = File_operations(file)
listing, dictionary = operation.list_info()

# Initializing variables for menu
sequence = None
choice = ""

# MAIN PROGRAM:
"""Display and control the menu"""
print("""           
      · Welcome   to   the ·
    ****** DNA kitchen ******""")
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
        print("You got a FRESH sequence: ", sequence)
    
    # Choices
    choice = input("""
What would you like to do?
··· Provide the letter and leave it in my hands! > """)
    
    if choice == "B" or choice == "b": # Bake/CREATE
        loop = True
        while loop == True:
            print ("\nLets create a new DNA chain!")
            largo = int(input("··· Enter the desired DNA sequence length: "))
            seq = DNA("")
            sequence = seq.create_seq(largo)
            print("Here is your freshly made DNA sequence!    ", sequence)
            choiceB = input("Are you happy with that sequence? Would you like to go back to the menu (Y/n)?  ")
            if choiceB == "y" or choiceB == "Y":
                loop = False

    elif choice == "L" or choice == "l": # LIST
        if file == None:
            print("\nYou must bake/create(B) and establish(E) a sequence to initiate list...")
            input("""
    Press ENTER to confirm.""")
        else:
            print("\nThese are all the DNA sequences available at the moment:")
            print("Id-Bases,Sequence")
            for item in listing:
                print(item)
            input("We are ready. Lets go back to the main menu (press ENTER).")
        
    elif choice == "E" or choice == "e": # Extract/SAVE
        print ("\nLet's freeze this DNA for later use.")
        file = (input("··· Enter a file name: "))
        operation = File_operations(file)
        operation.save(DNA(sequence))
        print(f"Your DNA sequence has just been saved to: {operation.directory}/{operation.file}")
        input("""Nothing else to do here... 
    Press ENTER to go back to the main menu.""")
        
    elif choice == "T" or choice == "t": # Take/LOAD
        if file == None:
            print("\nYou must bake/create(B) and establish(E) a sequence to initiate load...")
            input("""
    Press ENTER to confirm.""")
        else:
                print("\nLet's load a DNA from the list.")
                operation = File_operations(file)
                for item in listing:
                    print(item)
                numberL = input("··· Enter the Id.number that you want to load: ")
                loaded = operation.load(numberL)
                print("This is the sequence you want to load? ",loaded)
                choiceLOAD = input("Bring sequence to main menu (Y/n)? ")
                if choiceLOAD == "Y" or choiceLOAD == "y":
                    sequence = loaded

    elif choice == "U" or choice == "u": # Unwanted/DELETE
        if file == None:
            print("\nYou must bake/create(B) and establish(E) something so you can delete it!")
            input("""
    Press ENTER to confirm.""")
        else:
            print("\nLet's remove all those unwanted DNA's!") 
            for item in listing:
                print(item)
            numberD = (input("··· Enter the Id.number that you want to delete: "))
            print(f"Are you sure that you want to delete sequence {operation.load(numberD)} ?")
            makesure = input("(Y/n) ")
            if makesure == "y" or makesure == "Y":
                numberD = int(numberD)
                filepath = operation.delete(numberD)
                if os.path.exists(filepath): 
                    os.remove(filepath)
                    print(f"File '{filepath}' deleted successfully.")
                else: 
                    print(f"File '{filepath}' not found.")
            input("Press ENTER to go back to the cooking.")


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

 


#### En la INTERFAZ ####
# Check if file already exists:
        #if os.path.exists(filepath):
         #   raiseError


#print(sequence.measure_freqs())
#print(sequence.validate())
#subseq="CG"
#print(sequence.count_subseq(subseq))
#print(sequence.cg_percentage())
#print(sequence.mutate(5))

#length = 10         #int(input("Enter a sequence length: "))
#sequence = DNA("")
#seq = sequence.create_seq (length)
#seq2 = sequence.create_seq (length)
#seqdna = DNA(seq)
#
#operation = File_operations ("mango")
