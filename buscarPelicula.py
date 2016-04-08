from Tkinter import * #importamos la libreria que contiene los graficos
from rentaPeliculas import ventanaRenta
import MySQLdb
obj=ventanaRenta()
class buscar:

    def inicio(self):
        def buscar(peli):
            query="select * from altapeliculas where NOMBRE='%s'" % peli
            datos=[DB_HOST, DB_USER, DB_PASS, DB_NAME]
            conn=MySQLdb.connect(*datos) #conectar a la base de datos
            print 'conectado'
            print query
            cursor=conn.cursor() #crear un cursor
            cursor.execute(query) #ejecutar una consulta
            if query.upper().startswith('SELECT'):
                data=cursor.fetchall() # Traer los resultados de un select
                for registro in data:
                     identificador = registro[0]
                     nombre = registro[1]
                     categoria = registro[2]
                     duracion = registro[3]
                     calidad = registro[4]
                     precio = registro[5]
                     estatus = registro[6]
                     print "nombre=%s, categoria=%s, duracion=%s, calidad=%s, precio=%s" % (nombre, categoria, duracion, calidad, precio)
            else:
                conn.commit() #Hacer efectiva la escritura de datos
                data=None
            cursor.close() #cerrar el cursor
            conn.close() #cerrar la conexion
            obj.ventanaRentar(identificador, nombre, categoria, duracion, calidad, precio, estatus)
            print data
        DB_HOST='localhost'
        DB_USER='root'
        DB_PASS='123456'
        DB_NAME='caliz'
        ventana=Tk() #En esta linea creamos nuestra ventana principal, la cual hereda todas las funciones de Tkinter
        ventana.title('Busca de pelicula')#Con esto agregamos titulo a la ventana
        ventana.geometry("800x300+300+50")
        colorfondo="white"
        colorletra="black"
        ventana.configure(background=colorfondo)
        #vamos a crear etiquetas
        labelBlanco1=Label(ventana,text=" ",font=("Arial",12),bg=colorfondo,fg=colorletra)# Creamos una etiqueta usuario, y le agregamos a la ventana
        labelBlanco1.grid(row=1,column=1)#Con esto le damos la ubicacion en que queremos la etiqueta el grid tiene 4 filas 5 columnas
        labelPeli=Label(ventana,text="Pelicula a Rentar",font=("Arial",12),bg=colorfondo,fg=colorletra)# Creamos una etiqueta usuario, y le agregamos a la ventana
        labelPeli.grid(row=1,column=2)#Con esto le damos la ubicacion en que queremos la etiqueta el grid tiene 4 filas 5 columnas
        labelBlanco2=Label(ventana,text="                 ",font=("Arial",12),bg=colorfondo,fg=colorletra)# Creamos una etiqueta usuario, y le agregamos a la ventana
        labelBlanco2.grid(row=1,column=3)#Con esto le damos la ubicacion en que queremos la etiqueta el grid tiene 4 filas 5 columnas
        labelMostrarPeli=Label(ventana,text="      Nombre de la pelicula: ",font=("Arial",12),bg=colorfondo,fg=colorletra)# Creamos una etiqueta usuario, y le agregamos a la ventana
        labelMostrarPeli.grid(row=2,column=1)#Con esto le damos la ubicacion en que queremos la etiqueta el grid tiene 4 filas 5 columnas
        pelicula=StringVar()
        txtPelicula=Entry(ventana,textvariable=pelicula,font=("Arial",12),bg=colorfondo,fg=colorletra)
        txtPelicula.grid(row=2,column=2)
        #En esta parte creamos botones de comando

        btnAceptar=Button(ventana,text="Aceptar",bg='black',fg="white",command=lambda:(buscar(txtPelicula.get())),font=("Arial",15))
        btnAceptar.grid(row=2,column=3)
        btnAceptar2=Button(ventana,text="Cancelar",bg='red', command=ventana.destroy,font=("Arial",15),)
        btnAceptar2.grid(row=2,column=4)
        labelEncabezado1=Label(ventana,text="      ",font=("Arial",12),bg=colorfondo,fg=colorletra)
        labelEncabezado1.grid(row=3,column=1)
        labelEncabezado2=Label(ventana,text="      ",font=("Arial",12),bg=colorfondo,fg=colorletra)
        labelEncabezado2.grid(row=3,column=2)
        labelEncabezado3=Label(ventana,text="      ",font=("Arial",12),bg=colorfondo,fg=colorletra)
        labelEncabezado3.grid(row=3,column=3)
        labelEncabezado4=Label(ventana,text="      ",font=("Arial",12),bg=colorfondo,fg=colorletra)
        labelEncabezado4.grid(row=3,column=4)
        labelEncabezado5=Label(ventana,text="      ",font=("Arial",12),bg=colorfondo,fg=colorletra)
        labelEncabezado5.grid(row=3,column=5)
        labelEncabezado6=Label(ventana,text="      ",font=("Arial",12),bg=colorfondo,fg=colorletra)
        labelEncabezado6.grid(row=3,column=6)
        labelEncabezado1=Label(ventana,text="   NOMBRE   ",font=("Arial",12),bg=colorfondo,fg=colorletra)
        labelEncabezado1.grid(row=4,column=1)
        labelEncabezado2=Label(ventana,text="   CATEGORIA   ",font=("Arial",12),bg=colorfondo,fg=colorletra)
        labelEncabezado2.grid(row=4,column=2)
        labelEncabezado3=Label(ventana,text="   DURACION   ",font=("Arial",12),bg=colorfondo,fg=colorletra)
        labelEncabezado3.grid(row=4,column=3)
        labelEncabezado4=Label(ventana,text="   CALIDAD   ",font=("Arial",12),bg=colorfondo,fg=colorletra)
        labelEncabezado4.grid(row=4,column=4)
        labelEncabezado5=Label(ventana,text="   PRECIO   ",font=("Arial",12),bg=colorfondo,fg=colorletra)
        labelEncabezado5.grid(row=4,column=5)
        labelEncabezado5=Label(ventana,text="   ESTATUS   ",font=("Arial",12),bg=colorfondo,fg=colorletra)
        labelEncabezado5.grid(row=4,column=6)
        i=4
        query="select * from altapeliculas"
        datos=[DB_HOST, DB_USER, DB_PASS, DB_NAME]
        conn=MySQLdb.connect(*datos) #conectar a la base de datos
        print 'conectado'
        print query
        cursor=conn.cursor() #crear un cursor
        cursor.execute(query) #ejecutar una consulta
        if query.upper().startswith('SELECT'):
            data=cursor.fetchall()
            for registro in data:
                i=i+1
                identificador = registro[0]
                nombre = registro[1]
                categoria = registro[2]
                duracion = registro[3]
                calidad = registro[4]
                precio = registro[5]
                estatus = registro[6]
                print "nombre=%s, categoria=%s, duracion=%s, calidad=%s, precio=%s" % (nombre, categoria, duracion, calidad, precio)
                labelEncabezado1=Label(ventana,text=nombre,font=("Arial",12),bg=colorfondo,fg=colorletra)
                labelEncabezado1.grid(row=i,column=1)
                labelEncabezado2=Label(ventana,text=categoria,font=("Arial",12),bg=colorfondo,fg=colorletra)
                labelEncabezado2.grid(row=i,column=2)
                labelEncabezado3=Label(ventana,text=duracion,font=("Arial",12),bg=colorfondo,fg=colorletra)
                labelEncabezado3.grid(row=i,column=3)
                labelEncabezado4=Label(ventana,text=calidad,font=("Arial",12),bg=colorfondo,fg=colorletra)
                labelEncabezado4.grid(row=i,column=4)
                labelEncabezado5=Label(ventana,text=precio,font=("Arial",12),bg=colorfondo,fg=colorletra)
                labelEncabezado5.grid(row=i,column=5)
                labelEncabezado5=Label(ventana,text=estatus,font=("Arial",12),bg=colorfondo,fg=colorletra)
                labelEncabezado5.grid(row=i,column=6)
        else:
              conn.commit() #Hacer efectiva la escritura de datos
              data=None
        cursor.close()
        conn.close()
        ventana.mainloop()#con esto se ejecuta la ventana