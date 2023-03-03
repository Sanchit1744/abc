from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk


class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=YES)

        # Load the image
        self.image = Image.open('images/Construct.png')
        self.photo = ImageTk.PhotoImage(self.image)

        # Create the background label and pack it
        self.background_label = Label(self, image=self.photo)
        self.background_label.pack(fill=BOTH, expand=YES)

        # Allow the user to fit the image to the  size
        self.bind("<Configure>", self.resize)

    def resize(self, event):
        # Resize the image
        self.image = self.image.resize((event.width, event.height))
        self.photo = ImageTk.PhotoImage(self.image)
        self.background_label.config(image=self.photo)

# Create the Tkinter  and run the application
construct_page = Tk()
construct_page.geometry('1366x768')
# heading
def nextPagetoMaterials():
    construct_page.destroy()
    import Materials
# functions
def GoToPage():
    l1 = (combo2.get())
    if l1 == 2:
        construct_page.destroy()
        import Plans


lbl=Label(construct_page, text="Construct A House", fg='red', font=("Helvetica", 30))
lbl.place(x=20, y=10)

#label area availability
lbl1=Label(construct_page, text='Area Availability', font=("Helvetica", 26))
lbl1.place(x=90, y=200)
#text field of area availability
txtfld=Entry(construct_page, text="  1 ", bd=5, font=("Helvetica", 28))
txtfld.place(x=400, y=200, height = 50, width= 300)

#label Budget
lbl1=Label(construct_page, text='Budget', font=("Helvetica", 26))
lbl1.place(x=90, y=300)
#text field of budget
txtfld=Entry(construct_page, text=" 2  ", bd=5, font=("Helvetica", 28))
txtfld.place(x=400, y=300, height = 50, width= 300)

#label floor
lbl1=Label(construct_page, text='House Space', font=("Helvetica", 26))
lbl1.place(x=90, y=100)
#text field of floor
combo2 = ttk.Combobox()
combo2 = ttk.Combobox(state="readonly", values=["1RK", "1BHK", "2", "3BHK"], font=("Helvetica", 19))
combo2.place(x=400, y=100)


#label house space
lbl1=Label(construct_page, text='Floors', font=("Helvetica", 26))
lbl1.place(x=90, y=400)
#text field of floor
comboa = ttk.Combobox(state="readonly", values=["1", "2", "3", "4"], font=("Helvetica", 19))
comboa.place(x=400, y=400)


#creating button
btn= Button(construct_page, text='Confirm', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1', activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command=GoToPage)
btn.place(x=290, y=500)

btn= Button(construct_page, text='Materials', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1', activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command=nextPagetoMaterials)
btn.place(x=1000, y=100)


construct_page.mainloop()
