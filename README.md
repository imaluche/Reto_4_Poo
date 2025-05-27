# Reto_4_Poo
----------------------------------
### 1 Ejercicio: Cree la clase forma y a partir de esta las clases triangulo y rectangulo y sus subclases
```python
from math import acos, degrees #importamos funciones matematicas necesarias para teoremas de triangulos
from rectangulo import Point, Line #heredamos de un ejercicio anterior 
class Shape: #creamos la clase base con los metodos mas generales
    def __init__(self,aristas:list):
        self.is_regular = False
        self._aristas = aristas
        self._vertices = []
        self._inner_angles = [] 
    def compute_perimeter(self): 
        return None
    def compute_area(self):
        return None
    def get_aristas(self):
        pass
    def get_vertices(self):
        pass
    def get_inner_angles(self):
        pass
class Rectangle(Shape): #hereda de shape
    def __init__(self, aristas:list):
        if len(aristas) != 2:
            raise ValueError("El rectangulo debe tener 4 vertices.") #se necesitan minimo 2 lineas para construir el rectangulo
        else:
            flag:bool = (aristas[0].slope == "recta vertical" and aristas[1].slope == "recta horizontal") and (aristas[0].end == aristas[1].start) #las lineas deben ser verticales u horziontales)
            if flag:
             super().__init__(aristas)
             self._aristas = self._aristas
             self.is_regular = True
             self.base = aristas[1]
             self.altura = aristas[0]
             self._vertices = [(aristas[0].start), aristas[0].end, aristas[1].end, Point((aristas[0].start.x) + (aristas[1].lenght()), aristas[0].start.y)] 
             self._inner_angles = [90, 90, 90, 90] #los angulos siempre son 90 grados
    def compute_perimeter(self):
        return 2 * (self.base.lenght() + self.altura.lenght())
    def compute_area(self):
        return self.base.lenght() * self.altura.lenght()
    def get_inner_angles(self):
        return self._inner_angles
    def get_aristas(self):
        return self._aristas
    def get_vertices(self):
        return self._vertices
class Square(Rectangle): #caso especifico del rectangulo
    def __init__(self, lado:Line):
        if len(lado) != 1:
            raise ValueError("Solo es necesario ingresar una linea recta para formar el cuadrado.") #solo se necesita una linea para formar un cuadrado
        else:
            flag:bool = lado[0].slope == "recta vertical" or lado.slope == "recta horizontal"
            if flag:
                ladob= Line(lado[0].end, Point(lado[0].end.x + lado[0].lenght(), lado[0].end.y))
                super().__init__([(lado[0]),ladob])
                self.__aristas = self._aristas
                self.__vertices = self._vertices
                self.__inner_angles = self._inner_angles
    def get_inner_angles(self):
        return self.__inner_angles
    def get_aristas(self):
        return self.__aristas
    def get_vertices(self):
        return self.__vertices
class Triangle(Shape):#hereda de shape
    def __init__(self, aristas: list):
        if len(aristas) != 3:
            raise ValueError("Un triangulo debe tener 3 lados coincidentes") #al menos se ncesitan 3 lineas
        else:
            super().__init__(aristas)
            self._lado1= aristas[0]
            self._lado2= aristas[1]
            self._lado3= aristas[2]
            self.is_regular = False
            self._aristas = aristas
            self._vertices = [aristas[0].start, aristas[1].start, aristas[2].start] #los vertices son 3 puntos que son inicios/finales de las lineas
            inner = []
            for i in aristas: #recorre todos los lados para formar todos los angulos internos
                b= 1
                c= 2
                if i == aristas[1]:
                    b= 0
                    c= 2
                if i == aristas[2]:
                    b= 0
                    c= 1 
                va= i.lenght()
                vb= self._aristas[b].lenght()
                vc= self._aristas[c].lenght()               
                teocos = (((va)**2)-((vb)**2)-((vc)**2))/(-2*(vb*vc)) #teorema del coseno
                ang = acos(teocos)
                inner.append(degrees(ang)) #añadimos el angulo
            self._inner_angles = inner
    def compute_perimeter(self):
        return self._lado1.lenght() + self._lado2.lenght() + self._lado3.lenght()
    def compute_area(self):
        s = self.compute_perimeter() / 2
        a = self._lado1.lenght()
        b = self._lado2.lenght()
        c = self._lado3.lenght()
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5 #formula de heron (no es necesaria la altura ni base)
        return area
    def get_aristas(self):
        return self._aristas
    def get_vertices(self):
        return self._vertices
    def get_inner_angles(self):
        return self._inner_angles
class Equilatero(Triangle): #caso especifico de triangulo, todos sus lados son iguales
    def __init__(self, lado:Line): #solo se necesita un lado
        if (lado.slope == "recta vertical" or lado.slope == "recta horizontal"):
            raise ValueError("Un triangulo equilatero debe tener 3 lados coincidentes y no ser rectos")
        else:
            lado2 = Line(lado.end, Point(2*(lado.end.x), lado.start.y))
            lado3= Line(lado.start, lado2.end)
            #construimos los demas lados a partir del original
            super().__init__([lado,lado2,lado3]) 
            self.is_regular = True #el unico triangulo regular
            self.__aristas = [lado, lado2, lado3]
            self.__vertices = [lado.start, lado.end, lado2.end]
            self.__inner_angles = self._inner_angles
    def get_aristas(self):
        return self.__aristas
    def get_vertices(self):
        return self.__vertices
    def get_inner_angles(self):
        return self.__inner_angles
class Isoceles(Triangle): #caso especifico, dos de sus lados son iguales
    def __init__(self, ladodoble:Line): #solo ingresamos una linea
        if ladodoble.slope == "recta vertical" or ladodoble.slope == "recta horizontal":
            raise ValueError("Un triangulo isoceles debe tener 3 lados coincidentes")
        else:
            ladoespejo = Line(ladodoble.end, Point(2*(ladodoble.end.x), ladodoble.start.y)) #construimos el segundo lado igual, conociendo ambos podemos definir el tercero
            super().__init__([ladodoble, ladoespejo, Line(ladodoble.start, ladoespejo.end)])
            self.__aristas = [ladodoble, ladoespejo, Line(ladodoble.start, ladoespejo.end)]
            self.__vertices = [ladodoble.start, ladodoble.end, ladoespejo.end]
            self.__inner_angles = self._inner_angles
    def get_aristas(self):
        return self.__aristas
    def get_vertices(self):
        return self.__vertices
    def get_inner_angles(self):
        return self.__inner_angles
    
class Escaleno(Triangle): #todos los lados diferentes
    def __init__(self, aristas: list):
        confirm :bool= aristas[0].lenght() != aristas[1].lenght != aristas[2].lenght()
        if len(aristas) != 3 or confirm == False:
            raise ValueError("Un triangulo escaleno debe tener 3 lados coincidentes y de diferente longitud")
        else:
            super().__init__(aristas)
            self.__aristas = self._aristas 
            self.__vertices = self._aristas
            self.__inner_angles = self._inner_angles
    def get_aristas(self):
        return self.__aristas
    def get_vertices(self):
        return self.__vertices
    def get_inner_angles(self):
        return self.__inner_angles
class Trirectangle(Triangle): #hay un angulo de 90 grados
    def __init__(self, aristas: list):
        if len(aristas) != 3 or (aristas[0].slope == "recta vertical" and aristas[1].slope == "recta horziontal"): #dos lados siempre seran rectos por el angulo de 90
            raise ValueError("Un triangulo trirectangulo debe tener 3 lados coincidentes y uno de ellos debe ser vertical y otro horizontal")
        else:
            super().__init__(aristas) 
            self.__aristas = self._aristas
            self.__vertices = self._aristas
            self.__inner_angles = self._inner_angles
    def get_aristas(self):
        return self.__aristas
    def get_vertices(self):
        return self.__vertices
    def get_inner_angles(self):
        return self.__inner_angles      
if __name__ == "__main__":
    p0= Point(0, 0)
    p1= Point(0, 4)
    p2= Point(-3, 0)
    l0= Line(p0, p1)
    l1= Line(p1, p2)
    l3 = Line(p2,p0)
    l : list = [l0, l1, l3]
    escal= Trirectangle(l)
    print(escal.compute_perimeter())
    print(escal.compute_area())
    print(escal._inner_angles)
    for i in escal._vertices:
        print(f"({i.x},{i.y})")
```
#### explicacion:
- Inicialmente importamos las clases linea, punto y la funcion coseno de un ejercicio hecho con anterioridad y el modulo math respectivamente
- Componemos la clase base "Forma" con los metodos y atributos basicos de cualquier forma que se quiera definir ademas de getters para los atributos importantes de la case
- Definimos rectangulos los cuales siempre tienen angulos de 90 y sus metodos son simples de medir, esto sera hereaddo por una clase cuadrado que no sera mas que una instancia de rectangulo usando una misma linea rotada para tener las 2 lineas necesarias del rectangulo
- De manera similar definimos la clase triangulo, usando esta vez el teorema del coseno y la formula de heron para areas de triangulos para obtener los angulso internos y area del triangulo respectivamente (con estos teoremas no es necesario reescribir los metodos para cada caso)
- Definimos los respectivos casos de triangulos, tomando en cuenta como se suponen que deben estar armados (los equilateros e isoceles solo necesitan un lado para definirse, los lados de los escalenos son diferentes entre si, los trirectangulos tienen 2 lados rectos)
- Hecho esto instanciamos una clase triangulo de prueba para comprobar que las clases funcionen adecuadamente
----------------------------------
### 2 Restaurante revisado
```python
class producto:
 def __init__(self, nombre, precio): #lo mas elemental
    self._nombre = nombre
    self._precio = precio
    self._tipo = "producto"
 def get_nombre(self):
    return self._nombre
 def get_precio(self):
    return self._precio
 def get_tipo(self):
    return self._tipo
 def pedido(ls:list,le:list,lb:list,lp:list,lps:list):
   def añadir_producto(ltest,lend): #secuencia para elegir la comida
    for i in range (len(ltest)):
      print(str(i+1)+ ". "+ str((ltest[i])._nombre))
    d = int(input("indique el numero que desea pedir: "))
    lend.append(ltest[d-1])
    return d
   lf = []
   flag = True
   print(f"bienvenido")
   while flag == True:
        print(f"que desea pedir? (1 para sopas, 2 para ensaladas, 3 para bebidas, 4 para plato central, 5 para postres)")
        opcion = int(input("opcion: "))
        if opcion == 1: 
           print("que sopa desea pedir? (en caso de pedirse ccon un plato central se recibira un descuneto unico del 5%)")
           añadir_producto(ls,lf)
        if opcion == 2: 
           print("que ensalada desea pedir? (en caso de pedirse con un plato central y una bebida se recibira un descuento unico del 5%)")
           q = añadir_producto(le,lf)
           c = (input("desea vinagreta? (si/no)"))
           if c == "si":
              le[q-1].vinagreta(b=True)
        if opcion == 3:
           print("que bebida desea pedir? (en caso de pedirse con un plato central y unna ensalada se aplicara un descuento unico del 5%)")
           q = añadir_producto(lb,lf)
           c = (input("desea hielo? (si/no)"))
           if c == "si":
              lb[q-1].hielo(b = True)
           if lb[q-1].jugo == True:
               c= (input("desea azucar? (si/no)"))
               if c == "si":
                  lb[q-1].azucar(b = True)
        if opcion == 4:
           print("que plato central desea pedir? (en caso de pedirse con una ensalada u una bebida o con una sopa se aplicara un descuento unico del 5%)")
           añadir_producto(lp,lf)
        if opcion == 5:
           print("que postre desea pedir?")
           añadir_producto(lps,lf)
        f=input("desea pedir algo mas? (si/no)")
        if f == "no":
           flag = False
           return lf
class sopas(producto): #las sopas son un producto
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self._tipo = "sopa"
class ensaladas(producto): #las ensaladas son un producto
    def __init__(self, nombre, precio, p:bool=False): #indiciador de poder llevar vinagreta
        super().__init__(nombre, precio)
        self._tipo = "ensalada"
        self.p = p
    def vinagreta(self, b:bool = False):
       if (self.p == False):
          print("esa ensalada no lleva vinagreta")
       if (b == False):
         print("sin vinagreta")
       if (b == True) and (self.p == True):
         print("con vinagreta")
         self._precio= self._precio + 50
class bebidas(producto): #las bebidas son un producto
    def __init__(self, nombre, precio, jugo:bool = False):
        self.jugo = jugo
        super().__init__(nombre, precio)
        self._tipo = "bebida"
        if self.jugo == True:
           def azucar(self, b:bool = False):
            if b == False:
                print("sin azucar")
            else:
                self._precio = self._precio + 50
    def hielo(self, b:bool = False):
       if b == False:
         print("sin hielo")
       else:
         self._precio = self._precio+50
class platocentral(producto): #los platos centrales son un producto
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self._tipo = "plato central"
class postres(producto): #los postres son un producto
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self._tipo = "postre"
class Mediodepago:
   def __init__(self, disponible: float):
      self._efectivodisponible = disponible
      self._mensaje= 0
   def pagar(self, total):
      if total <= self._efectivodisponible:
         self._efectivodisponible = self._efectivodisponible - total
         print("su pago fue realizado con exito" + str(self._mensaje))
      else:
         print("no tiene suficiente dinero para realizar la transaccion")
class Tarjeta(Mediodepago): #una tarjeta tiene como datos privados el numero,el saldo disponible y el codigo de seguridad
   def __init__(self, disponible: float, numero: str, codigo: str):
      super().__init__(disponible)
      self.__numero = numero
      self.__codigo = codigo
      self._mensaje = ", podra ver el saldo de su tarjeta en el recibo"
   def get_numero(self):
      return self.__numero
   def get_codigo(self):
      return self.__codigo
class Efectivo(Mediodepago): #el efectivo no tiene datos privados, mas sin embargo la cantidad de dinero que se tiene es privado
   def __init__(self, disponible: float):
      super().__init__(disponible)
      self._mensaje = ", acerquese a un cajero en caso de que su cambio no sea el aducuado"
   def get_efectivo_disponible(self):
      return self._efectivodisponible
class cuenta():
    def __init__(self,l:list, pago:Mediodepago):
        self.elementos= l
        self.pago = pago
    def total(self):
       t = False
       c = False
       e = False
       b = False
       s = False
       discount = False
       print(f"Gracias por su visita, sus compras fuerzon las siguientes:")
       for i in (self.elementos):
          print(i._nombre)
       for i in (self.elementos):
          if i._tipo == "plato central":
             c = True
          if i._tipo == "ensalada":
             e = True
          if i._tipo == "bebida":
             b = True
          if i._tipo == "sopa":
             s = True 
       fl = (c and e and b) or (s and c)
       if  fl == True:
          print("debido a la compra del conjunto de 2 o mas de los tipos de productos seleccionados usted recibira un" \
           "descuento unico del 5% en su compra total")
          discount = True     #se aplican descuentos dependiendo de la compra de ciertos productos
       for i in self.elementos:
          t = t + i._precio
       if discount == True:
          t = t - (t*0.05)
          print("su descuento es del 5%")
       print(f"su total es: {t}")
       prop=input("desea dejar propina? (si/no)")
       if prop == "si":
            propina = int(input("indique el porcentaje de propina que desea dejar: "))
            t = t + (t*propina/100)
            print(f"su total con propina es: {t}")
       else:
           print(f"su total es: {t}")
       self.pago.pagar(t)          
if __name__ == "__main__": 
   menu = producto("menu", 0)
   s1 = sopas("ajiaco", 6000)
   s2 = sopas ("mondongo", 5000)
   s3 = sopas ("sopa de mariscos", 7000)
   lsopas = [s1, s2, s3]
   e1 = ensaladas("ensalda cesar", 2000, p = True)
   e2 = ensaladas("guacamole", 1500)
   e3 = ensaladas("ensalada de la casa", 1000, p = True)
   lensaladas = [e1, e2, e3]
   b1 = bebidas("limonada", 5000, jugo = True)
   b2 = bebidas("cocacola", 4000)
   b3 = bebidas("agua", 2000)
   lbebidas = [b1, b2, b3]
   p1 = platocentral("bandeja paisa", 20000)
   p2 = platocentral("arroz con pollo", 18000)
   p3 = platocentral("churrasco", 25000)
   p4 = platocentral("sobrebarriga", 22000)
   lplatos = [p1, p2, p3, p4]
   pt1 = postres("milhoja", 5000)
   pr2 = postres( "copa de helado", 4000)
   pt3 = postres("torta de cumpleaños", 10000)
   lpostres = [pt1, pr2, pt3]
   tarjeta = Tarjeta(100000, "1234-87345", "2504")
   billetera = Efectivo(50000)
   r = producto.pedido(lsopas,lensaladas,lbebidas,lplatos,lpostres)
   cuenta1 = cuenta(r,tarjeta)
   cuenta1.total()   
```
#### explicacion:
- En la clase Producto se agregaron los respectivos getters para obtener los valores importantes de los productos (tipo, nombre y precio), metodos que seran heredados por cada tipo de producto
- Se crea una clase general que representar un medio de pago, el cual heredara a efectivo y tarjeta. De esta clase heredaran un metodo que permita pagar (adicionalmente se agregaran atributos protegidos dependiendo de la clase, como por ejemplo un codigo de seguridad y un saldo/dinero disponible)
- Dentro de la clase Cuenta se añadira un booleano que identificara el tipo de platos que fueron comprados para a base de identificar ciertas combinaciones aplicar un descuento unico
- Calculado el total se usara el metodo pagar de una instancia dada de medio de pago (efectivo o tarjeta), en caso de que el total no supere el saldo de la tarjeta permitira hacer la compra, en caso contrario se advertira que esto no fue posible
----------------------------------
