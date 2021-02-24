""" Python Program that searches through a file."""
# Kacper Grzenda

import argparse #https://docs.python.org/3/library/argparse.html

parser = argparse.ArgumentParser(description='Store a String', usage='%(prog)s [Enter File Name]')#Store a String from user Input
parser.add_argument('file', type=str) #Parser takes in a file name which will be of type string
args = parser.parse_args()
print(args)