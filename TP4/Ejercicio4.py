from tkinter import *
from tkinter.ttk import Treeview

def aceptar(event,a,b):
    c = tv.insert("",END,text = a)
    tv.insert(c,END,text = b)
def alta(event):
    raiz2 = Tk()
    lbl1=Label(raiz2,text = "Nombre de ciudad")
    lbl2=Label(raiz2,text = "Codigo postal")
    ciud = StringVar
    post = StringVar
    txtCiudad = Entry(raiz2, textvariable = ciud)
    txtCodigo = Entry(raiz2, textvariable = post)
    lbl1.grid(column = 1,row=1)
    lbl2.grid(column = 1,row=2)
    txtCiudad.grid(column = 2,row=1)
    txtCodigo.grid(column = 2,row=2)
    btnAceptar = Button(raiz2,text = "Aceptar")
    btnCancelar= Button(raiz2,text = "Cancelar")
    btnAceptar.grid(column = 1,row=3)
    btnCancelar.grid(column = 2,row=3)
    btnAceptar.bind('<Button-1>',aceptar(ciud,post))
    raiz2.mainloop()

raiz = Tk()
tv = Treeview(raiz)
tv.pack()
ciudad1 = tv.insert("",1,text="Rosario")
codpos1 = tv.insert(ciudad1,1,text="2000")
ciudad2 = tv.insert("",5,text="Perez")
codpos2 = tv.insert(ciudad2,1,text="1111")
ciudad3 = tv.insert("",3,text="Funes")
codpos3 = tv.insert(ciudad3,1,text="3333")
ciudad4 = tv.insert("",4,text="Roldan")
codpos4 = tv.insert(ciudad4,1,text="8888")
ciudad5 = tv.insert("",2,text="Pueblo Esther")
codpos5 = tv.insert(ciudad5,1,text="9999")
altaBtn = Button(raiz, text = "Alta")
bajaBtn = Button(raiz, text = "Baja")
modificarBtn = Button(raiz, text = "Modificar")
altaBtn.bind('<Button-1>',alta)
altaBtn.pack()
bajaBtn.pack()
modificarBtn.pack()
raiz.mainloop()



