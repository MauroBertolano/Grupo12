from Practica.Tp5 import Socio
from Practica.Tp6 import  NegocioSocio
import tkinter as tk
from tkinter import *
from tkinter import ttk
def alta():
    root=tk.Tk()
    root.title("Nuevo Socio")
    root.marco=ttk.Frame(root, borderwidth=2)
    root.marco.grid(column=0, row=0)
    root.nom= StringVar()
    root.ape=StringVar()
    root.dni=StringVar()
    root.rotNom=Label(root.marco, text= "nombre:")
    root.rotAp=Label(root.marco, text= "apellido:")
    root.rotDni=Label(root.marco, text="dni:")

    root.N=ttk.Entry(root.marco, textvariable=root.nom)
    root.A=ttk.Entry(root.marco, textvariable=root.ape)
    root.D=ttk.Entry(root.marco, textvariable= root.dni)

    root.bot=ttk.Button(root.marco, text="Aceptar")
    root.rotNom.grid(column=1, row=2)
    root.rotAp.grid(column=1, row=3)
    root.rotDni.grid(column=1, row=4)

    root.N.grid(column=1, row=2)
    root.A.grid(column=1, row=3)
    root.D.grid(column=1, row=4)

    root.bot.grid(column=1, row=4)
    root.mainloop()

def cargardatos(root):
    s= Socio(dni=root.E.get(), nombre=root.N.get(), apellido=root.E.get())
    n.alta(s)

    root.destroy()
def baja():
    i=c.treeview.focus()
    if i:
        c.treeview.delete(i)
    else:
        a=tk.Tk()
        a.title("Borrar Socio")
        a.marco=ttk.Frame(a, borderwidth=2)
        a.marco.grid(column=0, row=0)
        a.msj=ttk.Label(a.marco, text="No ha seleccionado")
        a.bt=ttk.Button(a.marco, text="Salir",command=lambda: salir(a))
        a.msj.grid(column=0, row=1)
        a.bt.grid(column=0, row=2)
        a.mainloop()
def salir(root):
    root.destroy()
def modif():
    i=c.treeview.focus()
    a=tk.Tk()
    a.title("Modificar Socio")
    a.marco=ttk.Frame(a, borderwidth=2)
    a.marco.grid(column=0, row=0)
    if i:

        datos=c.treeview.item(i,"values")

        a.rotNom=Label(a.marco, text="Nombre:")
        a.rotAp=Label(a.marco, text="Apellido:")
        a.rotDni=Label(a.marco, text="DNI:")

        a.nombre= StringVar()
        a.ape=StringVar()
        a.dni=StringVar()

        a.N=ttk.Entry(a.marco, textvariable=a.nombre)
        a.A=ttk.Entry(a.marco, textvariable=a.ape)
        a.D=ttk.Entry(a.marco, textvariable=a.dni)
        a.N.insert(0, datos[0])
        a.A.insert(0,datos[1])
        a.D.insert(0,datos[2])
        a.bot=ttk.Button(a.marco, text="Aceptar")
        a.rotNom.grid(column=0, row=1)
        a.rotAp.grid(column=0, row=2)
        a.rotDni.grid(column=0, row=5)

        a.N.grid(column=1, row=1)
        a.A.grid(column=1, row=5)
        a.D.grid(column=1, row=5)
        a.bot.grid(column=1, row=4)
    else:
        a.msj=ttk.Label(a.marco, text="No hay ningun socio seleccionado")
        a.bt=ttk.Button(a.marco, text="Salir")
        a.msj.grid(column=0, row=1)
        a.bt.grid(column=0, row=3)
    a.mainloop()


c=tk.Tk()
c.title(" Socios Gestion Socios")
c.marco=ttk.Frame(c, borderwidth=1)
c.marco.grid(column=0, row=0)
c.treeview = ttk.Treeview(c.marco, selectmode=tk.BROWSE)
c.treeview = ttk.Treeview(c.marco, columns= ("nom", "ape", "dni"))
c.treeview.heading("#0", text="ID")
c.treeview.heading("nom", text="Nombre")
c.treeview.heading("ape", text="Apellido")
c.treeview.heading("dni", text="DNI")
n=NegocioSocio()
for s in n.todos():
    c.treeview.insert("", END, text=s.id, values=(s.nombre,s.apellido, s.dni ))

c.btAlta=Button(c.marco, text="Alta", command=alta)
c.btBaja=Button(c.marco, text="Baja", command=baja)
c.btModif=Button(c.marco, text="Modificar", command=modif)

c.marco.grid(column=0, row=0)
c.treeview.grid(column=0, row=0)
c.btAlta.grid(column=0, row=1)
c.btBaja.grid(column=1, row=1)
c.btModif.grid(column=2, row=1)

c.mainloop()
