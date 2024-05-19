'''
Name: tools.py

Author: Irina Simoes

Description: This file contains a module with all the functions that perform the core tasks on the menu.py.

'''

import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import sys

# _____________________ GET IRIS _____________________
def get_dataset():
    '''
    This function fetches the Iris dataset from the Seaborn library as a DataFrame object.

    I. Get a list of all datasets available in the Seasborn library
       https://github.com/mwaskom/seaborn-data
       https://seaborn.pydata.org/generated/seaborn.get_dataset_names.html

    II. Use the filter() function with a lambda to filter elements in the datasets names list returned by Seaborn 
        containing the 'iris' string. As the previous is wrapped in list, we then access it by indexing the first and only result 
        returned by the lambda function.
        https://seaborn.pydata.org/generated/seaborn.load_dataset.html
        https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-39.php

    III. Load the Iris dataset which is a DataFrame object by default, as the Seaborn library is closely integrated with pandas 
         data structures. Then we use the return statement to send the DataFrame back to the caller of the function, enabling 
         analysis.py to access the Iris dataset.
         https://seaborn.pydata.org/generated/seaborn.load_dataset.html)]
    '''

    # I.
    # Get a list of all datasets available in the Seasborn library
    datasets_list = sns.get_dataset_names()

    # II.
    # Access the list returned by Seaborn with datasets names
    iris_dataset = list(filter(lambda x: "iris" in x, datasets_list))[0]

    # Print dataset name (uncomment for sanity check) 
    #print(f"Dataset name is: {iris_dataset}")

    # III.
    # Load the Iris dataset as df
    df = sns.load_dataset(iris_dataset)

    # Return the DataFrame object
    return df


# _____________________ TXT SUMMARY _____________________
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
        Therefore, to keep the repository nicely organised, we specify the folder where the file should be saved. As the program is meant to be ran on different
        machines, the os module is used to construct a full path, as a hardcoded absolute path would throw an error.  Also, the file_path makes use of os.path.join 
        to ensure compatibility across different operating systems. 
        https://docs.python.org/3/library/functions.html#open
        https://stackoverflow.com/questions/72626730/python-launch-text-file-in-users-default-text-editor
        https://docs.python.org/3/library/os.path.html

    IV. Show message box & open the summary.txt file with the default text editor. As per Python documentation, 
        askokcancel returns a boolean value, so we check if response is True(OK) to open the file; otherwise we do nothing.
        https://stackoverflow.com/questions/72626730/python-launch-text-file-in-users-default-text-editor
        https://docs.python.org/3/library/tkinter.messagebox.html
    '''

    # I.
    print(f"\nStarting {__name__}/descriptive_summary()")

    # Initialise an empty string to store the summary
    summary = ''

    # Add overall summary, data types summary & summary header for each species
    descriptive_statistics = df.describe(include='all').to_string() 
    summary += f"(1) Overall Descriptive Statistics:\n{descriptive_statistics}\n\n"
    
    missing_values = df.isnull().sum().to_string()
    summary += f"(2) Data Types Summary:\n{missing_values}\n\n"
    
    print(f'\n\tOverall summary computed.')

    # II.
    summary += f"(3) Summary for Each Species:\n\n"

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
    
    print(f'\tSpecies summary computed.')

    # III.
    # Specify folder in which txt should be saved
    folder = 'results'
    file_name = 'I.variables_summary.txt'
    file_path = os.path.join(os.getcwd(), folder, file_name)

    # Save summary in a txt file
    with open(file_path, 'w', encoding='utf-8') as writer:
            writer.write(summary)
    print(f"\tDescriptive summaries added to the txt file.")

    # IV. 
    # Display message box with "OK" and "Cancel" buttons
    response = messagebox.askokcancel("Descriptive summary", "A text file with a descriptive summary of each variable will be saved in the results directory. Please click OK to open the file.")

    # If response is True open the file, otherwise do nothing
    if response:
        os.startfile(file_path)
        print(f"\tUser opened the file.")
    else:
        print(f"\tUser closed the pop-up.")
    
    # https://stackoverflow.com/questions/16676101/print-the-approval-sign-check-mark-u2713-in-python
    print("\n\t\u2713 Descriptive summary function successfully finished.")

# _____________________ OUTLIERS _____________________
def outliers_summary(df):
    '''
    This function computes a summary of outliers present in the Iris dataset by species, using the Inter Quartile Range (IQR) 
    approach to determine if an entry is an outlier. Given that the IQR measures the middle 50% of the data, outliers are 
    typically defined by statisticians as data points that fall 1.5 times above the third quartile or below the first quartile.
    Therefore, the formulas that define the outliers thresholds are:
            - Lower Bound = Q1 - 1.5 x IQR
            - Upper Bound = Q3 + 1.5 x IQR
    https://www.geeksforgeeks.org/detect-and-remove-the-outliers-using-python/
    https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/box-whisker-plots/a/identifying-outliers-iqr-rule
    
    I. Create a container for the DataFrame columns names which will be analysed for outliers, filtering out any categorical features.
       https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html
    
    II. Initialise outlier_summary as an empty list to store the outlier information for each species. Then start looping through 
        each unique species in the df, filtering it for the current species. Bearing in mind that all iterations will have to be recorded,
        we create empty arrays(lower/upper_array_agg) which will serve as containers to aggregate the outlier indices.

    III. Compute the IQR calculation for each variable within each species using Numpy's where() function to identify the indices of outliers, 
        which are stored in upper_array and lower_array. Then append each iteration to lower/upper_array_agg.
        https://numpy.org/doc/stable/reference/generated/numpy.where.html
        
    IV. Create a final for loop to iterate through the combined list of variables and their corresponding outlier arrays.
        If any outliers are found, the arrays are not empty and so the outlier information is appended to the summary list.
        If no outliers are found, a message indicating no outliers is appended to the list.
        https://realpython.com/python-zip-function/

    V.  The outlier information is written to a text file, with each item in the outlier_summary list being written line by line 
        with writer mode. As per Python official documentation, the file param in open() is a path-like object giving the pathname.
        Therefore, to keep the repository nicely organised, we specify the folder where the file should be saved. 
        As the program is meant to be ran on different machines, the os module is used to construct a full path, as a hardcoded absolute 
        path would throw an error. Also, the file_path makes use of os.path.join to ensure compatibility across different operating systems. 
        https://docs.python.org/3/library/functions.html#open
        https://stackoverflow.com/questions/72626730/python-launch-text-file-in-users-default-text-editor
        https://docs.python.org/3/library/os.path.html
    
    VI. After running the analysis, ask the user if they want to proceed with generating a scatter plot and viewing the results.
        If the user clicks OK, the generated file is opened using os.startfile.
        If the user clicks Cancel, the program does nothing apart from printing a debugging message.
        https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/tkMessageBox.html
    '''

    # I. 
    print(f"Starting {__name__}/outliers_summary()")
    
    # Get the list of columns names in the DataFrame
    variables = df.select_dtypes(include='number').columns
    
    # II.
    # Initialise an empty list to store outlier information
    outlier_summary = []  

    # Iterate over unique species values
    for species in df['species'].unique():

        # Filter dataframe for the current species
        df_species = df[df['species'] == species]
        print(f'\n\tLooping through {species}...')
        
        outlier_summary.append(f'\n>>> Outlier summary for {species} <<<\n')

        lower_array_agg = []
        upper_array_agg = []

        # III.
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
            
            # Create arrays of Boolean values indicating the outlier rows using Numpy's where() function
            # to find indices of all data points where the variable does meet the threshold condition
            upper_array = np.where(df_species[var] >= upper)[0]
            lower_array = np.where(df_species[var] <= lower)[0]

            lower_array_agg.append(lower_array)
            upper_array_agg.append(upper_array)

        # IV.
        # Check if any of the arrays contain outliers and append accordingly to the list.
        # Combine the variables and the arrays into a single iterable with zip() and loop through them 
        for var, lower_array, upper_array in zip(variables, lower_array_agg, upper_array_agg):
            
            # If any of the arrays isn't empty, append the outlier information to the list
            if len(lower_array) > 0 or len(upper_array) > 0:
                outlier_summary.append(f'\n\t\tOutliers found for {var}: \n\t\t\tLower bound: {lower_array} \n\t\t\tUpper bound: {upper_array}\n')
                print(f"\t\tOutlier summary for {var} appended to the array.")
            
            # If the arrays are empty, append a message stating so to maintain completeness 
            else:
                outlier_summary.append(f'\n\t\tNo outliers found for {var}\n')
                print(f"\t\tOutlier summary for {var} appended to the array.")
    
    # V.
    # Specify folder in which txt should be saved
    folder = 'results'
    file_name = 'II.outliers_summary.txt'
    file_path = os.path.join(os.getcwd(), folder, file_name)

    # Write the collected outlier information to a text file
    with open(file_path, "w") as file:
        for item in outlier_summary:
            file.write(item)
        print(f"\t\tOutlier summary for all variables for appended to the txt file.")

    # VI. 
    # Display message box with "OK" and "Cancel" buttons
    response = messagebox.askokcancel("Generate pair scatter plot", "A scatter plot of each pair of variables will be created and saved in the results directory. Please click OK to open the file.")

    # If response is True open the file, otherwise do nothing
    if response:
        os.startfile(file_path)
        print(f"\tUser opened the file.")
    else:
        print(f"\tUser closed the pop-up.")
    
    # https://stackoverflow.com/questions/16676101/print-the-approval-sign-check-mark-u2713-in-python
    print("\n\t\u2713 Outliers summary function successfully finished.")


def outliers_cleanup(df):
    '''
    Using the same logic as outliers_summary(df), this function computes a summary of outliers present in the Iris dataset by species.
    '''

    # I.
    print(f"Starting {__name__}/outliers_cleanup()")
    
    # Get the list of columns names in the DataFrame
    variables = df.select_dtypes(include='number').columns

    # Initialise empty array to store indices of outlier rows
    outlier_indices = []

    # Iterate over unique species values
    for species in df['species'].unique():
        
        # Filter dataframe for the current species
        df_species = df[df['species'] == species]
        print(f'\n\tLooping through {species}...')

        for var in variables: 
            # Calculate the upper and lower limits
            Q1 = df_species[var].quantile(0.25)  # The 1st quartile is the value below which 25% of the data can be found
            Q3 = df_species[var].quantile(0.75)  # The 3rd quartile is the value below which 75% of the data falls

            # Calculate the IQR, which measures the middle 50% of the data
            IQR = Q3 - Q1

            # Calculate the outlier thresholds as per the above formulas
            # Any data point below/above these values are considered outliers
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            
            # Use Numpy's where function to get [indices] of upper/lower outliers & combined them
            upper_outliers = np.where(df_species[var] >= upper)[0]
            lower_outliers = np.where(df_species[var] <= lower)[0]
            all_outliers = np.concatenate((upper_outliers, lower_outliers))
            
            # II.
            # Collect all indices by mapping local indices in df_species back to the global indices in the original df 
            # with iloc
            # https://www.geeksforgeeks.org/python-extracting-rows-using-pandas-iloc/
            global_outliers = df_species.iloc[all_outliers].index
            
            # Collect global outlier indices with extend() method to add multiple elements to a list
            # Tried appending but it didn't work as it would add the entire list as a single element, 
            # instead of adding each element of the provided iterable to the list individually
            # https://www.geeksforgeeks.org/append-extend-python/
            outlier_indices.extend(global_outliers)
    
    # III.
    # Drop outliers from the original df
    df = df.drop(index=outlier_indices)

    # Save the cleaned df as .csv file & specify folder in which the csv should be saved
    folder = 'results'
    file_name = 'II.dataframe_cleaned.csv'
    file_path = os.path.join(os.getcwd(), folder, file_name)
    df.to_csv(file_path,index=False)
    print("\tNew df saved as a .csv file.")
   
    # IV.
    # Display message box with "OK" and "Cancel" buttons
    response = messagebox.askokcancel("Outliers summary", "A text file with an outlier summary by species will be saved in the results directory. Please click OK to open the file.")

    # If response is True open the csv, otherwise do nothing
    if response:
        os.startfile(file_path)
        print(f"\tUser opened the file.")
    else:
        print(f"\tUser closed the pop-up.")
    
    # https://stackoverflow.com/questions/16676101/print-the-approval-sign-check-mark-u2713-in-python
    print("\n\t\u2713 Outliers cleanup function successfully finished.")

    return df
        

# _____________________ HISTOGRAM _____________________
def generate_histogram(df):
    '''
    This function saves a histogram of each variable in the Iris dataset to PNG files.
    '''

    print(f"Starting {__name__}/generate_histogram()")

    # I. 
    # Get the list of columns names in the DataFrame
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html
    variables = df.select_dtypes(include='number').columns
    
    # Dynamically calculate the number of rows and columns for the subplots
    num_variables = len(variables)       # Check how many variables the dataset contains
    num_rows = (num_variables + 1) // 2  # Ensure there are at least 2 plots per row
    num_columns = 2                      # Create 2 columns
    
    # II.
    # Create subplots
    fig, axes = plt.subplots(num_rows, num_columns, figsize=(10, 6))
    
    # Plot histograms for each variable
    # https://napsterinblue.github.io/notes/python/viz/subplots/
    # https://matplotlib.org/stable/gallery/color/named_colors.html#list-of-named-colors
    # Flatten the axes array
    axes = axes.flatten()           

    # Use enumerate() to get both the index and value of each pair
    for index, (col, ax) in enumerate(zip(variables, axes)):
        ax.hist(df[col], bins=20, color='darkgreen', edgecolor='black')
        ax.set_title(col)
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        
        # Cleanup the remainder unused subplots
        if index + 1 >= num_variables:
            [ax.set_visible(False) for ax in axes.flatten()[index+1:]]
            break
    
    # Adjust layout & set subplot suptitle
    plt.suptitle("\nDistribution of Variables in the Iris Dataset\n")
    plt.tight_layout()

    # III.
    # Specify folder in which PNG should be saved
    folder = 'results'
    file_name = 'IV.histograms.png'
    file_path = os.path.join(os.getcwd(), folder, file_name)

    # Save plot
    fig.savefig(fname=file_path)      

    # IV. 
    # Display message box with "OK" and "Cancel" buttons
    response = messagebox.askokcancel("Generate histograms", "A histogram of each variable will be plotted and saved in the results directory. Please click OK to open the file.")

    # If response is True open the file, otherwise do nothing
    if response:
        fig.show()
        print(f"\tUser opened the plot.")
    else:
        print(f"\tUser closed the pop-up.")
    
    # https://stackoverflow.com/questions/16676101/print-the-approval-sign-check-mark-u2713-in-python
    print("\n\t\u2713 Histogram function successfully finished.")

def generate_histogram_options(df,df_cleaned):
    response = messagebox.askyesno("Generate histogram", "Would you like to generate the histogram without the outliers?")

    if response:
        generate_histogram(df_cleaned)
    else:
        generate_histogram(df)


# _____________________ PAIRPLOT _____________________
def generate_pairplot(df):
    '''
    This function outputs a scatter plot of each pair of variables of the Iris dataset.
    '''
    # I.
    # Plot a pairplot to analyse the interaction between the different variables
    # https://python-charts.com/correlation/pairs-plot-seaborn/
    sns.pairplot(df, hue="species", corner=False, kind="reg", plot_kws={'line_kws':{'color':'black'}})

    # Adjust layout & set subplot suptitle
    plt.suptitle("Attribute Pairs by Species\n", fontsize=14)
    plt.tight_layout()

    # II.
    # Specify folder in which PNG should be saved
    folder = 'results'
    file_name = 'III.pairplot.png'
    file_path = os.path.join(os.getcwd(), folder, file_name)

    # Save plot
    plt.savefig(fname=file_path)      

    # III. 
    # Display message box with "OK" and "Cancel" buttons
    response = messagebox.askokcancel("Generate pair scatter plot", "A scatter plot of each pair of variables will be created and saved in the results directory. Please click OK to open the file.")

    # If response is True open the file, otherwise do nothing
    if response:
        plt.show()
        print(f"\tUser opened the plot.")
    else:
        print(f"\tUser closed the pop-up.")

def generate_pairplot_options(df,df_cleaned):
    response = messagebox.askyesno("Generate pair plot", "Would you like to generate the histogram without the outliers?")

    if response:
        generate_pairplot(df_cleaned)
    else:
        generate_pairplot(df)

