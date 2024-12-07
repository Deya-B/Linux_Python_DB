# Table of Contents
1. [Linux Commands I](#commandsI)
    1. [grep *'keyword'* {file}](#grep)
    2. [wc {file}](#wc)
    3. [sort](#sort)
    4. [cat {file1} {file2} > {file0}](#cat)
2. [Redirection](#redirection)
    1. [Redirecting the Output](#output)
    2. [Appending to a file](#appending)
    3. [Redirecting the Input](#input)
3. [Pipes](#pipes)
4. [Linux Commands II](#commandsII)
    1. [gzip](#gzip)
    2. [tar](#tar)
    3. [zcat](#zcat)
    4. [cut](#cut)
    5. [tr](#tr)
5. [Fourth Example](#fourth-examplehttpwwwfourthexamplecom)
    1. [grep *'keyword'* {file}](#grep)


# Linux Commands I <a name="commandsI"></a>
### grep *'keyword'* {file}: <a name="grep"></a>
Search files for specified words or patterns (regular expressions).
  * ```grep If tempfile.txt``` grep prints each line with the word If. The grep command is case sensitive; it distinguishes between If and if.
  * ```grep -i If tempfile.txt``` To ignore case sensitivity use -i

  * Some other useful options of grep are:
      * -v 🡒 display those lines that do NOT match
      * -n 🡒 precede each matching line with the line number
      * -c 🡒 print only the total count of matched lines

```
grep -iwvc file tempfile.txt
  # the number of lines without the words file or File
``` 
The grep command allows to searching in more than one file. If I wanted to search for the string file in my files tempfile.txt and sort.txt I would do this:
```
grep -ivc file tempfile.txt sort.txt
```
_Recursive use uf grep:_ <br>
If you have a bunch of text files in a directory hierarchy, e.g, in ~/ database/ and you want to find the file where a specific text is defined, then use the -r option of the grep command to do a recursive search. This will perform a recursive search operation trough files for the string "gmail" (as shown below) in the directory ~/database/ and all its sub-directories:
```
grep -rc gmail ~/database/
```

### wc {file} (word count): <a name="wc"></a>
Count number of lines/words/characters in file.
  * ```wc -w tempfile.txt``` To do a word count on tempfile.txt
  * ```wc -l tempfile.txt``` To find out how many lines the file has
  * ```wc tempfile.txt sort.txt``` To print how many lines, word and characters in files tempfile.txt and sort.txt

### sort <a name="sort"></a>
The command sort alphabetically or numerically sorts a list.
  * ```sort```
  Then type in the names of some animals. Press [Return] after each one. <br>
  dog cat bird ape; ^C (control c to stop)
  The output will be: ape bird cat dog

### cat {file1} {file2} > {file0}: <a name="cat"></a>
Concatenate file1 and file2 to file0.
  * ```cat list1.txt list2.txt > biglist.txt```<br>
  Example explained further down in "Appending to a file"


## Redirection <a name="redirection"></a>
Most processes initiated by UNIX commands write to the standard output (that is, they write to the terminal screen), and many take their input from the standard input (that is, they read it from the keyboard). <br>
There is also the standard error, where processes write their error messages, by default, to the terminal screen.

### Redirecting the Output <a name="output"></a>
```command > file``` Redirect standard output to a file.

We use the > symbol to redirect the output of a command. For example, to create a file called list1 containing a list of fruit, type 
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
```command >> file``` Append standard output to a file.

The form >> appends standard output to a file. So to add more items to the file list1, type
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
```command < file``` Redirect standard input from a file.

We use the < symbol to redirect the input of a command. <br>
Using < you can redirect the input to come from a file rather than the keyboard. For example, to sort the list of fruit, type <br>
  * ```sort < biglist.txt``` and the sorted list will be output to the screen.
  * ```sort < biglist.txt > slist.txt``` To output the sorted list to a file. Use cat to read the contents of the file slist.txt

## Pipes <a name="pipes"></a>
```command1 | command2```: pipe the output of command1 to the input of command2.

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

# Linux Commands II <a name="commandsII"></a>
### gzip <a name="gzip"></a>
This reduces the size of a file, thus freeing valuable disk space using the ZIP compressor. For example
  * ```gzip science.txt``` This will compress the file and place it in a file called science.txt.gz
To expand the file, use the gunzip command.
  * ```gunzip science.txt.gz```

### tar <a name="tar"></a>
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
 
### zcat <a name="zcat"></a>
zcat will read gzipped files without needing to uncompress them first.
  * ```zcat science.txt.gz```
  * ```zcat rm.txt.gz | less``` If the text scrolls too fast, pipe the output though less
  
### cut <a name="cut"></a>
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
Using a pipe you can connect the standard output of a process with the standard input of the cut command for example:
``` sh
ls -l | cut -d' ' -f2,4
```
To extract the fields 2 and 4 of the ls -l search.

### tr <a name="tr"></a>
The **tr** command with the option `-s` is used to translate, delete or squeezing repeated characters. 
``` sh
ls -l | tr -s ' '
```

A combination of **tr** and **cut**:
``` sh
ls -l | tr -s ' ' | cut -d' ' -f 4,5 –-output-delimiter='_'
```

tr is an UNIX utility for translating, or deleting, or squeezing repeated characters. It will read from stdin and write to stdout. 
``` sh
echo “Get + and put -” | tr + -
```

Although tr cannot accept the names of files as arguments, it can be used to modify copies of their contents by using the input/output redirection operators.
``` sh
tr '{}' '()' < file1 > file2
```
This command will read each character from “file1”, translate if it is a brace, and write the output in the “file2”.

Avoid uwing the output redirection operator to write to the same file from which the text is being read, as this will erase all of the text in that file, including that outputted by tr. Thus, for example, the following should not be used
  * ``` ```
  * ``` ```

### zcat

  * ``` ```
  * ``` ```
  * ``` ```

### zcat

  * ``` ```
  * ``` ```
  * ``` ```
