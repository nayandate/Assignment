from  tkinter import *
from tkinter import messagebox
def handle_login():
   user_email=user_input.get()
   user_password=password_input.get()
   if user_email=="aryanpatidar7879@gmail.com" and user_password=="Aryan123":
         messagebox.showinfo("Wow","login successful")
   else:
        messagebox.showinfo("Error","invalid")
ob=Tk()
ob.config(background='blue')
ob.title("Local Page")
ob.geometry("300x450")
label=Label(ob,text='Welcome Aryan')
label.pack()

label2=Label(ob,text='Enter your UserName',fg="white",bg="blue")
label2.config(font=('verdana',10))
label2.pack(pady=(20,5))
user_input=Entry(ob,width=40)
user_input.pack(pady=(1,5))

lable3=Label(ob,text='Enter your Password',fg="white",bg="blue")
lable3.config(font=('vardana',10))
lable3.pack(pady=(20,5))
password_input=Entry(ob,width=40)
password_input.pack(pady=(1,5))


button=Button(ob,text="Login",fg="black",bg="white",command=handle_login)
button.pack(pady=(10,20))



ob.mainloop()



'''

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Submit", command=show_name)
button.pack()

window.mainloop()'''