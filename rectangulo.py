
class Point: #definimos el punto por dos coordenadas en el plano
  def __init__(self, x: float, y: float): 
    self.x = x
    self.y = y
  def redo(self,nx,ny):
    self.x = nx
    self.y = ny
class Line:
   def __init__(self, ps:Point, pe:Point): #definimos un segmento de recta con 2 puntos
      self.start = ps
      self.end = pe
      if (self.start.y == self.end.y):
         q ="recta horizontal"
      elif (self.start.x == self.end.x):
         q ="recta vertical"
      else:
         q = (self.start.y - self.end.y)/(self.start.x - self.end.x)
      self.slope= q #definimos la pendiente de la recta a la cual pertenece el segmento
   def lenght(self):
      return float(((self.end.x - self.start.x)**2 + (self.end.y - self.start.y)**2)**0.5) 
   def function(self,x:float)->float:
      if self.slope == "recta horizontal":
         if self.start.y == 0:
            return "horizontal en el origen"
         else: 
            return "horizontal fuera del origen"
      if self.slope == "recta vertical":
         if self.start.x == 0:
            return "vertical en el origen"
         else: 
            return "vertical fuera del origen"
      b= self.start.y - ((self.slope)*(self.start.x))
      f=self.slope*x + b #definimos los componentes para formar la ecuacion de la recta
      return f
   def vertical_cross(self):
      if self.function(self.start.x) == "vertical en el origen":
            print("interseca con el eje y en toda su longitud ")
      elif self.function(self.start.x) == "vertical fuera del origen":
          print( "la recta vertical no interseca con el eje y")
      else:
         for i in range (self.start.x, self.end.x):
            if self.function(i) == self.function(0):
             print("interseca con y en: ")
             return i
            else:
               print("no interseca con y")
   def horizontal_cross(self):
      if self.function(self.start.y) == "horizontal en el origen":
            print("interseca con el eje x en toda su longitud ")
      elif self.function(self.start.y) == "horizontal fuera del origen":
          print( "la recta horizontal no interseca con el eje x")
      else:
         n=False
         for i in range (self.start.y, self.end.y):
            if i==0:
               n=True
               f=i
         if n==True:
            print("interseca con x en: ")
            return f
         else:
            print("no interseca con x")
   def discretizador(self,n):
      i:float=self.start.x
      l:list=[]
      while i<=self.end.x:
         if self.slope == "recta horizontal":
            l.append(Point(i,self.function(i)))
         elif self.slope == "recta vertical":
            l.append(Point(self.start.x,i))
         else:
            l.append(Point(i, self.function(i)))
         i= i + n  
      return l    
class Rectangle:
   def __init__(self, lh: Line, lv: Line): #definimos el rectangulo con su linea horizontal superior y linea vertical izquierda
      if lh.slope != "recta horizontal":
         raise ValueError("la linea horizontal ingresada no es horizontal, ingrese una linea valida (la coordenada y de los puntos debe coincidir)")
      if lv.slope != "recta vertical":
         raise ValueError("la linea vertical ingresada no es vertical, ingrese una linea valida (la coordenada x de los puntos debe coincidir)")
      if lv.end.x != lh.start.x and lv.end.y != lh.start.y:
         raise ValueError("No se puede formar un rectangulo con las lineas dadas (es necesario que el punto final de la linea vetical coincida con el inicial de la horizontal)")
      self.largo = lv.lenght()   
      self.ancho = lh.lenght()
      self.centro= Point(x=(lh.start.x +self.ancho/2), y= (lv.start.y + self.largo/2))
      self.pex1 = Point(x=(self.centro.x - self.largo/2), y=(self.centro.y - self.ancho/2))
      self.pex2 = Point(x=(self.centro.x - self.largo/2), y=(self.centro.y + self.ancho/2))
      self.pex3 = Point(x=(self.centro.x + self.largo/2), y=(self.centro.y + self.ancho/2))
      self.pex4 = Point(x=(self.centro.x + self.largo/2), y=(self.centro.y - self.ancho/2))
   def area(self):
      return self.largo * self.ancho
   def perimeter(self):
       return 2 * (self.largo + self.ancho)
   def pointinter(self, p:Point)->bool:
      if (self.pex1.x <= p.x <= self.pex3.x) and (self.pex1.y <= p.y <= self.pex3.y):
         return True
      else:
         return False    
class square(Rectangle):
   def __init__(self, centro:Point, lado:float):
      super().__init__(centro = centro, largo = lado, ancho = lado)
if __name__ == "__main__":
   p1= Point(float(input("ingrese la coordenada en x del punto inicial de la linea horizontal")),float(input("ingrese la coordenada en y del punto inicial de la linea horizontal")))
   p2= Point(float(input("ingrese la cordenada en x del punto final de la linea horizontal")),float(input("ingrese la cordenada en y del punto final de la linea horizontal")))
   l1= Line(p1,p2)
   p3= Point(float(input("ingrese la coordeanda en x del punto inicial de la linea vertical (debe coincidir con el punto inicial de la linea horizontal)")),float(input("ingrese la coordeanda en y del punto inicial de la linea vertical")))
   p4= Point(float(input("ingrese la coordenada en x del punto final de la linea vertical (DEBE COINCIDIR CON EL PUNTO INICIAL DE LA LINEA HORIZONTAL)")),float(input("ingrese la coordenada en y del punto final de la linea vertical (DEBE COINICIDIR CON EL PUNTO INICIAL DE LA LINEA HORIZONTAL)")))
   l2= Line(p3,p4)
   for i in (l2.discretizador(1)):
      print(f"({i.x},{i.y})")
   r= Rectangle(l1,l2)
   print( r.area())
   print( r.perimeter())
   print( r.pointinter(Point(2,2)))