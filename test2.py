from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import tkinter as ttk



def home():

    # Create the Tkinter home_page and run the application
    home_page = Tk()
    home_page.geometry('1366x768')
    # heading

    # functions

    # main code - e.g. buttons, etc
    btn = Button(home_page, text='Construct Plan', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1,command=construct)
    btn.place(x=955, y=400)

    # Button of Interior design
    btn = Button(home_page, text='Interior Plan', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command=intdesign)
    btn.place(x=955, y=500)
    home_page.image = Image.open('images/Home.png')
    home_page.photo = ImageTk.PhotoImage(home_page.image)
    lbl = Label(home_page, text="Home Page", fg='red', font=("Times New Roman", 31))
    lbl.place(x=60, y=50)

    home_page.mainloop()

def construct():
    construct_page = Tk()
    construct_page.geometry('1366x768')
    construct_page.title('Construction')



    lbl = Label(construct_page, text="Construct A House", fg='red', font=("Helvetica", 30))
    lbl.place(x=20, y=10)

    # label area availability
    lbl1 = Label(construct_page, text='Area Availability', font=("Helvetica", 26))
    lbl1.place(x=90, y=200)
    # text field of area availability
    txtfld = Entry(construct_page, text="  1 ", bd=5, font=("Helvetica", 28))
    txtfld.place(x=400, y=200, height=50, width=300)

    # label Budget
    lbl1 = Label(construct_page, text='Budget', font=("Helvetica", 26))
    lbl1.place(x=90, y=300)
    # text field of budget
    txtfld = Entry(construct_page, text=" 2  ", bd=5, font=("Helvetica", 28))
    txtfld.place(x=400, y=300, height=50, width=300)

    # label floor
    lbl1 = Label(construct_page, text='Floors', font=("Helvetica", 26))
    lbl1.place(x=90, y=100)
    # text field of floor
    txtfld = Entry(construct_page, text="  3 ", bd=5, font=("Helvetica", 28))
    txtfld.place(x=400, y=100, height=50, width=150)

    # label house space
    lbl1 = Label(construct_page, text='House Space', font=("Helvetica", 26))
    lbl1.place(x=90, y=400)
    # text field of floor
    txtfld = Entry(construct_page, text=" 4  ", bd=5, font=("Helvetica", 28))
    txtfld.place(x=400, y=400, height=50, width=150)

    # creating button
    btn = Button(construct_page, text='Confirm', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1, command=plans)
    btn.place(x=290, y=500)

    btn = Button(construct_page, text='Materials', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1,command=materials)
    btn.place(x=1000, y=100)

    construct_page.mainloop()

def plans():
    plans_page = Tk()
    plans_page.geometry('1366x768')
    plans_page.title('Construction Plan')
    # heading

    # functions

    # main code - e.g. buttons, etc
    btn = Button(plans_page, text='Plan A', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1)
    btn.place(x=100, y=180)
    btn = Button(plans_page, text='Plan B', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1)
    btn.place(x=100, y=290)
    btn = Button(plans_page, text='Plan C', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1)
    btn.place(x=100, y=400)
    btn = Button(plans_page, text='Plan D', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1)
    btn.place(x=100, y=510)
    btn = Button(plans_page, text='Plan E', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1)
    btn.place(x=100, y=620)

    plans_page.mainloop()

def intdesign():
    intdesg_page = Tk()
    intdesg_page.geometry('1366x768')
    intdesg_page.title('Interior')
    # heading

    lbl = Label(intdesg_page, text="Interior Design", fg='red', font=("Helvetica", 30))
    lbl.place(x=30, y=20)

    # label redesign
    lbl1 = Label(intdesg_page, text='Select options to be interiorize', font=("Helvetica", 26))
    lbl1.place(x=840, y=290)


    # label dimensions
    lbl1 = Label(intdesg_page, text='Dimensions  ', font=("Helvetica", 26))
    lbl1.place(x=850, y=420)

    txtfld = Entry(intdesg_page, text=" 1st txt  ", bd=5, font=("Helvetica", 28))
    txtfld.place(x=950, y=490, height=40, width=99)
    # 2nd txtfld
    txtfld2 = Entry(intdesg_page, text="2nd txt ", bd=5, font=("Helvetica", 28))
    txtfld2.place(x=1090, y=490, height=40, width=99)

    # creating button
    btn = Button(intdesg_page, text="Confirm", font=("Helvetica", 30), command=intplan)
    btn.place(x=980, y=600)

    intdesg_page.mainloop()

def intplan():
    intplans_page = Tk()
    intplans_page.geometry('1366x768')
    intplans_page.title('Interior Plan')
    # heading

    # functions

    # main code - e.g. buttons, etc
    btn = Button(intplans_page, text="Plan A", fg='blue', font=("Helvetica", 26))
    btn.place(x=180, y=180)
    btn = Button(intplans_page, text="Plan B", fg='blue', font=("Helvetica", 26))
    btn.place(x=180, y=280)
    btn = Button(intplans_page, text="Plan C", fg='blue', font=("Helvetica", 26))
    btn.place(x=180, y=380)
    btn = Button(intplans_page, text="Plan D", fg='blue', font=("Helvetica", 26))
    btn.place(x=180, y=480)
    btn = Button(intplans_page, text="Plan E", fg='blue', font=("Helvetica", 26))
    btn.place(x=180, y=580)

    intplans_page.mainloop()
def materials():
    material_page = Tk()
    material_page.geometry('1366x768')

    # label to be construced
    lbl1 = Label(material_page, text="Floors to be constructed", fg='red', font=("Helvetica", 26))
    lbl1.place(x=30, y=70)
 #combo1
    # label house space
    lbl3 = Label(material_page, text="House Space", fg='red', font=("Helvetica", 26))
    lbl3.place(x=30, y=130)
# combobox2

    # 1a
    lbl1a = Label(material_page, text="Concrete", fg='black', font=("Helvetica", 26))
    lbl1a.place(x=30, y=210)
    txtfld1a = Entry(material_page, text=" Concrete  ", bd=5, font=("Helvetica", 28))
    txtfld1a.place(x=250, y=210, height=40, width=130)
    # 1b
    lbl1b = Label(material_page, text="Brick", fg='black', font=("Helvetica", 26))
    lbl1b.place(x=30, y=290)
    txtfld1b = Entry(material_page, text=" Brick ", bd=5, font=("Helvetica", 28))
    txtfld1b.place(x=250, y=290, height=40, width=130)
    # 1c
    lbl1c = Label(material_page, text="Steel", fg='black', font=("Helvetica", 26))
    lbl1c.place(x=30, y=370)
    txtfld1c = Entry(material_page, text="Steel  ", bd=5, font=("Helvetica", 28))
    txtfld1c.place(x=250, y=370, height=40, width=130)
    # 1d
    lbl1d = Label(material_page, text="Glass", fg='black', font=("Helvetica", 26))
    lbl1d.place(x=30, y=450)
    txtfld1d = Entry(material_page, text="Glass  ", bd=5, font=("Helvetica", 28))
    txtfld1d.place(x=250, y=450, height=40, width=130)
    # 2a
    lbl2a = Label(material_page, text="Wood", fg='black', font=("Helvetica", 26))
    lbl2a.place(x=530, y=210)
    txtfld2a = Entry(material_page, text="Wood ", bd=5, font=("Helvetica", 28))
    txtfld2a.place(x=750, y=210, height=40, width=130)
    # 2b
    lbl2b = Label(material_page, text="Tiles", fg='black', font=("Helvetica", 26))
    lbl2b.place(x=530, y=290)
    txtfld2b = Entry(material_page, text="Tiles", bd=5, font=("Helvetica", 28))
    txtfld2b.place(x=750, y=290, height=40, width=130)
    # 2c
    lbl2c = Label(material_page, text="Cement", fg='black', font=("Helvetica", 26))
    lbl2c.place(x=530, y=370)
    txtfld2c = Entry(material_page, text="Cement", bd=5, font=("Helvetica", 28))
    txtfld2c.place(x=750, y=370, height=40, width=130)
    # 2d
    lbl2d = Label(material_page, text="Aggregate", fg='black', font=("Helvetica", 26))
    lbl2d.place(x=530, y=450)
    txtfld2d = Entry(material_page, text="Aggregate", bd=5, font=("Helvetica", 28))
    txtfld2d.place(x=750, y=450, height=40, width=130)

    lbl3a = Label(material_page, text="Cost(rs)", fg='black', font=("Helvetica", 26))
    lbl3a.place(x=750, y=560)
    txtfld3a = Entry(material_page, text="Cost", bd=5, font=("Helvetica", 28))
    txtfld3a.place(x=900, y=560, height=40, width=250)

    # creating button back
    btn1a = Button(material_page, text="Back", font=("Helvetica", 24))
    btn1a.place(x=9, y=3)

    # creating button estimate
    btn1b = Button(material_page, text='Estimate', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                   activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1)
    btn1b.place(x=900, y=110)

    material_page.mainloop()

def signup():
    cd_signup_window = Tk()
    cd_signup_window.geometry('1366x768')
    cd_signup_window.title('Registration')
    cd_signup_window.iconbitmap('')
    cd_signup_window.title('Sign Up')

    # set the window state to maximized
    # cd_signup_window.state('zoomed')

    # Functionality
    def name_enter(event):
        if name_entry.get() == 'Name':
            name_entry.delete(0, END)

    def username_enter(event):
        if username_entry.get() == 'Username':
            username_entry.delete(0, END)

    def answer_enter(event):
        if answer_entry.get() == 'Answer':
            answer_entry.delete(0, END)

    def password_enter(event):
        if password_entry.get() == 'Password':
            password_entry.delete(0, END)

    def hide(event):
        cd_open_eye.config(file='closeye.png')
        password_entry.config(show='*')
        cd_eye_btn.config(command=show)

    def show():
        cd_open_eye.config(file='openeye.png')
        password_entry.config(show='')
        cd_eye_btn.config(command=hide)

    # Heading Label
    cd_head_lbl = Label(cd_signup_window, text='REGISTRATION', font=('Times New Roman', 30, 'bold'), bg='white',
                        fg='firebrick1')
    cd_head_lbl.place(x=190, y=105)

    # Name input TextField
    name_entry = Entry(cd_signup_window, width=25, font=('Times New Roman', 20, 'bold'), bd=0, fg='firebrick1')
    name_entry.place(x=127, y=180)
    name_entry.insert(0, 'Name')
    name_entry.bind('<FocusIn>', name_enter)

    # Name line for TextField
    Frame(cd_signup_window, width=430, height=2, bg='firebrick1').place(x=127, y=215)

    # Username input TextField
    username_entry = Entry(cd_signup_window, width=25, font=('Times New Roman', 20, 'bold'), bd=0, fg='firebrick1')
    username_entry.place(x=127, y=250)
    username_entry.insert(0, 'Username')
    username_entry.bind('<FocusIn>', username_enter)

    # Username line for TextField
    Frame(cd_signup_window, width=430, height=2, bg='firebrick1').place(x=127, y=285)

    # list of options in dropdown-menu
    # Button
    cd_login_btn = Button(cd_signup_window, text='SIGNUP', font=('Open Sans', 17, 'bold'), fg='white', bg='firebrick1',
                          activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=30,
                          height=1)
    cd_login_btn.place(x=127, y=550)




    # Answer input TextField
    answer_entry = Entry(cd_signup_window, width=25, font=('Times New Roman', 20, 'bold'), bd=0, fg='firebrick1')
    answer_entry.place(x=127, y=400)
    answer_entry.insert(0, 'Answer')
    answer_entry.bind('<FocusIn>', answer_enter)

    # Answer line for TextField
    Frame(cd_signup_window, width=430, height=2, bg='firebrick1').place(x=127, y=435)

    # Password input TextField
    password_entry = Entry(cd_signup_window, width=25, font=('Times New Roman', 20, 'bold'), bd=0, fg='firebrick1')
    password_entry.place(x=127, y=475)
    password_entry.insert(0, 'Password')
    password_entry.bind('<FocusIn>', password_enter)

    # Password line for TextField
    Frame(cd_signup_window, width=430, height=2, bg='firebrick1').place(x=127, y=510)

    # Eye
    cd_open_eye = PhotoImage(file='images/openeye.png')
    cd_eye_btn = Button(cd_signup_window, image=cd_open_eye, bd=0, bg='white', activebackground='white', cursor='hand2',
                        command=hide)
    cd_eye_btn.place(x=1170, y=340)

    # Button
    cd_login_btn = Button(cd_signup_window, text='SIGNUP', font=('Open Sans', 17, 'bold'), fg='white', bg='firebrick1',
                          activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=30,
                          height=1)
    cd_login_btn.place(x=127, y=550)

    cd_signup_window.mainloop()


class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=YES)

        # Load the image
        self.image = Image.open('images/Picsart-main-login.jpg')
        self.photo = ImageTk.PhotoImage(self.image)

        # Create the background label and pack it
        self.background_label = Label(self, image=self.photo)
        self.background_label.pack(fill=BOTH, expand=YES)

        # Allow the user to fit the image to the window size
        self.bind("<Configure>", self.resize)

    def resize(self, event):
        # Resize the image
        self.image = self.image.resize((event.width, event.height))
        self.photo = ImageTk.PhotoImage(self.image)
        self.background_label.config(image=self.photo)



cd_login_window = Tk()
app = App(cd_login_window)
cd_login_window.geometry('1366x768')
cd_login_window.title('Login')

# set the window state to maximized
# cd_login_window.state('zoomed')

# Functionality
def username_enter(event):
    if username_entry.get()=='Username':
        username_entry.delete(0,END)
def password_enter(event):
    if password_entry.get()=='Password':
        password_entry.delete(0,END)
def hide(event):
    cd_open_eye.config(file='closeye.png')
    password_entry.config(show='*')
    cd_eye_btn.config(command=show)
def show():
    cd_open_eye.config(file='openeye.png')
    password_entry.config(show='')
    cd_eye_btn.config(command=hide)

# Heading Label


Label(cd_login_window, text='USER LOGIN', font=('Times New Roman', 30, 'bold'), bg='white', fg='firebrick1').place(x=875, y=120)


# Username input TextField
username_entry = Entry(cd_login_window, width=25, font=('Times New Roman', 20, 'bold'), bd=0, fg='firebrick1')
username_entry.place(x=780, y=240)
username_entry.insert(0, 'Username')
username_entry.bind('<FocusIn>', username_enter)

# Username line for TextField
Frame(cd_login_window, width=430, height=2, bg='firebrick1').place(x=780, y=285)

# Password input TextField
password_entry = Entry(cd_login_window, width=25, font=('Times New Roman', 20, 'bold'), bd=0, fg='firebrick1')
password_entry.place(x=780, y=335)
password_entry.insert(0, 'Password')
password_entry.bind('<FocusIn>', password_enter)

# Password line for TextField
Frame(cd_login_window, width=430, height=2, bg='firebrick1').place(x=780, y=380)

# Eye
cd_open_eye = PhotoImage(file='images/openeye.png')
cd_eye_btn = Button(cd_login_window, image=cd_open_eye, bd=0, bg='white', activebackground='white', cursor='hand2',command=hide)
cd_eye_btn.place(x=1170, y=340)

# Forgot Password
Button(cd_login_window, text='Forgot Password?', bd=0, bg='white', activebackground='white', cursor='hand2', font=('Times New Roman', 13, 'bold'), fg='firebrick1', activeforeground='firebrick1').place(x=1080, y=390)

# Button
Button(cd_login_window, text='LOGIN', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1', activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=25, height=1, command=home).place(x=780, y=450)

# Signup
Label(cd_login_window, text="Don't have an account?", font=('Open sans', 15, 'bold'), fg='firebrick1', bg='white').place(x=800, y=550)
Button(cd_login_window, text='Create One Now', font=('Open Sans', 15, 'bold underline'), fg='blue', bg='white', activeforeground='blue', activebackground='white', cursor='hand2', bd=0, command=signup).place(x=1030, y=545)





cd_login_window.mainloop()



















