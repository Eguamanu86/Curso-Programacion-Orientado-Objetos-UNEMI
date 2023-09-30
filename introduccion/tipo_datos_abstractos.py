import random

import json

class Tad: # Clase Tipo de datos abstractos

    random_max = 10

    def __init__(self, tope):
        self.tope = tope

        self.vector = []
        self.matriz = []

        self.pila = []
        self.cola = []

        self.dic_intervalos_tarifas = {}

    def cargar_vector(self):
        for i in range(self.tope):
            numero = random.randrange(self.random_max)
            self.vector.append(numero)


    def cargar_matriz(self):
        for i in range(self.tope):
            self.matriz.append([])
            for j in range(self.tope):
                numero = random.randrange(self.random_max)
                self.matriz[i].append(numero)


    def apilar(self, objeto):
        if len(self.pila) <= self.tope:
            self.pila.append(objeto)
            return True
        return False

    def desapilar(self):
        if len(self.pila) >= 0:
            return self.pila.pop()
        return None


    def encolar(self, objeto):
        if len(self.cola) <= self.tope:
            self.cola.append(objeto)
            return True
        return False

    def desencolar(self):
        if len(self.cola) >= 0:
            return self.cola.pop(0)
        return None


    def presentar_pila(self):
        for c in self.pila:
            print(c)


    def presentar_cola(self):
        for c in self.cola:
            print(c)


    def cargar_rango_intervalos_tarifas(self):
        f = open('introduccion/rango-intervalos-tarifas.json')
        self.dic_intervalos_tarifas= json.load(f)
        #print(self.dic_intervalos_tarifas)


    def get_buscar_precio_para_peso(self, peso):
        list_keys = list(self.dic_intervalos_tarifas.keys())

        list_keys_orden =  self.orden_por_seleccion(list_keys)

        key = self.get_key_por_peso(peso, list_keys_orden)
        value = self.dic_intervalos_tarifas[key]

        return value


    def get_key_por_peso(self, peso, list_keys_orden):
        menores_al_peso = list (filter(lambda x: float(x) <= peso, list_keys_orden))
        return menores_al_peso.pop()

    def orden_por_burbuja(self, arreglo):
        n = len(arreglo)
        for i in range(n-1):       # <-- bucle padre
            for j in range(n-1-i): # <-- bucle hijo
                if float(arreglo[j]) > float(arreglo[j+1]):
                    arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
        return arreglo

    def orden_por_seleccion(self, arreglo):
        for i in range(len(arreglo) - 1):   # <-- bucle padre
            menor = i # primer elemento por default será el mínimo
            for j in range(i + 1, len(arreglo)): # <-- bucle hijo
                if float(arreglo[j]) < float(arreglo[menor]):
                    menor = j
            if menor != i:
                arreglo[menor], arreglo[i] = arreglo[i], arreglo[menor]
        return arreglo
