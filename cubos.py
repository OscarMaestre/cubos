#!/usr/bin/env python

class Cubo(object):
    def __init__(self, ancho, alto, profundo):
        self.ancho=ancho
        self.alto=alto
        self.profundo=profundo
        
        
    def get_superficie_frontal(self):
        return self.ancho*self.alto
    
    def get_superficie_lateral(self):
        return self.alto*self.profundo
    
    def get_superficie_superior(self):
        return self.ancho*self.profundo
    
    def get_superficie(self):
        sf=self.get_superficie_frontal()
        sl=self.get_superficie_lateral()
        ss=self.get_superficie_superior()
        
        return (2*sf)+(2*sl)+(2*ss)
    
    def __str__(self ):
        cadena="Ancho:   {0}\n".format(self.ancho)
        cadena+="Alto:    {0}\n".format(self.alto)
        cadena+="Profundo:{0}\n".format(self.profundo)
        return cadena
    
    
    def rotar(self, eje):
        if eje=="z":
            aux=self.ancho
            self.ancho=self.alto
            self.alto=aux
            return
        if eje=="y":
            aux=self.ancho
            self.ancho=self.profundo
            self.profundo=aux
            return
        aux=self.alto
        self.alto=self.profundo
        self.profundo=aux
    
    def get_mayor_arista(self):
        if self.profundo>self.alto and self.alto>self.ancho:
            return "profundo"
        if self.alto>self.profundo and self.profundo>self.ancho:
            return "alto"
        
c=Cubo(2,4,6)

print (c.get_superficie_frontal())
print (c.get_superficie_lateral())
print (c.get_superficie_superior())
print (c.get_superficie())
print (c)
c.rotar("z")
print (c)
c.rotar("z")
print (c)
c.rotar("y")
print (c)
c.rotar("y")
print (c)
c.rotar("x")
print (c)
c.rotar("x")
print (c)
print (c.get_mayor_arista())