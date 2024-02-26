

from tkinter import *
from tkinter import messagebox


Raiz_SumaDados = Tk()
Raiz_SumaDados.title("SUMA DE TRES DADOS Y PROBABILIDADES  ")

#-----------METODO GET para obtener la variable de lña caja de texto




#--------------------------variables globales

global suma_dados     
global contador1 
global contador2 
global proba_sumadados

#------------------------------------------------------------

def Probabilidad_Dados ():
    
    contador1 = 0
    contador2 = 0
    proba_sumadados = 0
    for i in range(1 , 7):
        for j in range(1 ,7 ):
                suma_dados = i + j 

                if suma_dados == entry1.get():
                     contador1 += 1

                     proba_sumadados = contador1 / 36
                     
                


                else:  contador2 += 1

        
                print("ESTAS SON PRUEBS PARA SUBIR A GITHUB")
                    
    label3.config(text=proba_sumadados)
        

    
    # solo envia el ultimo resultado de la suma de dados
#-------------------------------------------------funcion suma de dados para mostar



def suma_Dedados () :
    for i in range(1 , 7):
        for j in range(1 ,7 ):
                suma_dados = i + j 
                label2.config( text=int(suma_dados) ) 
                print(suma_dados)
                 





#---------------------------------------------------------------------------
frame1 = Frame()
frame1.config(width=200 , height=200)
frame1.grid(row=0 , column=0)
frame1.config(bg="yellow")


frame2 = Frame()
frame2.config(width=200 , height=200)
frame2.grid(row=0 , column=1)
frame2.config(bg="red")


frame3 = Frame()
frame3.config(width=200 , height=200)
frame3.grid(row=1 , column=1)
frame3.config(bg="blue")

frame4 = Frame()
frame4.config(width=200 , height=200)
frame4.grid(row=0 , column=4)
frame4.config(bg="green")


frame5 = Frame()
frame5.config(width=200 , height=200)
frame5.grid(row=1 , column=4)
frame5.config(bg="pink")
##--------------------------------------------------------------------


label1 =Label()
label1.config(text="  LA SUMA DE LOS DADOS SON :  "  )
label1.grid(row=0 , column=2)



entry1 =Entry()
entry1.config()
entry1.grid(row=0 , column=3)




boton1 = Button(Raiz_SumaDados , text= " PRESIONA , SUMA DE DADOS ES :" ,  padx= 50 , pady= 50 , command=suma_Dedados)
boton1.grid( row=1 , column=2 )


valor=""
boton2 = Button(Raiz_SumaDados , text= " PRESIONA ,LA PROBABILIDAD DE SUMA ES :" ,  padx= 50 , pady= 50 , command=Probabilidad_Dados )
boton2.grid( row=2 , column=2 )







label2 = Label(Raiz_SumaDados  )
label2.config() #falta aplicar que los resultados lleguen a este label etiqueta
label2.grid(row=1 , column=3)


label3 = Label(Raiz_SumaDados  )
label3.config() #falta aplicar que los resultados lleguen a este label etiqueta
label3.grid(row=2 , column=3)


Raiz_SumaDados.mainloop()

