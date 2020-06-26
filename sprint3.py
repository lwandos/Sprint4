from tkinter import* 

def btnClick(numbers):
    global Operator
    Operator = Operator + str(numbers)
    text_input.set(Operator)

def btnClearDisplay():
    global Operator
    Operator =""
    text_input.set("")    

def btnEqualInput():
    global Operator
    sumup = str(eval(Operator))
    text_input.set(sumup)
    Operator=""



cal = Tk()
cal.title("Calculator")
Operator = ""
text_input = StringVar()

#creating a calculator display
txtDisplay = Entry(cal, font=('arial', 15,'bold'), textvariable=text_input,
             bd=30, insertwidth=4, bg="blue", justify='right').grid(columnspan=4)

btn7=Button(cal,padx=12,bd=8,fg="black",font=('arial', 20, 'bold'),
            text="7" , command=lambda:btnClick(7)).grid(row=1,column=0)

btn8=Button(cal,padx=12 ,bd=8,fg="black",font=('arial', 20, 'bold'),
            text="8", command=lambda:btnClick(8)).grid(row=1,column=1)

btn9=Button(cal,padx=12,bd=8,fg="black",font=('arial', 20, 'bold'),
            text="9", command=lambda:btnClick(9)).grid(row=1,column=2)


addition=Button(cal,padx=12,bd=8,fg="black",font=('arial', 20, 'bold'),
            text="+", command=lambda:btnClick("+")).grid(row=1,column=3)

#=====================================================

btn4=Button(cal,padx=12,bd=8,fg="black",font=('arial', 20, 'bold'),
            text="4", command=lambda:btnClick(4)).grid(row=2,column=0)

btn5=Button(cal,padx=12 ,bd=8,fg="black",font=('arial', 20, 'bold'),
            text="5", command=lambda:btnClick(5)).grid(row=2,column=1)

btn6=Button(cal,padx=12,bd=8,fg="black",font=('arial', 20, 'bold'),
            text="6", command=lambda:btnClick(6)).grid(row=2,column=2)

subraction=Button(cal,padx=12,bd=8,fg="black",font=('arial', 20, 'bold'),
            text="-", command=lambda:btnClick("-")).grid(row=2,column=3)

#=======================================================================

btn1=Button(cal,padx=12,bd=8,fg="black",font=('arial', 20, 'bold'),
            text="1", command=lambda:btnClick(1)).grid(row=3,column=0)

btn2=Button(cal,padx=12 ,bd=8,fg="black",font=('arial', 20, 'bold'),
            text="2", command=lambda:btnClick(2)).grid(row=3,column=1)

btn3=Button(cal,padx=12,bd=8,fg="black",font=('arial', 20, 'bold'),
            text="3", command=lambda:btnClick(3)).grid(row=3,column=2)

multiply=Button(cal,padx=12,bd=8,fg="black",font=('arial', 20, 'bold'),
            text="*", command=lambda:btnClick("*")).grid(row=3,column=3)

#===============================================================================

btn0=Button(cal,padx=12, pady=12, bd=8,fg="black",font=('arial', 20, 'bold'),
            text="0", command=lambda:btnClick(0)).grid(row=4,column=0)

btnClear=Button(cal,padx=12, pady=12, bd=8,fg="black",font=('arial', 20, 'bold'),
            text="C", command=btnClearDisplay).grid(row=4,column=1)
 
btnEqual=Button(cal,padx=12, pady=12,bd=8,fg="black",font=('arial', 20, 'bold'),
            text="=",command = btnEqualInput).grid(row=4,column=2)
 
division=Button(cal,padx=12, pady=12,bd=8,fg="black",font=('arial', 20, 'bold'),
            text="/", command=lambda:btnClick("/")).grid(row=4,column=3)                                

cal.mainloop() 
