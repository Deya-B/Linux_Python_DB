# Linux Regular expressions
- Special characters which help search data and matching complex patterns.
- Regular expressions are shortened as ‘regexp’ or ‘regex’.
- They are used in many Linux programs like grep, bash, rename, sed, etc.

## 1. Basic Regular expressions

| Symbol | Description | 
| ------ | ----------- | 
| `.` | matches any character.<br> Example: `pepit.`→ Find anything that matches pepit- followed by any character: pepito, pepita, pepitos...|
| `^` | only match THOSE at the BEGINNING of a line.<br> Example: `^pepito`→ Lines that match pepito as the FIRST word | 
| `$` | only match THOSE at the END of a line. <br> Example 1: `pepito$`→ Lines that have pepito at the end of the line.<br> Example 2: `^pepito$`→ Lines that ONLY have the word pepito| 
|`[abc]`| match ANY character WITHIN the brackets.<br> Example 1: `pepit[aei]`→ Find pepita, pepite, pepiti. <br> Example 2: `[0-9]`→ Match one character from 0-9 (it finds all numbers, but counts them as individual matches; for example if there is 1996, it finds it as 1,9,9,6) | 
| `[^abc]` |match any character NOT in the group in the brackets.<br> Example: `[^0-9]`→ Find anything that is NOT a number |
| `*` | after a character or expression means zero or more repetitions.<br> Example 1: `[0-9]*`→ Match all characters from 1-9 (here we do find all characters of 1996 together. Check it out with `grep -o "[0-9]*"`) <br> Example 2: "a*" → Match a or a with any-(but only one)-thing next to it | 

### 1.1 Examples with files:
- Lines with... any character (.), starting with (^), ending with ($):
  ```Nushell
  head -n 100 adult.data | grep "^25"              # Display all lines starting with 25
  head -n 100 adult.data | grep "Mexico, <=50K$"   # Display all lines ending with “Mexico, <=50K”
  head -n 100 adult.data | grep ".th"              # Display all lines 
  ```
- Mixing with numbers within `[]`:
  ```Nushell
  containing “th” preceded by any character
  head -n 100 adult.data | grep "[0-9]th"                # Lines containing “th” preceded by any numeric character
  head -n 100 adult.data | grep "[1-9][0-9]*th"          # Preceded by any number
  head -n 100 adult.data | grep "^[1-9][0-9]*, Private"  # Lines whose first field is a number and whose second field is “Private”
  head -n 100 adult.data | grep "[^0-9]*"                # Lines containing non numerical data
  ```
  
### 1.2 Deeper analysis into what is happening:
```Nushell
$ cat myfile.txt | grep "[^0-9]*"
```
  ![`cat myfile.txt | grep "[^0-9]*`](./imagesregex/Captura%20desde%202024-12-10%2020-44-35.png)
In this image we can see the result of using the regular expression `[^0-9]*` in a file with lines containing both letters and numbers. Whit this expression we remove lines with ONLY numbers, but those lines including both letters and numbers are shown.

On the other hand...
```Nushell
cat myfile.txt | grep "^[^0-9]*$"
```
![cat myfile.txt | grep "^[^0-9]*$"](./imagesregex/Captura%20desde%202024-12-10%2020-45-32.png)
In this we can se the result of using `^[^0-9]*$` instead. As observed only lines that DO NOT CONTAIN numeric characters are displayed.

The following expression extracts the opposite, **lines that contain only numbers**:
```Nushell
cat myfile.txt | grep "^[0-9]*$"
```

### 1.3 Escaping Meta-characteres
If we want to search for a character that has a special meaning (such
as . or ∧), we have to precede it with a backslash \
```Nushell
head -n 100 adult.data | grep "^[A-Z].*\.$" # Lines starting with a capital letter and ending with a period/dot
head -n 100 adult.data | grep "^\^"         # Lines that start with the ∧ symbol
```

## 2 Splice-junction Gene Sequences data set
For the following examples you must download the splice.data file:
```Nushell
wget https://archive.ics.uci.edu/ml/machine-learning-databases/molecular-biology/splice-junction-gene-sequences/splice.data
```

### 2.1 Grouping
- Sometimes we may want to group expressions using parentheses
- If we want the () symbols to be interpreted as group delimiters, we must escape them

Whilst with... 
- `GTA` We obtain all the exact matches GTA separately. <br> This means: GTAGTAAAA, will be identified as the two matches GTA, GTA.
- `GTA*` We obtain matches that contain GT+anything (any number of times) and resets with the start of a new GT. <br> This means GTAGTAAAA = (will yield) GTA, GTAAAA.

With **grouping** we can:
- `\(GTA\)*` Obtain GTA an indeterminate number of times

And with these is something else...
- `[GTA]` We obtain anything that is G, T, or A, singly. <br> This means: CCAGCTGCACAGGAGG = A, G, T, G, A, A, G, G, A, G, G.
- `[GTA]*` We obtain anything that is G, T, or A, single or group together between C's. Said in another way: all nucleotides except C, or any unbroken (by C) combination of these. <br> This means: CCAGCTGCACAGGAGG = AG, TG, A, AGGAGG.

### Extended regular expressions
- The option **-E** allows grep to understand a more extensive set of regular expressions (egrep)
- Extended regular expressions include all the basic meta-characters plus additional ones
- For example, the `()` are group delimiters with the -E option (we don't need to escape them " \\")

`cat splice.data | grep -E "GTA(GTA)*"` = `cat splice.data | grep "GTA\(GTA\)*"` <br> The 1st expression with **-E** option is equal to the 2nd without -E option.



```Nushell

```


  
```Nushell

```
