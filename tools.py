import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
import seaborn as sns
import pandas as pd

def get_dataset():

    # https://github.com/mwaskom/seaborn-data
    datasets_list = sns.get_dataset_names()

    # Access the list returned by Seaborn with datasets names, filtering out the string
    # matching the 'iris' substring and adding it to a new list.
    # Then access the list with the returned name by indexing the result.
    iris_dataset = list(filter(lambda x: "iris" in x, datasets_list))[0]

    # Print dataset name (uncomment for sanity check) 
    #print(f"Dataset name is: {iris_dataset}")

    # Load the dataset which is a DataFrame object by default, as the Seaborn library is 
    # closely integrated with pandas data structures.
    # https://seaborn.pydata.org/generated/seaborn.load_dataset.html)]
    df = sns.load_dataset(iris_dataset)

    # Return the DataFrame object
    return df

def descriptive_summary(df):

    # Initialise an empty string to store the summary
    summary = ''

    # Add overall summary, data types summary & summary header for each species
    summary += f"(1) Overall Descriptive Statistics:\n{df.describe(include='all').to_string()}\n\n"
    summary += f"(2) Data Types Summary:\n{df.dtypes.to_string()}\n\n"
    summary += f"(3) Summary for Each Species:\n\n"

    # Group the DataFrame by species & initialise counter for the below for loop
    # https://realpython.com/pandas-groupby/
    df_species = df.groupby('species')
    counter = 0

    # Iterate over each species and generate summary statistics
    '''
    As we are grouping by multiple species, the group name will be a tuple so each group should be unpacked into two variables.
    Each iteration will then generate summary statistics for each species, and concatenate it to the summary container.
    https://realpython.com/python-for-loop/
    https://www.geeksforgeeks.org/how-to-iterate-over-dataframe-groups-in-python-pandas/
    '''
    for species, group_df in df_species:
        counter += 1
        summary += f"3.{counter} Summary for {species}\n"
        summary += f"a) Descriptive Statistics:\n{group_df.describe(include='all').to_string()}\n\n"
        summary += f"b) Missing Values:\n{group_df.isnull().sum().to_string()}\n\n"  # Add missing values summary
        summary += f"c) Unique Values:\n{group_df.nunique().to_string()}\n\n"  # Add unique values summary
        summary += "\n\n"
    
    # Save summary in a txt file
    with open("summary.txt", 'w', encoding='utf-8') as writer:
            writer.write(summary)
    
    messagebox.showinfo("Descriptive summary", "A text file with a descriptive summary of each variable will be saved in the results directory. Please click OK to open the file.")

def generate_histogram():
    messagebox.showinfo("Generate histogram", "You clicked Option 2")

def generate_pairplot():
    messagebox.showinfo("Option 3", "You clicked Option 3")


def opening_menu(username):

    # https://www.geeksforgeeks.org/tkinter-cheat-sheet/
    # Create the main window
    root = tk.Tk()
    root.title("PETALIST || Iris Dataset Analysis")

    # Load image
    image = tk.PhotoImage(file="C:/Users/ifs/OneDrive/Documents/ATU/Programming & Scripting/pands-project/images/menu_background.png")
    image = image.subsample(2, 2)  # Resize by a factor of 2 in both dimensions

    # Create a label to display the image
    image_label = tk.Label(root, image=image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)  # Fill the entire window with the image

    # Create Font object
    # https://pythonexamples.org/python-tkinter-button-change-font/
    # https://www.geeksforgeeks.org/tkinter-fonts/
    font_buttons = font.Font(family='Agency FB', size=10, weight="bold")
    font_label_heading = font.Font(family='Agency FB', size=26, weight="bold")
    font_label_text = font.Font(family='Agency FB', size=14)

    # Create labels for text
    label1 = tk.Label(root, fg="gray9", bg="white", text=f"Hello {username},", font=font_label_heading)
    label1.place(relx=0.54, rely=0.2, anchor="sw")
    label2 = tk.Label(root, fg="gray9", bg="white", text="\nWelcome to Petalist, the Iris dataset analysis program.\nPlease select one of the options below:                      .", font=font_label_text)
    label2.place(relx=0.54, rely=0.3, anchor="sw")

    # Create buttons
    # Colours: https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
    button1 = tk.Button(root, text=".get descriptive summary", command=lambda: descriptive_summary(df), bg="white", fg="gray9")
    button1.place(relx=0.60, rely=0.4, anchor="center")  # Place button relative to the center of the window
    button1['font'] = font_buttons

    button2 = tk.Button(root, text=".generate histogram", command=generate_histogram, bg="white", fg="gray9")
    button2.place(relx=0.59, rely=0.5, anchor="center")  # Place button relative to the center of the window
    button2['font'] = font_buttons

    button3 = tk.Button(root, text=".generate pair scatter plot", command=generate_pairplot, bg="white", fg="gray9")
    button3.place(relx=0.60, rely=0.6, anchor="center")  # Place button relative to the center of the window
    button3['font'] = font_buttons

    # Maximize the window
    root.state('zoomed')

    # Run the main event loop
    root.mainloop()
