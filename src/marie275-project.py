import sys # to read the files frome the system
import re # to verify the numbers 
import argparse # to read from terminal

MEM_SIZE = 4096 # the capacity of memory
MAX_STEPS = 100000 # to no infinity loop
INT_MIN, INT_MAX = -32768, 32767 # to verify the numbers

NO_OPERAND = {"clear", "not", "input", "output", "halt"} # instruction need no operand

WITH_OPERAND = { # instruction need operand
    "load", "store", "add", "subt", "mult",
    "div", "and", "or", "jump", "skipcond",
    "loadi", "storei", "addi"
}

