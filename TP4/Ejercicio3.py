from tkinter import *
from tkinter.ttk import Treeview

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


raiz.mainloop()
