from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=YES)

        # Load the image
        self.image = Image.open('images/Interior.jpg')
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
material_page= Tk()
app = App(material_page)
material_page.geometry('1366x768')
# heading

#label to be construced
lbl1=Label(material_page, text="Floors to be constructed", fg='red', font=("Helvetica", 26))
lbl1.place(x=30, y=70)
#combobox
comboa = ttk.Combobox(state="readonly", values=["1", "2", "3", "4"], font=("Helvetica", 19))
comboa.place(x=490, y=70)



#label house space
lbl3=Label(material_page, text="House Space", fg='red', font=("Helvetica", 26))
lbl3.place(x=30, y=130)
#combobox
combo2 = ttk.Combobox()
combo2 = ttk.Combobox(state="readonly", values=["1RK", "1BHK", "2BHK", "3BHK"], font=("Helvetica", 19))
combo2.place(x=490, y=130)
#1a
lbl1a=Label(material_page, text="Concrete", fg='black', font=("Helvetica", 26))
lbl1a.place(x=30, y=210)
txtfld1a=Entry(material_page, text=" Concrete  ", bd=5, font=("Helvetica", 28))
txtfld1a.place(x=250, y=210, height = 40, width= 130)
#1b
lbl1b=Label(material_page, text="Brick", fg='black', font=("Helvetica", 26))
lbl1b.place(x=30, y=290)
txtfld1b=Entry(material_page, text=" Brick ", bd=5, font=("Helvetica", 28))
txtfld1b.place(x=250, y=290, height = 40, width= 130)
#1c
lbl1c=Label(material_page, text="Steel", fg='black', font=("Helvetica", 26))
lbl1c.place(x=30, y=370)
txtfld1c=Entry(material_page, text="Steel  ", bd=5, font=("Helvetica", 28))
txtfld1c.place(x=250, y=370, height = 40, width= 130)
#1d
lbl1d=Label(material_page, text="Glass", fg='black', font=("Helvetica", 26))
lbl1d.place(x=30, y=450)
txtfld1d=Entry(material_page, text="Glass  ", bd=5, font=("Helvetica", 28))
txtfld1d.place(x=250, y=450, height = 40, width= 130)
#2a
lbl2a=Label(material_page, text="Wood", fg='black', font=("Helvetica", 26))
lbl2a.place(x=530, y=210)
txtfld2a=Entry(material_page, text="Wood ", bd=5, font=("Helvetica", 28))
txtfld2a.place(x=750, y=210, height = 40, width= 130)
#2b
lbl2b=Label(material_page, text="Tiles", fg='black', font=("Helvetica", 26))
lbl2b.place(x=530, y=290)
txtfld2b=Entry(material_page, text="Tiles", bd=5, font=("Helvetica", 28))
txtfld2b.place(x=750, y=290, height = 40, width= 130)
#2c
lbl2c=Label(material_page, text="Cement", fg='black', font=("Helvetica", 26))
lbl2c.place(x=530, y=370)
txtfld2c=Entry(material_page, text="Cement", bd=5, font=("Helvetica", 28))
txtfld2c.place(x=750, y=370, height = 40, width= 130)
#2d
lbl2d=Label(material_page, text="Aggregate", fg='black', font=("Helvetica", 26))
lbl2d.place(x=530, y=450)
txtfld2d=Entry(material_page, text="Aggregate", bd=5, font=("Helvetica", 28))
txtfld2d.place(x=750, y=450, height = 40, width= 130)

lbl3a=Label(material_page, text="Cost(rs)", fg='black', font=("Helvetica", 26))
lbl3a.place(x=750, y=560)
txtfld3a=Entry(material_page, text="Cost", bd=5, font=("Helvetica", 28))
txtfld3a.place(x=900, y=560, height = 40, width= 250)

#creating button back
btn1a = Button(material_page, text = "Back", font=("Helvetica", 24))
btn1a.place(x=9, y=3)

#creating button estimate
btn1b= Button(material_page, text='Estimate', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1', activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1)
btn1b.place(x=900, y=110)





material_page.mainloop()





