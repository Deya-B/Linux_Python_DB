# Linux Introduction
## UNIX, GNU/Linux?
UNIX is an operating system which was conceived and implemented by Ken Thompson and Dennis Ritchie (both of AT&T Bell Laboratories) in 1969 and first released in 1970. 
Later they rewrote it in a new programming language, C, to make it portable. The availability and portability of UNIX caused it to be widely adopted, 
copied and modified by academic institutions and businesses.

## The GNU/Linux operating system
The GNU/Linux operating system is made up of three parts; the kernel, the shell and the programs.

## The kernel
The kernel of UNIX is the core of the operating system: it allocates time and memory to programs and handles the filestore and communications in response to system calls.

As an illustration of the way that the shell and the kernel work together, suppose a user types rm myfile.txt (which has the effect of removing the file myfile.txt). 
The shell searches the filestore for the file containing the program rm, and then requests the kernel, through system calls, to execute the program rm on myfile.txt. 
When the process rm myfile has finished running, the shell then returns the UNIX prompt % to the user, indicating that it is waiting for further commands.

## The shell
The shell acts as an interface between the user and the kernel. When a user logs in, the login program checks the username and password, and then starts another program called the shell. 
The shell is a command line interpreter (CLI). It interprets the commands the user types in and arranges for them to be carried out. 
The commands are themselves programs: when they terminate, the shell gives the user another prompt ($ on our systems).

The user can customise his/her own shell, and deferent users can use different shells on the same machine. 
The bash shell is the most wide spread and arguably one of the simplest shell to begin with, but there are also plenty of other shells like the Bourne, Korn or Cshell. 
You can detect your shell using the command:
```
$echo $SHELL
```

The bash shell has certain features to help the user inputting commands.

Filename Completion - By typing part of the name of a command, filename or directory and pressing the [Tab] key, the tcsh shell will complete the rest of the name automatically. 
If the shell finds more than one name beginning with those letters you have typed, it will beep, prompting you to type a few more letters before pressing the tab key again.

History - The shell keeps a list of the commands you have typed in. If you need to repeat a command, use the cursor keys to scroll up and down the list or type history 
for a list of previous commands.

## The “Programms”
UNIX systems also have a graphical user interface (GUI) similar to Microsoft Windows which provides an easy to accecess a wide variety of applications for communication, 
work, education and entertainment (for example KDE desktop or GNOMAdektop). However, knowledge of UNIX is required for operations which aren't covered by a graphical program, 
or for when there is no windows interface available, for example, in a telnet session.

## Files and processes
Everything in UNIX is either a file or a process.

- A process is an executing program identified by a unique PID (process identifier).

- A file is a collection of data. They are created by users using text editors, running compilers etc.

**Examples of files:**
- a document (report, essay etc.)
- the text of a program written in some high-level programming language
- instructions comprehensible directly to the machine and incomprehensible to a casual user, for example, a collection of binary digits (an executable or binary file);
- a directory, containing information about its contents, which may be a mixture of other directories (subdirectories) and ordinary files.

## The Directory Structure
All the files are grouped together in the directory structure. The file-system is arranged in a hierarchical structure, like an inverted tree. 
The top of the hierarchy is traditionally called root (written as a slash / ).

## Starting an UNIX terminal
To open an UNIX terminal window in the KDE desktop, click on the "Terminal" icon from Applications/Accessories/Terminal menus.

An UNIX Terminal window will then appear with a $ prompt, waiting for you to start entering commands.
