import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
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
    folder = 'results'
    file_name = 'summary.txt'
    file_path = os.path.join(os.getcwd(), folder, file_name)

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
    folder = 'results'
    file_name = 'histograms.png'
    file_path = os.path.join(os.getcwd(), folder, file_name)

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
    # I.
    # Plot a pairplot to analyse the interaction between the different variables
    # https://python-charts.com/correlation/pairs-plot-seaborn/
    sns.pairplot(df, hue="species", corner=True, kind="reg", plot_kws={'line_kws':{'color':'black'}})

    # Adjust layout & set subplot suptitle
    plt.tight_layout()
    plt.suptitle("Attribute Pairs by Species", fontsize=16)

    # II.
    # Specify folder in which PNG should be saved
    folder = 'results'
    file_name = 'pairplot.png'
    file_path = os.path.join(os.getcwd(), folder, file_name)

    # Save plot
    plt.savefig(fname=file_path)      

    # III. 
    # Display message box with "OK" and "Cancel" buttons
    response = messagebox.askokcancel("Generate pair scatter plot", "A scatter plot of each pair of variables will be created and saved in the results directory. Please click OK to open the file.")

    # If response is True open the file, otherwise do nothing
    if response:
        plt.show()
    else:
         pass


def outliers_summary(df):

    print(f"Starting {__name__}")
    
    # Get the list of columns names in the DataFrame
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html
    variables = df.select_dtypes(include='number').columns
    outlier_summary = []  # Initialize an empty list to store outlier information

    # Iterate over unique species values
    for species in df['species'].unique():
        # Filter dataframe for the current species
        df_species = df[df['species'] == species]
        print(f'\n\tLooping through {species}...')
        outlier_summary.append(f'\n>>> Outlier summary for {species} <<<\n')

        lower_array_agg = []
        upper_array_agg = []

        for var in variables: 
            # Calculate the upper and lower limits
            Q1 = df_species[var].quantile(0.25) # The 1st quartile is the value below which 25% of the data can be found
            Q3 = df_species[var].quantile(0.75) # The 3rd quartile is the value below which 75% of the data falls

            # Calculate the IQR, which measures the middle 50% of the data
            IQR = Q3 - Q1

            # Calculate the outlier thresholds as per the above formulas
            # Any data point below/above these values are considered outliers
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            
            # Create arrays of Boolean values indicating the outlier rows using Numpy’s `where` function
            # to find indices of all data points where the variable does meets the threshold condition
            # https://numpy.org/doc/stable/reference/generated/numpy.where.html
            upper_array = np.where(df_species[var] >= upper)[0]
            lower_array = np.where(df_species[var] <= lower)[0]

            lower_array_agg.append(lower_array)
            upper_array_agg.append(upper_array)

        # Check if any of the arrays contain outliers and append accordingly to the list.
        # Combine the variables and the arrays into a single iterable with zip() and loop through them 
        for var, lower_array, upper_array in zip(variables, lower_array_agg, upper_array_agg):
            # If any of the arrays isn't empty, append the outlier information to the list
            if len(lower_array) > 0 or len(upper_array) > 0:
                outlier_summary.append(f'\n\t\tOutliers found for {var}: \n\t\t\tLower bound: {lower_array} \n\t\t\tUpper bound: {upper_array}\n')
                print(f"\t\tOutlier summary for {var} appended to the array.")
            # If the arrays are empty, do nothing to prevent cluttering the list
            else:
                outlier_summary.append(f'\n\t\tNo outliers found for {var}\n')
                print(f"\t\tOutlier summary for {var} appended to the array.")
    
    # III.
    # Specify folder in which txt should be saved
    folder = 'results'
    file_name = 'outliers_summary.txt'
    file_path = os.path.join(os.getcwd(), folder, file_name)

    # Write the collected outlier information to a text file
    with open(file_path, "w") as file:
        for item in outlier_summary:
            file.write(item)
        print(f"\t\tOutlier summary for all variables for appended to the txt file.")

    # IV. 
    # Display message box with "OK" and "Cancel" buttons
    response = messagebox.askokcancel("Generate pair scatter plot", "A scatter plot of each pair of variables will be created and saved in the results directory. Please click OK to open the file.")

    # If response is True open the file, otherwise do nothing
    if response:
        os.startfile(file_path)
    else:
         pass
    
    # https://stackoverflow.com/questions/16676101/print-the-approval-sign-check-mark-u2713-in-python
    print("\n\t\u2713 Outliers function succesfully finished.")


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
    # https://tk-tutorial.readthedocs.io/en/latest/button/button.html
    # https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/button.html
    button1 = tk.Button(root, text=" .get descriptive summary", height=1, width=25,  anchor="w", justify="left", command=lambda: descriptive_summary(df), bg="LightSteelBlue4", fg="white")
    button1.place(relx=0.60, rely=0.4, anchor="center")  # Place button relative to the center of the window
    button1['font'] = font_buttons

    button2 = tk.Button(root, text=" .generate histogram", height=1, width=25,  anchor="w", justify="left", command=lambda: generate_histogram(df), bg="LightSteelBlue4", fg="white")
    button2.place(relx=0.60, rely=0.5, anchor="center")  # Place button relative to the center of the window
    button2['font'] = font_buttons

    button3 = tk.Button(root, text=" .generate pair scatter plot", height=1, width=25, anchor="w", justify="left", command=lambda: generate_pairplot(df), bg="LightSteelBlue4", fg="white")
    button3.place(relx=0.60, rely=0.6, anchor="center")  # Place button relative to the center of the window
    button3['font'] = font_buttons

    button4 = tk.Button(root, text=" .identify & handle outliers", height=1, width=25, anchor="w", justify="left", command=lambda: outliers_summary(df), bg="LightSteelBlue4", fg="white")
    button4.place(relx=0.60, rely=0.7, anchor="center")  # Place button relative to the center of the window
    button4['font'] = font_buttons

    # Maximize the window
    root.state('zoomed')

    # Run the main event loop
    root.mainloop()