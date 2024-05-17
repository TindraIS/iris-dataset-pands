import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys


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
    '''
    This function creates a descriptive statistic summary of the variables in the Iris dataset.
    I. Initialise an empty string to store the summary and then we add overall summary, data types summary & 
        summary header for each species.
    II. Group the DataFrame by species & initialise a counter to be used to loop through them, as demonstrated in one of the lectures.
        Start the for loop - as we are grouping by multiple species, the group name will be a tuple so each group should be unpacked into two variables.
        Each iteration will then generate summary statistics for each species, and concatenate it to the summary container.
        https://realpython.com/pandas-groupby/
        https://realpython.com/python-for-loop/
        https://www.geeksforgeeks.org/how-to-iterate-over-dataframe-groups-in-python-pandas/
    III. Save summary in a txt file with writer mode. As per Python official documentation, the file param in open() is a path-like object giving the pathname.
        Therefore, to keep the repository nicely organised, we can specify the folder where the file should be saved. As the program is meant to be ran on different
        machines, the os module is used to get a relative path, as an absolute path would throw an error. 
        https://docs.python.org/3/library/functions.html#open
        https://stackoverflow.com/questions/72626730/python-launch-text-file-in-users-default-text-editor
        https://docs.python.org/3/library/os.path.html
    IV. Show message box & open the summary.txt file with the default text editor. As per Python documentation, 
        askokcancel returns a boolean value, so we check if response is True(OK) to open the file; otherwise we do nothing.
        https://stackoverflow.com/questions/72626730/python-launch-text-file-in-users-default-text-editor
        https://docs.python.org/3/library/tkinter.messagebox.html
    '''

    # I.
    # Initialise an empty string to store the summary
    summary = ''

    # Add overall summary, data types summary & summary header for each species
    summary += f"(1) Overall Descriptive Statistics:\n{df.describe(include='all').to_string()}\n\n"
    summary += f"(2) Data Types Summary:\n{df.dtypes.to_string()}\n\n"
    summary += f"(3) Summary for Each Species:\n\n"

    # II.
    # Group the DataFrame by species & initialise counter for the below for loop
    df_species = df.groupby('species')
    counter = 0

    # Iterate over each species and generate summary statistics
    for species, group_df in df_species:
        counter += 1
        summary += f"3.{counter} Summary for {species}\n"

        descriptive_statistics = group_df.describe(include='all').to_string() 
        summary += f"a) Descriptive Statistics:\n{descriptive_statistics}\n\n" # Add descriptive statistics summary with pd.describe()
        
        missing_values = group_df.isnull().sum().to_string()
        summary += f"b) Missing Values:\n{missing_values}\n\n"  # Add missing values summary with pd.isnull()
        
        unique_values = group_df.nunique().to_string()
        summary += f"c) Unique Values:\n{unique_values}\n\n"  # Add unique values summary with pd.nunique()
        summary += "\n\n"
    

    # III.
    # Specify folder in which txt should be saved
    file_path = os.path.join(os.getcwd(), 'descriptive summary', 'summary.txt')

    # Save summary in a txt file
    with open(file_path, 'w', encoding='utf-8') as writer:
            writer.write(summary)
    
    # IV. 
    # Display message box with "OK" and "Cancel" buttons
    response = messagebox.askokcancel("Descriptive summary", "A text file with a descriptive summary of each variable will be saved in the results directory. Please click OK to open the file.")

    # If response is True open the file, otherwise do nothing
    if response:
        os.startfile(file_path)
    else:
         pass


def generate_histogram(df):
    '''
    This function saves a histogram of each variable in the Iris dataset to PNG files.
    '''
    # I. 
    # Get the list of columns names in the DataFrame
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html
    variables = df.select_dtypes(include='number').columns
    
    # Dynamically calculate the number of rows and columns for the subplots
    num_variables = len(variables)       # Check how many variables the dataset contains
    num_rows = (num_variables + 1) // 2  # Ensure there are at least 2 plots per row
    num_columns = 2                    # Create 2 columns
    
    # II.
    # Create subplots
    fig, axes = plt.subplots(num_rows, num_columns, figsize=(12, 8))
    
    # Plot histograms for each variable
    # https://napsterinblue.github.io/notes/python/viz/subplots/
    # https://matplotlib.org/stable/gallery/color/named_colors.html#list-of-named-colors
    # Flatten the axes array
    axes = axes.flatten()           

    # Use enumerate() to get both the index and value of each pair
    for index, (col, ax) in enumerate(zip(variables, axes)):
        ax.hist(df[col], bins=20, color='sandybrown', edgecolor='black')
        ax.set_title(col)
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        
        # Cleanup the remainder unused subplots
        if index + 1 >= num_variables:
            [ax.set_visible(False) for ax in axes.flatten()[index+1:]]
            break
    
    # Adjust layout & set subplot suptitle
    plt.tight_layout()
    plt.suptitle("Distribution of Variables in the Iris Dataset\n")

    # III.
    # Specify folder in which PNG should be saved
    file_path = os.path.join(os.getcwd(), 'histograms', 'histograms.png')

    # Save plot
    fig.savefig(fname=file_path)      

    # IV. 
    # Display message box with "OK" and "Cancel" buttons
    response = messagebox.askokcancel("Generate histograms", "A histogram of each variable will be plotted and saved in the results directory. Please click OK to open the file.")

    # If response is True open the file, otherwise do nothing
    if response:
        fig.show()
    else:
         pass


def generate_pairplot(df):
    '''
    This function outputs a scatter plot of each pair of variables of the Iris dataset.
    '''
    # Plot a pairplot to analyse the interaction between the different variables
    # https://python-charts.com/correlation/pairs-plot-seaborn/
    sns.pairplot(df, hue="species", corner=True, kind="reg", plot_kws={'line_kws':{'color':'black'}})

    # Adjust layout & set subplot suptitle
    plt.tight_layout()
    plt.suptitle("Attribute Pairs by Species", fontsize=16)

    # III.
    # Specify folder in which PNG should be saved
    file_path = os.path.join(os.getcwd(), 'pair plot', 'pairplot.png')

    # Save plot
    plt.savefig(fname=file_path)      

    # IV. 
    # Display message box with "OK" and "Cancel" buttons
    response = messagebox.askokcancel("Generate pair scatter plot", "A scatter plot of each pair of variables will be created and saved in the results directory. Please click OK to open the file.")

    # If response is True open the file, otherwise do nothing
    if response:
        plt.show()
    else:
         pass

    messagebox.showinfo("Option 3", "You clicked Option 3")


def opening_menu(username, df, descriptive_summary, generate_histogram, generate_pairplot):

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
    # https://stackoverflow.com/questions/70406400/understanding-python-lambda-behavior-with-tkinter-button
    button1 = tk.Button(root, text=".get descriptive summary", command=lambda: descriptive_summary(df), bg="white", fg="gray9")
    button1.place(relx=0.60, rely=0.4, anchor="center")  # Place button relative to the center of the window
    button1['font'] = font_buttons

    button2 = tk.Button(root, text=".generate histogram", command=lambda: generate_histogram(df), bg="white", fg="gray9")
    button2.place(relx=0.59, rely=0.5, anchor="center")  # Place button relative to the center of the window
    button2['font'] = font_buttons

    button3 = tk.Button(root, text=".generate pair scatter plot", command=lambda: generate_pairplot(df), bg="white", fg="gray9")
    button3.place(relx=0.60, rely=0.6, anchor="center")  # Place button relative to the center of the window
    button3['font'] = font_buttons

    # Maximize the window
    root.state('zoomed')

    # Run the main event loop
    root.mainloop()