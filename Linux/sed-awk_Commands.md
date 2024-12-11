## The sed command
[sed](https://www.gnu.org/software/sed/) (stream editor) is a non-interactive command-line text editor
```Nushell
sed OPTIONS... [SCRIPT] [INPUTFILE...]
```
- Performs basic text transformations (substitutions, deletions, etc.) on the input stream
- Makes only one pass over the input, processing the text line by line
- Able to filter text in a pipeline

For example `sed 's/dog/cat/g' input.txt` replaces every appearance of dog with cat.

By default sed writes to the standard output. This behavior can be changed with the -i option to edit the file “in place”: `sed -i 's/dog/cat/g' input.txt`

### sed scripts
A sed script is a set of commands separated by semicolons (;) or newlines.

A sed command has the following syntax:
```Nushell
[addr]X[options]
```
- **[addr]** is an optional address that can be a line number, a range of lines or a regular expression
- **X** is a single-letter command to be executed on the lines that match the address pattern
- Some commands have **[options]** that modify their default behavior

Examples:
```Nushell
sed '10,20s/dog/cat/g' input.txt
```
- 10,20 is the address: lines 10 to 20
- s/dog/cat/ is the command: replace dog by cat
- g is an option to the s command: replace all appearances in each line

```Nushell
sed 's/dog/cat/' input.txt
```
- No address: perform substitution in all lines
- No options: replace only the first ocurrence in each line

### Basic sed commands
```Nushell
s/regexp/string/[flags]
```
- Substitute regular expression regexp by string, flags are optional:
    - g, replaces all matches, not just the first.
    - N, where N is a number, replace only the Nth match
    - p, prints the new line after replacement

- `q[exit_code]` EXIT sed without processing any more commands or input.
- `d` Delete the current line and start next cycle ignoring any other commands
- `p` Print the current line, usually used together with the -n option
- `n` If automatic output is not disabled, print the current line and replace it with the next input line; useful to skip lines
- `a \ newline` Insert the text given in a newline - 'a' appends after the text
- `i \ newline` Insert the text given in a newline - 'i' appends before the text


### sed addresses
- The address determines the line or lines on which a sed command will be executed
- If the address is missing, the command is run on all lines
- The address can be a line number, a line range or a regular expression
- The symbol ! at the end of an address means complement: all lines except those matching the address pattern

#### Numeric addresses
- `sed '125s/dog/cat/' input.txt` A **single number** indicates the line where the command should be executed
- `sed '$s/dog/cat/' input.txt` The **$** symbol refers to the last line in the input
- `sed '1i\Header' input.txt` Insert text 'Header' before the first line

#### Range addresses
1. `N,M`
Where N an M are integers, matches all lines between N and M (inclusive). <br>
`sed '30,40s/dog/cat/' input.txt` Replace dog by cat in lines from 30 to 40

2. `N~M`
Where N and M integers, matches lines N, N+M, N+2M, ... <br>
`sed '2~2s/dog/cat/' input.txt` Replace dog by cat in all even lines

#### Regular expression addresses
- `/regexp/` Where regexp is a regular expression. Refers to all lines that match regexp.
- sed accepts the same regular expressions as grep
- Option -E for extended regular expressions

Examples:
- `sed '/^[A-Z]/s/dog/cat/' input.txt` Replace dog by cat in all lines starting with a capital letter
- `sed '/dog/a\previous line has a dog' input.txt` Append line 'previous line has a dog' after each line containing 'dog'
- `sed '10,20d' input.txt` Delete lines 10 to 20
- `sed -n '/regexp/p' input.txt` Print all lines containing the regular expression regexp (grep)
- `sed '10,20!/s/dog/cat/' input.txt` Replace dog by cat in all lines except 10-20
- `sed '/regexp/!/s/dog/cat/' input.txt` Replace dog by cat in all lines not matching regexp

### Command grouping

- ``
- ``
- ``
- ``
- ``





```Nushell

```

```Nushell

```



```Nushell

```



```Nushell

```
