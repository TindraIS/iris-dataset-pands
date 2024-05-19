<picture align="center">
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/TindraIS/pands-project/main/images/dark_header.png">
  <img alt="Light header" src="https://raw.githubusercontent.com/TindraIS/pands-project/main/images/light_header.png">
</picture>


## Description

This repository was created in the context of the __Programming &amp; Scripting module__ @ ATU, and contains a program named _Petalist_ which performs an analysis of the Iris flower dataset. [^1] [^2] [^3]

When running `analysis.py`, __the program entry point__, the `menu.py` module is triggered and a [graphic user interface (GUI)](https://raw.githubusercontent.com/TindraIS/pands-project/main/images/menu_screenshot.png) is computed with the tkinter library, displaying four clickable analysis options:
- Get a descriptive summary
- Identify and handling outliers
    - Get an outlier summary by species
    - Remove outliers from the dataset
- Generate pair scatter plots
- Generate histograms

When one of the options is selected, the corresponding function is called back in `tools.py` and the output is saved in the /results directory.

### Data Source

The Iris flower dataset was created by the British statistician and biologist Ronald Fisher in his 1936 paper _The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis_. It consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor), including measurements in centimeters for the length and the width of the sepals and petals. 

### Program Inspiration

I wanted to create a user-centric program that presents several analysis options, ensuring a scripting oriented-project opposed to what I had done for the other module, which was done on a Jupyter Notebook. Initially, I considered using `argparse` for all the options, but after further research, I found an [article](https://www.geeksforgeeks.org/popup-menu-in-tkinter/) about creating pop-up menus with the tkinter library. Happy with the challenge, I read the documentation and began building on top of it.

In terms of the concepts used, I incorporated what was shown in the lectures as well as some functions and modules from the weekly tasks: command-line arguments, creating text files, saving files, reading CSVs, try-except blocks, if statements, for loops, etc. 

After adding the outliers function, I needed a way to ask the user if the analysis should be done with or without the outliers. It wouldn't make much sense to keep it if the plots didn't use the cleaned DataFrame as the data source. As a result, I added the function options and amended the opening_menu() parameters.


Had I more time and fewer kids (_just kidding_), I would have created more analysis options, such as correlation analysis or linear regression.

### Comments

The step-by-step logic and references have been added at the beginning of the functions instead of inline to make the code easier to read and work with. No insights regarding the interpretation of data gathered have been produced, but rather we kept true to the assingment brief of explaining how Python can be used in data analysis as well as its outputs.

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
│   └── III.pairplot.png             # Output of tools.generate_pairplot(df) & assigment mandatory task
│   └── IV.histograms.png            # Output of tools.generate_histogram(df) & assigment mandatory task
├── analysis.py                      # Program entry point
├── error.log                        # File capturing info on errors that occur in analysis.py
├── menu.py                          # Module containing the function that computes the GUI with tkinter when analysis.py is run
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
    - OS
    - Logging
    - Argparse
* Any IDE of personal choice to run the notebook in a local environment. The author used Visual Studio Code in the development. 

## Get Help

For any issues with the code, please refer to GitHub's Issues section and create a new ticket.

## Author
Irina S.


[^1]: [Iris flower dataset Wikipedia page](https://en.wikipedia.org/wiki/Iris_flower_data_set)
[^2]: [README header inspired by Pandas GitHub Repository](https://github.com/pandas-dev/pandas)
[^3]: [The Hitchhiker’s Guide to Python - Structure of the repository](https://docs.python-guide.org/writing/structure/#structure-of-the-repository)