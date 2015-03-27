from Tkinter import *
from smtplib import SMTP
import datetime

root = Tk()
# so people don't screw around with the window
root.resizable(0,0)

topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

def loginScreen(msg, subj, from_addr, to_addr):  
    global msg_str, subj_str, from_str, to_str
    msg_str = msg
    subj_str = subj
    from_str = from_addr
    to_str = to_addr
    print subj_str
    
    destroyAll()

    global password_field

    Label(topframe, text="Enter your password below:").grid(row=0)

    password_label = Label(bottomframe, text="Password").grid(row=1)
    password_field = Entry(bottomframe, show="*")
    password_field.grid(row=1, column=1, padx=20)

    sendbutton = Button(bottomframe, text="Send Message", command =lambda: sendMsg(password_field.get()))
    sendbutton.grid(row=2, column=0, ipady=20)

    cancelbutton = Button(bottomframe, text="Cancel", command = messageScreen)
    cancelbutton.grid(row=2, column=1, ipady=20)
    

def sendMsg(password_field): 
    password = password_field

    debuglevel = 0

    smtp = SMTP()
    smtp.set_debuglevel(debuglevel)
    smtp.connect('smtp.gmail.com', 465)
    smtp.login(from_addr, password)

    to_addr = ["ticha.seth@gmail.com"]

    email = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (from_str, ", ".join(to_addr), subj_str, msg_str)

    smtp.sendmail(from_str, to_addr, email)
    smtp.quit()
    destroyAll()

# clear screen
def destroyAll():
    for child in topframe.winfo_children():
        child.destroy()
    for child in bottomframe.winfo_children():
        child.destroy()

def messageScreen():
    destroyAll()

    # text area
    global msg, subj, from_addr, to_addr

    from_label = Label(topframe, text="From:")
    from_label.grid(row=0)
    from_addr = Entry(topframe)
    from_addr.grid(row=0, column=1, padx=20)

    to_label = Label(topframe, text="To:")
    to_label.grid(row=1)
    to_addr = Entry(topframe)
    to_addr.grid(row=1, column=1, padx=20)
    
    subj_label = Label(topframe, text="Subject:")
    subj_label.grid(row=2)
    subj = Entry(topframe)
    subj.grid(row=2, column=1, padx=20)
    
    msg_label = Label(bottomframe, text="Message:").grid(row=0, column=0)
    msg = Text(bottomframe, height = 10, width = 60, highlightbackground="#D3F2E6")
    msg.grid(row=1)

    sendbutton = Button(bottomframe, text="Next", command = lambda:loginScreen(msg.get("1.0",'end-1c'), subj.get(), from_addr.get(), to_addr.get()))
    sendbutton.grid(row=2)

messageScreen()
mainloop()

