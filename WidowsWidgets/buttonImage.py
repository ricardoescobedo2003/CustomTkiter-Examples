from customtkinter import *
from PIL import Image

app = CTk()
app.resizable(False, False)
app.geometry("500x400")
app.title("Window Test")

#Podemos definir entre light o dark segun el tema
set_appearance_mode("dark")

img = Image.open("examen.png")


btn = CTkButton(master=app, text="Click Me", corner_radius=32, fg_color="#C850C0",
                hover_color="#4158D0", border_color="#FFCC70",
                border_width=2, image=CTkImage())

btn.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()