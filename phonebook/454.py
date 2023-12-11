from tkinter import *
from tkhtmlview import *
 
# Create Object
root = Tk()
 
# Set Geometry
root.geometry("400x400")
root.config(bg="Blue")
 
# Add label
my_label = HTMLLabel(root, html="""
        <fieldset>
        <legend border=5 style="border-color:black;">HTMLcode</legend>
        <h1>GEEKSFORGEEKS</h1>
        <h2>GEEKSFORGEEKS</h2>
        <h3>GEEKSFORGEEKS</h3>
        <h4>GEEKSFORGEEKS</h4>
        <h5>GEEKSFORGEEKS</h5>
        <h6>GEEKSFORGEEKS</h6>
        </fieldset>
    """)

# Adjust label
my_label.pack(pady=20, padx=20)

 
# Execute Tkinter
root.mainloop()
