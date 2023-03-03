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

        # Allow the user to fit the image to the intplans_page size
        self.bind("<Configure>", self.resize)

    def resize(self, event):
        # Resize the image
        self.image = self.image.resize((event.width, event.height))
        self.photo = ImageTk.PhotoImage(self.image)
        self.background_label.config(image=self.photo)




intplans_page = Tk()
app = App(intplans_page)
intplans_page.geometry('1366x768')
# heading

# functions

# main code - e.g. buttons, etc
btn=Button(intplans_page, text="Plan A", fg='blue', font=("Helvetica", 26))
btn.place(x=180, y=180)
btn=Button(intplans_page, text="Plan B", fg='blue', font=("Helvetica", 26))
btn.place(x=180, y=280)
btn=Button(intplans_page, text="Plan C", fg='blue', font=("Helvetica", 26))
btn.place(x=180, y=380)
btn=Button(intplans_page, text="Plan D", fg='blue', font=("Helvetica", 26))
btn.place(x=180, y=480)
btn=Button(intplans_page, text="Plan E", fg='blue', font=("Helvetica", 26))
btn.place(x=180, y=580)






intplans_page.mainloop()


# Create the Tkinter intplans_page and run the application

