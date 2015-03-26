from Tkinter import *

def onclick():
   pass

root = Tk()
# so people don't screw around with the window
root.resizable(0,0)

# text area is placed in the top frame...
topframe = Frame(root)
topframe.pack()
# login frame
loginframe = Frame(root)
loginframe.pack()

# ...send button is placed in the bottom
bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

def loginScreen(): 
    data = text.get("1.0",'end-1c')

    # clear previous screen
    for child in topframe.winfo_children():
        child.destroy()
    for child in bottomframe.winfo_children():
        child.destroy()

    Label(topframe, text="Enter your email address and password below:").grid(row=0)

    # draws login frame
    username_label = Label(bottomframe, text="User Name").grid(row=0)
    username_field = Entry(bottomframe).grid(row=0, column=1, padx=20)
    
    password_label = Label(bottomframe, text="Password").grid(row=1)
    password_field = Entry(bottomframe).grid(row=1, column=1, padx=20)

    sendbutton = Button(bottomframe, text="Send Message", command = messageScreen, fg="black")
    sendbutton.grid(row=2, column=0, ipady=20)

    cancelbutton = Button(bottomframe, text="Cancel", command = messageScreen, fg="black")
    cancelbutton.grid(row=2, column=1, ipady=20)
    
    print data


def destroyAll():
    for child in topframe.winfo_children():
        child.destroy()

def messageScreen():
    # text area
    global text

    scroll = Scrollbar(root)
    text = Text(topframe, height = 10, width = 60)
    scroll.pack(side=RIGHT, fill=Y)
    text.pack(side=LEFT, fill=Y)
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)

    text.insert(END, "Type your message here...")

    # send button
    blackbutton = Button(bottomframe, text="Send Message", command = loginScreen, fg="black")
    blackbutton.pack( side = BOTTOM)

messageScreen()
mainloop()

