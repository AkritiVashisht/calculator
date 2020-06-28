import tkinter as tk
expression = ""
def press(no):
    global expression
    expression += str(no)
    equation.set(expression)
def equal():
    global expression
    try:
        ans = str(eval(expression))
        equation.set(ans)
    except:
        equation.set("Invalid Input")
    expression = ""
def clean():
    global expression
    expression = ""
    equation.set("")

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("442x238")

equation = tk.StringVar()
equation.set("")

ent = tk.Entry(bg = "PaleGreen1" , width = 50 , textvariable = equation)
ent.grid(row = 0,columnspan = 40)

frame = tk.Frame(master= window , relief = tk.RAISED , borderwidth = 1)
frame.grid(row = 1 ,column = 0 )
button = tk.Button(text = "1", bg = "light slate blue", master = frame , height = 2 ,width = 14 ,command= lambda: press(1))
button.pack()

frame = tk.Frame(master= window , relief = tk.RAISED , borderwidth = 1)
frame.grid(row = 1 ,column = 1 )
button = tk.Button(text = "2", bg = "light slate blue", master = frame , height = 2 ,width = 14 ,command=lambda: press(2))
button.pack()

frame = tk.Frame(master= window , relief = tk.RAISED , borderwidth = 1)
frame.grid(row = 1 ,column = 2)
button = tk.Button(text = "3", bg = "light slate blue", master = frame , height = 2 ,width = 14 ,command=lambda: press(3))
button.pack()

frame = tk.Frame(master= window , relief = tk.RAISED , borderwidth = 1)
frame.grid(row = 1 ,column = 3 )
button = tk.Button(text = "CLEAR", bg = "light slate blue", master = frame , height = 2 ,width = 14 ,command= lambda: clean())
button.pack()

frame = tk.Frame(master= window , relief = tk.RAISED , borderwidth = 1)
frame.grid(row = 2 ,column = 0 )
button = tk.Button(text = "4", bg = "light slate blue", master = frame , height = 2 ,width = 14 ,command=lambda: press(4))
button.pack()

frame = tk.Frame(master= window , relief = tk.RAISED , borderwidth = 1)
frame.grid(row = 2 ,column = 1 )
button = tk.Button(text = "5", bg = "light slate blue", master = frame , height = 2 ,width = 14 ,command=lambda: press(5))
button.pack()

frame = tk.Frame(master= window , relief = tk.RAISED , borderwidth = 1)
frame.grid(row = 2 ,column = 2 )
button = tk.Button(text = "6", bg = "light slate blue", master = frame , height = 2 ,width = 14 ,command=lambda: press(6))
button.pack()

frame = tk.Frame(master= window , relief = tk.RAISED , borderwidth = 1)
frame.grid(row = 2 ,column = 3 )
button = tk.Button(text = "-", bg = "light slate blue", master = frame , height = 2 ,width = 14 ,command=lambda: press("-"))
button.pack()

frame = tk.Frame(master= window , relief = tk.RAISED , borderwidth = 1)
frame.grid(row = 3 ,column = 0 )
button = tk.Button(text = "7", bg = "light slate blue", master = frame , height = 2 ,width = 14 ,command=lambda: press(7))
button.pack()

frame = tk.Frame(master= window , relief = tk.RAISED , borderwidth = 1)
frame.grid(row = 3 ,column = 1 )
button = tk.Button(text = "8", bg = "light slate blue", master = frame , height = 2 ,width = 14 ,command=lambda: press(8))
button.pack()

frame = tk.Frame(master= window , relief = tk.RAISED , borderwidth = 1)
frame.grid(row = 3 ,column = 2 )
button = tk.Button(text = "9", bg = "light slate blue", master = frame , height = 2 ,width = 14 ,command=lambda: press(9))
button.pack()

frame = tk.Frame(master= window , relief = tk.RAISED , borderwidth = 1)
frame.grid(row = 3 ,column = 3)
button = tk.Button(text = "+", bg = "light slate blue", master = frame , height = 2 ,width = 14 ,command=lambda: press("+"))
button.pack()
frame = tk.Frame(master= window , relief = tk.RAISED , borderwidth = 1)
frame.grid(row = 4 ,column = 0 )
button = tk.Button(text = "0", bg = "light slate blue", master = frame , height = 2 ,width = 14 ,command=lambda: press(0))
button.pack()

frame = tk.Frame(master= window , relief = tk.RAISED , borderwidth = 1)
frame.grid(row = 4 ,column = 1 )
button = tk.Button(text = ".", bg = "light slate blue", master = frame , height = 2 ,width = 14 ,command=lambda: press("."))
button.pack()

frame = tk.Frame(master= window , relief = tk.RAISED , borderwidth = 1)
frame.grid(row = 4 ,column = 2 )
button = tk.Button(text = "/", bg = "light slate blue", master = frame , height = 2 ,width = 14 ,command=lambda: press('/'))
button.pack()

frame = tk.Frame(master= window , relief = tk.RAISED , borderwidth = 1)
frame.grid(row = 4 ,column = 3 )
button = tk.Button(text = "*", bg = "light slate blue", master = frame , height = 2 ,width = 14 ,command=lambda: press("*"))
button.pack()

frame = tk.Frame(master= window , relief = tk.RAISED , borderwidth = 1)
frame.grid(row = 5 ,columnspan = 4 )
button = tk.Button(text = "EVALUATE", bg = "light slate blue", master = frame , height = 2 ,width = 14 ,command=lambda: equal())
button.pack()

window.mainloop()
