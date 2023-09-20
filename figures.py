from abc import ABC, abstractmethod
class Figura(ABC):
    @property
    @abstractmethod
    def area(self):
        pass
    
    @property
    @abstractmethod
    def perimetre(self):
        pass
    
class Cercle(Figura):
    def __init__(self,radi):
        self.aradi=radi
    
    @property
    def radi(self):
        return self.aradi
    
    @property
    def area(self):
        return 3.14*self.aradi**2
    
    @property
    def perimetre(self):
        return 2*3.14*self.aradi
    
class Rectangle(Figura):
    def __init__(self,base,altura):
        self.abase=base
        self.aaltura=altura
        
    @property
    def area(self):
        return self.abase*self.aaltura
    
    @property
    def perimetre(self):
        return 2*self.aaltura+2*self.abase
    
class Quadrat(Rectangle):
    def __init__(self,costat):
        super().__init__(costat,costat)
        
class Triangle(Figura):
    def __init__(self,costat):
        self.acostat=costat
        
    @property
    def area(self):
        return self.acostat**2*(3**0.5)/4
    
    @property
    def perimetre(self):
        return 3*self.acostat
    
cercle=Cercle(150)
triangle=Triangle(70)
rectangle=Rectangle(20,30)
quadrat=Quadrat(20)
print("Area del cercle",cercle.area)
print("Perimetre del cercle",cercle.perimetre)
print("Area del triangle",triangle.area)
print("Perimetre del triangle",triangle.perimetre)
print("Area del rectangle",rectangle.area)
print("Perimetre del rectangle",rectangle.perimetre)
print("Area del quadrat",quadrat.area)
print("Perimetre del quadrat",quadrat.perimetre)