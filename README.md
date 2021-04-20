# Project: Graph Theory 2021

**Student ID: G00373427

## About the Project
This project allows a user to search through a text file (.txt) using a [regular expression](#regular-expression) and outputs the matching lines of the file to the regular expression. The file path, file name and regular expression are input into the command line as command line arguments, which then the regular expression gets turned into a NFA which is used to search through the file and output the matching file lines to the regular expression.

## Project Instructions
Once Downloaded to Pc run programme in your Linux command line as so:
```
$ python3 graph-theory-project.py /mnt/c/folder/folder/folder/filefolder filename.txt "Regular Expression"
```

* '/mnt/c/folder/folder/folder/filefolder': The path to the folder the .txt file is located in.

* 'filename.txt': The name of the file you wish to match your expression to.

* '"Regular Expression"': Your regular expression e.g. ("abb.*.a.", "(a.b|b*)", "a.b.c.d.e.d.f.g", "1.(0.0)*.1")

## Technology Used

* Python 2.7.16

## Algorithm Explanation 
An infix expression is passed into a shunting algorithm where each character, operator or number in the infix is stripped apart and segmented into different stacks. If it is a character or number place them on the postfix stack. If it is an operator check what value, the operator holds by checking the operator precedence and then append the operator on top of the prefix stack, but check is the bracket operator exist keep all operators in between the brackets.

Once the infix expression is converted into the prefix expression, the prefix expression needs to be converted into an NFA through the Thompson construction algorithm which involves stripping the postfix and passing it through arrows which checks if the character from the stripped-down prefix will reach the accept state. These states are controlled by placing the arrows on stacks, this allows the algorithm to keep track of the current and previous states.

The NFA then gets compared to each word from the file the user input through the console. If the NFA is a match a print statement will by output in the console letting the user know there was a match by printing the word out. The match is decided by looping through each character in each word of the file and passing it through the NFA which checks if the character in the word will pass the accept state in the NFA.

## General Info
#### Regular Expression
A regular expression is a group of letters, numbers or special characters that specify a special pattern. This pattern can be used to find a specific sequence of letters or numbers in a file by using an algorithm (like this one coded or more of an advanced algorithm). Regular Expressions are useful for filtering which make them very flexible and [adaptable](https://www.softwaretestinggenius.com/rehearsal-of-qtp-in-1-hr-interview-questions-31-40/) for many projects. More details about Regular expression can be found [here](https://en.wikipedia.org/wiki/Regular_expression).

#### NFA
A non-deterministic finite automaton is used to match words(strings) to regular expressions. An NFA gives path for specific input from the current state to the next sate to the complete state and in some cases no state. Each NFA can be desgined differently to get optimal effienecy for a regular expression.

#### Postfix
A Postfix expression is a group of operators and characters, numbers where the operators are placed after the characters and numbers. e.g. (100.*.1., abb.*.a.)  
#### Infix
An Infix expression is where there is an operator in between characters or numbers. e.g. (a*b, 1.1)

