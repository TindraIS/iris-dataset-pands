import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

def option1():
    messagebox.showinfo("Option 1", "You clicked Option 1")

def option2():
    messagebox.showinfo("Option 2", "You clicked Option 2")

def option3():
    messagebox.showinfo("Option 3", "You clicked Option 3")

# Create the main window
root = tk.Tk()
root.title("Programming & Scripting || Iris Dataset Analysis")

# Load image
image = tk.PhotoImage(file="C:/Users/ifs/OneDrive/Documents/ATU/Programming & Scripting/pands-project/images/menu_background2.png")
image = image.subsample(2, 2)  # Resize by a factor of 2 in both dimensions

# Create a label to display the image
image_label = tk.Label(root, image=image)
image_label.place(x=0, y=0, relwidth=1, relheight=1)  # Fill the entire window with the image

# Create Font object
# https://pythonexamples.org/python-tkinter-button-change-font/
# https://www.geeksforgeeks.org/tkinter-fonts/
font_buttons = font.Font(family='Agency FB', size=10, weight="bold")
font_label_heading = font.Font(family='Agency FB', size=26, weight="bold")
font_label_text = font.Font(family='Agency FB', size=12)

# Create labels for text
label1 = tk.Label(root, fg="gray9", bg="white", text="Hello Irina,", font=font_label_heading)
label1.place(relx=0.60, rely=0.3, anchor="sw")
label2 = tk.Label(root, fg="gray9", bg="white", text="\nWelcome to the Iris dataset analysis program.\nPlease select one of the options below:        .", font=font_label_text)
label2.place(relx=0.60, rely=0.4, anchor="sw", )

# Create buttons
# Colours: https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
button1 = tk.Button(root, text=".get descriptive summary", command=option1, bg="white", fg="gray9")
button1.place(relx=0.65, rely=0.5, anchor="center")  # Place button relative to the center of the window
button1['font'] = font_buttons

button2 = tk.Button(root, text=".generate histogram", command=option2, bg="white", fg="gray9")
button2.place(relx=0.64, rely=0.6, anchor="center")  # Place button relative to the center of the window
button2['font'] = font_buttons

button3 = tk.Button(root, text=".generate pair scatter plot", command=option3, bg="white", fg="gray9")
button3.place(relx=0.65, rely=0.7, anchor="center")  # Place button relative to the center of the window
button3['font'] = font_buttons

# Maximize the window
root.state('zoomed')

# Run the main event loop
root.mainloop()