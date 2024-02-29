class Motocicleta ():

    #atributos generales de la clase motopcicleta
    estado = "nueva"
    motor = False

    # metodo contructor conn los distintros atributos especificos

    def __init__(self , color , matricula , combustible_litros , numero_ruedas , marca , modelo , fecha_fabricacion , velocidad_punta , peso) :
        
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso



    # metodos de la motocicleta

    def arrancar(self) :
        
        if self.motor :
            print(f"el motor va a empezar a arrancar")

        else :
            print(f"el motor ya esta en funcionamiento")



    def detener(self):

        if self.motor:
            print(f"el motor se va a detener en estos momentos")

        else :
            print(f" el motor ya se encuentra detenido")


motocicleta1 = Motocicleta("rojo" , "xs34" , 10 , 2 , "honda" , "XR150" , 3/6/2019 , "230KM/H" , "250kg")

motocicleta1.detener()
print(motocicleta1.marca)
        
    