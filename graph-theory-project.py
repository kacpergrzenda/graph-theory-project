""" Python Program that searches through a file."""
# Kacper Grzenda

import argparse #https://docs.python.org/3/library/argparse.html
import os #https://docs.python.org/3/library/os.html
from pathlib import Path

# User Input.
parser = argparse.ArgumentParser(description='Store a String', usage='%(prog)s [Enter Directory Path, File Name, Expression]')#Store a String from user Input | python3 graph-theory-project.py /mnt/c/Users/kacper/Desktop/test
parser.add_argument('file', type=str, nargs='+', help='an integer for the accumulator') #Parser takes in a file name which will be of type string
args = parser.parse_args()
print(args.file)


# Change Directory.
filePath = Path(args.file[0])
os.chdir(filePath)

# Concatenation DirectoryPath and File Name.
fullPath = args.file[0] + args.file[1]
print(fullPath)

# Open File in Read Mode.
f = open(fullPath, "r")
print(f.read())
# Find the Expression|Word User is Searching for
expression = f.read().find(args.file[2])
print(expression)



f.close()


# print(filePath)

# retval = os.getcwd()

# print ("Current working directory %s" % retval)


# os.chdir("/mnt/c/Users/kacper/Desktop/college 3rd Year/Semester2/GraphTheory")
# #os.chdir(filePath)
# retval = os.getcwd()

# print ("Current working directory %s" % retval)


# print(os.listdir(os.getcwd()))

#C:\Users\kacper\Desktop\test
# /mnt/c/Users/kacper/Desktop/test
#/mnt/c/Users/kacper/Desktop/college 3rd Year/Semester2/GraphTheory
#sys.path.insert(1,args.file)
#print(args)
#print(args.file )
#path = 'C:\\Users\\kacper\\repo\\graph-theory-project\\test.txt'
#os.chdir(args.file)
#f = open('C:/Users/kacper/repo/graph-theory-project/test.txt', "r")
# test = os.listdir('../graph-theory-project/')
# test2 = os.path.abspath("path")
# test3 = os.path.exists(args.file)
# print(args.file)
# print(test2)
# print(test3)
#os.scandir
#C:\Users\kacper\Desktop\college$3rd$Year\Semester2\GraphTheory\test.txt
# filePath = input("Enter File Path:")
# regularExpression = input("Enter Regular expression:")
# \\mnt\\c\\Users\\kacper\\Desktop\\GraphTheory\\test.txt
# /mnt/c/Users/kacper/Desktop/GraphTheory/test.txt
# filePath = open('C:/Users/kacper/Desktop/college 3rd Year/Semester2/GraphTheory/test.txt', 'r')
# print(filePath.read())
#print(f.getcwd())