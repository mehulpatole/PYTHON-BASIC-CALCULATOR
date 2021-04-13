from tkinter import *

def click(event):
    text= event.widget.cget("text")
    
    if text== "clear":
        var1.set("")
        display.update()
    elif text=="=":

        try:
            val= eval(display.get())
            var1.set(val)
            display.update()
        except Exception as f:
            var1.set("invalid operation")
    else:
        var1.set(var1.get()+text)
        display.update()
        


a= Tk()   
a.title("CALCULATOR")
a.geometry("350x375")
var1= StringVar()
var1.set(" ")
display= Entry(a, textvariable= var1,bg= "black",fg= "white",bd= "5",width= "50")
display.pack(padx= 10,pady= 10)

f1= Frame(a,bg= "grey")
b1=Button(f1,text= "1" ,bd= "4",bg="black",fg="white",width="10")
b1.pack(padx= 2,pady=2,side=LEFT)
b1.bind("<Button-1>", click)

b2=Button(f1,text= "2", bd= "4",bg="black",fg="white",width="10")
b2.pack(padx= 2,pady=2,side=LEFT)
b2.bind("<Button-1>", click)

b3=Button(f1,text= "3", bd= "4",bg="black",fg="white",width="10")
b3.pack(padx= 2,pady=2,side= LEFT)
b3.bind("<Button-1>", click)

f1.pack()



f1= Frame(a,bg= "grey")
b1=Button(f1,text= "4" ,bd= "4",bg="black",fg="white",width="10")
b1.pack(padx= 2,pady=2,side=LEFT)
b1.bind("<Button-1>", click)

b2=Button(f1,text= "5", bd= "4",bg="black",fg="white",width="10")
b2.pack(padx= 2,pady=2,side=LEFT)
b2.bind("<Button-1>", click)

b3=Button(f1,text= "6", bd= "4",bg="black",fg="white",width="10")
b3.pack(padx= 2,pady=2,side= LEFT)
b3.bind("<Button-1>", click)

f1.pack()


f1= Frame(a,bg= "grey")
b1=Button(f1,text= "7" ,bd= "4",bg="black",fg="white",width="10")
b1.pack(padx= 2,pady=2,side=LEFT)
b1.bind("<Button-1>", click)

b2=Button(f1,text= "8", bd= "4",bg="black",fg="white",width="10")
b2.pack(padx= 2,pady=2,side=LEFT)
b2.bind("<Button-1>", click)

b3=Button(f1,text= "9", bd= "4",bg="black",fg="white",width="10")
b3.pack(padx= 2,pady=2,side= LEFT)
b3.bind("<Button-1>", click)

f1.pack()


f1= Frame(a,bg= "grey")
b1=Button(f1,text= "+" ,bd= "4",bg="black",fg="white",width="10")
b1.pack(padx= 2,pady=2,side=LEFT)
b1.bind("<Button-1>", click)

b2=Button(f1,text= "0", bd= "4",bg="black",fg="white",width="10")
b2.pack(padx= 2,pady=2,side=LEFT)
b2.bind("<Button-1>", click)

b3=Button(f1,text= "-", bd= "4",bg="black",fg="white",width="10")
b3.pack(padx= 2,pady=2,side= LEFT)
b3.bind("<Button-1>", click)

f1.pack()

f1= Frame(a,bg= "grey")
b1=Button(f1,text= "*" ,bd= "4",bg="black",fg="white",width="10")
b1.pack(padx= 2,pady=2,side=LEFT)
b1.bind("<Button-1>", click)

b2=Button(f1,text= "/", bd= "4",bg="black",fg="white",width="10")
b2.pack(padx= 2,pady=2,side=LEFT)
b2.bind("<Button-1>", click)

b3=Button(f1,text= "%", bd= "4",bg="black",fg="white",width="10")
b3.pack(padx= 2,pady=2,side= LEFT)
b3.bind("<Button-1>", click)

f1.pack()


f1= Frame(a,bg= "grey")
b1=Button(f1,text= "clear" ,bd= "4",bg="black",fg="white",width="17")
b1.pack(padx= 3,pady=2,side=LEFT)
b1.bind("<Button-1>", click)

b2=Button(f1,text= "=", bd= "4",bg="black",fg="white",width="17")
b2.pack(padx= 3,pady=2,side=LEFT)
b2.bind("<Button-1>", click)



f1.pack()

lb= Label(a, text= "Developed by ©mehulpatole")
lb.pack()



a.mainloop()