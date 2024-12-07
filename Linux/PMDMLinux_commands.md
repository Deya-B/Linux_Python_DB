# Table of Contents
1. [Linux Commands III](#commandsIII)
    1. [](#)
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
```sh
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

  * ```head -n 100 adult.data | fmt -70 -s``` Display the first lines of file adult.data cropping lines to 70 characters
  * ```head -n 100 adult.data | fmt -70 -tu``` Cropping lines to 70 characters, indenting each first line and using uniform spacing



```sh

``` 
