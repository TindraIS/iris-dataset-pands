import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
import argparse
import seaborn as sns
import pandas as pd
import tools


# ---------------------------------- MAIN CODE ---------------------------------- #

# Wrap code in a try-except statement to handle errors in case arguments are not provided in the cmd line
'''
Initialise the ArgumentParser object, will allows for cmd line arguments to be defined.
Customise thethe parser by:
    (1) specifying the program name that will be used in the usage message;
    (2) defining a general description for the program and a closing message.
The prog arg can be interpolatedprog into the epilog string using the old-style string formatting operator %.
Given that f-strings replace names with their values as they run, the program will crashwith a NameError.

Define optional arguments for the filename and the Wikipedia's query with the following params:
    (1) Set long and short form flags;
    (2) Set required to false so that the program don't throw an error if no arguments are provided in the cmd line, 
        but rather handle the error in the below try-except statement;
    (3) Set metavar to empty to clean up the -h message by not showing the uppercase dest values (FILENAME and QUERY);
    (4) Set the helper with a brief description of what the argument does.
'''

try:
    parser = argparse.ArgumentParser(
    prog="analysis.py",
    description="Petalist is a program that runs an analysis on Fisher's Iris dataset.",
    epilog="Thanks for using %(prog)s!")
    parser.add_argument("-n", "--username", metavar="", required=True, help='Please enter your name.')
    args = parser.parse_args()

    # Declare variables 
    USERNAME = args.username    # Assign the filename provided in the cmd line to FILENAME using the dot notation on args
    df = tools.get_dataset()
    descriptive_summary = tools.descriptive_summary
    generate_histogram = tools.generate_histogram  
    generate_pairplot = tools.generate_pairplot 

    tools.opening_menu(USERNAME, df, descriptive_summary, generate_histogram, generate_pairplot)
    
except: 
    # Print a help message, including the program usage and information about the arguments defined with the ArgumentParser
    parser.print_help()
