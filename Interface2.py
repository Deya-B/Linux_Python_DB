class Interface2():
    """Interface of my DNA playground program"""
    def menu (self):
        pass
-------------------------------------------------------------------
def menu(self):
        """Display and control the menu"""
        print("""           
              · Welcome   to   the ·
            ****** DNA kitchen ******""")
        menu = ("""
                    ~ MENU ~

        B - Bake a fresh DNA            (Create DNA chain)
        O - Open to spice up your DNA!  (Operations with DNA)  
        L - List DNA stock              (List of all the DNA available)
        E - Store DNA in chest freezer  (Save DNA)
        T - Thaw DNA for use            (Load DNA)
        U - Unwanted DNA to discard     (Delete DNA)
        S - Stop cooking                (Exit)
                  """)
        # Initualize variables
        #sequence = None
        #file = None
        choice = ""
        while choice != "boletus" or "BOLETUS":
            print(menu)
            
            # Show available sequence under menu
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
            if choice == "B" or choice == "b": # CREATE
                loop = True
                while loop == True:
                    print ("\nLets create a new DNA chain!")
                    largo = int(input("··· Enter the desired DNA sequence length: "))
                    seq = DNA("")
                    sequence = seq.create_seq(largo)
                    print("Here is your freshly made DNA sequence!    ", sequence)
                    choiceB = input("Would you like to go back to the menu (Y/n)?  ")
                    if choiceB == "y" or choiceB == "Y":
                        loop = False

            elif choice == "L" or choice == "l": # LIST
                if file == None:
                    print("\nYou must bake/create (B) and store(E) a sequence to initiate list...")
                    input("""
            Press ENTER to confirm.""")
                else:
                    print ("\nThese are all the DNA sequences available at the moment:")
                    operation.list_info()   
                    for item in operation.filelist:
                        print(item)
                    choiceL = input("Would you like to use one of these (Y/n)?")
                    if choiceL == "Y" or choiceL == "y":

                    input("We are ready. Lets go back to the main menu (press ENTER).") # CARGAR ALGUNA? >IR A LOAD
                
            elif choice == "E" or choice == "e": # SAVE
                print ("\nLet's freeze this DNA for later use.")
                file = (input("··· Enter a file name: "))
                operation = File_operations(file)
                operation.save(seq)
                print(f"Your DNA sequence has just been saved to: {operation.directory}/{operation.file}")
                input("""Nothing else to do here... 
            Press ENTER to go back to the main menu.""")

            elif choice == "T" or choice == "t": # LOAD
                print("\nLet's load a DNA from the list use.")
                number = input("··· Enter the number of the sequence that you would like to load: ")
                loading = operation.load(number)
                print(loading)


            elif choice == "U" or choice == "u": # DELETE
                print ("yeah!"*5)

            elif choice == "O" or choice == "o": # OPERATIONS
                print ("yeah!"*6)            

            elif choice == "S" or choice == "s": # EXIT
                break
-------------------------------------------------------------------
-------------------------------------------------------------------
class Interface1():
    """Interface of my DNA playground program"""
    def loading (self):
        print("\nLet's load a DNA from the list use.")
        number = input("··· Enter the number of the sequence that you would like to load: ")
        loading = operation.load(number)
        return loading

    def menu(self):
        """Display and control the menu"""
        print("""           
              · Welcome   to   the ·
            ****** DNA kitchen ******""")
        menu = ("""
                    ~ MENU ~

        B - Bake a fresh DNA            (Create DNA chain)
        O - Open to spice up your DNA!  (Operations with DNA)  
        L - List DNA stock              (List of all the DNA available)
        E - Store DNA in chest freezer  (Save DNA)
        T - Thaw DNA for use            (Load DNA)
        U - Unwanted DNA to discard     (Delete DNA)
        S - Stop cooking                (Exit)
                  """)
        # Starting up variables
        sequence = None
        file = None
        choice = ""
        while choice != "boletus" or "BOLETUS":
            print(menu)
            
            # Show available sequence under menu
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
            if choice == "B" or choice == "b": # CREATE
                loop = True
                while loop == True:
                    print ("\nLets create a new DNA chain!")
                    largo = int(input("··· Enter the desired DNA sequence length: "))
                    seq = DNA("")
                    sequence = seq.create_seq(largo)
                    print("Here is your freshly made DNA sequence!    ", sequence)
                    choiceB = input("Would you like to go back to the menu (Y/n)?  ")
                    if choiceB == "y" or choiceB == "Y":
                        loop = False

            elif choice == "L" or choice == "l": # LIST
                if file == None:
                    print("\nYou must bake/create (B) and store(E) a sequence to initiate list...")
                    input("""
            Press ENTER to confirm.""")
                else:
                    print ("\nThese are all the DNA sequences available at the moment:")
                    operation.list_info()   
                    for item in operation.filelist:
                        print(item)
                    input("We are ready. Lets go back to the main menu (press ENTER).") # CARGAR ALGUNA? >IR A LOAD
                
            elif choice == "E" or choice == "e": # SAVE
                print ("\nLet's freeze this DNA for later use.")
                file = (input("··· Enter a file name: "))
                operation = File_operations(file)
                operation.save(sequence)
                print(f"Your DNA sequence has just been saved to: {operation.directory}/{operation.file}")
                input("""Nothing else to do here... 
            Press ENTER to go back to the main menu.""")

            elif choice == "T" or choice == "t": # LOAD
                print("\nLet's load a DNA from the list use.")
                number = input("··· Enter the number of the sequence that you would like to load: ")
                loading = operation.load(number)
                print(loading)


            elif choice == "U" or choice == "u": # DELETE
                print ("yeah!"*5)

            elif choice == "O" or choice == "o": # OPERATIONS
                print ("yeah!"*6)            

            elif choice == "S" or choice == "s": # EXIT
                break
