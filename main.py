import platform
import time
from tkinter import Tk, Button, Label

# Autodetect the operating system
if platform.system() == "Windows":
    import win32api
elif platform.system() == "Linux":
    import Xlib.display

# Autoclicker function
def autoclick():
    # Get the current mouse position
    if platform.system() == "Windows":
        x, y = win32api.GetCursorPos()
    elif platform.system() == "Linux":
        display = Xlib.display.Display()
        root = display.screen().root
        root.query_pointer()._data

    # Perform the click
    if platform.system() == "Windows":
        win32api.mouse_event(win32api.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32api.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    elif platform.system() == "Linux":
        display = Xlib.display.Display()
        root = display.screen().root
        root.warp_pointer(x, y)
        display.sync()
        display.allow_events(Xlib.X.AsyncPointer, Xlib.X.CurrentTime)
        time.sleep(0.1)
        display.flush()

# Create the Tkinter window
window = Tk()
window.title("Autoclicker")

# Create the autoclick button
autoclick_button = Button(window, text="Autoclick", command=autoclick)
autoclick_button.pack()

# Create a label for instructions
instructions_label = Label(window, text="Press the 'Autoclick' button to start autoclicking.")
instructions_label.pack()

# Start the Tkinter event loop
window.mainloop()
