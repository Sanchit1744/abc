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
window= Tk()
app = App(window)
window.geometry('1366x768')
# heading

#label to be construced
lbl=Label(window, text="Floors to be constructed", fg='red', font=("Helvetica", 26))
lbl.place(x=30, y=70)
#combobox
combo = ttk.Combobox()
combo = ttk.Combobox(state="readonly", values=["1", "2", "3", "4"], font=("Helvetica", 19))
combo.place(x=490, y=70)

def comboFloor():
    catch= combo.current()
    catch2 = combo2.current()
    if catch == '1':
        x=1
    elif catch == '2':
        x=2
    elif catch == '3':
        x=3
    elif catch == '4':
        x=4

    if catch2 == '1RK':
        y = 1
    elif catch2 == '1BHK':
        y = 1.5
    elif catch2 == '2BHK':
        y = 2.5
    elif catch2 == '3BHK':
        y = 3.5
    concrete = x *y *20 +20
    brick = x*y*15   +15
    steel = x*y* 25  +24
    glass = x*y* 5
    wood = x*y* 10
    tiles = x*y* 2.5
    asphalt = x*y* 20  +15
    aggregate = x*y*26  +26



#label house space
lbl=Label(window, text="House Space", fg='red', font=("Helvetica", 26))
lbl.place(x=30, y=130)
#combobox
combo2 = ttk.Combobox()
combo2 = ttk.Combobox(state="readonly", values=["1RK", "1BHK", "2BHK", "3BHK"], font=("Helvetica", 19))
combo2.place(x=490, y=130)





#1a
lbl=Label(window, text="Concrete", fg='black', font=("Helvetica", 26))
lbl.place(x=30, y=210)
txtfld=Entry(window, text=" Concrete  ", bd=5, font=("Helvetica", 28))
txtfld.place(x=250, y=210, height = 40, width= 130)
#1b
lbl=Label(window, text="Brick", fg='black', font=("Helvetica", 26))
lbl.place(x=30, y=290)
txtfld=Entry(window, text=" Brick ", bd=5, font=("Helvetica", 28))
txtfld.place(x=250, y=290, height = 40, width= 130)
#1c
lbl=Label(window, text="Steel", fg='black', font=("Helvetica", 26))
lbl.place(x=30, y=370)
txtfld=Entry(window, text="Steel  ", bd=5, font=("Helvetica", 28))
txtfld.place(x=250, y=370, height = 40, width= 130)
#1d
lbl=Label(window, text="Glass", fg='black', font=("Helvetica", 26))
lbl.place(x=30, y=450)
txtfld=Entry(window, text="Glass  ", bd=5, font=("Helvetica", 28))
txtfld.place(x=250, y=450, height = 40, width= 130)
#2a
lbl=Label(window, text="Wood", fg='black', font=("Helvetica", 26))
lbl.place(x=530, y=210)
txtfld=Entry(window, text="Wood ", bd=5, font=("Helvetica", 28))
txtfld.place(x=750, y=210, height = 40, width= 130)
#2b
lbl=Label(window, text="Tiles", fg='black', font=("Helvetica", 26))
lbl.place(x=530, y=290)
txtfld=Entry(window, text="Tiles", bd=5, font=("Helvetica", 28))
txtfld.place(x=750, y=290, height = 40, width= 130)
#2c
lbl=Label(window, text="Asphalt", fg='black', font=("Helvetica", 26))
lbl.place(x=530, y=370)
txtfld=Entry(window, text="Asphalt", bd=5, font=("Helvetica", 28))
txtfld.place(x=750, y=370, height = 40, width= 130)
#2d
lbl=Label(window, text="Aggregate", fg='black', font=("Helvetica", 26))
lbl.place(x=530, y=450)
txtfld=Entry(window, text="Aggregate", bd=5, font=("Helvetica", 28))
txtfld.place(x=750, y=450, height = 40, width= 130)

lbl=Label(window, text="Cost(rs)", fg='black', font=("Helvetica", 26))
lbl.place(x=750, y=560)
txtfld=Entry(window, text="Cost", bd=5, font=("Helvetica", 28))
txtfld.place(x=900, y=560, height = 40, width= 250)

#creating button back
btn = Button(window, text = "Back", font=("Helvetica", 24))
btn.place(x=9, y=3)

#creating button estimate
btn= Button(window, text='Estimate', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1', activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1)
btn.place(x=900, y=110)























window.mainloop()
