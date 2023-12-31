from tkinter import *
import time
import random
from functools import partial
import re

root = Tk()

def check_win():
    global liste_X
    global liste_O
    global switch
    if "A" in liste_X and "B" in liste_X and "C" in liste_X:
        print("Winner! ABC")
        setup()
    if "A" in liste_O and "B" in liste_O and "C" in liste_O:
        print("Winner! ABC")
        setup()
    if "D" in liste_X and "E" in liste_X and "F" in liste_X:
        print("Winner! DEF")
        setup()
    if "D" in liste_O and "E" in liste_O and "F" in liste_O:
        print("Winner! DEF")
        setup()
    if "G" in liste_X and "H" in liste_X and "I" in liste_X:
        print("Winner! GHI")
        setup()
    if "G" in liste_O and "H" in liste_O and "I" in liste_O:
        print("Winner! GHI")
        setup()   
    if "A" in liste_X and "D" in liste_X and "G" in liste_X:
        print("Winner! ADG")
        setup()
    if "A" in liste_O and "D" in liste_O and "G" in liste_O:
        print("Winner! ADG")
        setup()
    
    if "B" in liste_X and "E" in liste_X and "H" in liste_X:
        print("Winner! BEH")
        setup()
    if "B" in liste_O and "E" in liste_O and "H" in liste_X:
        print("Winner! BEH")
        setup()
    if "C" in liste_X and "F" in liste_X and "I" in liste_X:
        print("Winner! CFI")
        setup()
    if "C" in liste_O and "F" in liste_O and "I" in liste_O:
        print("Winner! CFI")
        setup()
    if "A" in liste_X and "E" in liste_X and "I" in liste_X:
        print("Winner! AEI")
        setup()
    if "A" in liste_O and "E" in liste_O and "I" in liste_O:
        print("Winner! AEI")
        setup()
    if "G" in liste_X and "E" in liste_X and "C" in liste_X:
        print("Winner! GEC")
        setup()
    if "G" in liste_O and "E" in liste_O and "C" in liste_O:
        print("Winner! GEC")
        setup()
    if R0_C0['text'] != "" and R0_C1['text'] != "" and R0_C2['text'] != "" and R1_C0['text'] != "" and R1_C1['text'] != "" and R1_C2['text'] != "" and R2_C0['text'] != "" and R2_C1['text'] != "" and R2_C2['text'] != "":
        print("Match nul")
        setup()


    print("check")

def haut_gauche():
    global liste_X
    global liste_O
    global switch
    if switch == True:
        R0_C0.config(text="X", state=DISABLED)
        liste_X.append("A")
        switch = False
    else:
        R0_C0.config(text="O", state=DISABLED)
        liste_O.append("A")
        switch = True
    check_win()
    print("A")

def haut_milieu():
    global liste_X
    global liste_O
    global switch
    if switch == True:
        R0_C1.config(text="X", state=DISABLED)
        liste_X.append("B")
        switch = False
    else:
        R0_C1.config(text="O", state=DISABLED)
        liste_O.append("B")
        switch = True
    check_win()
    print("B")

def haut_droit():
    global liste_X
    global liste_O
    global switch
    if switch == True:
        R0_C2.config(text="X", state=DISABLED)
        liste_X.append("C")
        switch = False
    else:
        R0_C2.config(text="O", state=DISABLED)
        liste_O.append("C")
        switch = True
    print("C")
    check_win()

def milieu_gauche():
    global liste_X
    global liste_O
    global switch
    
    if switch == True:
        R1_C0.config(text="X", state=DISABLED)
        liste_X.append("D")
        switch = False
    else:
        R1_C0.config(text="O", state=DISABLED)
        liste_O.append("D")
        switch = True
    print("D")
    check_win()

def milieu_milieu():
    global liste_X
    global liste_O
    global switch
    
    if switch == True:
        R1_C1.config(text="X", state=DISABLED)
        liste_X.append("E")
        switch = False
    else:
        R1_C1.config(text="O", state=DISABLED)
        liste_X.append("E")
        switch = True
    print("E")
    check_win()

def milieu_droit():
    global liste_X
    global liste_O
    global switch
    
    if switch == True:
        R1_C2.config(text="X", state=DISABLED)
        liste_X.append("F")
        switch = False
    else:
        R1_C2.config(text="O", state=DISABLED)
        liste_O.append("F")
        switch = True
    print("F")
    check_win()

def bas_gauche():
    global liste_X
    global liste_O
    global switch

    if switch == True:
        liste_X.append("G")
        R2_C0.config(text="X", state=DISABLED)
        switch = False
    else:
        R2_C0.config(text="O", state=DISABLED)
        liste_O.append("G")
        switch = True
    print("G")
    check_win()


def bas_milieu():
    global liste_X
    global liste_O
    global switch

    if switch == True:
        R2_C1.config(text="X", state=DISABLED)
        liste_X.append("H")
        switch = False
    else:
        R2_C1.config(text="O", state=DISABLED)
        liste_O.append("H")
        switch = True
    print("H")
    check_win()

def bas_droite():
    global liste_X
    global liste_O
    global switch
    
    if switch == True:
        R2_C2.config(text="X", state=DISABLED)
        liste_X.append("I")
        switch = False
    else:
        R2_C2.config(text="O", state=DISABLED)
        liste_O.append("I")
        switch = True
    check_win()
    print("I")
    check_win()










#Necessary widgets
R0_C0 = Button(root, text="", command=haut_gauche)
R0_C1 = Button(root, text="", command=haut_milieu)
R0_C2 = Button(root, text="", command=haut_droit)
R1_C0 = Button(root, text="", command=milieu_gauche)
R1_C1 = Button(root, text="", command=milieu_milieu)
R1_C2 = Button(root, text="", command=milieu_droit)
R2_C0 = Button(root, text="", command=bas_gauche)
R2_C1 = Button(root, text="", command=bas_milieu)
R2_C2 = Button(root, text="", command=bas_droite)

#padding

pad1 = Label(root, text="|")
pad2 = Label(root, text="|")
pad3 = Label(root, text="|")
pad4 = Label(root, text="|")
pad5 = Label(root, text="|")
pad6 = Label(root, text="|")

pad7 = Label(root, text="-")
pad8 = Label(root, text="-")
pad9 = Label(root, text="-")
pad10 = Label(root, text="-")
pad11 = Label(root, text="-")
pad12 = Label(root, text="-")

pad13 = Label(root, text="+")
pad14 = Label(root, text="+")
pad15 = Label(root, text="+")
pad16 = Label(root, text="+")

#Variables

liste_X = []
liste_O = []

switch = True 
#True = X, False = O


#Setup
def setup():
    liste_X = []
    liste_O = []
    switch = True
    R0_C0.config(text="")
    R0_C1.config(text="")
    R0_C2.config(text="")
    R1_C0.config(text="")
    R1_C1.config(text="")
    R1_C2.config(text="")
    R2_C0.config(text="")
    R2_C1.config(text="")
    R2_C2.config(text="")
    R0_C0.grid(row=0, column=0)
    pad1.grid(row=0, column=1)
    R0_C1.grid(row=0, column=2)
    pad2.grid(row=0, column=3)
    R0_C2.grid(row=0, column=4)

    pad7.grid(row=1, column=0)
    pad13.grid(row=1, column=1)
    pad8.grid(row=1, column=2)
    pad14.grid(row=1, column=3)
    pad9.grid(row=1, column=4)

    R1_C0.grid(row=2, column=0)
    pad3.grid(row=2, column=1)
    R1_C1.grid(row=2, column=2)
    pad4.grid(row=2, column=3)
    R1_C2.grid(row=2, column=4)

    pad10.grid(row=3, column=0)
    pad15.grid(row=3, column=1)
    pad11.grid(row=3, column=2)
    pad16.grid(row=3, column=3)
    pad12.grid(row=3, column=4)

    R2_C0.grid(row=4, column=0)
    pad5.grid(row=4, column=1)
    R2_C1.grid(row=4, column=2)
    pad6.grid(row=4, column=3)
    R2_C2.grid(row=4, column=4)


setup()

root.mainloop()