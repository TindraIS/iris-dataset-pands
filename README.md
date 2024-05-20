<picture align="center">
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/TindraIS/pands-project/main/images/dark_header.png">
  <img alt="Light header" src="https://raw.githubusercontent.com/TindraIS/pands-project/main/images/light_header.png">
</picture>

This repository was created in the context of the __Programming &amp; Scripting module__ @ ATU, and contains a program named _Petalist_ which performs an analysis of the Iris flower dataset. [^1] [^2] [^3]

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
│   └── III.pairplot_cleaned.png     # Output of tools.generate_pairplot(df) & assigment mandatory task
│   └── III.pairplot_original.png    # Output of tools.generate_pairplot(df) & assigment mandatory task
│   └── IV.histograms_cleaned.png    # Output of tools.generate_histogram(df) & assigment mandatory task
│   └── IV.histograms_original.png   # Output of tools.generate_histogram(df) & assigment mandatory task
│   └── V.PCA_cleaned.png            # Output of tools.perform_PCA(df)
│   └── V.PCA_original.png           # Output of tools.perform_PCA(df)
├── analysis.py                      # Program entry point
├── error.log                        # File capturing info on errors that occur in analysis.py
├── menu.py                          # Module containing the function that computes the GUI with tkinter when analysis.py is run
├── tools.py                         # Module containing functions that perform the core tasks on the menu.py
├── helpers.py                       # Module containing helper functions pertaining to saving and creating files
├── .gitignore                       # File specifying all the untracked files that Git should ignore
└── README.md                        # This file with the project description
```

## Description

  ### Overview

When running `analysis.py`, _the program entry point_, the `menu.py` module is triggered and a [graphic user interface (GUI)](https://raw.githubusercontent.com/TindraIS/pands-project/main/images/menu_screenshot.png) is computed with the tkinter library, displaying five clickable analysis options. When one of the options is selected, the corresponding function is called back in `tools.py` and the output is saved in the /results directory.

- __Get a descriptive summary__
  
  It triggers the `descriptive_summary()` in `tools.py` and creates a descriptive statistic summary of the variables in the Iris dataset.
  
  <details>
  <summary>The below resources were used to solve the task:</summary>
  
  - https://realpython.com/pandas-groupby/
  - https://realpython.com/python-for-loop/
  - https://www.geeksforgeeks.org/how-to-iterate-over-dataframe-groups-in-python-pandas/ 
  - https://docs.python.org/3/library/functions.html#open
  - https://stackoverflow.com/questions/72626730/python-launch-text-file-in-users-default-text-editor
  - https://docs.python.org/3/library/os.path.html
  - https://stackoverflow.com/questions/72626730/python-launch-text-file-in-users-default-text-editor
  - https://docs.python.org/3/library/tkinter.messagebox.html
  - https://stackoverflow.com/questions/70356069/defining-and-using-a-dictionary-of-colours-in-a-plot
  
  </details>

- __Identify and handling outliers__
  
  - __Get an outlier summary by species__
    
    It computes a summary of outliers present in the Iris dataset by species, using the Inter Quartile Range (IQR) approach to determine if an entry is an outlier using the below formulas: [^4] [^5]
    <div align="center">

    ![Lower Bound](https://latex.codecogs.com/svg.image?{\color{Golden}\text{Lower&space;Bound}=Q_1-1.5\times\text{IQR}})
    
    ![Upper Bound](https://latex.codecogs.com/svg.image?{\color{Golden}\text{Upper&space;Bound}=Q_3&plus;1.5\times\text{IQR}})
    </div>
    
    <details>
    <summary>The below resources were used to solve the task:</summary>
    
    - https://www.geeksforgeeks.org/detect-and-remove-the-outliers-using-python/
    - https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/box-whisker-plots/a/identifying-outliers-iqr-rule
    - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html
    - https://numpy.org/doc/stable/reference/generated/numpy.where.html
    - https://realpython.com/python-zip-function/
    - https://docs.python.org/3/library/functions.html#open
    - https://stackoverflow.com/questions/72626730/python-launch-text-file-in-users-default-text-editor
    - https://docs.python.org/3/library/os.path.html
    - https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/tkMessageBox.html
    
    </details>
    
  - __Remove outliers from the dataset__
  
    Using the same IQR logic, this option removes the outliers present in the Iris dataset for each of the species.
    
    <details>
    <summary>The below resources were used to solve the task:</summary>
    
    - https://www.geeksforgeeks.org/python-extracting-rows-using-pandas-iloc/
    - https://www.geeksforgeeks.org/append-extend-python/
    - https://stackoverflow.com/questions/16676101/print-the-approval-sign-check-mark-u2713-in-python
    
    </details>
    
- __Generate pair scatter plots__
  
  It outputs a scatter plot of each pair of variables of the Iris dataset, prompting the user to choose to compute the plot with or without outliers.
  
  <details>
  <summary>The below resources were used to solve the task:</summary>
  
  - https://python-charts.com/correlation/pairs-plot-seaborn/
  
  </details>
  
- __Generate histograms__
  
  It saves a histogram subplot of each variable in the Iris flower dataset as a PNG file.
  
  <details>
  <summary>The below resources were used to solve the task:</summary>
  
  - https://matplotlib.org/stable/gallery/color/named_colors.html#list-of-named-colors
  - https://stackoverflow.com/questions/70356069/defining-and-using-a-dictionary-of-colours-in-a-plot
  - https://napsterinblue.github.io/notes/python/viz/subplots/
  - https://stackoverflow.com/questions/16676101/print-the-approval-sign-check-mark-u2713-in-python
  
  </details>
  
- __Compute PCA__
  
  It computes a PCA and reduces the 4-dimensional Iris dataset to 2 dimensions/features, outputing a scatter plot of the principal components making it easier to understand how are species distributed.
  
  <details>
  <summary>The below resources were used to solve the task:</summary>
  
  - https://www.turing.com/kb/guide-to-principal-component-analysis
  - https://towardsdatascience.com/a-step-by-step-introduction-to-pca-c0d78e26a0dd
  - https://builtin.com/machine-learning/pca-in-python
  - https://saturncloud.io/blog/what-is-sklearn-pca-explained-variance-and-explained-variance-ratio-difference
  - https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
  - https://docs.python.org/3/library/os.path.html
  - https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/tkMessageBox.html
  
  </details>



  ### Data Source

The Iris flower dataset was created by the British statistician and biologist Ronald Fisher in his 1936 paper _The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis_. It consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor), including measurements in centimeters for the length and the width of the sepals and petals. 

  ### Program Inspiration

I wanted to create a user-centric program that presents several analysis options, ensuring a scripting oriented-project opposed to what I had done for the other module, which was done on a Jupyter Notebook. Initially, I considered using `argparse` for all the options, but after further research, I found an [article](https://www.geeksforgeeks.org/popup-menu-in-tkinter/) about creating pop-up menus with the tkinter library. Happy with the challenge, I read the documentation and began building on top of it.

In terms of the concepts used, I incorporated what was shown in the lectures as well as some functions and modules from the weekly tasks: command-line arguments, creating text files, saving files, reading CSVs, try-except blocks, if statements, for loops, etc. 

After adding the outliers function, I needed a way to ask the user if the analysis should be done with or without the outliers. It wouldn't make much sense to keep it if the plots didn't use the cleaned DataFrame as the data source. As a result, I added the function options and amended the opening_menu() parameters.

Had I more time and fewer kids (_just kidding_), I would have created more analysis options, such as correlation analysis or linear regression.

  ### Commentary & References

The step-by-step logic and references have been added at the beginning of the functions instead of inline to make the code easier to read and work with. No insights regarding the interpretation of data gathered have been produced, but rather we kept true to the assingment brief of explaining how Python can be used in data analysis as well as its outputs.





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
    - Scikit-learn
* Any IDE of personal choice to run the notebook in a local environment. The author used Visual Studio Code in the development. 


## Get Help

For any issues with the code, please refer to GitHub's Issues section and create a new ticket.


## Author
Irina S.


[^1]: [Iris flower dataset Wikipedia page](https://en.wikipedia.org/wiki/Iris_flower_data_set)
[^2]: [README header inspired by Pandas GitHub Repository](https://github.com/pandas-dev/pandas)
[^3]: [The Hitchhiker’s Guide to Python - Structure of the repository](https://docs.python-guide.org/writing/structure/#structure-of-the-repository)
[^4]: [Codecogs Latex Equation Editor ](https://latex.codecogs.com/eqneditor/editor.php)
[^5]: [StackOverflow: How to render LaTeX in README.md on GitHub](https://stackoverflow.com/questions/35498525/latex-rendering-in-readme-md-on-github)
