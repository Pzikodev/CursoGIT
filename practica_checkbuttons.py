from tkinter import *

root=Tk()

root.title("Ejemplo Checkbuttons")

Checkbutton(root, text="Playa").pack()
Checkbutton(root, text="Montaña").pack()
Checkbutton(root, text="Turismo rural").pack()

root.mainloop()