from tkinter import *
import tkinter.ttk as ttk

from TP6.Guia6 import NegocioSocio, DniRepetido, LongitudInvalida, MaximoAlcanzado
from TP5.Guia5 import Socio

class PresentacionSocio(object):

    def __init__(self):
        self.negocio=NegocioSocio()
        self.root = Tk()
        self.root.geometry("654x277")
        self.root.title("ABM Socios")

        columns=('ID', 'Nombre', 'Apellido', 'DNI')
        self.tree = ttk.Treeview(self.root, columns=columns, show='headings')
        self.tree.place(relx=0.02, rely=0.04, relheight=0.79, relwidth=0.96)

        for c in columns:
            self.tree.heading(c, text=c)
            self.tree.column(c, width=163, minwidth=20, stretch=1)

        alta = Button(self.root, text='Alta', command=lambda: self.altaMod('Alta'))
        alta.place(relx=0.02, rely=0.85, height=25, width=50)
        baja = Button(self.root, text='Baja', command=self.borrar)
        baja.place(relx=0.1, rely=0.85, height=25, width=50)
        modificar = Button(self.root, text='Modificacion', command=self.modif)
        modificar.place(relx=0.18, rely=0.85, height=25, width=90)

        self.actualizar()

        self.root.mainloop()


    def modif(self):
        a = self.tree.selection()[0]
        id_socio = self.tree.item(a, 'values')[0]
        self.altaMod('Modificar', self.negocio.buscar(id_socio))
        self.actualizar()


    def borrar(self):
        for c in self.tree.selection():
            id_socio = self.tree.item(c, 'values')[0]
            self.negocio.baja(id_socio)
        self.actualizar()


    def actualizar(self):
        for c in self.tree.get_children():
            self.tree.delete(c)
        socios = self.negocio.todos()
        for s in socios:
            self.tree.insert('', 'end', text=s.id, values=(s.id, s.nombre, s.apellido, s.dni))


    def altaMod(self, titulo, socio=None):
        self.root2 = Tk()
        self.root2.title(titulo)

        lblId = Label(self.root2, text='ID', width=10)
        lblNombre = Label(self.root2, text='Nombre', width=10)
        lblApellido = Label(self.root2, text='Apellido', width=10)
        lblDni = Label(self.root2, text='DNI', width=10)

        self.varId = IntVar()
        self.varNombre = StringVar()
        self.varApellido = StringVar()
        self.varDni = IntVar()

        self.txtId = Entry(self.root2, textvariable=self.varId)
        self.txtNombre = Entry(self.root2, textvariable=self.varNombre)
        self.txtApellido = Entry(self.root2, textvariable=self.varApellido)
        self.txtDni = Entry(self.root2, textvariable=self.varDni)

        self.txtId.insert(0, getattr(socio, 'id', 0))
        self.txtNombre.insert(0, getattr(socio, 'nombre', ''))
        self.txtApellido.insert(0, getattr(socio, 'apellido', ''))
        self.txtDni.insert(0, getattr(socio, 'dni', 0))

        btnAceptar = Button(self.root2, text='Aceptar', command=self.aceptar)
        btnCancelar = Button(self.root2, text='Cancelar', command=self.root2.destroy)

        lblId.grid(column=1, row=1)
        lblNombre.grid(column=1, row=2)
        lblApellido.grid(column=1, row=3)
        lblDni.grid(column=1, row=4)
        self.txtId.grid(column=2, row=1)
        self.txtNombre.grid(column=2, row=2)
        self.txtApellido.grid(column=2, row=3)
        self.txtDni.grid(column=2, row=4)
        btnAceptar.grid(column=1, row=5)
        btnCancelar.grid(column=2, row=5)

        self.txtId.configure(state=DISABLED)

        if socio is None:
            self.accion = self.alta
        else:
            self.accion = self.modificar

        self.root2.mainloop()


    def aceptar(self):
        self.accion()
        self.actualizar()
        self.root2.destroy()


    def alta(self):
        socioAlta = Socio(nombre=self.txtNombre.get(), apellido=self.txtApellido.get(), dni=self.txtDni.get())
        try:
            self.negocio.alta(socioAlta)
        except DniRepetido as dr:
            self.error(dr)
        except LongitudInvalida as li:
            self.error(li)
        except MaximoAlcanzado as ma:
            self.error(ma)


    def modificar(self):
        socio = Socio(id=self.txtId.get(), dni=self.txtDni.get(), nombre=self.txtNombre.get(), apellido=self.txtApellido.get())
        self.negocio.modificacion(socio)


    def error(self, e):
        err = Tk()
        lblError = Label(err, text=e)
        lblError.pack()
        btnAceptar = Button(err, text='Aceptar', command=err.destroy)
        btnAceptar.pack()
        print(e)
        err.mainloop()


if __name__ == '__main__':
    a=PresentacionSocio()
