#! /usr/bin/env python3
import argparse #https://docs.python.org/3/library/argparse.html

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator') #python3 myargs.py 10 12

parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')  #python3 myargs.py --sum 10 12

args = parser.parse_args()
print(args.accumulate(args.integers))
