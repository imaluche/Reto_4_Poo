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
   
   
