## Linux Commands I
- **grep** *'keyword'* {file}: search files for specified words or patterns (regular expressions).
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

- **wc** {file} (word count): count number of lines/words/characters in file
  * ```wc -w tempfile.txt``` To do a word count on tempfile.txt
  * ```wc -l tempfile.txt``` To find out how many lines the file has
  * ```wc tempfile.txt sort.txt``` To print how many lines, word and characters in files tempfile.txt and sort.txt

- **sort** The command sort alphabetically or numerically sorts a list.
  * ```sort```
  Then type in the names of some animals. Press [Return] after each one. <br>
  dog cat bird ape; ^C (control c to stop)
  The output will be: ape bird cat dog

- **cat** {file1} {file2} > {file0}: concatenate file1 and file2 to file0
  * ```cat list1.txt list2.txt > biglist.txt```<br>
  Example explained further down in "Appending to a file"


## Redirection
Most processes initiated by UNIX commands write to the standard output (that is, they write to the terminal screen), and many take their input from the standard input (that is, they read it from the keyboard). <br>
There is also the standard error, where processes write their error messages, by default, to the terminal screen.

### Redirecting the Output
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

### Appending to a file
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

### Redirecting the Input
```command < file``` Redirect standard input from a file.

We use the < symbol to redirect the input of a command. <br>
Using < you can redirect the input to come from a file rather than the keyboard. For example, to sort the list of fruit, type <br>
  * ```sort < biglist.txt``` and the sorted list will be output to the screen.
  * ```sort < biglist.txt > slist.txt``` To output the sorted list to a file. Use cat to read the contents of the file slist.txt

## Pipes
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

  
  * ``` ```
  * ``` ```
  * ``` ```
  
