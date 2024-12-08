# Table of Contents
1. [Linux Commands III](#commandsIII)
    1. [ `wget`](#wget)
    2. [Filters](#filters)
        1. [`fmt`](#fmt)
        2. [`split`](#split)
        3. [`paste`](#paste)
        4. [`shuf`](#shuf)
        5. [`uniq`](#uniq)
        6. [`join`](#join)
        7. [Summary](#summary)
        8. [`comm`](#comm)
    3. [](#)
2. [](#)
    1. [](#)

# Linux Commands III <a name="commandsIII"></a>

### `wget`: <a name="wget"></a>
GNU Wget is a free utility for non-interactive download of
files from the Web. It supports HTTP, HTTPS, and FTP
protocols, as well as retrieval through HTTP proxies.
```sh
wget archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data
``` 

## Filters <a name="filters"></a>
- A filter is a program that reads the standard input, performs some operation on it, and writes the result to the standard output.
- Filters are usually combined using pipelines.
- Some programs that can be used as filters: ``head, tail, tr, fmt, grep, sort``.
```sh
ls -la | grep 2016 | sort | head | tr ’[0-9]’ ’*’
``` 

See `head` and `tail` in [Linux_BasicCommands](https://github.com/Deya-B/Linux_Python_DB/blob/main/Linux/Linux_BasicCommands.md)

See `tr`, `grep` and `sort` in [Linux_AdvancedCommands](https://github.com/Deya-B/Linux_Python_DB/blob/main/Linux/Linux_AdvancedCommands.md)


### `fmt`: <a name="fmt"></a>
```
SYNOPSIS
    fmt [-WIDTH] [OPTION]... [FILE]...

DESCRIPTION
    Reformat each paragraph in the FILE(s), writing to standard output.
    The option -WIDTH is an abbreviated form of --width=DIGITS.

    -s, --split-only
        split long lines, but do not refill
    -t, --tagged-paragraph
        indentation of first line different from second
    -u, --uniform-spacing
        one space between words, two after sentences
    -w, --width=WIDTH
        maximum line width (default of 75 columns)
```

```sh
# Display the first lines of file adult.data cropping lines to 70 characters
head -n 100 adult.data | fmt -70 -s

#  Cropping lines to 70 characters, indenting each first line and using uniform spacing
head -n 100 adult.data | fmt -70 -tu
```

### `split`: <a name="split"></a>
Split a file into pieces.
```
SYNOPSIS
    split [OPTION]... [FILE [PREFIX]]

DESCRIPTION
    Output pieces of FILE to PREFIXaa, PREFIXab, ...; default size
    is 1000 lines, and default PREFIX is ’x’.

    -b, --bytes=SIZE
        put SIZE bytes per output file
    -l, --lines=NUMBER
        put NUMBER lines/records per output file
    -n, --number=CHUNKS
        generate CHUNKS output files; see explanation below
```

```sh
# Split the file adult.data into pieces with 10000 lines each (last piece is probably smaller)
split -l 10000 adult.data adult_part_

# Split the file adult.data into 4 pieces of approximately equal size, without breaking lines
split -n 4 adult.data adult_part_
```

### `paste`: <a name="paste"></a>
Merge lines of files. It's complementary to cut.
```
SYNOPSIS
    paste [OPTION]... [FILE]...

DESCRIPTION
    Write lines consisting of the sequentially corresponding lines
    from each FILE, separated by TABs, to standard output.

    -d, --delimiters=LIST
        reuse characters from LIST instead of TABs
```

```sh
# Create files f2.txt and f6.txt from adult.data
cut adult.data -d "," -f 2 > f2.txt 
cut adult.data -d "," -f 6 > f6.txt

# Paste files f2.txt and f6.txt
paste -d "," f2.txt f6.txt

# Extract columns 6 and 4 from adult.data to a new file separated with "|":
adult.data -d "," -f 4 > columna4.txt
cut adult.data -d "," -f 6 > columna6.txt
paste -d "|" columna6.txt columna4.txt > columns6and4.txt`
```

```sh
# Add a first column with the line number to file adult.data
echo {1..32562} | tr " " "\n" > nums.txt
paste -d "," nums.txt adult.data > adult-nums.data

# Without a temporary file (Para crear un fichero con las filas numeradas)
echo {1..32562} | tr " " "\n" | paste -d "," /dev/stdin adult.data > adult-nums.data
echo {1..32562} | tr " " "\n" | paste -d "," - adult.data > adult-nums.data
```

### `shuf`: <a name="shuf"></a>
Generate random permutations.
```
SYNOPSIS
    shuf [OPTION]... [FILE]
DESCRIPTION
    Write a random permutation of the input lines to standard output.

    -i, --input-range=LO-HI
        treat each number LO through HI as an input line
    -n, --head-count=COUNT
        output at most COUNT lines
    -r, --repeat
        output lines can be repeated
```

```sh
# Create a random permutation of numbers 2 to 9
shuf -i 2-9

# Shuffle the first 10 rows of adult-nums.data
head adult-nums.data | shuf
head adult-nums.data | cut -d, -f 1-4 | shuf

# Get only the first 5 shuffled rows
head adult-nums.data | shuf -n 5

# Generate 15 shuffled rows (with repetition)
head adult-nums.data | shuf -n 15 -r
head adult-nums.data | cut -d, -f 1-4 | shuf -r -n 10

# Sort random permutation (numeric)
shuf -i 0-29 | sort -g
``` 

### `uniq`: <a name="uniq"></a>
Report or omit repeated adjacent lines.
```
SYNOPSIS
    uniq [OPTION]... [INPUT [OUTPUT]]

DESCRIPTION
    Filter adjacent matching lines from INPUT (or standard input),
    writing to OUTPUT (or standard output).

    -c, --count
        prefix lines by the number of occurrences
    -i, --ignore-case
        ignore differences in case when comparing
    -u, --unique
        only print unique lines

    Note: ’uniq’ does not detect repeated lines unless they are
    adjacent.
```
Combined with sort, is possible to gather repeated lines together, then with uniq we remove repeated lines.
```sh
# Display the unique values of field 6 in adult.data
cut -d "," -f 6 adult.data | sort | uniq

# Same counting the number of occurrences of each value
cut -d "," -f 6 adult.data | sort | uniq -c
``` 

### `join`: <a name="join"></a>
Join lines of two files on a common field.
```sh
SYNOPSIS
    join [OPTION]... FILE1 FILE2

DESCRIPTION
    For each pair of input lines with identical join fields, write
    a line to standard output. The default join field is the first,
    delimited by blanks.

    -a FILENUM
        also print unpairable lines from file FILENUM, where
        FILENUM is 1 or 2, corresponding to FILE1 or FILE2
    -j FIELD
        equivalent to ’-1 FIELD -2 FIELD’
    -t CHAR
        use CHAR as input and output field separator
    -v FILENUM
        like -a FILENUM, but suppress joined output lines
    -1 FIELD
        join on this FIELD of file 1
    -2 FIELD
        join on this FIELD of file 2
    -i, --ignore-case
        ignore differences in case when comparing fields

    Important: FILE1 and FILE2 must be sorted on the join fields.
```
1. Create files f13.txt and f17.txt from adult-nums.data
```sh
cut adult-nums.data -d "," -f 1,3 | shuf -n 1000 | sort -t "," -k 1,1 > f13.txt
cut adult-nums.data -d "," -f 1,7 | shuf -n 1000 | sort -t "," -k 1,1 > f17.txt
```
2. Join them on the first field
```sh
join -t "," -1 1 -2 1 f13.txt f17.txt

# Same but showing all lines of file 1
join -t "," -1 1 -2 1 -a 1 f13.txt f17.txt
```
> `-1`    indicates the table of the left<br>
> `1`     is the value from which you want to join

> `-2`    is the table on the right<br>
>`1`     is the value from which you want to join<br>

- JOIN » joins columns/fields using the keys in common, if a key is not present in one of the sides it desapears. 
- Left JOIN »  joins fields keeping all the keys on the left
- Right join » joins fields keeping all the keys on the right
- Full outer join » joins fields keeping ALL the keys


#### Summary <a name="summary"></a>
| command | function |
|------|---------------------|
| `split`<br> [options] [file] [prefix]<br> Ex: Split the text into 500-line files with: `split -l500 tiny_text --verbose` |  Divide big files into smaller files of 1000-line chunks |
| `cut` <br> [option] [file]<br> Ex: Extract just the second column: `cut -d',' -f2 example.csv` | Extracts fields or specific sections of a file/piped data.<br> It separates based on: fields, delimiters, byte positions or character positions |
| `paste`<br> [options] [file1-name] [file2-name]<br> Ex: Contents of two files separated by a comma `paste -d "," file1.txt file2.txt` | Join by columns/fields (without order)<br> Merging multiple files or lines of text into a single file or output |
| `join`<br> [options] [file1-name] [file2-name]<br> Ex: Join two files based on second field in each file  `join -1 2 -2 1 file1 file2`| Join by columns/fields<br> Merge two different files based on a common field |
| `grep`<br> '[search_pattern]' [file_name]<br> Ex: Search for a String in Files with Specific Extensions `grep 'ransomware' *.txt` | Search files for a specified textual pattern. Select rows with a given criteria... |
| `cat`<br> [options] [file_name]<br> Ex: Redirect Contents of Multiple Files `cat test1.txt test2.txt > test3.txt` | Joins by rows. Concatenates or Reads one or multiple files and prints their content row by row to the terminal.<br> `cat` is used to view file contents, combine files, and create new files.  |


### `comm`: <a name="comm"></a>
Compare sorted files FILE1 and FILE2 line by line.
```
SYNOPSIS
    comm [OPTION]... FILE1 FILE2

DESCRIPTION
    With no options, produce three-column output. Column one contains
    lines unique to FILE1, column two contains lines unique to FILE2,
    and column three contains lines common to both files.

    -1 suppress column 1 (lines unique to FILE1)
    -2 suppress column 2 (lines unique to FILE2)
    -3 suppress column 3 (lines that appear in both files)
```
Create files a.txt and b.txt
```sh
cut adult.data -d "," -f 1-5 | shuf -n 1000 | sort > a.txt
cut adult.data -d "," -f 1-5 | shuf -n 1000 | sort > b.txt
```

```sh
# Display lines that appear only in file a.txt
comm -23 a.txt b.txt

# Display lines that appear in both files
comm -12 a.txt b.txt
```
