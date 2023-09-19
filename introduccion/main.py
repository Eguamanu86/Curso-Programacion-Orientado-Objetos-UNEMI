from tipo_datos_abstractos import Tad
from model.cliente import Cliente

tad = Tad(5)
tad.cargar_vector()
tad.cargar_matriz()

cliente1 = Cliente('09264006151','Ernesto','Guaman', 'Milagro', 1000)
cliente2 = Cliente('09899998887','Juan','Perez', 'Cuenca', 500)

tad.apilar(cliente1)
tad.apilar(cliente2)

tad.presentar_pila()
