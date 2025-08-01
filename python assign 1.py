from tkinter import *
from time import strftime

# Create the main window
root = Tk()
root.title("Digital Clock")
root.geometry("350x100")
root.resizable(False, False)
root.configure(bg="black")

# Function to update time
def time():
    string = strftime('%H:%M:%S %p')  # 12-hour format with AM/PM
    label.config(text=string)
    label.after(1000, time)  # Update every 1000 milliseconds (1 second)

# Label configuration
label = Label(root, font=('Arial', 40, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center')

# Start the clock
time()

# Run the GUI
root.mainloop()