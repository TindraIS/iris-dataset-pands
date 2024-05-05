import seaborn as sns
import pandas as pd


def get_dataset():

    # https://github.com/mwaskom/seaborn-data
    datasets_list = sns.get_dataset_names()

    # Access the list returned by Seaborn with datasets names, filtering out the string
    # matching the 'iris' substring and adding it to a new list.
    # Then access the list with the returned name by indexing the result.
    iris_dataset = list(filter(lambda x: "iris" in x, datasets_list))[0]

    # Sanity check: print dataset name
    print(f"Dataset name is: {iris_dataset}")

    # Load the dataset which is a DataFrame object by default, as the Seaborn library is 
    # closely integrated with pandas data structures.
    # https://seaborn.pydata.org/generated/seaborn.load_dataset.html)]
    df = sns.load_dataset(iris_dataset)

    return df


df = get_dataset()

df.info()



This button calls descriptive_summary function in the the command param. 
    button1 = tk.Button(root, text=".get descriptive summary", command=descriptive_summary, bg="white", fg="gray9")

However, only the messagebox shows, the describe does not show in the terminal
def descriptive_summary():
    messagebox.showinfo("Text file with a descriptive summary of each variable", "Please return to the results directory to access the file.")

    df = get_dataset()

    df.describe()