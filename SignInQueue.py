from Tkinter import *
from datetime import *

top = Tk()
slaveWindow = Tk()

MainHolder = [""]

#Submit button puts input into an array and appends it to the main array
def buttonPress():
    x = 0
    dateandtime = datetime.now()
    timestamp = dateandtime.strftime("%d-%b-%Y (%H:%M:%S.%f)")

    #Get Input From Customer into Veriables
    Entry1 = E1.get()
    Entry2 = E2.get()
    OptionMenu1 = StartVar.get()
    Entry3 = OE1.get()

    #Assign Into Array then add into main array
    CustomerInfo = [Entry1, Entry2, OptionMenu1, Entry3, timestamp]
    MainHolder.append(CustomerInfo)

    #Testing Purposes
    for x in range(len(MainHolder)):
        arrayLength = x

    print x

    #Prints Inputs Onto Second Window
    global L5
    L5 = Label(slaveWindow, text = MainHolder[x])
    L5.pack()

def clearPress():
    L5.pack_forget()

#Adds an extra box it other is selected
def otherUpdate(stringy):
    stringy = StartVar.get()
    if stringy == "Other":
        L4.pack(side=TOP, anchor="w")
        OE1.pack(side=TOP, anchor="w")
    else:
        L4.pack_forget()
        OE1.pack_forget()
    return




#GUI for Master Window

#Rank Input
L1 = Label(top, text="Rank")
L1.pack( side = TOP, anchor="w")
E1 = Entry(top, bd =5)
E1.pack(side = TOP, anchor="w")

#Name Input
L2 = Label(top, text="Last Name, First Name")
L2.pack( side = TOP, anchor="w")
E2 = Entry(top, bd =5)
E2.pack(side = TOP, anchor="w")

StartVar = StringVar(top)
StartVar.set("Select Reason for Visit")

#Drop Down Menu is L3 + L4
L3 = Label(top, text="Reason for Visit")
L3.pack( side = TOP, anchor="w")
OM1 = OptionMenu(top, StartVar, "PCS", "Separation", "Retirement", "Inbound", "Claims", "Other", command=otherUpdate)
OM1.pack(side = TOP, anchor="w")

L4 = Label(top, text="Reason for Visit")
L4.pack_forget()
OE1 = Entry(top, bd=5)
OE1.pack_forget()

B2 = Button(top, text="Clear", command=clearPress)
B2.pack(side=BOTTOM, anchor="s")

B1 = Button(top, text="Submit", command=buttonPress)
B1.pack(side =BOTTOM, anchor="s")


top.mainloop()
