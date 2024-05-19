import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
import os
import tools

def opening_menu(username, df, df_cleaned):

    # https://www.geeksforgeeks.org/popup-menu-in-tkinter/
    # https://www.geeksforgeeks.org/tkinter-cheat-sheet/
    # Create the main window
    root = tk.Tk()
    root.title("PETALIST || Iris Dataset Analysis")

    # Load image
    folder = 'images'
    file_name = 'menu_background.png'
    file_path = os.path.join(os.getcwd(), folder, file_name)
    image = tk.PhotoImage(file=file_path)
    image = image.subsample(2, 2)  # Resize by a factor of 2 in both dimensions

    # Create a label to display the image
    image_label = tk.Label(root, image=image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)  # Fill the entire window with the image

    # Create Font object
    # https://pythonexamples.org/python-tkinter-button-change-font/
    # https://www.geeksforgeeks.org/tkinter-fonts/
    font_buttons = font.Font(family='Sitka Small', size=8, weight="bold")
    font_options = font.Font(family='Sitka Small', size=8)
    font_label_heading = font.Font(family='Sitka Small', size=26, weight="bold")
    font_label_text = font.Font(family='Sitka Small', size=10)

    # Create labels for text
    label1 = tk.Label(root, 
                      fg="#5E7F73", bg="white", 
                      text=f"Hello {username},", 
                      font=font_label_heading)
    label1.place(relx=0.50, rely=0.3, anchor="sw")
    label2 = tk.Label(root, 
                      fg="#5E7F73", bg="white", 
                      text="Welcome to Petalist, the Iris dataset analysis \nprogram. Please select one of the options below:", 
                      font=font_label_text, anchor='w')
    label2.place(relx=0.50, rely=0.4, anchor="sw")

    # Define buttons configurations
    button_height = 1
    button_width = 30
    button_anchor = "w"
    button_justify = "left"
    button_bg = "#5E7F73"
    button_fg = "white"
    
    # Create buttons
    # Colours: https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
    # https://stackoverflow.com/questions/70406400/understanding-python-lambda-behavior-with-tkinter-button
    # https://tk-tutorial.readthedocs.io/en/latest/button/button.html
    # https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/button.html

    # Button 1--------------------------------------------------------------------

    button1 = tk.Button(root, 
                        text=" I .get descriptive summary", 
                        command=lambda: tools.descriptive_summary(df),
                        width=button_width, 
                        height=button_height, 
                        anchor=button_anchor, 
                        justify=button_justify, 
                        bg=button_bg, 
                        fg=button_fg)
    button1.place(relx=0.60, rely=0.5, anchor="center")  # Place button relative to the center of the window
    button1['font'] = font_buttons


    # Button 2 --------------------------------------------------------------------

    # Create the list of options & a dictionary mapping options to their respective functions
    options_list = ["Get a summary of outliers", "Remove outliers from the dataset"] 
    option_functions = {
        "Get a summary of outliers": tools.outliers_summary,
        "Remove outliers from the dataset": tools.outliers_cleanup
        }
    
    # Variable to keep track of the option selected in tk.OptionMenu() & set the default value of the variable
    value_inside = tk.StringVar(root,"II .identify & handle outliers") 
    
    # Create the optionmenu widget and passing the options_list and value_inside to it 
    # https://www.geeksforgeeks.org/how-to-change-background-color-of-tkinter-optionmenu-widget/
    button2 = tk.OptionMenu(root, value_inside, *options_list) 
    button2['font'] = font_buttons
    button2.place(relx=0.60, rely=0.6, anchor="center")  # Place button relative to the center of the window

    # Se the background color of Options Menu & displayed options
    button2.config(width=23, 
                   height=button_height, 
                   anchor=button_anchor, 
                   justify=button_justify, 
                   bg=button_bg, 
                   fg=button_fg)
    button2["menu"].config(bg="#7A9F92",fg='white',font=font_options)

    # Configure the OptionMenu to call the appropriate function when an option is selected
    for option in options_list:
        button2["menu"].entryconfig(option, command=lambda opt=option: option_functions[opt](df))

    # Button 3 --------------------------------------------------------------------

    button3 = tk.Button(root, 
                        text="III .generate pair scatter plot", 
                        command=lambda: tools.generate_pairplot_options(df,df_cleaned),
                        width=button_width, 
                        height=button_height, 
                        anchor=button_anchor, 
                        justify=button_justify, 
                        bg=button_bg, 
                        fg=button_fg)
    button3.place(relx=0.60, rely=0.7, anchor="center")  # Place button relative to the center of the window
    button3['font'] = font_buttons

    
    # Button 4 --------------------------------------------------------------------
    
    button4 = tk.Button(root, 
                        text="IV .generate histogram",  
                        command=lambda: tools.generate_histogram_options(df, df_cleaned),
                        width=button_width, 
                        height=button_height, 
                        anchor=button_anchor, 
                        justify=button_justify, 
                        bg=button_bg, 
                        fg=button_fg)
    button4.place(relx=0.60, rely=0.8, anchor="center")  # Place button relative to the center of the window
    button4['font'] = font_buttons

    # Maximize the window
    root.state('zoomed')

    # Run the main event loop
    root.mainloop()