from tkinter import *
import tkinter.messagebox as msg
import time

root = Tk()
root.geometry("250x370")
root.wm_maxsize(250,370)
root.wm_minsize(250,370)
root.title("Calculator")

#Click function for button 9,8,7
def click(event):
    print("")
    global Scvalue
    text = event.widget.cget("text")#Way to bring out the text from the buttom
    print(text)
    if text == "=":
        if Scvalue.get().isdigit():
            value = int(Scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as error:
                print(error)
                value = "Error"
                time.sleep(1)
                value = ""
                Scvalue.set(value)

        Scvalue.set(value)
        screen.update()

    elif text == "C":
        Scvalue.set("")
        screen.update()
    elif text =="X":
        val = str(Scvalue.get())
        Scvalue.set(val[:-1])
        screen.update()


    else:

        Scvalue.set(Scvalue.get() + text)
        screen.update()



#Making the screen for displaying the digits
Scvalue = StringVar()
Scvalue.set("")
# border_color = Frame(root, background="red")
screen = Entry(root, highlightthickness=5,textvar = Scvalue , font = "lucida 20 bold")
screen.pack(fill="x", ipadx=10, ipady=10)


#Making frames for buttons
Frame1 = Frame(root, bg = "grey")
b = Button(Frame1, padx =30, pady = 5,text="9", font = "lucida 10 bold", bg ="grey",fg ="white")
b.pack(side = LEFT,padx =5, pady = 5)
b.bind("<Button-1>", click)

b = Button(Frame1 , padx = 30, pady = 5,text="8", font = "lucida 10 bold",bg ="grey")
b.pack(side = LEFT,padx =5, pady = 5)
b.bind("<Button-1>", click)

b = Button(Frame1, padx = 30, pady = 5,text="7", font = "lucida 10 bold",bg ="grey")
b.pack(side= LEFT,padx =5, pady = 3)
b.bind("<Button-1>", click)

Frame1.pack()


Frame1 = Frame(root, bg = "grey")
b = Button(Frame1, padx = 30, pady = 5,text="6", font = "lucida 10 bold",bg ="grey")
b.pack(side = LEFT,padx =5, pady = 5)
b.bind("<Button-1>", click)

b = Button(Frame1, padx = 30, pady = 5,text="5", font = "lucida 10 bold",bg ="grey")
b.pack(side = LEFT,padx =5, pady = 5)
b.bind("<Button-1>", click)

b = Button(Frame1, padx = 30, pady = 5,text="4", font = "lucida 10 bold",bg ="grey")
b.pack(side= LEFT,padx =5, pady = 5)
b.bind("<Button-1>", click)

Frame1.pack()


Frame1 = Frame(root, bg = "grey")
b = Button(Frame1, padx = 30, pady = 5,text="3", font = "lucida 10 bold",bg ="grey")
b.pack(side = LEFT,padx =5, pady = 5)
b.bind("<Button-1>", click)

b = Button(Frame1, padx = 30, pady = 5,text="2", font = "lucida 10 bold",bg ="grey")
b.pack(side = LEFT,padx =5, pady = 5)
b.bind("<Button-1>", click)


b = Button(Frame1, padx = 30, pady = 5,text="1", font = "lucida 10 bold",bg ="grey")
b.pack(side= LEFT,padx =5, pady = 5)
b.bind("<Button-1>", click)

Frame1.pack()


Frame1 = Frame(root, bg = "grey")
b = Button(Frame1, padx = 29, pady = 5,text="0", font = "lucida 10 bold",bg ="grey")
b.pack(side = LEFT,padx =5, pady = 5)
b.bind("<Button-1>", click)

b = Button(Frame1, padx = 28, pady = 5,text="00", font = "lucida 10 bold",bg ="grey")
b.pack(side = LEFT,padx =5, pady = 5)
b.bind("<Button-1>", click)

b = Button(Frame1, padx = 29, pady = 5,text="+", font = "lucida 10 bold",bg ="grey")
b.pack(side= LEFT,padx =5, pady = 5)
b.bind("<Button-1>", click)

Frame1.pack()


Frame1 = Frame(root, bg = "grey")
b = Button(Frame1, padx = 31, pady = 5,text="-", font = "lucida 10 bold",bg ="grey")
b.pack(side = LEFT,padx =5, pady = 5)
b.bind("<Button-1>", click)

b = Button(Frame1, padx = 31, pady = 5,text="*", font = "lucida 10 bold",bg ="grey")
b.pack(side = LEFT,padx =5, pady = 5)
b.bind("<Button-1>", click)

b = Button(Frame1, padx = 30, pady = 5,text="/", font = "lucida 10 bold",bg ="grey")
b.pack(side= LEFT,padx =5, pady = 5)
b.bind("<Button-1>", click)

Frame1.pack()

Frame1 = Frame(root, bg = "grey")
b = Button(Frame1, padx = 28, pady = 5,text="=", font = "lucida 10 bold",bg ="grey")
b.pack(side = LEFT,padx =5, pady = 5)
b.bind("<Button-1>", click)

b = Button(Frame1, padx = 28, pady = 5,text="X", font = "lucida 10 bold",bg ="red")
b.pack(side = LEFT,padx =5, pady = 5)
b.bind("<Button-1>", click)

b = Button(Frame1, padx = 32, pady = 5,text="C", font = "lucida 10 bold",bg ="red")
b.pack(side= LEFT,padx =5, pady = 5)
b.bind("<Button-1>", click)

 #Frame1 = Frame(root, bg = "grey")
 #b = Button(Frame1, padx = 60, pady = 5,text="COPY", font = "lucida 10 bold", fg = "black")
 #b.pack(padx =120, pady = 120, fill= X)
 #b.bind("<Button-1>", click)

def Help():
    global status
    sbar = msg.showinfo("@2024",f"This is a Calculator by cleverly")
    sbar.pack()
Button(root, text = "@2024", command =Help).pack(side = BOTTOM, fill = X)

Frame1.pack()

root.mainloop()