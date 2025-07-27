from tkinter import *
from tkinter import messagebox
from gen_password import gen_pass

#-----------------------------Save Passwords----------------------------------#



root = Tk()
root.config(padx=20,pady=20)

can = Canvas(height=500,width=500)
logo = PhotoImage(file='pass.png')

can.create_image(250,250,image=logo)
# can.pack()
can.grid(row=0,column=1)

web = Label(root,text="Website: ",font=('Arial',10,'bold'))
web.grid(row=1,column=0,pady=2)
em = Label(root,text="Email/Username: ",font=('Arial',10,'bold'))
em.grid(row=2,column=0,pady=2)
password = Label(root,text="Password: ",font=('Arial',10,'bold'))
password.grid(row=3,column=0,pady=2)



web_entry = Entry(root,width=87)
web_entry.grid(row=1,column=1,columnspan=2,sticky='w')
web_entry.focus()
em_entry = Entry(root,width=87)
em_entry.grid(row=2,column=1,columnspan=2,sticky='w')
em_entry.insert(0,'reena@gmail.com')
password_entry = Entry(root,width=70)
password_entry.grid(row=3,column=1,sticky='w')


#-------------Add Button---------------#
def add_data():
    web = web_entry.get()
    em = em_entry.get()
    password = password_entry.get()
    # print(f"{web}|{em}|{password}")
    data = f"{web}|{em}|{password}"
    if web =="" or em=="":
        messagebox.showerror('Oops!',"Please Don't Leave Any Field Empty!")
    else:
        is_ok = messagebox.askokcancel(title=web,message=f"These are the details entered:\nEmail:{em}\nPassword:{password}.\nIs it ok to save?")
        if is_ok:
        # file = open('data.txt','a')
            with open('data.txt','a') as file:
                file.write(f"{data}\n")
                web_entry.delete(0,END)
                password_entry.delete(0,END)

            msg = messagebox.showinfo('File Data',"Data Saved into 'Data.txt' file")

def gen_pswd():
    password = gen_pass()
    password_entry.insert(0,password)



gen_btn = Button(root,text="Generate Password",font=('Arial',10,'bold'),command=gen_pswd)
gen_btn.grid(row=3,column=2,sticky='w')
add_btn = Button(root,text="Add",width=89,font=('Arial',10,'bold'),command=add_data)
add_btn.grid(row=4,column=1,columnspan=2,pady=2)


root.mainloop()