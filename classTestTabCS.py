import tkinter as tk
from tkinter import ttk

def main():
    app = Application()  # pass root as an argument here
    app.mainloop()  # call mainloop function

#define class before we use it
class Application(tk.Tk): #creates a tkinter instance within the class itself

    #the application IS a tkinter instance
    def __init__(self): #pass root as an argument to call mainloop function outside the class
        super().__init__()  # the same as running root = Tk.tk()
        self.title("Simple App")

        self.columnconfigure(0, weight = 1) #using self instead of root
        self.columnconfigure(1, weight = 3)
        self.rowconfigure(0, weight = 1)

        frame = InputForm(self)
        frame.grid(row=0, column = 0, sticky="nsew", padx=5, pady= 5)

        frame2 = InputForm(self)
        frame2.grid(row=0, column = 1, sticky="nsew", padx=5, pady= 5)

class InputForm(ttk.Frame): #inherit from a frame
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # creating a text entry
        self.entry = tk.Entry(self)
        self.entry.grid(row=0, column=0, sticky="ew")

        self.entry.bind("<Return>", lambda event: self.add_to_list())  # binding something to a specific key press!

        self.entry_btn = tk.Button(self, text="Add",
                                   command=self.add_to_list)  # make sure to pass the function as it is and not to execute it!
        self.entry_btn.grid(row=0, column=1, sticky="e")

        #making a new button to clear all entries in a list
        self.entry_btn2 = tk.Button(self, text="Clear",
                                   command=self.clear_list)  # make sure to pass the function as it is and not to execute it!
        self.entry_btn2.grid(row=0, column=2, sticky="e")

        self.text_list = tk.Listbox(self)
        self.text_list.grid(row=1, column=0, columnspan=3,
                            sticky="news")  # sticky function helps text_list stick to certain sides of the window

    def add_to_list(self, _event = None): #put an underscore in front of event to let it know that "event" is not really used as anything -- only for design. Will NOT affect the code at all
        text = self.entry.get()  # get the text from entry
        if text:  # making sure something was added to textbox
            self.text_list.insert(tk.END, text)  # insert to the end of that widget
            self.entry.delete(0, tk.END)  # erases values automatically without user manually clearing it themselves
            # tk.END just means the end of something -- it's a constant that just makes it easier

    def clear_list(self):
        self.text_list.delete(0, tk.END)

if __name__ == "__main__": #common practice conditional
    main()

