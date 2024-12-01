import os

class File_operations():
    """Data files management \n
    Attibutes: file, directory (by default: working directory)"""
    def __init__(self, file = None, directory = None):
        self.file = file
        self.directory = directory
        self.filelist = []
        self.filedic = {}

    def save(self, sequence):
        """
        Save the current DNA chain. Requires: \n
        sequence = the sequence you want to save \n
        filename = name of the file where it will be saved \n
        directory = by defect is the current directory. One or multiple directores hanging 
        from the current directory can be created using the following sintax: dir/n...dirs """ 
        if self.directory is None:
            self.directory = os.getcwd()
        else:
            newpath = os.path.join(os.getcwd(), self.directory)
            os.makedirs(str(self.directory), exist_ok=True) # no issues raised if exists, just use
            self.directory = newpath

        newfilename = self.file +".dna"
        self.file = newfilename
        newfile = os.path.join(self.directory, newfilename)

        sequence_str = str(sequence) # passing DNA class to string so we can use the write function
        with open(newfile, "w") as file:
            file.write(sequence_str)
        return self.file, self.directory
    
    def list_info(self):
        """List all DNA chains with extension .dna in the current directory."""
        # Re-start file list and dictionary:
        self.filelist = []
        self.filedic = {}
        # List files in the current directory:
        files = os.listdir()  
        n = 1  # Line counter starts at 1 for each file
        for file in files:
            if file.endswith(".dna"):
                with open(file, 'r') as f:  # Open the file directly
                    for line in f:
                        components = line.strip().split(",")
                        # Process valid lines
                        if len(components) < 2:
                            print(f"Skipping malformed line in file {file}: {line.strip()}")
                        else:
                            sequences = components[:2]  # Take only length and DNA
                            mount = ",".join(sequences)
                            self.filelist.append(f"[{n}] -  {mount}") # Create list
                            self.filedic[n] = file  # Create dictionary for later file retrieval
                            n += 1
        return self.filelist, self.filedic, n # n=Obtain the numbers present in the list for later error handling

    def load(self, number):
        """
        Read a DNA chain from the list of elements shown by List.\n
        Requires: number >> Provide the number of the sequence you want to retrieve"""
        listing, _, _ = self.list_info()
        for item in listing:
            if item.startswith(f"[{number}]"):
                extracting = item.strip().split(",")
                loading = extracting [1]
                return loading

    def delete(self, number):
        """
        Delete a DNA chain from the list of elements shown by List. \n
        Requires: number >> Provide the number of the sequence you want to retrieve"""
        listing, dictionary, _ = self.list_info()
        for item in listing:
            if item.startswith(f"[{str(number)}]"):
                filename = dictionary[number]
                filepath = os.path.join(os.getcwd(), filename)
                return filepath
            
