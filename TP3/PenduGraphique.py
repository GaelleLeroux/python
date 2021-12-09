from tkinter import Image, PhotoImage, Tk, Label, Button,Canvas,Entry
import os
import EclatementPendule as p

mw= Tk()
mw.title("Pendu")
mw['bg']='bisque'


txt1=Label(mw,text="cc")
entry1=Entry(mw)

#ButtonQuit=Button(mw,text="Quitter",command=mw.destroy)
#ButtonQuit.pack()



can1=Canvas(mw,width=300,height=300)
path = os.path.join(os.path.dirname(__file__), "bonhomme1.gif")
photo=PhotoImage(file=path)
items=can1.create_image(150,150,image=photo)

ButtonLancer=Button(mw,text="Lancer le jeu",command=p.pendu)
ButtonLancer.grid(row=2)



txt1.grid(row=1,sticky='E')
can1.grid(row=1,column=3,rowspan=3,padx=10,pady=5,sticky='news')






mw.mainloop()

