from DNAclass import DNA
import textwrap

class OperationsSubmenu:
    """Submenu for DNA operations"""

    def __init__(self, sequence):
        self.sequence = sequence

    def submenu(self):
        """DNA operations submenu loop"""
        while True:
            menu = textwrap.dedent("""
        ~ Submenu: DNA OPERATIONS ~ 
        ---------------------------
        1 - Re-generate DNA        (Create a fresh DNA sequence)
        2 - Validate DNA           (Check if sequence is valid)
        3 - Mutate DNA             (Introduce mutations)
        4 - Measure frequencies    (Nucleotide frequencies)
        5 - Count subsequences     (Occurrences of a subsequence)
        6 - Synthesize reverse/complement
        7 - Measure GC%            (GC percentage)
        8 - Back to main menu
-------------------------------------------------------------------""")
            print(menu)
        # Display the current DNA sequence
            sequence_display = (
                f"You are working with this sequence: * {self.sequence} * \n"
                f"-------------------------------------------------------------------")
            print(sequence_display)
        
            try:
                choice = input("··· Enter an option: ").strip()
                menu_range = "12345678"
                if choice not in menu_range:
                    error_msg = textwrap.dedent("""
                                Number out of range, enter a number from 1 to 8.
                                Press ENTER to continue
                                """)
                    raise ValueError(error_msg)
            except ValueError as e:
                input(f"Invalid input: {e}")
                continue

        # Re-generate
            if choice == "1":
                new_length = int(input("Enter the length of the new DNA sequence: "))
                self.sequence = DNA("").create_seq(new_length)
                print(f"This is your fresh DNA sequence: {self.sequence}.")
                input("Press ENTER.")

        # Validate
            elif choice == "2":
                if DNA(self.sequence).validate():
                    validation_log = "** Valid DNA **"
                else:
                    validation_log = "X Invalid DNA X"
                    
                print(f"""
                      Validation log: 
                      ---------------
                      {validation_log} 
                      """)
                input("Press ENTER to go back to the menu.")

        # Mutate
            elif choice == "3":
                mutations = int(input("Number of mutations: "))
                original_sequence = self.sequence
                mutated_sequence, mutated_positions = DNA(self.sequence).mutate(mutations)
                number_positions = [x+1 for x in mutated_positions]
                print(f"""
                      Mutation log:
                      -------------
                      Original sequence: {original_sequence}
                      Mutated sequence:  {mutated_sequence}
                      Positions mutated: {sorted(number_positions)}
                      """)
                input("Press ENTER to go back to the menu.")

        # Fequencies
            elif choice == "4":
                freqs = DNA(self.sequence).measure_freqs()
                print(f"""
                      Nucleotide frequencies log: 
                      ---------------------------
                      {freqs} 
                      """)
                input("Press ENTER to go back to the menu.")

        # Count Subsequences
            elif choice == "5":
                subseq = input("Enter the subsequence: ").strip().upper()
                count, positions = DNA(self.sequence).count_subseq(subseq)
                locate_positions = [x+1 for x in positions]
                print(f"""
                      Count ocurrences of a subsequence log:
                      -------------------------------------
                      Subsequence repetitions: {count}
                      Location of the repetitions: {locate_positions}
                      """)
                input("Press ENTER to go back to the menu.")

        # Reverse/Complement
            elif choice == "6":
                original, reverse, complement = DNA(self.sequence).synt_complement()
                print(f"""
                      Synthesize reverse/complement log:
                      ----------------------------------
                      Original:   {original}
                      Reverse:    {reverse}
                      Complement: {complement}
                      """)
                input("Press ENTER to go back to the menu.")

        # GC%
            elif choice == "7":
                gc_content = DNA(self.sequence).cg_percentage()
                print(f"""
                      GC percentage log: 
                      -----------------------
                      GC%: {gc_content:.2f}
                      """)
                input("Press ENTER to go back to the menu.")

        # Back to main menu
            elif choice == "8":
                return self.sequence
                break

        # Wrong menu option
            else:
                input("Invalid option. Please try again.")

        return self.sequence
