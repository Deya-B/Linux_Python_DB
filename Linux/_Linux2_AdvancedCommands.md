# Table of Contents
1. [Linux Commands I](#commands1)
    1. [`grep 'keyword' {file}`](#grep)
    2. [`wc {file}`](#wc)
    3. [`sort` I](#sort1)
    4. [`cat {file1} {file2} > {file0}`](#cat)
2. [Redirection](#redirection)
    1. [Redirecting the Output](#output)
    2. [Appending to a file](#appending)
    3. [Redirecting the Input](#input)
3. [Pipes `|`](#pipes)
4. [Linux Commands II](#commands2)
    1. [`gzip`](#gzip)
    2. [`tar`](#tar)
    3. [`zcat`](#zcat)
    4. [`cut`](#cut)
    5. [`tr`](#tr)
    6. [`date`](#date)
    7. [`file`](#file)
    8. [`stat`](#stat)
    9. [`basename` (and `dirname`)](#basename)
    10. [`diff`](#diff)
    11. [`sort` II](#sort2)
    12. [`find`](#find)
    13. [`xargs`](#xargs)


# Linux Commands I <a name="commands1"></a>
### `grep 'keyword' {file}`: <a name="grep"></a>
grep searches files for specified words (without regular expressions) or patterns (regular expressions)
```
SYNOPSIS
    grep [OPTIONS] PATTERN [FILE...]

DESCRIPTION
    grep searches the named input FILEs for lines containing a match to
    the given PATTERN.

    -i, --ignore-case
        Ignore case distinctions in both the PATTERN and the input
        files.
    -n, --line-number
        Prefix each line of output with the 1-based line number
        within its input file.
    -c, --count
        Suppress normal output; instead print a count of matching
        lines for each input file.
```

  * ```grep If tempfile.txt``` grep prints each line with the word If. The grep command is case sensitive; it distinguishes between If and if.
  * ```grep -i If tempfile.txt``` To ignore case sensitivity use -i

  * Some other useful options of grep are:
      * -v 🡒 display those lines that do NOT match
      * -n 🡒 precede each matching line with the line number
      * -c 🡒 print only the total count of matched lines

```
grep -iwvc file tempfile.txt             # The number of lines without the words file or File
head -n 100 adult.data | grep -i "Married"  # Display lines that contain the string Married
head -n 100 adult.data | grep -in "Married" # Same showing line number
head -n 100 adult.data | grep -c "Married"  # Count number of appearances
```

The grep command allows to searching in more than one file. If I wanted to search for the string file in my files tempfile.txt and .txt I would do this:
```
grep -ivc file tempfile.txt sort.txt
```
_Recursive use uf grep:_ <br>
If you have a bunch of text files in a directory hierarchy, e.g, in ~/ database/ and you want to find the file where a specific text is defined, then use the -r option of the grep command to do a recursive search. This will perform a recursive search operation trough files for the string "gmail" (as shown below) in the directory ~/database/ and all its sub-directories:
```
grep -rc gmail ~/database/
```

### `wc {file}` (word count): <a name="wc"></a>
Count number of lines/words/characters in file.
  * ```wc -w tempfile.txt``` To do a word count on tempfile.txt
  * ```wc -l tempfile.txt``` To find out how many lines the file has
  * ```wc tempfile.txt sort.txt``` To print how many lines, word and characters in files tempfile.txt and sort.txt

### `sort` I <a name="sort1"></a>
Refer to [`sort` II](#sort2) <br>
The command sort alphabetically or numerically sorts a list or lines of a file.
```
SYNOPSIS
    sort [OPTION]... [FILE]...

DESCRIPTION
    Write sorted concatenation of all FILE(s) to standard output.

    -b, --ignore-leading-blanks
        ignore leading blanks
    -d, --dictionary-order
        consider only blanks and alphanumeric characters
    -f, --ignore-case
        fold lower case to upper case characters
    -g, --general-numeric-sort
        compare according to general numerical value
    -r, --reverse
        reverse the result of comparisons
    -k, --key=KEYDEF
        sort via a key; KEYDEF gives location and type
    -t, --field-separator=SEP
        use SEP instead of non-blank to blank transition

    KEYDEF is F[.C][OPTS][,F[.C][OPTS]] for start and stop position,
    where F is a field number and C a character position in the
    field; both are origin 1, and the stop position defaults to the
    line’s end. If neither -t nor -b is in effect, characters in a
    field are counted from the beginning of the preceding whitespace.
    OPTS is one or more single-letter ordering options [bdfgiMhnRrV],
    which override global ordering options for that key. If no key
    is given, use the entire line as the key.
```

  * ```sort```
  Then type in the names of some animals. Press [Return] after each one. <br>
  dog cat bird ape; ^C (control c to stop)
  The output will be: ape bird cat dog

### `cat` {file1} {file2} > {file0}: <a name="cat"></a>
Concatenate file1 and file2 to file0.
  * ```cat list1.txt list2.txt > biglist.txt```<br>
  Example explained further down in "Appending to a file"


## Redirection <a name="redirection"></a>
Most processes initiated by UNIX commands write to the standard output (that is, they write to the terminal screen), and many take their input from the standard input (that is, they read it from the keyboard). <br>
There is also the standard error, where processes write their error messages, by default, to the terminal screen.

### Redirecting the Output <a name="output"></a>
Most command line programs send their output to the standard output. <br>
We can redirect the standard output to a file with the > symbol.

```command > file```

For example, to create a file called list1 containing a list of fruit, type 
```
cat > list1.txt
```
Then type in the names of some fruits. Press [Return/Enter] after each one.
```
pear banana apple
# ^C {this means press [Ctrl] and [c] to stop}
```
What happens is the cat command reads the standard input (the keyboard) and the > redirects the output, which normally goes to the screen, into a file called list1.txt <br>
To read the contents of the file, type:
```
cat list1.txt
```
>Exercise:
>
> Using the above method, create another file called list2.txt containing the following fruit: orange, plum, mango, grapefruit. Read the contents of list2.txt.

### Appending to a file <a name="appending"></a>
We can use >> to redirect the standard output appending to a file.

```command >> file``` 

So to add more items to the file list1, type
```
cat >> list1.txt
```
Then type in the names of more fruit, for ex. peach grape orange; ^C (Control C to stop).<br>
You should now have two files. One contains six fruits, the other contains four fruits.<br>
We will now use the **cat** command to *join* (concatenate) list1 and list2 into a new file called biglist.
```
cat list1.txt list2.txt > biglist.txt
```
What this is doing is reading the contents of list1.txt and list2.txt in turn, then outputting the text to the file biglist.txt

### Redirecting the Input <a name="input"></a>
Most command line programs read their input from the standard input.

```command < file``` 

Using < you can redirect the input to come from a file rather than the keyboard. For example, to sort the list of fruit, type <br>
  * ```sort < biglist.txt``` and the sorted list will be output to the screen.
 To redirect both the input and the output use both > and < in a single system call:
  * ```sort < biglist.txt > slist.txt``` To output the sorted list to a file. Use cat to read the contents of the file slist.txt

## Pipelines `|` <a name="pipes"></a>
Pipelines allow to redirect the output from a command to the input of another, without writing to files:<br>
```command1 | command2```: pipe the output of command1 to the input of command2.

Instead of doing this:
```sh
ls > list.txt
sort < list.txt
```
We can do
```sh
ls | sort
```

Suppose that we want to list in reverse order the strings included in the file biglist.txt that do not contain the character "a" <br>
One method to get a sorted list of names is to type,
```
grep -v a biglist.txt > names.txt
sort -r < names.txt
cat names.txt
```
This is a bit slow and you have to remember to remove the temporary file called names when you have finished. 

What you really want to do is connect the output of the grep command directly to the input of the sort command. This is exactly what pipes do. 

The symbol for a pipe is the vertical bar |
```
grep -vi a biglist.txt | sort -r
```
This command line will give the same result as above, but quicker and cleaner

Other examples:
  * ```ls -lp | grep /```
  * ```ls -lp | grep -v /```

# Linux Commands II <a name="commands2"></a>
### `gzip` <a name="gzip"></a>
This reduces the size of a file, thus freeing valuable disk space using the ZIP compressor. For example
  * ```gzip science.txt``` This will compress the file and place it in a file called science.txt.gz
To expand the file, use the gunzip command.
  * ```gunzip science.txt.gz```

### `tar` <a name="tar"></a>
In Linux, tar command is useful as it can combine several files into a single uncompressed (or compressed) file. Tar command, also called tape archiving. With the help of this command, the individual files in a directory can be unpacked and extracted from the archive file.

Most used tar options:
```
-c  create a archive file
-x  extract a archive file
-v  show the progress of archive file
-f  filename of archive file
-t  viewing content of archive file
-j  compress archive through bzip2
-z  compress archive through gzip
-r  append or update files or directories to existing archive file
```
Examples:
  * ```tar -cvzf tarPrueba.tar.gz ./tarPrueba/``` To create a compresseddd gzip archive file called tarPrueba.tar.gz of the directory ./tarPrueba
  * ```tar -tvzf tarPrueba.tar.gz``` To list contents of a tar archive
  * ```tar -xvzf tarPrueba.tar.gz``` To untar or extract a tar file
  * ```tar -xvzf tarPrueba.tar.gz -C ./tarPruebaNew``` To untar in a different directory: option -C {specified directory}
Some times, you may want to compress an entire directory, but excluding certain files or directories.
You can do so by appending an ```--exclude``` switch for each directory or file you want to exclude.

    * ```tar -czvf archive.tar.gz /home/ubuntu --exclude=*.mp4``` To compress /home/ubuntu excluding all .mp4 files
 
### `zcat` <a name="zcat"></a>
zcat will read gzipped files without needing to uncompress them first.
  * ```zcat science.txt.gz```
  * ```zcat rm.txt.gz | less``` If the text scrolls too fast, pipe the output though less
  
### `cut` <a name="cut"></a>
```
SYNOPSIS
    cut OPTION... [FILE]...
DESCRIPTION
    Print selected parts of lines from each FILE to standard output.

    -d, --delimiter=DELIM
        use DELIM instead of TAB for field delimiter
    -f, --fields=LIST
        select only these fields; also print any line that
        contains no delimiter character, unless the -s option
        is specified
    -s, --only-delimited
        do not print lines not containing delimiters
```
The cut command is used for text processing. 
You can use this command to extract portion of text from a file by selecting columns (fields) or characters.
For example, let's say you have a file (fruit.txt) which contains the following ASCII text, being the field delimiter the | character:
``` sh
$ cat fruit.txt
apples|Spain
oranges|Spain
pears|Israel
```
to extract the second column type,
```cut -d'|' -f2 fruit.txt```

When the field ```delimiter = tab``` you can omit the -d option. For example:
``` sh
$ cat fruit.txt
apples	Spain		red
oranges	Spain		juice
pears	Israel		galia
kiwis	SouthAfrica	green

$ cut -f 3 fruit.txt
red
juice
galia
green
```

  * ```cut adult.data -d "," -f 4``` Display the 4th column of file adult.data
  * ```cut adult.data -d "," -f 4-6``` Columns 4 to 6

Using a pipe you can connect the standard output of a process with the standard input of the cut command for example:
``` sh
ls -l | cut -d' ' -f2,4
```
To extract the fields 2 and 4 of the ls -l search.

### `tr` <a name="tr"></a>
```
SYNOPSIS
    tr [OPTION]... SET1 [SET2]
DESCRIPTION
    Translate, squeeze, and/or delete characters from standard input,
    writing to standard output.
    -c, -C, --complement
        use the complement of SET1
    -d, --delete
        delete characters in SET1, do not translate
    -s, --squeeze-repeats
        replace each sequence of a repeated character that is listed
        in the last specified SET, with a single occurrence of that
        character
```
* The **tr** command with the option `-s` is used to translate, delete or squeezing repeated characters. 
``` sh
ls -l | tr -s ' '
```

* A combination of **tr** and **cut**:
``` sh
ls -l | tr -s ' ' | cut -d' ' -f 4,5 –-output-delimiter='_'
```

* tr is an UNIX utility for translating, or deleting, or squeezing repeated characters. It will read from stdin and write to stdout. 
``` sh
echo “Get + and put -” | tr + -
```

* Although tr cannot accept the names of files as arguments, it can be used to modify copies of their contents by using the input/output redirection operators.
``` sh
tr '{}' '()' < file1 > file2
```
> This command will read each character from “file1”, translate if it is a brace, and write the output in the “file2”.

> [!CAUTION]
> Avoid using the same output file from the input, this will erase all the text in that file, including the outputted by tr. Thus, the following should not be used: `tr s S < file1 > file1`

* *When numerous characters need to be replaced*: tr can also replace characters in a specified range by their counterparts in another specified range:
> A range is indicated by inserting a hyphen between the first and last characters and then placing all of this in square brackets.
``` sh
cat file2 | tr '[A-Z]' '[a-z]' > file3
```
> This will replace every upper case letter in a file named file2 by its lower case counterpart and write the result to a file called file3

* tr can also be used to remove particular characters using -d option:
``` sh
echo “eduardo serrano” | tr -d 'dn'
```

* `-s` option replaces each sequence of repeated characters that is listed in the last specified set, with a single instance. The following command translates all newlines in the file data.txt into spaces yielding a **single line**.
```sh
tr -s '\n' ' ' < data.txt
```

* More examples:
  - Use the standarized argument [:digit:] to remove all the digits:
    ```sh
    echo “Bank account: 0001 00 12345678” | tr -d [:digit:]
    ```
  - To remove all the characters except digits:
    ```sh
    echo “Bank account 0001 00 12345678” | tr -cd [:alpha:]
    ```
  - The option `-c` (complement) causes tr to work on the characters that are NOT in the given set:
    ```sh
    echo “Bank account: 0001 00 12345678” | tr -cd [:digit:]
    ```
  - To remove the punctuation characteres you can replace all the punctuation characters by spaces: 
    ```sh
    cat file2 | tr '[:punct:]' ' ' > file3
      # replace all the punctuation characters in file2 and redirect output to file3
    ```
* Even more examples:
  ```sh
  head -n 100 adult.data | tr ’,’ ’;’             # Replace ’,’ by ’;’
  head -n 100 adult.data | tr ’a-z’ ’A-Z’         # Capitalize all letters
  head -n 100 adult.data | tr ’0-9’ ’$’           # Replace all numeric characters by $
  head -n 100 adult.data | tr -c ’0-9a-zA-Z’ ’-’  # Replace all non alphanumeric characters by -
  head -n 100 adult.data | tr -d ’0-9’            # Delete all numbers
  head -n 100 adult.data | tr -s ’ ’              # Eliminate repeated spaces
  ```

### `date` <a name="date"></a>
Prints or sets the system date and time.
```sh
$ date
jue sep 7 21:50:32 CEST 2017

$ date +%y-%m-%d
17-09-07

$ date +%T
21:50:43
```

### `file` <a name="file"></a>
Prints information from the files. <br>
**file** tests each argument in an attempt to classify it. <br>
There are three sets of tests, performed in the following order: file-system tests, magic tests, and language tests. The first test that succeeds causes the file type to be printed.

```sh
$ file rm.txt
rm.txt: UTF-8 Unicode English text
```
It is possible to use the wild-card * to access the information of several files together. For example:
```sh
$ file *csv
uk-500.csv: ASCII English text, with CR line terminators
uk-500_tab.csv: ASCII English text
```

### `stat` <a name="stat"></a>
Display a file or file system status
```sh
$ stat rm.txt
$ stat *csv    # use * to access the status of several files together
```
* To access to the file meta-information individually use the -c command option. For example:
  * ```stat -c %A rm.txt``` - Print file access rights in human readable format - %A
  * ```stat -c %U rm.txt``` - Get user name of the owner - %U
  * ```stat -c %y rm.txt``` - Time of the last modification - %y 
  * ```stat -c %s rm.txt``` - Print the size in bytes - %s

### `basename` (and `dirname`) <a name="basename"></a>
The basename command strips any "path" name components from a filename, leaving the "pure" filename.
```sh
$ basename /usr/bin/sort
sort

$ basename include/stdio.h
stdio.h

$ basename /home/mikel/bin/stdio.h .h     # strip a suffix from a filename
stdio
```
The dirname command strips the filename itself, giving you the "directory" part of the pathname:
```sh
$ dirname /home/mikel/bin/stdio.h
/home/mikel/bin
```

### `diff` <a name="diff"></a>
This diff command compares the contents of two files and displays the differences.

```diff file1 file2``` To see the differences between file1 and file2
> Lines beginning with a < denotes file1, while lines beginning with a > denotes file2.

### `sort` II <a name="sort2"></a>
Refer to [`sort` I](#sort1) <br>
* ```sort data.txt``` - To sort the lines in this file alphabetically
* ```sort -ru data.txt``` - The option `-u` filters out repeated lines in a file and `-r` prints the output in reverse order

Normally, sort decides how to sort lines based on the entire line: it compares every character from the first character in a line, to the last one.

If, on the other hand, you want sort to compare a limited subset of your data, you can specify which fields to compare using the `-k` option. The column separator is, by default, any blank character (however you can specify your own using the `-t` option).
```sh
sort -k 2 data.txt
sort -t "," -k 6,6 adult.data   # Sort by the 6th field
shuf -i 0-29 | sort             # Sort a random permutation
shuf -i 0-29 | sort -g          # Sort random permutation (numeric)
```

> [!WARNING]  
> Beware!!
> Note the output difference of the following two commands
> ```sh
>     $ sort -u data.txt | sort -k 2
>     $ sort -uk 2 data.txt
> ```


### `find` <a name="find"></a>
This searches through the directories for files and directories with a given name, date, size, or any other attribute you care to specify. 
It is a simple command but with many options - you can read the manual by typing man find. 
* ```find . -name "*.txt" -print``` - To search for all files with extension .txt, starting at the current directory (.) and exploring through all sub-directories
* ```find . -name "[a-z][a-z][0-9][0-9].txt"``` - To find all files that begin with two lower case characters, followed by two numbers followed by .txt
* ```find . -type d``` - `[ -type d ]` To find all directories in your working directory (`-type e` for files)
* ```find . -size +1M -ls``` - To find files over 1Mb in size
* ```find /var/adm -mtime +3``` - To find all files that have not been modified in the last three days
* ```find / -mmin -30``` - To find all directories that have been modified in the last 30 minutes
* ```find . -maxdepth 1 -type f``` - To find all the files in the working directory descending until at most one level (be careful with the order of the options in the command)
There are many other options(for example finding files that are newer or older than other files), consult the manual.

### `xargs` <a name="xargs"></a>
The command xargs is used mainly to combine with other commands.
* ```find . -maxdepth 1 -name "*.html" -mmin -10 | xargs cp -t kk/``` - to copy files to the kk/ directory
* ```find -type f | xargs file``` - Get information from files

* Delete files that have white-spaces in their filenames:
```sh
$ touch "The Geek Stuff.txt" #this creates a empty file
$ ls
The Geek Stuff.txt
$ find . -name "*.c" | xargs rm -rf
$ ls
one.h two.h The Geek Stuff.c

# To delete files including those that have spaces in the filenames
use the -print0 option with find command and -0 option with xargs command:
$ find . -name "*.txt" -print0 | xargs -0 rm -i
```
> The option `print0` indicates `find` to print all results to the standard output (separated with the ASCII NUL character ‘\000’)
>  
> The option `-0` tells `xargs` that the input will be separated with the ASCII NUL character ‘\000’

* We can force the output of the xargs into multiple lines using `-n`. In the following examples, we used -n option to adjust the items per line displayed in the xargs output:
```sh
echo "a b c d e f"| xargs -n 1
echo "a b c d e f"| xargs -n 3
```

* As we have shown the sort command is used to order file lines. To order sequences use the xargs command pipelined. For example:
```sh
echo "f d c b e a"| xargs -n 1 | sort
```

* Note that `-n` will be mandatory when xargs is combined with commands with a fixed number of arguments.<br>
  For example, because basename only admits one argument you must type:
> ```sh
> find . -name "*.html" | xargs -n 1 basename
> ```
> or to concanate several files located on different directories and redirecte the output you can type:
> ```sh
> find . -name "*.html" | xargs -n 1 cat > all.file
> ```
