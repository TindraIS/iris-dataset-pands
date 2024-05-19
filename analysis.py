'''
Name: analysis.py

Author: Irina Simoes

Description: This program is the main file of the pands-project repository, orchestrating the running logic.
    I. As showed in one of the lectures, use the logging module to record the error details to a txt file for debugging purposes
        with the below configurations passed as parameters:
        - Only log messages with level ERROR or higher.
        - Error messages will be recoded in the error.log file.
        - Open the log file in append mode, so that previous data doesn't get overriden.
        - Format of the error messages with the time it occured, error level and error message.

    II. Wrap code in a try-except statement to handle errors in case arguments are not provided in the cmd line or any other error occurs.

    III. Initialise the ArgumentParser object, which allows for cmd line arguments to be defined.
        Customise the parser by:
            (1) specifying the program name that will be used in the usage message;
            (2) defining a general description for the program and a closing message.
        The prog arg can be interpolatedprog into the epilog string using the old-style string formatting operator %.
        Given that f-strings replace names with their values as they run, the program will crashwith a NameError.

        Define optional arguments for the filename with the following params:
            (1) Set long and short form flags;
            (2) Set required to True as the program isn't meant to run without a name being provided in the cmd line, 
            (3) Set metavar to empty to clean up the -h message by not showing the uppercase dest values (USERNAME);
            (4) Set the helper with a brief description of what the argument does.

    IV. Specify tkinter opening menu function parameters:
            (1) usarname is taken from the cmd line argument
            (2) df is the Iris dataset returned by the get_dataset() function in the tools module
            (3) df_cleaned is the .csv Iris dataset returned by the outliers_cleanup() function in the tools module
                - First, we create contains for the folder and file name;
                - Secondly, to avoid using a hardcoded absolute path which would throw an error when running on different machines,
                we construct the full file path using the os module.
                - Finally, the data is loaded into a DataFrame using pandas' read_csv(), passing the file path as a param.

    V. Call the opening_menu() function from the menu module, passing in the above parameters.

References:
    - https://docs.python.org/3/howto/logging.html
    - https://realpython.com/python-logging/
    - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
    - https://realpython.com/command-line-interfaces-python-argparse/
    - https://stackoverflow.com/questions/1009860/how-can-i-read-and-process-parse-command-line-arguments
    - https://docs.python.org/3/library/argparse.html
    - https://www.w3schools.com/python/python_try_except.asp
'''

import argparse
import os
import pandas as pd
import tools
import menu
import logging

# I.
# Set up logging configuration
logging.basicConfig(level=logging.ERROR, filename='error.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')
# II. 
try:
    # III. 
    # Create an ArgumentParser object to handle cmd line arguments
    parser = argparse.ArgumentParser(
        prog="analysis.py",
        description="Petalist is a program that runs an analysis on Fisher's Iris dataset.",
        epilog="Thanks for using %(prog)s!")
    
    # Define a required cmd line argument for the username
    parser.add_argument("-u", "--username", 
                        metavar="", 
                        required=True, 
                        help='Please enter your name.')
    
    # Parse the cmd line arguments
    args = parser.parse_args()

    # IV. 
    # Declare variables that contain the opening_menu() parameters
    username = args.username                                # Assign the username provided in the cmd line
    df = tools.get_dataset()                                # Load the dataset using a function from the tools module
    
    folder = 'results'                                      # Specify the folder and filename for the cleaned dataset
    file_name = 'II.dataframe_cleaned.csv'
    file_path = os.path.join(os.getcwd(),folder,file_name)  # Construct the full file path
    df_cleaned = pd.read_csv(file_path)                     # Read in the cleaned dataset into a pandas DataFrame

    # V.
    # Call the opening menu function from the menu module, passing in the username and DataFrames as parameters
    menu.opening_menu(username, df, df_cleaned)

except:
    # If an exception occurs, log the error before printing the help message
    logging.error("An error occurred", exc_info=True)
    # Print the help message, including the program usage and information about the arguments
    parser.print_help()
