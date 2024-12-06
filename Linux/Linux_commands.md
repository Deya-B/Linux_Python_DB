## Basic commands I
- ls (list): The ls command lists the contents of your current working directory.
  * ```ls -a``` To list all files in your home directory
  * ```ls -l``` Access the file's information,including: location, type, size (adding the -h option, ls -lh, print files size in human readble format), who owns it and can accesss it, the inode and time last modified.
  * ```ls -t``` Sort the files by modification time
  * ```ls -p``` Append / indicator to directories
    
- mkdir {dir} (make directory)
  * ```mkdir directory_name``` This command creates {directory_name} in your current working directory
    
- cd {dir} (change directory)
  * ```cd directory_name``` To change to the directory you have just made. Or any subdirectory in your working directory
  * ```cd ..``` (..) means the parent of the current directory, therefore use this command to scale back one directory
  * ```cd path/to/directory``` To change to any directory add the full path

- pwd (print working directory)
  * ```pwd``` display the path of the current directory
 
- clear (clear screen)
  * ```clear```

## Getting Help
- man {command} (manual): Type man command to read the manual page for a particular command.
  * ```man ls > tempfile.txt```

- whatis {command}: Gives a one-line description of the command, but omits any information about options etc.
  * ```whatis wc```

- apropos {keyword}: When you are not sure of the exact name of a command, will give you the commands with keyword in their manual page header.
  * ```apropos copy```

## Basic commands II
- **cp** {file1 file2} (copy): is the command which makes a copy of file1 in the current working directory and calls it file2.
  * ```cp ~/tempfile.txt .``` The above command means copy the file tempfile.txt to the current directory, keeping the name the same.
  * ```cp -r ~/linuxstaff ~/linuxstaff_backup``` To recursively copy all files and directories from ~/linuxstaff (downwards) to ~/linuxstaff_backup
 
- **mv** {file1 file2} (move): moves (or renames) file1 to file2
  * ```mv tempfile.txt backups/``` First, create an empty backups sub-directory in your linuxstaff directory, then change to your linuxstuff directory (can you remember how?). Then, inside the linuxstuff directory, type the given command in order to move the file tempfile.txt to your backups directory.
 
- **rm** {file} (remove), **rmdir** {dir} (remove directory)
  * ```rm tempfile.txt``` To delete (remove) a file, use the rm command
  * ```rmdir backups/``` to remove a directory (make sure it is empty first). With this command Linux will not let you remove a non-empty directory.
  * ```rm -r ./backups/``` CAUTION: It is possible to remove directories and their contents recursively using this command: command **rm -r** {directory}

- **cat** {file} (concatenate): The command cat can be used to display the contents of a file on the screen. 
  * ```cat tempfile.txt```
  * ```cat unix1.html unix2.html unix3.html``` To display three files called unix1.html, unix2.html and unix3.html
  > When using cat be warned that it will not pause between page breaks, it literally displays the whole file in one go.

- **less** {file}: The command less writes the contents of a file onto the screen a page at a time.
  * ```less tempfile.txt```
  > Press the [space-bar] if you want to see another page, [Enter] if you want to scroll the file line by line, and type [q] if you want to quit reading. As you can see, less is used in preference to cat for long files.
  > Using less, you can search though a text file for a keyword (pattern). For example, to search through tempfile.txt for the word 'file'type a forward slash [/] followed by the word to search
  * ```/file```  less finds and highlights the keyword.
  > Type [n] to search for the next occurrence of the word.
 
- **head** {file}: The head command writes the first ten lines of a file to the screen.
  * ```head tempfile.txt```
  * ```head -15 tempfile.txt``` first 15 lines...

- **tail** {file}: The tail command writes the last ten lines of a file to the screen.
  * ```tail tempfile.txt```
  * ```tail -30 tempfile.txt``` las 30 lines...
 
- **ln**: Symbolic links or soft link, is a special kind of file that points to another file (target file).
  > Unlike a hard link, a symbolic link does not contain the data of the target file. It simply points to another entry somewhere in the file system.
  > 
  > This difference gives symbolic links certain qualities that hard links do not have, such as the ability to link to directories, or to files on remote computers networked through NFS.
  * ```ln -s sort.txt symbolic.txt``` To create a symbolic link called *symbolic.txt* to your target file *sort.txt*
  > Also, when you delete a target file, symbolic links to that file become unusable, whereas hard links preserve the contents of the file.

## Useful Commands
- **grep** : It searches files for specified words or patterns (regular expressions).
  * ```grep If tempfile.txt``` grep prints each line with the word If. The grep command is case sensitive; it distinguishes between If and if.
  * ```grep -i If tempfile.txt``` To ignore upper/lower case distinctions, use the -i option

> Some other useful options of grep are:
> 
  > -v 🡒 display those lines that do NOT match
  >
  > -n 🡒 precede each matching line with the line number
  >
  > -c 🡒 print only the total count of matched lines
  
  * ```grep -iwvc file tempfile.txt``` the number of lines without the words file or File
- 
  * ``````
  * ``````
- 
  * ``````
  * ``````
  * ``````
  * ``````

  * ``` ```
  * ``` ```
  * ``` ```
  * ``` ```
  * ``` ```
  
