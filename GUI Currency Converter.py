# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:40:13 2020

@author: Parth
"""

import tkinter
from tkinter import *

expression=''

def enter(num):
    global expression
    
    expression=expression+str(num)
    equation.set(expression)
    
def equalto(): 
    try: 
  
        global expression 
  
        total = str(eval(expression))   
        equation.set(total)   
        expression = "" 
   
    except: 
  
        equation.set("Error") 
        expression = "" 

def clrscr(): 
    global expression 

    expression = "" 
    equation.set("")
    
def rte():
    global expression
    
    exp=float(expression)
    euro=0.012*exp
    equation.set(euro)
    
def etr():
    global expression
    
    exp=float(expression)
    rupee=85.54*exp
    equation.set(rupee)

def rtp():
    global expression
    
    exp=float(expression)
    pound=0.010*exp
    equation.set(pound)

def ptr():
    global expression
    
    exp=float(expression)
    rupee=95.40*exp
    equation.set(rupee)
    
def rtu():
    global expression
    
    exp=float(expression)
    usd=0.013*exp
    equation.set(usd)

def utr():
    global expression
    
    exp=float(expression)
    rupee=76.01*exp
    equation.set(rupee)
    
def rtc():
    global expression
    
    exp=float(expression)
    cd=0.018*exp
    equation.set(cd)

def ctr():
    global expression
    
    exp=float(expression)
    rupee=55.73*exp
    equation.set(rupee)
    
def rty():
    global expression
    
    exp=float(expression)
    rupee=0.093*exp
    equation.set(rupee)

def ytr():
    global expression
    
    exp=float(expression)
    yuan=10.76*exp
    equation.set(yuan)
    
def rtye():
    global expression
    
    exp=float(expression)
    rupee=1.41*exp
    equation.set(rupee)

def yetr():
    global expression
    
    exp=float(expression)
    yen=0.71*exp
    equation.set(yen)


if __name__=='__main__':
    
    gui=tkinter.Tk()
    equation=StringVar()
    
    gui.configure(background="grey")
    gui.title('Simple Currency Calculator')
    gui.geometry('375x210')
    
    text_ip=Entry(gui,justify='left'
                  ,textvariable=equation)
    text_ip.grid(columnspan=5, ipadx=75)
    
    equation.set('')
    
    button1= Button(gui,text='1',fg='white',bg='blue',
                    command=lambda: enter(1),height=1,width=7,
                    activebackground='powder blue')
    button1.grid(row=2,column=0)
    
    button2= Button(gui,text='2',fg='white',bg='blue',
                    command=lambda: enter(2),height=1,width=7,
                    activebackground='powder blue')
    button2.grid(row=2,column=1)
    
    button3= Button(gui,text='3',fg='white',bg='blue',
                    command=lambda: enter(3),height=1,width=7,
                    activebackground='powder blue')
    button3.grid(row=2,column=2)
    
    button4= Button(gui,text='4',fg='white',bg='blue',
                    command=lambda: enter(4),height=1,width=7,
                    activebackground='powder blue')
    button4.grid(row=3,column=0)
    
    button5= Button(gui,text='5',fg='white',bg='blue',
                    command=lambda: enter(5),height=1,width=7,
                    activebackground='powder blue')
    button5.grid(row=3,column=1)
    
    button6= Button(gui,text='6',fg='white',bg='blue',
                    command=lambda: enter(6),height=1,width=7,
                    activebackground='powder blue')
    button6.grid(row=3,column=2)
    
    button7= Button(gui,text='7',fg='white',bg='blue',
                    command=lambda: enter(7),height=1,width=7,
                    activebackground='powder blue')
    button7.grid(row=4,column=0)
    
    button8= Button(gui,text='8',fg='white',bg='blue',
                    command=lambda: enter(8),height=1,width=7,
                    activebackground='powder blue')
    button8.grid(row=4,column=1)
    
    button9= Button(gui,text='9',fg='white',bg='blue',
                    command=lambda: enter(9),height=1,width=7,
                    activebackground='powder blue')
    button9.grid(row=4,column=2)
    
    button0= Button(gui,text='0',fg='white',bg='blue',
                    command=lambda: enter(0),height=1,width=7,
                    activebackground='powder blue')
    button0.grid(row=5,column=0)
    
    dot= Button(gui,text='.',fg='white',bg='blue',
                command=lambda: enter("."),height=1,width=7,
                activebackground='powder blue')
    dot.grid(row=5,column=1)
    
    equal= Button(gui,text='=',fg='white',bg='blue',
                  command=equalto,height=1,width=7,
                  activebackground='powder blue')
    equal.grid(row=5,column=2)
    
    rte= Button(gui,text='Rs. to eur',fg='white',bg='black',
                command=rte,height=1,width=7,
                activebackground='dim gray')
    rte.grid(row=6,column=0)
    
    etr= Button(gui,text='eur to Rs',fg='white',bg='black',
                command=etr,height=1,width=7,
                activebackground='dim gray')
    etr.grid(row=6,column=1)

    rtp= Button(gui,text='Rs to Pds',fg='white',bg='black',
                command=rtp,height=1,width=7,
                activebackground='dim gray')
    rtp.grid(row=6,column=3)
    
    ptr= Button(gui,text='Pds to Rs',fg='white',bg='black',
                command=ptr,height=1,width=7,
                activebackground='dim gray')
    ptr.grid(row=6,column=4)
    
    rtu= Button(gui,text='Rs to $',fg='white',bg='black',
                command=rtu,height=1,width=7,
                activebackground='dim gray')
    rtu.grid(row=8,column=0)
    
    utr= Button(gui,text='$ to Rs',fg='white',bg='black',
                command=utr,height=1,width=7,
                activebackground='dim gray')
    utr.grid(row=8,column=1)
    
    rtc= Button(gui,text='Rs to can',fg='white',bg='black',
                command=rtc,height=1,width=7,
                activebackground='dim gray')
    rtc.grid(row=8,column=3)    
    
    ctr= Button(gui,text='can to Rs',fg='white',bg='black',
                command=ctr,height=1,width=7,
                activebackground='dim gray')
    ctr.grid(row=8,column=4)
    
    rty= Button(gui,text='Rs to Yuan',fg='white',bg='black',
                command=rty,height=1,width=7,
                activebackground='dim gray')
    rty.grid(row=9,column=0)
    
    ytr= Button(gui,text='Yuan to Rs',fg='white',bg='black',
                command=ytr,height=1,width=7,
                activebackground='dim gray')
    ytr.grid(row=9,column=1)
    
    rtye= Button(gui,text='Rs to Yen',fg='white',bg='black',
                 command=rtye,height=1,width=7,
                 activebackground='dim gray')
    rtye.grid(row=9,column=3)
    
    yetr= Button(gui,text='Yen to Rs',fg='white',bg='black',
                 command=yetr,height=1,width=7,
                 activebackground='dim gray')
    yetr.grid(row=9,column=4)
    
    clear= Button(gui,text='AC',fg='black',bg='dark orange',
                  command=clrscr,height=1,width=7,
                  activebackground='powder blue')
    clear.grid(row=2,column=4)
    
    
    gui.mainloop()