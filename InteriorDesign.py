from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=YES)

        # Load the image
        self.image = Image.open('images/InteriorDesign.png')
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
intdesg_page= Tk()
app = App(intdesg_page)
intdesg_page.geometry('1366x768')
# heading


lbl=Label(intdesg_page, text="Interior Design", fg='red', font=("Helvetica", 30))
lbl.place(x=30, y=20)

#label redesign
lbl1=Label(intdesg_page, text='Select options to be interiorize', font=("Helvetica", 26))
lbl1.place(x=840, y=290)

#combobox
combo = ttk.Combobox()
combo = ttk.Combobox(state="readonly", values=["Hall", "Kitchen", "Bedroom", "Bathroom", "Floor", "Cieling", "Balcony"], font=("Helvetica", 19))
combo.place(x=890, y=362)



#label dimensions
lbl1=Label(intdesg_page, text='Dimensions  ', font=("Helvetica", 26))
lbl1.place(x=850, y=420)


txtfld=Entry(intdesg_page, text=" 1st txt  ", bd=5, font=("Helvetica", 28))
txtfld.place(x=950, y=490, height = 40, width= 99)
#2nd txtfld
txtfld2=Entry(intdesg_page, text="2nd txt ", bd=5, font=("Helvetica", 28))
txtfld2.place(x=1090, y=490, height = 40, width= 99)

#creating button
btn = Button(intdesg_page, text = "Confirm", font=("Helvetica", 30))
btn.place(x=980, y=600)






intdesg_page.mainloop()
