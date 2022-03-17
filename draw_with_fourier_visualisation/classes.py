class complex :
    def __init__(self,a,b):
        self.re = a
        self.im = b
    
    def __add__(self,other):
        return complex(self.re + other.re, self.im + other.im)
    
    def __mul__(self,other):
        return complex(self.re * other.re - self.im * other.im,
                       self.re * other.im + self.im * other.re) 
        
