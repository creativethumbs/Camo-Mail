# program that sends 'encrypted' emails

from Tkinter import *
import smtplib
import datetime
import email.utils
from email.mime.text import MIMEText
import getpass

root = Tk()
# so people don't screw around with the window
root.resizable(0,0)
root.wm_title("Camo Mail")

topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

# prefix of mail server
server = smtplib.SMTP('smtp.gmail.com:587') 

def loginScreen(msg, subj, from_addr, to_addr):  
    global msg_str, subj_str, from_str, to_str, server
    msg_str = msg
    subj_str = subj
    from_str = from_addr
    to_str = to_addr

    destroyAll()

    for i in range(len(from_str)):
        if from_str[i] == '@':
            prefix = from_str[i+1 : i+4]
            if prefix == 'yah': 
                server = smtplib.SMTP('smtp.mail.yahoo.com',587)
            elif prefix == 'hot': 
                server = smtplib.SMTP('smtp.live.com',587)

    global password_field

    Label(topframe, text="Enter your password below:").grid(row=0)

    password_label = Label(bottomframe, text="Password").grid(row=1)
    password_field = Entry(bottomframe, show="*")
    password_field.grid(row=1, column=1, padx=20)

    sendbutton = Button(bottomframe, text="Send Message", command =lambda: sendMsg(password_field.get()))
    sendbutton.grid(row=2, column=0, ipady=20)

    cancelbutton = Button(bottomframe, text="Cancel", command = messageScreen)
    cancelbutton.grid(row=2, column=1, ipady=20)

# encrypts the message and subject
def encrypt():
    global msg_str, subj_str
    encryptedMsg = []
    encryptedSubj = []

    for i in range(len(msg_str)):  
        encryptedMsg.append(msg_str[i])
        if msg_str[i] != '\n':
            encryptedMsg.append(' ') 

    for i in range(len(subj_str)):  
        encryptedSubj.append(subj_str[i])
        encryptedSubj.append(' ')   

    msg_str = ''.join(encryptedMsg)
    subj_str = ''.join(encryptedSubj)

def sendMsg(password_field): 
    password = password_field 
    encrypt()

    header = 'From: %s\n' % from_str
    header += 'To: %s\n' % to_str 
    header += 'Subject: %s\n\n' % subj_str
    message = header + msg_str

    try: 
        server.starttls()
        server.login(from_str, password)
        server.sendmail(from_str, to_str, message)
        server.quit()

        destroyAll()
        Label(topframe, text="Message sent.").grid(row=0)
    except:
        destroyAll()
        Label(topframe, text="Invalid username, password, or recipient").grid(row=0)
    sendbutton = Button(bottomframe, text="Send Another Message", command = messageScreen)
    sendbutton.grid(row=1, column=0, ipady=20)

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

