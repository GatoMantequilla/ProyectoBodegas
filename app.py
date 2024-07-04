import json # Para trabajar con la gestión de archivos, primero tenemos que importar la librería JSON

class GESTION: # Luego de esto, se define la clase 'GESTION'
    @staticmethod
    def guardar_bodegas(bodegas, filename="bodegas.json"): # En la clase, se define una función para guardar bodegas en un archivo JSON destinado a ello
        with open(filename, "w") as file: # Esta función abrirá el archivo JSON definido para poder escribir en él
            json.dump([vars(b) for b in bodegas], file, indent = 4) # Luego guardará en el archivo cada atributo ingresado, dentro del archivo JSON

    @staticmethod
    def cargar_bodegas(filename="bodegas.json"): # Se define otra función en la misma clase, esta vez para mostrar las bodegas guardadas
        try:
            with open(filename, "r") as file: # La función intentará, si es que existe, abrir el archivo definido para leerlo
                bodegas_data = json.load(file) 
                return [BODEGAS(**data) for data in bodegas_data] # Luego la función devolverá todos los datos ingresados en el archivo abierto
        except (FileNotFoundError, json.JSONDecodeError):
            return [] # En el caso de que no haya archivo o haya algún error, en lugar de arrojar el código de error, el código simplemente devolverá algo vacío

class BODEGAS: # Luego se define otra clase, esta vez llamada 'BODEGAS'
    def __init__(self, identificador, capacidad, espacio_usado, productos):
        self.identificador = identificador
        self.capacidad = capacidad
        self.espacio_usado = espacio_usado
        self.productos = productos # Tras esto, se definen los atributos de esta clase, en este caso son cuatro

    def __str__(self): # Este método entregará la información de las bodegas en cadenas
        return f"Identificador:{self.identificador}, Capacidad:{self.capacidad}, Espacio usado:{self.espacio_usado}, Productos:{self.productos}"  

class PANEL_CONTROL: # Se define otra función llamada 'PANEL_CONTROL'
    def __init__(self):
        self.bodegas = GESTION.cargar_bodegas() # Esta función cargará las bodegas que se encuentran en la clase GESTIÓN 

    def buscar_bodega(self,identificador): # Se define dentro de esta clase, una función para buscar una bodega
        for bodega in self.bodegas:
            if bodega.identificador == identificador:
                return bodega # Si existe una bodega guardada cuyo parámetro de identificador es igual al que se ha ingresado, se devolverá esta bodega
            else:
                print("Bodega NO encontrada")
                return None # En otro caso, se devolverá un mensaje que dirá al usuario que no se encontró dicha bodega
            
    def crear_bodega(self,identificador,capacidad,espacio_usado,productos): # Se define una función para crear una nueva bodega
        nueva_bodega = BODEGAS(identificador,capacidad,espacio_usado,productos) # La nueva bodega será definida con los atributos de la clase BODEGAS
        self.bodegas.append(nueva_bodega) # Luego de haber ingresado todos los atributos, la nueva bodega es añadida
        GESTION.guardar_bodegas(self.bodegas) # Después de eso, la bodega ingresada es almacenada en la clase GESTION con la función de guardar bodegas
        print("Bodega creada con exito...") # Finalmente se imprime el mensaje de que la bodega ha sido creada

    def eliminar_bodega(self, identificador):
        bodega = self.buscar_bodega(identificador) #Se busca la bodega con este identificador
        if bodega: #Si la bodega existe
            self.bodegas.remove(bodega) #Se elimina la bodega de bodegas
            GESTION.guardar_bodegas(self.bodegas) #Se guardan los cambios hechos
            print("Bodega eliminada con éxito...") 

    @staticmethod
    def crear_objeto(): # Se define una función que crea un objeto nuevo
        identificador_obj = input("Ingrese el id: ")
        nombre = input("Ingrese el nombre del objeto: ")
        espacio_necesario = float(input("Ingrese el espacio necesario del objeto: "))
        cantidad = int(input('Ingrese la cantidad que desea añadir: '))
        if cantidad > 0 and espacio_necesario > 0:
            objeto = {"Identificador_obj": identificador_obj, "Nombre": nombre, "Espacio_necesario": espacio_necesario, 'Cantidad': cantidad} # Se crea el diccionario que contiene los parametros del objeto
            return objeto #Se devuelve en forma de diccionario
        else:
            print('Parámetros ingresados inválidos')

    def buscar_si_esta_obj_bodega(self, bodega, identificador_obj): # Se define una función que encuentre un objeto en una bodega
        lista = bodega.productos() # Los objetos dentro de la bodega se almacenan en una lista
        for obj in lista: # Luego, la lista es recorrida
            if obj.get("Identificador_obj") == identificador_obj: 
                return True # Si el identificador de un objeto es igual al que se ha ingresado para buscar, se devuelve el booleano 'Verdadero'
            else:
                return False # En caso contrario, se devuelve el valor 'Falso'

    def buscar_obj_bodega(self, bodega, identificador_obj): # Se define una función que busque un objeto dentro de una bodega
        lista = bodega.productos # Al igual que en el caso anterior, los productos de la bodega se almacenan en una lista
        for obj in lista:
            if obj.get("Identificador_obj") == identificador_obj: # La lista es recorrida, y si hay un objeto con el mismo identificador que el ingresado, se devolverá ese objeto
                return obj
            else:
                print("Este objeto no se encuentra en esta bodega") # En caso contrario, se devolverá al usuario el mensaje de que el objeto no está en la bodega
                return False

    def evaluar_espacio(self, cantidad, bodega, objeto): # Se define una función que evalúa el espacio de la bodega
        espacio_necesario = objeto["Espacio_necesario"] * cantidad # El espacio necesario se calculará como el espacio necesario que el objeto requiere multiplicado por la cantidad de objetos
        espacio_disponible = float(bodega.capacidad) - float(bodega.espacio_usado) # El espacio disponible restará los espacios total y usado convertidos a valores numéricos
        if espacio_disponible >= espacio_necesario:
            return True # Si el espacio disponible es mayor o igual al requerido, se agregará el producto
        else:
            print("Espacio insuficiente...") # En caso de que no, se avisará al usuario de que el espacio no es suficiente para realizar esta acción
            return False
        
    def redefinir_espacio_suma(self, cantidad, bodega, objeto): # Se define la función que redefine el espacio que queda (esta vez suma)
        espacio_a_agregar = objeto["Espacio_necesario"] * cantidad # Se define el espacio que se quiere agregar como el espacio que necesita el objeto multiplicado por la cantidad de objetos que se van a añadir
        bodega.espacio_usado = float(bodega.espacio_usado) + float(espacio_a_agregar) # Entonces el espacio usado es igual al espacio usado antes de esta suma más el espacio que se va a ocupar

    def redefinir_espacio_resta(self, cantidad, bodega, objeto): # Se define la función que redefine el espacio que queda (esta vez resta)
        espacio_a_restar = objeto["Espacio_necesario"] * cantidad  #El espacio que quitaremos sera el espacio del objeto por cuantos estamos quitando
        bodega.espacio_usado = float(bodega.espacio_usado) - float(espacio_a_restar) #Espacio usado - espacio que usaban los objetos que estamos quitando = espacio restante

    def agregar_objeto(self, identificador):
        objeto = self.crear_objeto() #Llamamos a esta funcion para crear el diccionario que define al objeto
        bodega = self.buscar_bodega(identificador) #Buscamos la bodega con ese identificador
        cantidad = objeto['Cantidad'] #La cantidad a agregar sera la cantidad predefinida antes dentro del objeto
        if self.evaluar_espacio(cantidad, bodega, objeto): #(NO SUFICIENTE = FALSE, SUFICIENTE = TRUE)
            if self.buscar_obj_bodega(bodega, objeto): #Se busca el obj en la bodega
                decision = input(f"El objeto de nombre {objeto['Nombre']} ya existe en esta bodega. ¿Desea agregar más cantidad del mismo? (Y/N): ") #Si ya existe se pregunta si se quiere agregar más
                if decision.upper() == "Y":
                    self.redefinir_espacio_suma(cantidad, bodega, objeto) #Redefine espacio
                    print("Objeto redefinido en la bodega exitosamente...")
            else:
                bodega.productos.append(objeto)  # Se agrega el objeto a la lista de productos de la bodega
                self.redefinir_espacio_suma(cantidad, bodega, objeto) # Añade el espacio usado por esta cantidad de objeto
                GESTION.guardar_bodegas(self.bodegas)  # Luego, se guardan los cambios en el archivo JSON
                print("Su objeto ha sido agregado a la bodega exitosamente...")

    def eliminar_objeto(self, Identificador, Identificador_obj):
        bodega = self.buscar_bodega(Identificador) #Se busca bodega
        objeto = self.buscar_obj_bodega(bodega, Identificador_obj) #Se busca objeto en la bodega
        if objeto and bodega: #Si existe objeto y bodega
            bodega.productos.remove(objeto) #Se quita
            cantidad = objeto['Cantidad']
            self.redefinir_espacio_resta(cantidad, bodega, objeto) #Quitamos el espacio que utilizaba
            GESTION.guardar_bodegas(self.bodegas) #Guardamos
            print(f"El objeto {objeto['Nombre']} ha sido eliminado de la bodega")

    def mostrar_bodega(self, identificador):
        bodega = self.buscar_bodega(identificador) #Buscamos bodega y se imprimen sus valores
        print(f"Id: {bodega.identificador}")
        print(f"Capacidad: {bodega.capacidad}")
        print(f"Espacio usado: {bodega.espacio_usado}")
        print(f'Productos: {bodega.productos}')

    def mostrar_bodegas(self):
        for bodega in self.bodegas: #Iteramos mostrar_bodega para mostrar todas las bodegas
            print(f"Id: {bodega.identificador}")
            print(f"Capacidad: {bodega.capacidad}")
            print(f"Espacio usado: {bodega.espacio_usado}")
            print(f'Productos: {bodega.productos}')

    def mostrar_productos_bodega(self, identificador): #Iteramos mostrar_producto_bodega para mostrar todos los productos de la bodega
        bodega = self.buscar_bodega(identificador)
        print(f"{bodega.productos}")

    def mostrar_producto_bodega(self, identificador, identificador_obj): 
        bodega = self.buscar_bodega(identificador) #Buscamos bodega 
        objeto = self.buscar_obj_bodega(bodega,identificador_obj) #Producto en bodega
        if objeto and bodega: #Si existe objeto y bodega se imprimen los valores del producto
            print(f"Id: {objeto['identificador_obj']}")
            print(f"Nombre: {objeto['Nombre']}")
            print(f"Espacio por unidad: {objeto['Espacio_necesario']}")
            print(f"Cantidad: {objeto['Cantidad']}")

    def cambiar_cantidad_objeto(self, identificador, identificador_obj):
        bodega = self.buscar_bodega(identificador) #Buscamos bodega
        objeto = self.buscar_obj_bodega(bodega,identificador_obj) #Buscamos bodega 
        if objeto and bodega: #Si existe objeto y bodega se pide la cantidad
            print(f"Actualmente en esta bodega hay {objeto['Cantidad']} de {objeto['Nombre']}")
            cantidad = int(input("¿A que cantidad desea cambiarlo?: ")) 
            if cantidad < 0: #Se revisa si es una cantidad valida (No puede ser menor a 0 o 0)
                print("Dato ingresado invalido")
            else:
                if self.evaluar_espacio(cantidad, bodega, objeto): #Se evalua el espacio si es suficiente
                    total = objeto['Cantidad']
                    self.redefinir_espacio_resta(total, bodega, objeto) #Se quita el espacio utilizado por la cantidad anterior
                    self.redefinir_espacio_suma(cantidad, bodega, objeto) #Se suma el espacio utilizado por la cantidad nueva
                    objeto['Cantidad'] = cantidad 
                    GESTION.guardar_bodegas(self.bodegas) #Se guardan los cambios
                    print("Su objeto ha sido redefinido exitosamente....")

def dar_opciones():
    print(" ")
    print(" ")
    print("..................................................")
    print(" ")
    print(" ")
    print("Ingrese la opcion que desee trabajar:")
    print("1. Crear bodega")
    print("2. Eliminar bodega")
    print("3. Mostrar información de una bodega")
    print("4. Mostrar información de todas las bodegas")
    print("5. Mostrar información de un producto")
    print("6. Mostrar información de productos")
    print("7. Cambiar cantidad de un producto")
    print("8. Agregar producto a una bodega")
    print("9. Eliminar producto")
    print('0. Terminar programa')
    eleccion = int(input("Ingrese su elección: "))
    return eleccion
    
def menu():

    Panel_Control = PANEL_CONTROL()

    while True:
        eleccion = dar_opciones()
        if eleccion == 1:
            productos = []
            espacio_usado = 0
            identificador = input("Ingrese su id: ")
            capacidad = int(input("Ingrese su capacidad: "))
            Panel_Control.crear_bodega(identificador,capacidad,espacio_usado,productos)

        elif eleccion == 2:
            identificador = input("Ingrese el id de la bodega: ")
            Panel_Control.eliminar_bodega(identificador)

        elif eleccion == 3:
            identificador = input("Ingrese el id de la bodega: ")
            Panel_Control.mostrar_bodega(identificador)

        elif eleccion == 4:
            Panel_Control.mostrar_bodegas()

        elif eleccion == 5:
            identificador_bodega = input("Ingrese el id de la bodega: ")
            identificador_obj = input("Ingrese el id de su objeto: ")
            Panel_Control.mostrar_producto_bodega(identificador_bodega,identificador_obj)

        elif eleccion == 6:
            identificador = input("Ingrese el id de la bodega: ")
            Panel_Control.mostrar_productos_bodega(identificador)

        elif eleccion == 7:
            identificador_bodega = input("Ingrese el id de la bodega: ")
            identificador_obj = input("Ingrese el id de su objeto: ")
            Panel_Control.cambiar_cantidad_objeto(identificador_bodega,identificador_obj)

        elif eleccion == 8:
            identificador_bodega = input("Ingrese el id de la bodega: ")
            Panel_Control.agregar_objeto(identificador_bodega)

        elif eleccion == 9:
            identificador_bodega = input("Ingrese el id de la bodega: ")
            identificador_obj = input("Ingrese el id de su objeto: ")
            Panel_Control.eliminar_objeto(identificador_bodega, identificador_obj)

        elif eleccion == 0:
            print("Programa terminado")
            break

        else:
            print("Elección no valida")        

        
#########################################################################################################################

menu()

