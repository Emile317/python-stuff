import pyperclip
import tkinter as tk
from tkinter import ttk

code_input = pyperclip.paste()

def main():
    replaced_code = code_input.replace(replace.get(), replaced.get())
    pyperclip.copy(replaced_code)
    complete_label = ttk.Label(mainframe, text="Your code was replaced and has been copied to your clipboard! Click below to quit.")
    complete_label.grid(column=0, row=4)
    def quit_program():
        quit()
    quit_button = ttk.Button(mainframe, text="Quit", command=quit_program)
    quit_button.grid(column=0, row=5)

root = tk.Tk()
root.title("Code Replacer")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

input_label = ttk.Label(mainframe, text="""Your input (pasted from clipboard):
{}""".format(code_input))
input_label.grid(column=0, row=0, sticky=(tk.W))

replace_label = ttk.Label(mainframe, text="Type what you want to replace:")
replace_label.grid(column=0, row=1, sticky=(tk.W))

replace_value = tk.StringVar()
replace = ttk.Entry(mainframe, textvariable=replace_value)
replace.grid(column=1, row=1, sticky=(tk.W))

replaced_label = ttk.Label(mainframe, text="Type what you want to replace it with:")
replaced_label.grid(column=0, row=2, sticky=(tk.W))

replaced_value = tk.StringVar()
replaced = ttk.Entry(mainframe, textvariable=replaced_value)
replaced.grid(column=1, row=2, sticky=(tk.W))

button = tk.Button(mainframe, text="replace text", command=main)
button.grid(column=0, row=3, sticky='w')

root.mainloop()