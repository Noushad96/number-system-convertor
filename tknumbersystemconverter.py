#nukber system converter

from tkinter import *
from tkinter import ttk
root=Tk()
root.title("number system conversion")
root.geometry("333x100")

# logic
def click():
    if (dataa.current()==0):    # agar decimal number hua to
        if (data.current()==0):    # decimal number
            value=int(combo1.get())  # combo1 k input ko integer bnake,value(variable) me store krega
            combo2.set(value)       #value(variable) ko combo2(entrybox) m print krega
        elif (data.current()==1): #  octal number
            value=int(combo1.get())   
            rvalue=oct(value).replace("0o","")  # value(variable)ko octal m covert krega
            combo2.set(rvalue) #value(variable) ko combo2(entrybox) m print krega
        elif (data.current()==2):  #binary number
            value=int(combo1.get())
            rvalue=bin(value).replace("0b","")  #convert to binary
            combo2.set(rvalue)
        else :
            value=int(combo1.get())
            rvalue=hex(value).replace("0x","") # convert to hexadecimal
            combo2.set(rvalue)
    elif (dataa.current()==1) :   # agar octal number hua to
        if (data.current()==0):    # decimal
            value=int(combo1.get(),8)   #combo1 ko decimal me convert
            combo2.set(value)  # combo2 me print krega
            
        elif (data.current()==1): #octal
            value=int(combo1.get()) # same input store krega
            combo2.set(value)  # octal hi print krega
        elif (data.current()==2):   #binary
            value=int(combo1.get(),8)  #converted into decimal
            rvalue=bin(value).replace("0b","") # converted into binary
            combo2.set(rvalue)
        else :
            value=int(combo1.get(),8) # converted to decimal
            rvalue=hex(value).replace("0x","") #converted to hexadecimal
            combo2.set(rvalue)
    elif (dataa.current()==2) : # binary
        if (data.current()==0): # decimal
            value=int(combo1.get(),2) # converted to decimal
            combo2.set(value)
            
        elif (data.current()==1):  #octal
            value=int(combo1.get(),2)  #converted to decimal
            rvalue=oct(value).replace("0o","") ##converted to octal
            combo2.set(rvalue)
        elif (data.current()==2): #binary
            value=int(combo1.get())#sme as binary
            combo2.set(value)
        else :
            value=int(combo1.get(),2) #converted to decimal
            rvalue=hex(value).replace("0x","") #converted to hexadecimal
            combo2.set(rvalue)
    else:
        if (data.current()==0):
            value=int(combo1.get(),16) #converted to decimal
            combo2.set(value)
            
        elif (data.current()==1):
            value=int(combo1.get(),16) #converted todecimal
            rvalue=oct(value).replace("0o","") #converted to octal
            combo2.set(rvalue)
        elif (data.current()==2):
            value=int(combo1.get(),16) #converted to decimal
            rvalue=bin(value).replace("0b","") #converted to binary
            combo2.set(rvalue)
        else :
            value=int(combo1.get()) #saved as it is
            combo2.set(value)
####################       From     ########################################

#create label From
lbl=Label(root,text="From").grid(row=1,column=1)

# create combobox
combovar1=StringVar()
dataa=ttk.Combobox(root,width=15,textvariable=combovar1 ,state="readonly") #create combobox
dataa.grid(row=1,column=2)
dataa['value']=("decimal number","octal number","binary number","hexadecimal")

# create entry widgets
combo1=StringVar(root)
screen1=Entry(root,textvariable=combo1)  # entry box bnaya 
screen1.grid(row=1,column=3)    # entry box ko pack kiya 
screen1.focus()        #cursor aa jayega 
Button(root,text="covert",command=click).grid(row=2,column=5 )

############################### To  ###################################

#create label for (to)
lbl=Label(root,text="to").grid(row=3,column=1)

# create combobox  for (to)
combovar2=StringVar()
data=ttk.Combobox(root,width=15,textvariable=combovar2 ,state="readonly") #create combobox
data.grid(row=3,column=2)
data['value']=("decimal number","octal number","binary number","hexadecimal")

# create entry widget for (to)
combo2=StringVar(root)
screen2=Entry(root,text=combo2)  # entry box bnaya 
screen2.grid(row=3,column=3)    # entry box ko pack kiya 
screen2.focus()
#####################################################################
# initial value of combobox
data.current(1)  # by default index value pe jo h usse show krega
dataa.current(0) # by default index value pe jo h usse show krega

root.resizable(0,0) # to fix the frame size or fix geometry
root.mainloop()


