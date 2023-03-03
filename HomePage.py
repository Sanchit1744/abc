from tkinter import *
from PIL import Image, ImageTk

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=YES)

        # Load the image
        self.image = Image.open('images/Home.png')
        self.photo = ImageTk.PhotoImage(self.image)

        # Create the background label and pack it
        self.background_label = Label(self, image=self.photo)
        self.background_label.pack(fill=BOTH, expand=YES)

        # Allow the user to fit the image to the home_page size
        self.bind("<Configure>", self.resize)

    def resize(self, event):
        # Resize the image
        self.image = self.image.resize((event.width, event.height))
        self.photo = ImageTk.PhotoImage(self.image)
        self.background_label.config(image=self.photo)

# Create the Tkinter home_page and run the application
home_page = Tk()
app = App(home_page)
home_page.geometry('1366x768')
# heading

def nextPagetoConstruct():
    home_page.destroy()
    import Construct
# functions

def nextPagetoInterior():
    home_page.destroy()
    import InteriorDesign

# main code - e.g. buttons, etc
btn= Button(home_page, text='Construct Plan', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1', activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command =nextPagetoConstruct)
btn.place(x=955, y=400)

# Button of Interior design
btn= Button(home_page, text='Interior Plan', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1', activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command =nextPagetoInterior )
btn.place(x=955, y=500)

lbl=Label(home_page, text="Home Page", fg='red', font=("Times New Roman", 31))
lbl.place(x=60, y=50)



home_page.mainloop()
