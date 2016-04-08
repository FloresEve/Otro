from Tkinter import *
from tkMessageBox import *
class al:
    def pri_alta(self):
        print

        root = Tk()
        root.title('Usuarios')
        colorfondo="white"
        colorletra="black"
        root.configure(background=colorfondo)
        root.geometry("500x200+300+50")
        no_label = Label(root,text="ID usuario :",font=("Arial",12),bg=colorfondo,fg=colorletra)
        no_label.grid(row=1,column=1)
        no_str = StringVar()
        no_entry = Entry(root,textvariable=no_str)
        no_entry.grid(row=1,column=2)
        # row 1 : the name
        nombre_label = Label(root,text="Nombre :",font=("Arial",12),bg=colorfondo,fg=colorletra)
        nombre_label.grid(row=2,column=1)
        nombre_str = StringVar()
        nombre_entry = Entry(root,textvariable=nombre_str)
        nombre_entry.grid(row=2,column=2)
        #row 2 : the last name
        email_label= Label(root,text="Email : ",font=("Arial",12),bg=colorfondo,fg=colorletra)
        email_label.grid(row=3,column=1)
        email_str = StringVar()
        email_entry = Entry(root,textvariable=email_str)
        email_entry.grid(row=3,column=2)
        #row 3 : the email
        tipo_label = Label(root,text="Tipo de usuario : ",font=("Arial",12),bg=colorfondo,fg=colorletra)
        tipo_label.grid(row=4,column=1)
        tipo__str = StringVar()
        tipo_entry = Entry(root,textvariable=tipo__str)
        tipo_entry.grid(row=4,column=2)

        def entrar():
            showinfo('Verificar', 'Guardado exitosamente')
            print
            id=no_entry.get()
            nombre=nombre_entry.get()
            email=email_entry.get()
            tip=tipo_entry.get()
            print nombre
            print  id
            print  email
            print tip
            import MySQLdb
            bd = MySQLdb.connect("localhost","root","123456","caliz" )
            cursor = bd.cursor()
            sql = "INSERT INTO usuario (ID,NOMBRE,EMAIL,TIPO  ) VALUES ('%s','%s','%s','%s')" %(id,nombre,email,tip)
            try:
                print
                cursor.execute(sql)
                bd.commit()
            except:
                bd.rollback()
                bd.close()
        #row 4 : end
        finish = Button(root,text="Guardar",command=entrar,font=("Arial",15),bg='black',fg="white")
        finish.grid(row=5,column=3)
        cancelar = Button(root,text="Cancelar",command=root.destroy,font=("Arial",15),bg='red',fg="white")
        cancelar.grid(row=5,column=4)
        root.mainloop()
