from Tkinter import *

root = Tk()
root.geometry("500x400+50+50")
root.title("Calculator")

Tops = Frame(root, width = 700, height=80, bd=8, relief="raise",bg="green")
Tops.pack(side=TOP)

Below = Frame(root, width = 200, height=20, bd=4, relief="raise", bg="red")
Below.pack(side=BOTTOM)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def btnClick(numbers):
    global operator
    operator= operator + str(numbers)
    text_input.set(operator)

def btnClear():
    global operator
    operator= ""
    text_input.set("")

def btnEqual():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""

operator = ""
text_input = StringVar()
                             
    


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

txtDisplay = Entry(Tops, font=('arial' ,15, 'bold'), textvariable=text_input, width = 21, bd=4, justify = 'right')
txtDisplay.grid(row =0, column =0)

btn7 = Button(Below, pady=1, bd=4, fg="black", bg="lightgreen",font=('arial', 16, 'bold'),width=2, height=2,
text= "7", command=lambda:btnClick(7)).grid(row = 0, column = 0)

btn8 = Button(Below, pady=1, bd=4, fg="black",bg="#ab9eed",font=('arial', 16, 'bold'),width=2, height=2,
text= "8",command=lambda:btnClick(8)).grid(row = 0, column = 1)

btn9 = Button(Below, pady=1, bd=4, fg="black",bg="#ab9eed",font=('arial', 16, 'bold'),width=2, height=2,
text= "9",command=lambda:btnClick(9)).grid(row = 0, column = 2)

btnadd = Button(Below, pady=1, bd=4, fg="black",bg="#f93939",font=('arial', 16, 'bold'),width=2, height=2,
text= "+",command=lambda:btnClick("+")).grid(row = 0, column = 3)

btn4 = Button(Below, pady=1, bd=4, fg="black",bg="#ab9eed",font=('arial', 16, 'bold'),width=2, height=2,
text= "4", command=lambda:btnClick(4)).grid(row = 1, column = 0)

btn5 = Button(Below, pady=1, bd=4, fg="black",bg="lightgreen",font=('arial', 16, 'bold'),width=2, height=2,
text= "5", command=lambda:btnClick(5)).grid(row = 1, column = 1)

btn6 = Button(Below, pady=1, bd=4, fg="black",bg="#f93939",font=('arial', 16, 'bold'),width=2, height=2,
text= "6",command=lambda:btnClick(6)).grid(row =1, column =2)

btnsub = Button(Below, pady=1, bd=4, fg="black",bg="#ab9eed",font=('arial', 16, 'bold'),width=2, height=2,
text= "-", command=lambda:btnClick("-")).grid(row = 1, column = 3)

btn1 = Button(Below, pady=1, bd=4, fg="black",bg="#ab9eed",font=('arial', 16, 'bold'),width=2, height=2,
text= "1", command=lambda:btnClick(1)).grid(row = 2, column = 0)

btn2 = Button(Below, pady=1, bd=4, fg="black",bg="#f93939",font=('arial', 16, 'bold'),width=2, height=2,
text= "2", command=lambda:btnClick(2) ).grid(row = 2, column = 1)

btn3 = Button(Below, pady=1, bd=4, fg="black",bg="lightgreen",font=('arial', 16, 'bold'),width=2, height=2,
text= "3", command=lambda:btnClick(3)).grid(row = 2, column = 2)

btnmult = Button(Below, pady=1, bd=4, fg="black",bg="#ab9eed",font=('arial', 16, 'bold'),width=2, height=2,
text= "*", command=lambda:btnClick("*")).grid(row = 2, column = 3)

btn0 = Button(Below, pady=1, bd=4, fg="black",bg="#f93939",font=('arial', 16, 'bold'),width=2, height=2,
text= "0", command=lambda:btnClick("0")).grid(row = 3, column = 0)

btnclear = Button(Below, pady=1, bd=4, fg="black",bg="#ab9eed",font=('arial', 16, 'bold'),width=2, height=2,
text= "C",command =btnClear).grid(row = 3, column = 1)

btnEquals = Button(Below, pady=1, bd=4, fg="black",bg="#ab9eed",font=('arial', 16, 'bold'),width=2, height=2,
text= "=",command =btnEqual).grid(row = 3, column = 2)

btndiv = Button(Below, pady=1, bd=4, fg="black",bg="lightgreen",font=('arial', 16, 'bold'),width=2, height=2,
text= "/", command=lambda:btnClick("*")).grid(row = 3, column = 3)
              





root.mainloop()

