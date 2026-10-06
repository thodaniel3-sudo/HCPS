"""
HCPS Advanced GUI Extension
"""

import tkinter as tk



def create_dashboard():


    window = tk.Tk()


    window.title(
        "HCPS Engineering Dashboard"
    )


    window.geometry(
        "900x600"
    )


    title = tk.Label(

        window,

        text=
        "Hybrid Composite Prediction System",

        font=("Arial",20,"bold")

    )


    title.pack(
        pady=20
    )



    window.mainloop()
