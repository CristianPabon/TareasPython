from tkinter import *

Pestaña = Tk()
Pestaña.geometry("400x300")
Pestaña.title('Trabajo Tkinter')
Pestaña.config(bg='blue')

lb1 = Label(Pestaña, text = 'Ejemplo de Tkinter', bg ='white', font = 'Times 15')
lb1.pack()

def Comando():
  Iniciar = 'Gracias por por presionar el botón, muy amable'
  lb2 = Label(Pestaña, text = Iniciar, font = 'Times 15').pack()

Bt1 = Button(
  Pestaña,
  text='Iniciar',
  command = Comando
)
Bt1.pack()

Pestaña.mainloop()