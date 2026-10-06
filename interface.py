"""
===========================================================
interface.py

Hybrid Composite Prediction System (HCPS)

This module contains all the graphical interface functions
used throughout the software.

Author: Daniel Thomas
===========================================================
"""

import tkinter as tk
from tkinter import messagebox


# ---------------------------------------------------------
# Create Main Window
# ---------------------------------------------------------

def create_window():

    root = tk.Tk()

    root.title("Hybrid Composite System (HCPS)")
    root.geometry("1100x700")
    root.configure(bg="#EAF2F8")

    return root


# ---------------------------------------------------------
# Create Title
# ---------------------------------------------------------

def create_title(root):

    title = tk.Label(
        root,
        text="HYBRID COMPOSITE SYSTEM",
        font=("Arial",22,"bold"),
        fg="navy",
        bg="#EAF2F8"
    )

    title.pack(pady=10)

    subtitle = tk.Label(
        root,
        text="Development of an Eco-friendly Epoxy composite Reinforced with Bio-waste for Automotive Application",
        font=("Arial",12),
        bg="#EAF2F8"
    )

    subtitle.pack()

    author = tk.Label(
    root,
    text="By Daniel Thomas",
    font=("Arial", 11, "italic"),
    fg="gray",
    bg="#EAF2F8"
)

    author.pack(pady=3)
# ---------------------------------------------------------
# Create Input Frame
# ---------------------------------------------------------

def create_input_frame(root):

    frame = tk.LabelFrame(
        root,
        text="Material Properties",
        padx=20,
        pady=20,
        font=("Arial",12,"bold")
    )

    frame.pack(
        padx=20,
        pady=20,
        fill="both"
    )

    return frame


# ---------------------------------------------------------
# Create Labels and Entry Boxes
# ---------------------------------------------------------

def create_entries(frame):

    labels = [

        "Epoxy Density (g/cm³)",
        "Cow Horn Density (g/cm³)",
        "Cotton Density (g/cm³)",
        "Limestone Density (g/cm³)",

        "Epoxy (%)",
        "Cow Horn (%)",
        "Cotton (%)",
        "Limestone (%)",

      
    ]

    entries = []

    for i, text in enumerate(labels):

        label = tk.Label(
            frame,
            text=text,
            font=("Arial",11)
        )

        label.grid(
            row=i,
            column=0,
            sticky="w",
            pady=8
        )

        entry = tk.Entry(
            frame,
            width=25
        )

        entry.grid(
            row=i,
            column=1,
            padx=15
        )

        entries.append(entry)

    return entries


# ---------------------------------------------------------
# Create Buttons
# ---------------------------------------------------------

def create_buttons(
    root,
    calculate,
    predict,
    compare,
    graph,
    report,
    reset,
    ai_status
):

    button_frame = tk.Frame(
        root,
        bg="#C5E2F9"
    )

    button_frame.pack(pady=20)

    buttons = [

    ("Calculate", calculate),

    ("Predict", predict),

    ("Compare", compare),

    ("Plot Graph", graph),

    ("Export Report", report),

    ("AI Status", ai_status),

    ("Reset", reset)

]

    for text, command in buttons:

        button = tk.Button(

            button_frame,

            text=text,

            width=15,

            height=2,

            font=("Arial",10,"bold"),

            bg="#1491E3",

            fg="white",

            command=command

        )

        button.pack(
            side="left",
            padx=8
        )


# ---------------------------------------------------------
# Show Results
# ---------------------------------------------------------

def show_results(title, message):

    messagebox.showinfo(
        title,
        message
    )


# ---------------------------------------------------------
# Show Error
# ---------------------------------------------------------

def show_error(message):

    messagebox.showerror(
        "Error",
        message
    )


# ---------------------------------------------------------
# Ask Question
# ---------------------------------------------------------

def ask_question(message):

    return messagebox.askyesno(
        "Confirmation",
        message
    )


# ---------------------------------------------------------
# Status Bar
# ---------------------------------------------------------

def create_status_bar(root):

    status = tk.Label(

        root,

        text="Status : Ready",

        anchor="w",

        bg="lightgray"

    )

    status.pack(

        side="bottom",

        fill="x"

    )

    return status


# ---------------------------------------------------------
# Update Status
# ---------------------------------------------------------

def update_status(status, message):

    status.config(
        text=message
    )
def clear_entries(entries):
    """
    Clears all input boxes.
    """

    for entry in entries:
        entry.delete(0, tk.END)

# ---------------------------------------------------------
# End of File
# ---------------------------------------------------------