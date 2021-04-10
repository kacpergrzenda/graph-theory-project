""" Python Program that searches through a file."""
# Kacper Grzenda

import argparse  # https://docs.python.org/3/library/argparse.html
import os  # https://docs.python.org/3/library/os.html
from pathlib import Path


class State:
    """A state and its arrows in Thompson's construction."""

    # Constructor.
    def __init__(self, label, arrows, accept):
        """Label is the arrow labels, arrows is a list of states to point to, accept is a boolean as to wheter this is an accept state."""
        self.label = label
        self.arrows = arrows
        self.accept = accept


class NFA:
    """An non-deterministic finite automaton."""

    def __init__(self, start, end):
        self.start = start
        self.end = end


def re_to_nfa(postfix):
    # A stack for NFAs.
    stack = []
    # Loop through the postfix r.e. left to right.
    for c in postfix:
        # Concatenation.
        if c == '.':
            # Pop top NFA off stack.
            nfa2 = stack[-1]
            stack = stack[:-1]
            # Pop the next NFA off stack.
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Make accept state of NFA1 non-accept.
            nfa1.end.accept = False
            # Make it point at start state of nfa2.
            nfa1.end.arrows = [nfa2.start]
            # Make a new NFA with nfa1's start state and nfa2's end state.
            nfa = NFA(start=nfa1.start, end=nfa2.end)
            # Push to the stack.
            stack.append(nfa)
        elif c == '|':
            # Pop top NFA off stack.
            nfa2 = stack[-1]
            stack = stack[:-1]
            # Pop the next NFA off stack.
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Create new start and end states.
            start = State(label=None, arrows=[], accept=False)
            end = State(label=None, arrows=[], accept=True)
            # Make new start state point at old start states.
            start.arrows.append(nfa1.start)
            start.arrows.append(nfa2.start)
            # Make old end states non-accept.
            nfa1.end.accept = False
            nfa2.end.accept = False
            # Point old end states to new one.
            nfa1.end.arrows.append(end)
            nfa2.end.arrows.append(end)
            # Make a new NFA.
            nfa = NFA(start, end)
            # Push to the stack.
            stack.append(nfa)
        elif c == '*':
            # Pop one NFA off stack.
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Create new start and end states.
            start = State(label=None, arrows=[], accept=False)
            end = State(label=None, arrows=[], accept=True)
            # Make new start state point at old start states.
            start.arrows.append(nfa1.start)
            # And at the new end state.
            start.arrows.append(end)
            # Make old accept state non-accept.
            nfa1.end.accept = False
            # Make old end state point to new end state.
            nfa1.end.arrows.append(end)
            # Make old end state point to old start state
            nfa1.end.arrows.append(nfa1.start)
            # Make a new NFA.
            nfa = NFA(start, end)
            # Push to the stack.
            stack.append(nfa)
        else:
            # Create an NFA for the non-special charcter c.
            # Create the end state.
            end = State(label=None, arrows=[], accept=True)
            # Create the start state, pointed at the end state.
            start = State(label=c, arrows=[], accept=False)
            # Point new start state at new end state.
            start.arrows.append(end)
            # Create the NFA with the start and end state.
            nfa = NFA(start=start, end=end)
            # Append the NFA to the NFA stack.
            stack.append(nfa)

    # There should only be one NFA on the stack.
    if len(stack) != 1:
        return None
    else:
        return stack[0]


def shunt(infix):
    """Convert infix expressions to postfix."""
    # The eventual output.
    postfix = ""
    # The shunting yard operator stack.
    stack = ""
    # operator precedence.
    prec = {'*': 100, '.': 90, '|': 80}
    # loop through the input a cahracter at a time.
    for c in infix:
        # If c is a digit.
        # c is an operator.
        if c in {'*', '.', '|'}:
            # check what is on the stack.
            while len(stack) > 0 and stack[-1] != '(' and prec[stack[-1]] >= prec[c]:
                # Append operator at top of stack to output.
                postfix = postfix + stack[-1]
                # Remove operator from stack.
                stack = stack[:-1]
            # Push c to stack.
            stack = stack + c
        elif c == '(':
            # Push c to stack.
            stack = stack + c
        elif c == ')':
            while stack[-1] != '(':
                # Append operator at top of stack to output.
                postfix = postfix + stack[-1]
                # Remove operator from stack.
                stack = stack[:-1]
            # Remove open bracket from stack.
            stack = stack[:-1]
        else:
            # Push c to stack.
            postfix = postfix + c
    while len(stack) != 0:
        # Append operator at top of stack to output.
        postfix = postfix + stack[-1]
        # Remove operator from stack.
        stack = stack[:-1]
    return postfix


# User Input.
# Store a String from user Input | python3 graph-theory-project.py /mnt/c/Users/kacper/Desktop/test | 
# python3 graph-theory-project.py /mnt/c/Users/kacper/Desktop/test test.txt "*kacper"
# python3 graph-theory-project.py /mnt/c/Users/kacper/Desktop/test test.txt "abb.*.a."
parser = argparse.ArgumentParser(
    description='Store a String', usage='%(prog)s [Enter Directory Path, File Name, Expression]')
# Parser takes in a file name which will be of type string
parser.add_argument('file', type=str, nargs='+',
                    help='an integer for the accumulator')
args = parser.parse_args()
print(args.file)


# Change Directory.
filePath = Path(args.file[0])
os.chdir(filePath)

# Concatenation DirectoryPath and File Name.
fullPath = args.file[0] + "/" + args.file[1]
print(fullPath)

# Open File in Read Mode.
f = open(fullPath, 'r')
# print(f.read().find( args.file[2])) #Find the line Number of the word enterd by user
print(f"{args.file[2]} - > {args.file[2]}")
print(f"postfix: {shunt(args.file[2])}")
print(f"nfa:    {re_to_nfa(shunt(args.file[2]))}")


#Close File .
f.close()


# print(filePath)

# retval = os.getcwd()

# print ("Current working directory %s" % retval)


# os.chdir("/mnt/c/Users/kacper/Desktop/college 3rd Year/Semester2/GraphTheory")
# #os.chdir(filePath)
# retval = os.getcwd()

# print ("Current working directory %s" % retval)


# print(os.listdir(os.getcwd()))

# C:\Users\kacper\Desktop\test
# /mnt/c/Users/kacper/Desktop/test
# /mnt/c/Users/kacper/Desktop/college 3rd Year/Semester2/GraphTheory
# sys.path.insert(1,args.file)
# print(args)
#print(args.file )
#path = 'C:\\Users\\kacper\\repo\\graph-theory-project\\test.txt'
# os.chdir(args.file)
#f = open('C:/Users/kacper/repo/graph-theory-project/test.txt', "r")
# test = os.listdir('../graph-theory-project/')
# test2 = os.path.abspath("path")
# test3 = os.path.exists(args.file)
# print(args.file)
# print(test2)
# print(test3)
# os.scandir
# C:\Users\kacper\Desktop\college$3rd$Year\Semester2\GraphTheory\test.txt
# filePath = input("Enter File Path:")
# regularExpression = input("Enter Regular expression:")
# \\mnt\\c\\Users\\kacper\\Desktop\\GraphTheory\\test.txt
# /mnt/c/Users/kacper/Desktop/GraphTheory/test.txt
# filePath = open('C:/Users/kacper/Desktop/college 3rd Year/Semester2/GraphTheory/test.txt', 'r')
# print(filePath.read())
# print(f.getcwd())
