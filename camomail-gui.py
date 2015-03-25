from Tkinter import *

def onclick():
   pass

root = Tk()
# so people don't screw around with the window
#root.resizable(0,0)

# text area is placed in the top frame...
topframe = Frame(root)
topframe.pack()
# ...send button is placed in the bottom
bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

def retrieve_input():
    data = text.get("1.0",'end-1c')
    print data

# text area
scroll = Scrollbar(root)
text = Text(topframe, height = 10, width = 60)
scroll.pack(side=RIGHT, fill=Y)
text.pack(side=LEFT, fill=Y)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

text.insert(END, "Type your message here...")


# send button
blackbutton = Button(bottomframe, text="Send", command = retrieve_input, fg="black")
blackbutton.pack( side = BOTTOM)


mainloop()

