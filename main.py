from ast import operator
from hmac import compare_digest
from tkinter import *
import time
from turtle import clear

root=Tk()
root.geometry('1390x690+0+0')
root.resizable(0,0)
root.title('Restaurant Management System')

root.config(bg='Firebrick4')
# frames
TopFrame=Frame(root,bd=10,relief=RIDGE,bg='red4')
TopFrame.pack(side=TOP)
labelTitle=Label(TopFrame,text='Restaurant Management System',font=('fantasy',30,'bold'),fg='yellow',bd=10,bg='firebrick4',width=45)
labelTitle.grid(row=0,column=0)
# menu_frame
MenuFrame=Frame(root,bd=10,relief=RIDGE,bg='red4')
MenuFrame.pack(side=LEFT)

# cost_frame
CostFrame=Frame(MenuFrame,bd=4,relief=RIDGE,bg='red4',pady=10)
CostFrame.pack(side=BOTTOM)

# Food_frame
FoodFrame=LabelFrame(MenuFrame,text='Food',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4',)
FoodFrame.pack(side=LEFT)

# Drink_frame
drinksFrame=LabelFrame(MenuFrame,text='Drinks',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
drinksFrame.pack(side=LEFT)

# Desert_frame
desertFrame=LabelFrame(MenuFrame,text='Desert',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
desertFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='red4')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='red4')
calculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='red4')
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='red4')
buttonFrame.pack()

# functions 
def roti():
    if var1.get()==1:
        textroti.config(state=NORMAL)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        

def daal():
    if var2.get()==1:
        textdaal.config(state=NORMAL)
        textdaal.focus()

    else:
        textdaal.config(state=DISABLED)
        

def fish():
    if var3.get()==1:
        textfish.config(state=NORMAL)
        textfish.focus()

    else:
        textfish.config(state=DISABLED)
        

def sabji():
    if var4.get() == 1:
        textsabji.config(state=NORMAL)
        textsabji.focus()
    elif var4.get() == 0:
        textsabji.config(state=DISABLED)
        


def kebab():
    if var5.get() == 1:
        textkebab.config(state=NORMAL)
        textkebab.focus()
    elif var5.get() == 0:
        textkebab.config(state=DISABLED)
        


def chawal():
    if var6.get() == 1:
        textchawal.config(state=NORMAL)
        textchawal.focus()
    elif var6.get() == 0:
        textchawal.config(state=DISABLED)
        


def mutton():
    if var7.get() == 1:
        textmutton.config(state=NORMAL)
        textmutton.focus()
    elif var7.get() == 0:
        textmutton.config(state=DISABLED)
        


def paneer():
    if var8.get() == 1:
        textpaneer.config(state=NORMAL)
        textpaneer.focus()
    elif var8.get() == 0:
        textpaneer.config(state=DISABLED)
        


def chicken():
    if var9.get() == 1:
        textchicken.config(state=NORMAL)
        textchicken.focus()
    elif var9.get() == 0:
        textchicken.config(state=DISABLED)
        


def lassi():
    if var10.get() == 1:
        textlassi.config(state=NORMAL)
        textlassi.focus()
    elif var10.get() == 0:
        textlassi.config(state=DISABLED)
       


def coffee():
    if var11.get() == 1:
        textcoffee.config(state=NORMAL)
        textcoffee.focus()
    elif var11.get() == 0:
        textcoffee.config(state=DISABLED)
        


def faluda():
    if var12.get() == 1:
        textfaluda.config(state=NORMAL)
        textfaluda.focus()
    elif var12.get() == 0:
        textfaluda.config(state=DISABLED)
        


def shikanji():
    if var13.get() == 1:
        textshikanji.config(state=NORMAL)
        textshikanji.focus()
    elif var13.get() == 0:
        textshikanji.config(state=DISABLED)
        


def jaljeera():
    if var14.get() == 1:
        textjaljeera.config(state=NORMAL)
        textjaljeera.focus()
    elif var14.get() == 0:
        textjaljeera.config(state=DISABLED)
        


def roohafza():
    if var15.get() == 1:
        textroohafza.config(state=NORMAL)
        textroohafza.focus()
    elif var15.get() == 0:
        textroohafza.config(state=DISABLED)
        


def masalatea():
    if var16.get() == 1:
        textmasalatea.config(state=NORMAL)
        textmasalatea.focus()
    elif var16.get() == 0:
        textmasalatea.config(state=DISABLED)
        


def badammilk():
    if var17.get() == 1:
        textbadammilk.config(state=NORMAL)
        textbadammilk.focus()
    elif var17.get() == 0:
        textbadammilk.config(state=DISABLED)
        


def colddrinks():
    if var18.get() == 1:
        textcolddrinks.config(state=NORMAL)
        textcolddrinks.focus()
    elif var18.get() == 0:
        textcolddrinks.config(state=DISABLED)
        


def oreocake():
    if var19.get() == 1:
        textoreo.config(state=NORMAL)
        textoreo.focus()
    elif var19.get() == 0:
        textoreo.config(state=DISABLED)
        


def baklawacake():
    if var20.get() == 1:
        textapple.config(state=NORMAL)
        textapple.focus()
    elif var20.get() == 0:
        textapple.config(state=DISABLED)
       


def kitkatcake():
    if var21.get() == 1:
        textkitkat.config(state=NORMAL)
        textkitkat.focus()
    elif var21.get() == 0:
        textkitkat.config(state=DISABLED)
        


def vanillacake():
    if var22.get() == 1:
        textvanilla.config(state=NORMAL)
        textvanilla.focus()
    elif var22.get() == 0:
        textvanilla.config(state=DISABLED)
       


def bananacake():
    if var23.get() == 1:
        textbanana.config(state=NORMAL)
        textbanana.focus()
    elif var23.get() == 0:
        textbanana.config(state=DISABLED)
        


def browniecake():
    if var24.get() == 1:
        textbrownie.config(state=NORMAL)
        textbrownie.focus()
    elif var24.get() == 0:
        textbrownie.config(state=DISABLED)
       


def friut():
    if var25.get() == 1:
        textpineapple.config(state=NORMAL)
        textpineapple.focus()
    elif var25.get() == 0:
        textpineapple.config(state=DISABLED)
        


def hotchocolate():
    if var26.get() == 1:
        textchocolate.config(state=NORMAL)
        textchocolate.focus()
    elif var26.get() == 0:
        textchocolate.config(state=DISABLED)
        


def blackforest():
    if var27.get() == 1:
        textblackforest.config(state=NORMAL)
        textblackforest.focus()
    elif var27.get() == 0:
        textblackforest.config(state=DISABLED)
        

#Variables

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

# textvariable
e_roti=StringVar()
e_daal=StringVar()
e_sabji = StringVar()
e_chawal = StringVar()
e_fish = StringVar()
e_mutton = StringVar()
e_kebab = StringVar()
e_chicken = StringVar()
e_paneer = StringVar()

e_lassi=StringVar()
e_coffee = StringVar()
e_faluda = StringVar()
e_shikanji = StringVar()
e_roohafza = StringVar()
e_jaljeera = StringVar()
e_masalatea = StringVar()
e_badammilk = StringVar()
e_coldrinks = StringVar()

e_oreo=StringVar()
e_baklawa = StringVar()
e_kitkatcake = StringVar()
e_vanillacake = StringVar()
e_bananacake = StringVar()
e_browniecake = StringVar()
e_friut = StringVar()
e_hotchocolate = StringVar()
e_blackforest = StringVar()

costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()
##FOOD

roti=Checkbutton(FoodFrame,text='Roti',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1,command=roti)
roti.grid(row=0,column=0,sticky=W)

daal=Checkbutton(FoodFrame,text='Daal',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2,command=daal)
daal.grid(row=1,column=0,sticky=W)

fish=Checkbutton(FoodFrame,text='Fish',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3)
fish.grid(row=2,column=0,sticky=W)

sabji=Checkbutton(FoodFrame,text='Sabji',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4,command=fish)
sabji.grid(row=3,column=0,sticky=W)

kebab=Checkbutton(FoodFrame,text='kebab',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5,command=kebab)
kebab.grid(row=4,column=0,sticky=W)

chawal=Checkbutton(FoodFrame,text='Chawal',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6,command=chawal)
chawal.grid(row=5,column=0,sticky=W)

mutton=Checkbutton(FoodFrame,text='Mutton',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,command=mutton)
mutton.grid(row=6,column=0,sticky=W)

paneer=Checkbutton(FoodFrame,text='Paneer',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8,command=paneer)
paneer.grid(row=7,column=0,sticky=W)

chicken=Checkbutton(FoodFrame,text='Chicken',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9,command=chicken)
chicken.grid(row=8,column=0,sticky=W)

#Entry Fields for Food Items

textroti=Entry(FoodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roti)
textroti.grid(row=0,column=1)

textdaal=Entry(FoodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_daal)
textdaal.grid(row=1,column=1)

textfish=Entry(FoodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_fish)
textfish.grid(row=2,column=1)

textsabji = Entry(FoodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_sabji)
textsabji.grid(row=3, column=1)

textkebab = Entry(FoodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kebab)
textkebab.grid(row=4, column=1)

textchawal = Entry(FoodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chawal)
textchawal.grid(row=5, column=1)

textmutton = Entry(FoodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_mutton)
textmutton.grid(row=6, column=1)

textpaneer = Entry(FoodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_paneer)
textpaneer.grid(row=7, column=1)

textchicken = Entry(FoodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chicken)
textchicken.grid(row=8, column=1)

#Drinks

lassi=Checkbutton(drinksFrame,text='Lassi',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10,command=lassi)
lassi.grid(row=0,column=0,sticky=W)

coffee=Checkbutton(drinksFrame,text='Coffee',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11,command=coffee)
coffee.grid(row=1,column=0,sticky=W)

faluda=Checkbutton(drinksFrame,text='Faluda',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12,command=faluda)
faluda.grid(row=2,column=0,sticky=W)

shikanji=Checkbutton(drinksFrame,text='Shikanji',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13,command=shikanji)
shikanji.grid(row=3,column=0,sticky=W)

jaljeera=Checkbutton(drinksFrame,text='Jaljeera',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14,command=jaljeera)
jaljeera.grid(row=4,column=0,sticky=W)

roohafza=Checkbutton(drinksFrame,text='Roohafza',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15,command=roohafza)
roohafza.grid(row=5,column=0,sticky=W)

masalatea=Checkbutton(drinksFrame,text='Masala Tea',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16,command=masalatea)
masalatea.grid(row=6,column=0,sticky=W)

badammilk=Checkbutton(drinksFrame,text='Badam Milk',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17,command=badammilk)
badammilk.grid(row=7,column=0,sticky=W)

colddrinks=Checkbutton(drinksFrame,text='Cold Drinks',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18,command=colddrinks)
colddrinks.grid(row=8,column=0,sticky=W)
#entry fields for drink items

textlassi = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_lassi)
textlassi.grid(row=0, column=1)

textcoffee = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_coffee)
textcoffee.grid(row=1, column=1)

textfaluda = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_faluda)
textfaluda.grid(row=2, column=1)

textshikanji = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_shikanji)
textshikanji.grid(row=3, column=1)

textjaljeera = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_jaljeera)
textjaljeera.grid(row=4, column=1)

textroohafza = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_roohafza)
textroohafza.grid(row=5, column=1)

textmasalatea = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_masalatea)
textmasalatea.grid(row=6, column=1)

textbadammilk = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_badammilk)
textbadammilk.grid(row=7, column=1)

textcolddrinks = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_coldrinks)
textcolddrinks.grid(row=8, column=1)

# Desert

oreocake=Checkbutton(desertFrame,text='Oreo Cake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19,command=oreocake)
oreocake.grid(row=0,column=0,sticky=W)

baklawa=Checkbutton(desertFrame,text='Baklawa',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20,command=baklawacake)
baklawa.grid(row=1,column=0,sticky=W)

kitkatcake=Checkbutton(desertFrame,text='Kitkat Cake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21,command=kitkatcake)
kitkatcake.grid(row=2,column=0,sticky=W)

vanillacake=Checkbutton(desertFrame,text='Vanilla Ice-cream',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22,command=vanillacake)
vanillacake.grid(row=3,column=0,sticky=W)

bananacake=Checkbutton(desertFrame,text='Banana Milk Shake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23,command=bananacake)
bananacake.grid(row=4,column=0,sticky=W)

browniecake=Checkbutton(desertFrame,text='pudding',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24,command=browniecake)
browniecake.grid(row=5,column=0,sticky=W)

friut=Checkbutton(desertFrame,text='Furit plate ',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25,command=friut)
friut.grid(row=6,column=0,sticky=W)

hotchocolate=Checkbutton(desertFrame,text='Hot Chocolate',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26,command=hotchocolate)
hotchocolate.grid(row=7,column=0,sticky=W)

blackforestcake=Checkbutton(desertFrame,text='Black Forest',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27,command=blackforest)
blackforestcake.grid(row=8,column=0,sticky=W)

#entry fields for desert

textoreo = Entry(desertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_oreo)
textoreo.grid(row=0, column=1)

textapple = Entry(desertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_baklawa)
textapple.grid(row=1, column=1)

textkitkat = Entry(desertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kitkatcake)
textkitkat.grid(row=2, column=1)

textvanilla = Entry(desertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_vanillacake)
textvanilla.grid(row=3, column=1)

textbanana = Entry(desertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_bananacake)
textbanana.grid(row=4, column=1)

textbrownie = Entry(desertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_browniecake)
textbrownie.grid(row=5, column=1)

textpineapple = Entry(desertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_friut)
textpineapple.grid(row=6, column=1)

textchocolate = Entry(desertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_hotchocolate)
textchocolate.grid(row=7, column=1)

textblackforest = Entry(desertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_blackforest)
textblackforest.grid(row=8, column=1)

#costlabels & entry fields

labelCostofFood=Label(CostFrame,text='Cost of Food',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofFood.grid(row=0,column=0)

textCostofFood=Entry(CostFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textCostofFood.grid(row=0,column=1)

labelCostofDrinks=Label(CostFrame,text='Cost of Drinks',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofDrinks.grid(row=1,column=0)

textCostofDrinks=Entry(CostFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1,column=1)

labelCostofCakes=Label(CostFrame,text='Cost of Cakes',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofCakes.grid(row=2,column=0)

textCostofCakes=Entry(CostFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofcakesvar)
textCostofCakes.grid(row=2,column=1)

labelSubTotal=Label(CostFrame,text='Sub Total',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(CostFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3)

labelServiceTax=Label(CostFrame,text='Service Tax',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelServiceTax.grid(row=1,column=2)

textServiceTax=Entry(CostFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3)

labelTotalCost=Label(CostFrame,text='Total Cost',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(CostFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3)

#Buttons

buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=6)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=6)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=6)
buttonSave.grid(row=0,column=2)

#buttonSend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5)
#buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=6)
buttonReset.grid(row=0,column=4)
#textarea for receipt

textReceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

# calculator
operator=''
def buttonClick(numbers):
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))  
    calculatorField.delete(0,END) 
    calculatorField.insert(0,result)
    operator='' 
  
    
    
calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='yellow',bg='pink',bd=6,width=6,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='yellow',bg='firebrick4',bd=6,width=6,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='yellow',bg='firebrick4',bd=6,width=6,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='yellow',bg='firebrick4',bd=6,width=6,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)




root.mainloop()
