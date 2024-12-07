# Table of Contents
1. [Branching introduction](#intro)
    1. [Basic IF Statement](#basicif)
    2. [](#)
2. [](#)
3. [](#)
4. [](#)
5. [](#)
6. [](#)


References: [tutorials](https://ryanstutorials.net/bash-scripting-tutorial/bash-if-statements.php)

# 1. Branching introduction <a name="intro"></a>
In this section of our Bash Scripting Tutorial you will learn the ways you may use if statements in your Bash scripts to help automate tasks.

If statements (and, closely related, case statements) allow us to make decisions in our Bash scripts. They allow us to decide whether or not to run a piece of code based upon conditions that we may set. If statements, combined with loops (which we'll look at in the next section) allow us to make much more complex scripts which may solve larger tasks.

Like what we have looked at in previous sections, their syntax is very specific so stay on top of all the little details.

## 1.1 Basic IF Statement <a name="basicif"></a>
A basic if statement effectively says: <br>
if a particular test is true then perform a given set of actions.
```sh
if [ <some test> ]
then
 ‪  <commands>
fi
```
Example:
```sh
#!/bin/bash 
FILE=$(ls *html | head -1) 
echo "Exit code: $?" # return exit code to 0 (TRUE) or 1 (FALSE) 
if [ -e $FILE ] 
then 
  echo "$FILE exists" 
fi
```
The square brackets ( [ ] ) in the if statement above are actually a reference to the command test: such as typing in the bash shell `$ test -e $FILE`

This means that all of the operators that test allows may be used here as well.

### `test` <a name="test"></a>
Check the test manual (`man test`) to see all of the possible operators, some of the more common ones are:
|Operator			|				Description 					|
|-------------|-----------------------------|
|! EXPRESSION |			The EXPRESSION is false.|
|-z STRING		|			The length of STRING is zero (ie it is empty).|
| STRING1 = STRING2 | STRING1 is equal to STRING2 |
| STRING1 != STRING2 | STRING1 is not equal to STRING2 |
| INTEGER1 -eq INTEGER2 | INTEGER1 is numerically equal to INTEGER2 |
| INTEGER1 -gt INTEGER2 | INTEGER1 is numerically greater than INTEGER2 |
| INTEGER1 -lt INTEGER2 | INTEGER1 is numerically less than INTEGER2 |
| -d FILE | FILE exists and is a directory |
| -e FILE | FILE exists |
| -r FILE | FILE exists and the read permission is granted |
| -s FILE | FILE exists and it's size is greater than zero (ie. it is not empty) |
| -w FILE | FILE exists and the write permission is granted |
| -x FILE | FILE exists and the execute permission is granted |
| <FILE1> -nt <FILE2> | True, if <FILE1> is newer than <FILE2> (mtime) |
| <FILE1> -ot <FILE2> | True, if <FILE1> is older than <FILE2> (mtime) |

*NOTE:*
  - The spaces before an after the <some test> are mandatory!!
  - = is slightly different to **-eq**
  	- [ 001 = 1 ] will return false as = does a string comparison (ie. character for character the same)
    - whereas -eq does a numerical comparison meaning [ 001 -eq 1 ] will return true
  - You'll notice that in the **if** statement above we indented the commands that were run if the statement was true. This is referred to as indenting and is an important part of writing good, clean code (in any language, not just Bash scripts). The aim is to improve readability and make it harder for us to make simple, silly mistakes. There aren't any rules regarding indenting in Bash so you may indent or not indent however you like and your scripts will still run exactly the same. I would highly recommend you do indent your code however (especially as your scripts get larger) otherwise you will find it increasingly difficult to see the structure in your scripts.

### AND and OR <a name="andor"></a>
(preferred way) The way often recommended to logically connect several tests with AND and OR is to use **several single test commands** and to **combine** them with the shell && and || **list control operators**:
```sh
if [ -n "$FILE" ] && [ -e "$FILE" ]; then
   echo "$FILE is not null and a file named $FILE exists"
fi
```
(el lado oscuro) The logical operators AND and OR for the test-command itself are -a and -o, thus:
```sh
if [ -n "$FILE" -a -e "$FILE" ]
then
    echo "$FILE is not null and a file named $FILE exists"
fi
```

### NOT <a name="not"></a>
As for AND and OR, there are 2 ways to negate a test with the shell keyword ! or passing ! as an argument to test. 

Here ! negates the exit status of the command test which is 0 (true), and the else part is executed:
```sh
if ! [ -d '/tmp' ]
then 
   echo "/tmp doesn't exists"
else 
   echo "/tmp exists"
fi
```

Here the test command itself exits with status 1 (false) and the else is also executed:
```sh
if  [ ! -d '/tmp' ]; then echo "/tmp doesn't exists"; else echo "/tmp exists"; fi
```

## 1.2 IF ... ELSE Statement / IF.. ELIF... ELSE Statement <a name="ifelse"></a>
Sometimes we want to perform a certain set of actions if a statemen is true, and another set of actions if it is false. We can accommodate this with the else mechanism:
```sh
if [ <some test> ]
then
   <commands>
else
   <other commands>
fi
```

Loock at the following example: 
```sh
DIR=$( pwd )/prueba
mkdir $DIR 

if [ $? -eq 0 ] 
then
        echo "Creando directorio $DIR"
else
        echo "Error al crear directorio $DIR"
fi
```

Sometimes we may have a series of conditions that may lead to different paths.
```sh
if [ <some test> ]
then
   <commands>
elif [ <some test> ] 
then
   <different commands>
else
   <other commands>
fi
```

# 2. LOOPS <a name="loops"></a>






```sh

```


