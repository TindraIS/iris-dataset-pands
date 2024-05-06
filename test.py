import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
import argparse
import seaborn as sns
import pandas as pd

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

# Group the DataFrame by species for the below for loop
df_species = df.groupby('species')

# Initialize an empty string to store the summary
summary = ''

# Iterate over each group and generate summary statistics
for species, group_df in df_species:
    summary += f"Summary for  {species} species\n"
    summary += group_df.describe(include='all').to_string() + "\n\n"
 
with open("summary.txt", 'w', encoding='utf-8') as writer:
        writer.write(summary)