from tkinter import *
import os
from payload import gen


root = Tk()
root.title('MSF Payload Generator -MRCrushed')
root.geometry("800x400")
Label(text='MRCrushed payload Generator', font='lucida 25').grid(row=0,column=2,pady=25)

def get_val():
    gen(apk_val.get(),lhost_val.get(),lport_val.get())


apk_label = Label(root,text="Enter Payload Name",font="courier 15").grid(row=3,column=1)
lhost_label = Label(root,text="Enter LHOST",font="courier 15").grid(row=4,column=1)
lport_label = Label(root,text="Enter LPORT",font="courier 15").grid(row=5,column=1)

apk_val = StringVar()
lhost_val =  StringVar()
lport_val = StringVar()

lport_val.set(4444)




apk_entry =  Entry(root,textvariable=apk_val).grid(row=3,column=2)
lhost_entry =  Entry(root,textvariable=lhost_val).grid(row=4,column=2)
lport_entry = Entry(root,textvariable=lport_val).grid(row=5,column=2)

Button(root,text="Generate Payload",command=get_val).grid(row=7,column=2)

root.mainloop()