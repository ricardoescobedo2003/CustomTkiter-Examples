from customtkinter import*

app =CTk()
app.geometry("500x500")

label = CTkLabel(master=app, text="Hola desde el test", font=("Arial, 20"))

label.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()