from Tkinter import *
from datetime import *



top = Tk()

def buttonPress():
    dateandtime = datetime.now()

    Entry1 = E1.get()
    Entry2 = E2.get()
    OptionMenu1 = StartVar.get()

    print Entry1, Entry2, OptionMenu1, dateandtime

L1 = Label(top, text="Rank")
L1.pack( side = TOP, anchor="w")
E1 = Entry(top, bd =5)
E1.pack(side = TOP, anchor="w")

L2 = Label(top, text="Last Name, First Name")
L2.pack( side = TOP, anchor="w")
E2 = Entry(top, bd =5)
E2.pack(side = TOP, anchor="w")

StartVar = StringVar(top)
StartVar.set("Select Reason for Visit")

L3 = Label(top, text="Reason for Visit")
L3.pack( side = TOP, anchor="w")
OM1 = OptionMenu(top, StartVar, "PCS", "Separation", "Retirement", "Inbound", "Claims", "Other")
OM1.pack(side = TOP, anchor="w")

L4 = Label(top, text="Reason for Visit")
L4.pack_forget()
OE1 = Entry(top, bd=5)
OE1.pack_forget()

B1 = Button(top, text="OK", command=buttonPress)
B1.pack(side =TOP, anchor="s")



top.mainloop()