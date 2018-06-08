from tkinter import *

def asignavalor(v):
    x=[]
    y=''
    res=0
    for i in v:
        if (i.isdigit()):
            y=y+i
        else:
            x.append(y)
            x.append(i)
            y=''
    x.append(y)
    cant=int(len(x))-1
    res=int(x[0])
    for i in range (0, cant):
        if(x[i]=='-'):
            res=res-int(x[i+1])
        elif(x[i]=='+'):
            res=res+int(x[i+1])
        elif(x[i]=='*'):
            res=res*int(x[i+1])
        elif(x[i]=='/'):
            res=res/int(x[i+1])
    text.set(res)


raiz = Tk()
b0=Button(raiz,text ="0", command = lambda : text.set(text.get()+'0'))
b1=Button(raiz,text ="1", command = lambda : text.set(text.get()+'1'))
b2=Button(raiz,text ="2", command = lambda : text.set(text.get()+'2'))
b3=Button(raiz,text ="3", command = lambda : text.set(text.get()+'3'))
b4=Button(raiz,text ="4", command = lambda : text.set(text.get()+'4'))
b5=Button(raiz,text ="5", command = lambda : text.set(text.get()+'5'))
b6=Button(raiz,text ="6", command = lambda : text.set(text.get()+'6'))
b7=Button(raiz,text ="7", command = lambda : text.set(text.get()+'7'))
b8=Button(raiz,text ="8", command = lambda : text.set(text.get()+'8'))
b9=Button(raiz,text ="9", command = lambda : text.set(text.get()+'9'))
igual=Button(raiz,text ="=", command = lambda : asignavalor(text.get()))
mas=Button(raiz,text ="+", command = lambda : text.set(text.get()+'+'))
menos=Button(raiz,text ="-", command = lambda : text.set(text.get()+'-'))
por=Button(raiz,text ="*", command = lambda : text.set(text.get()+'*'))
div=Button(raiz,text ="/", command = lambda : text.set(text.get()+'/'))
text = StringVar()
txtBox=Entry(raiz, textvariable = text)
txtBox.grid(row=1, column=1, columnspan = 4)

b0.grid(column=1,row=5)
b1.grid(column=1,row=4)
b2.grid(column=2,row=4)
b3.grid(column=3,row=4)
b4.grid(column=1,row=3)
b5.grid(column=2,row=3)
b6.grid(column=3,row=3)
b7.grid(column=1,row=2)
b8.grid(column=2,row=2)
b9.grid(column=3,row=2)
igual.grid(column=2,row=5, columnspan = 2, ipadx = 13)
mas.grid(column=4,row=2)
menos.grid(column=4,row=3)
por.grid(column=4,row=4)
div.grid(column=4,row=5)


raiz.mainloop()
