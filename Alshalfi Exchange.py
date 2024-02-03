from tkinter import Tk, ttk
from tkinter import *

#تعريف قيم الصرف
USD_to_yer = 560
EUR_to_yer = 1200
SAR_to_yer = 139

currency = ['USD ','EUR','SAR','GBP']
Yemen = ['RER']

# Colors
cor0 = "#FFFFFF" 
cor1 = "#333333"
cor2 = "#E85D51"

window = Tk ()
window.geometry ('400x400')
window.title ("Alshalfi Exchange")
window.configure (bg=cor0)
window.resizable(height = False, width = False)

#frames
frame = Frame(window, width =400,height=100, bg=cor2)
frame.grid (row=0,column=0)


def convert_currency (from_currency , to_currency, amount):
    if from_currency == to_currency:
        return amount
    elif from_currency in currency and to_currency in Yemen:
        return amount * USD_to_yer
    elif from_currency in Yemen  and to_currency in currency:
        return amount / USD_to_yer
    else:
        return None
    
    
def convert_currency (from_currency , to_currency, amount):
    if from_currency == to_currency:
        return amount
    elif from_currency in currency and to_currency in Yemen:
        return amount * EUR_to_yer
    elif from_currency in Yemen  and to_currency in currency:
        return amount / EUR_to_yer
    else:
        return None
    

def convert_currency (from_currency , to_currency, amount):
    if from_currency == to_currency:
        return amount
    elif from_currency in currency and to_currency in Yemen:
        return amount * SAR_to_yer
    elif from_currency in Yemen  and to_currency in currency:
        return amount / SAR_to_yer
    else:
        return None

    
    
    
main = Frame(window, width =400,height=360, bg=cor0)
main.grid (row=1 , column=0)
app_name =Label(frame ,compound = LEFT ,text=" Currncy Exchnage  ",height=3 , padx=2,pady=0,anchor=CENTER,font=('Arial 20 bold'),bg=cor2,fg=cor0)
app_name.place (x=120,y=20)
# main frame
result = Label (main ,text="  ",width= 22 ,height=2 , pady=7, relief ='solid' , anchor=CENTER,font=('Ivy 15 bold'),bg=cor0,fg=cor1)
result.place (x=68 , y=15)

from_label = Label (main ,text=" From ",width= 8 ,height=1 , pady=0,padx=0, relief ='flat' , anchor=NW,font=('Ivy 12 bold'),bg=cor0,fg=cor1)
from_label.place (x=84,y=90)
combo1 = ttk.Combobox(main , width=8, justify= CENTER,font=("Ivy 12 bold"))
combo1['values'] = (currency)
combo1.place (x=85,y=120)
To_label = Label (main ,text=" TO ",width= 8 ,height=1 , pady=0,padx=0, relief ='flat' , anchor=NW,font=('Ivy 12 bold'),bg=cor0,fg=cor1)
To_label.place (x=220,y=90)
combo2 = ttk.Combobox(main , width=8, justify= CENTER,font=("Ivy 12 bold"))
combo2['values'] = (Yemen)
combo2.place (x=220,y=120)
value = Entry (main,width=27,justify= CENTER,font=("Ivy 12 bold"),relief=SOLID)
value.place (x=78,y=163)
button=Button (main,text="تحويل العملة",width=23,padx=7,height=2, bg=cor2,fg=cor0,font=("Ivy 13 bold"),relief= SOLID)
button.place (x=77,y=225)



def on_button_click ():
    from_currency = combo1.get()
    to_currency = combo2.get ()
    amount = float (value.get())
    converted_amount = convert_currency(from_currency, to_currency, amount)
    result.config(text=f"The rsult: {converted_amount:.2f} {to_currency}")

    if result is not None:
        print (f"{ converted_amount}")
    
    
   
button.config(command=on_button_click)
window.mainloop()



