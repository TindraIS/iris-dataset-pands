    # Create the list of options 
    options_list = ["hist", "pair plot", "Option 3", "Option 4"] 
    
    # Variable to keep track of the option selected in OptionMenu & set the default value of the variable
    value_inside = tk.StringVar(root).set(" .generate a test         ") 
    
    # Create the optionmenu widget and passing the options_list and value_inside to it 
    # https://www.geeksforgeeks.org/how-to-change-background-color-of-tkinter-optionmenu-widget/
    button5 = tk.OptionMenu(root, value_inside, *options_list) 
    button5['font'] = font_buttons

    # Se the background color of Options Menu & displayed options
    button5.config(bg="LightSteelBlue4", fg="white", height=1, width=20, anchor="w", justify="left")
    button5["menu"].config(bg="LightSteelBlue3")

    # Create a dictionary mapping options to their respective functions
    option_functions = {
    "hist": generate_histogram,
    "pair plot": generate_pairplot
    }

    # Configure the OptionMenu to call the appropriate function when an option is selected
    for option in options_list:
        button5["menu"].entryconfig(option, command=lambda opt=option: option_functions[opt]())

    button5.place(relx=0.60, rely=0.7, anchor="center")  # Place button relative to the center of the window


