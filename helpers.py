'''
This files handles repetitive tasks pertaining to saving and creating files which performed multiple times in tools.py
'''

import os
import pandas as pd

def save_text_file(folder, file_name, content):
    '''
    This function saves a container in a txt file with writer mode. As per Python official documentation, the file param in open() is a path-like object giving the pathname.
    Therefore, to keep the repository nicely organised, we specify the folder where the file should be saved. As the program is meant to be ran on different
    machines, the os module is used to construct a full path, as a hardcoded absolute path would throw an error.  Also, the file_path makes use of os.path.join 
    to ensure compatibility across different operating systems. 
    After saving the file, it returns its path so that the file can be manipulated.
    
    https://docs.python.org/3/library/functions.html#open
    https://stackoverflow.com/questions/72626730/python-launch-text-file-in-users-default-text-editor
    https://docs.python.org/3/library/os.path.html
    '''

    folder = folder
    file_name = file_name
    file_path = os.path.join(os.getcwd(), folder, file_name)
    with open(file_path, 'w', encoding='utf-8') as writer:
        writer.write(content)

    return file_path


def save_csv_file(folder, file_name, df):
    '''
    This function saves a DataFrame as a CSV file with pandas to_csv(). To keep the repository nicely organised, we specify the folder where the file should be saved. 
    Also, as the program is meant to be ran on different machines, the os module is used to construct a full path, as a hardcoded absolute path would throw an error.  
    The file_path makes use of os.path.join to ensure compatibility across different operating systems. 
    After saving the file, it returns its path so that the function can be called by the "options" functions and not be empty.
    https://stackoverflow.com/questions/72626730/python-launch-text-file-in-users-default-text-editor
    https://docs.python.org/3/library/os.path.html
    '''

    folder = folder
    file_name = file_name    
    file_path = os.path.join(os.getcwd(), folder, file_name)
    df.to_csv(file_path, index=False)
    
    return file_path


def save_plot(folder, file_name, fig):
    '''
    This function saves plots as PNG files with matplotlib savefid(). To keep the repository nicely organised, we specify the folder where the file should be saved. 
    Also, as the program is meant to be ran on different machines, the os module is used to construct a full path, as a hardcoded absolute path would throw an error.  
    The file_path makes use of os.path.join to ensure compatibility across different operating systems. 
    After saving the file, it returns its path so that it can be maniputed in other parts of the code.
    https://stackoverflow.com/questions/72626730/python-launch-text-file-in-users-default-text-editor
    https://docs.python.org/3/library/os.path.html
    '''

    folder = folder
    file_name = file_name    
    file_path = os.path.join(os.getcwd(), folder, file_name)
    fig.savefig(fname=file_path)
    
