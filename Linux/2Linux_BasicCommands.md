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

- **cat** {file} (concatenate): The cat (concatenate) command in Linux displays file contents. It reads one or multiple files and prints their content to the terminal. cat is used to view file contents, combine files, and create new files [very GOOD examples](https://phoenixnap.com/kb/linux-cat-command#:~:text=The%20cat%20(concatenate)%20command%20in,files%2C%20and%20create%20new%20files.).
  * ```cat tempfile.txt```
  * ```cat unix1.html unix2.html unix3.html``` To display three files called unix1.html, unix2.html and unix3.html
  > When using cat be warned that it will not pause between page breaks, it literally displays the whole file in one go.

- **less** {file}: The command less writes the contents of a file onto the screen a page at a time.
  * ```less tempfile.txt```
  > Press the [space-bar] if you want to see another page, [Enter] if you want to scroll the file line by line, and type [q] if you want to quit reading. As you can see, less is used in preference to cat for long files.
  > Using less, you can search though a text file for a keyword (pattern). For example, to search through tempfile.txt for the word 'file'type a forward slash [/] followed by the word to search
  * ```/file```  less finds and highlights the keyword.
  > Type [n] to search for the next occurrence of the word.
 
- **head** {file}:
```sh
SYNOPSIS
  head [OPTION]... [FILE]...

DESCRIPTION
  Print the first 10 lines of each FILE to standard output.
  -c, --bytes=[-]NUM
  print the first NUM bytes of each file; with the leading ’-’,
  print all but the last NUM bytes of each file
  -n, --lines=[-]NUM
  print the first NUM lines instead of the first 10; with the
  leading ’-’, print all but the last NUM lines of each file
```
  * ```head tempfile.txt```
  * ```head -15 tempfile.txt``` first 15 lines...
  * ```head -n 100 adult.data``` Display the first 100 lines of file adult.data
  * ```head -n -100 adult.data``` Display all the lines in file adult.data except the last 100

- **tail** {file}:
```sh
SYNOPSIS
  tail [OPTION]... [FILE]...
DESCRIPTION
  Print the last 10 lines of each FILE to standard output.
  -c, --bytes=[+]NUM
  output the last NUM bytes; or use -c +NUM to output starting
  with byte NUM of each file
  -n, --lines=[+]NUM
  output the last NUM lines, instead of the last 10; or use -n
  +NUM to output starting with line NUM
```
  * ```tail tempfile.txt```
  * ```tail -30 tempfile.txt``` last 30 lines...
  * ```tail -n 100 adult.data``` Display the last 100 lines of file adult.data
  * ```tail -n +100 adult.data``` Display the content in file adult.data starting in line 100
  * ```head -n 200 adult.data | tail -n +100``` Display lines 100 to 200
  * ```head -n 200 adult.data | tail -n 101```
  * ```tail -n +100 adult.data | head -n 101```
 
- **ln**: Symbolic links or soft link, is a special kind of file that points to another file (target file).
  > Unlike a hard link, a symbolic link does not contain the data of the target file. It simply points to another entry somewhere in the file system.
  > 
  > This difference gives symbolic links certain qualities that hard links do not have, such as the ability to link to directories, or to files on remote computers networked through NFS.
  * ```ln -s sort.txt symbolic.txt``` To create a symbolic link called *symbolic.txt* to your target file *sort.txt*
  > Also, when you delete a target file, symbolic links to that file become unusable, whereas hard links preserve the contents of the file.

