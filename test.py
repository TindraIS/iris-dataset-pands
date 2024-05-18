    # Create the list of options 
    options_list = ["Option 1", "Option 2", "Option 3", "Option 4"] 
    
    # Variable to keep track of the option selected in OptionMenu 
    value_inside = tk.StringVar(root) 
    
    # Set the default value of the variable 
    value_inside.set(" .generate a test         ") 
    
    # Create the optionmenu widget and passing the options_list and value_inside to it 
    # https://www.geeksforgeeks.org/how-to-change-background-color-of-tkinter-optionmenu-widget/
    button4 = tk.OptionMenu(root, value_inside, *options_list) 
    button4.place(relx=0.60, rely=0.7, anchor="center")  # Place button relative to the center of the window
    button4['font'] = font_buttons
    # Se the background color of Options Menu to green
    button4.config(bg="LightSteelBlue4", fg="white", height=1, width=20, anchor="w", justify="left")
    
    # Set the background color of Displayed Options to Red
    button4["menu"].config(bg="LightSteelBlue3")

    button4 = tk.OptionMenu(root, value_inside, *options_list, command=select_option_function)) 

def select_option_function(event):
    option = var.get()