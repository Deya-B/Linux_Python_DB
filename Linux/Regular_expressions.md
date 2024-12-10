## Linux Regular expressions
- Special characters which help search data and matching complex patterns.
- Regular expressions are shortened as ‘regexp’ or ‘regex’.
- They are used in many Linux programs like grep, bash, rename, sed, etc.

### Basic Regular expressions

| Symbol | Description | 
| ------ | ----------- | 
| `.` | matches any character.<br> Example: `pepit.`🠪 Find anything that matches pepit- followed by any character: pepito, pepita, pepitos...|
| `^` | only match THOSE at the BEGINNING of a line.<br> Example: `^pepito`🠪 Lines that match pepito as the FIRST word | 
| `$` | only match THOSE at the END of a line. <br> Example 1: `pepito$`🠪 Lines that have pepito at the end of the line.<br> Example 2: `^pepito$`🠪 Lines that ONLY have the word pepito| 
|`[abc]`| match ANY character WITHIN the brackets.<br> Example 1: `pepit[aei]`🠪 Find pepita, pepite, pepiti. <br> Example 2: `[0-9]`🠪 Match one character from 0-9 (it finds all numbers, but counts them as individual matches; for example if there is 1996, it finds it as 1,9,9,6) | 
| `[^abc]` |match any character NOT in the group in the brackets.<br> Example: `[^0-9]`🠪 Find anything that is NOT a number |
| `*` | after a character or expression means zero or more repetitions.<br> Example: `[0-9]*`🠪 Match all characters from 1-9 (here we do find all characters of 1996 together. Check it out with `grep -o "[0-9]*"`) | 



#### Examples with files:
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
  
