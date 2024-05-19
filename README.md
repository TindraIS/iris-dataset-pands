<picture align="center">
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/TindraIS/pands-project/main/images/dark_header.png">
  <img alt="Light header" src="https://raw.githubusercontent.com/TindraIS/pands-project/main/images/light_header.png">
</picture>


## Description
This repository was created in the context of the Programming &amp; Scripting module @ ATU, and contains a program named Petalist which performs an analysis of the Iris flower dataset.[^1] [^2]

## Contents

```
pands-project/
├── images/
│   ├── dark_header.png              # README header displayed whenever GitHub's theme is dark
│   ├── dark_header.png              # README header displayed whenever GitHub's theme is light
│   └── menu_background.png          # Background image displayed in tkinter GUI
├── results/
│   ├── I.variables_summary.txt      # Output of tools.descriptive_summary(df)
│   ├── II.dataframe_cleaned.csv     # Output of tools.outliers_cleanup(df)
│   └── II.outliers_summary.txt      # Output of tools.outliers_summary(df)
│   └── III.pairplot.png             # Output of tools.generate_pairplot(df)
│   └── IV.histograms.png            # Output of tools.generate_histogram(df)
├── analysis.py                      # Program entry point
├── error.log                        # File capturing info on errors that occur in analysis.py
├── menu.py                          # Module containing the function that computes the GUI with tkinter
├── tools.py                         # Module containing functions that perform the core tasks on the menu.py
├── .gitignore                       # File specifying all the untracked files that Git should ignore
└── README.md                        # This file
```

## Getting Started

### Dependencies
* Python 3.11.7 kernel
* Python Modules
    - Pandas
    - Matplotlib
    - Seaborn
    - NumPy
    - Tkinter
* Any IDE of personal choice to run the notebook in a local environment. The author used Visual Studio Code in the development. 

## Get Help

For any issues with the code, please refer to GitHub's Issues section and create a new ticket.

## Author
Irina S.


[^1]: [Iris flower dataset Wikipedia page](https://en.wikipedia.org/wiki/Iris_flower_data_set)
[^2]: [README header inspired by Pandas GitHub Repository](https://github.com/pandas-dev/pandas)