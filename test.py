import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
import argparse
import seaborn as sns
import pandas as pd
from skimpy import skim


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



# Initialise an empty string to store the summary
summary = ''

# Add overall summary, data types summary & summary header for each species
summary += f"(1) Overall Descriptive Statistics:\n{df.describe(include='all').to_string()}\n\n"
summary += f"(2) Data Types Summary:\n{df.dtypes.to_string()}\n\n"
summary += f"(3) Summary for Each Species:\n\n"

# Group the DataFrame by species & initialise counter for the below for loop
df_species = df.groupby('species')
counter = 0

# Iterate over each species and generate summary statistics
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