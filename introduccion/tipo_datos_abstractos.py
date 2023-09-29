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
