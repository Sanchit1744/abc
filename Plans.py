from tkinter import *
from PIL import Image, ImageTk

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=YES)

        # Load the image
        self.image = Image.open('images/Plans.png')
        self.photo = ImageTk.PhotoImage(self.image)

        # Create the background label and pack it
        self.background_label = Label(self, image=self.photo)
        self.background_label.pack(fill=BOTH, expand=YES)

        # Allow the user to fit the image to the plans_page size
        self.bind("<Configure>", self.resize)

    def resize(self, event):
        # Resize the image
        self.image = self.image.resize((event.width, event.height))
        self.photo = ImageTk.PhotoImage(self.image)
        self.background_label.config(image=self.photo)

# Create the Tkinter plans_page and run the application
plans_page = Tk()
app = App(plans_page)
plans_page.geometry('1366x768')
# heading

# functions

# main code - e.g. buttons, etc
btn= Button(plans_page, text='Plan A', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1', activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1)
btn.place(x=100, y=180)
btn= Button(plans_page, text='Plan B', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1', activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1)
btn.place(x=100, y=290)
btn= Button(plans_page, text='Plan C', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1', activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1)
btn.place(x=100, y=400)
btn= Button(plans_page, text='Plan D', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1', activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1)
btn.place(x=100, y=510)
btn= Button(plans_page, text='Plan E', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1', activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1)
btn.place(x=100, y=620)






plans_page.mainloop()
