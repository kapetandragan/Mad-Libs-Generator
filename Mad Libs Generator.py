import tkinter as tk
from tkinter import messagebox

def generate_story():
    noun = noun_entry.get()
    verb = verb_entry.get()
    adjective = adjective_entry.get()
    
    if noun and verb and adjective:
        story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb}.\n"
        messagebox.showinfo("Mad Libs Generator", story)
    else:
        messagebox.showerror("Mad Libs Generator", "Please fill in all the fields!")

# Create the main window
window = tk.Tk()
window.title("Mad Libs Generator")

# Create labels and entry fields for noun, verb, and adjective
noun_label = tk.Label(window, text="Noun:")
noun_label.pack()
noun_entry = tk.Entry(window)
noun_entry.pack()

verb_label = tk.Label(window, text="Verb:")
verb_label.pack()
verb_entry = tk.Entry(window)
verb_entry.pack()

adjective_label = tk.Label(window, text="Adjective:")
adjective_label.pack()
adjective_entry = tk.Entry(window)
adjective_entry.pack()

# Create a button to generate the story
generate_button = tk.Button(window, text="Generate Story", command=generate_story)
generate_button.pack()

# Run the main event loop
window.mainloop()