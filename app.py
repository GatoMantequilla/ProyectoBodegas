class GESTION:
    @staticmethod
    def guardar_bodegas(bodegas, filename="bodegas.json"):
        with open(filename, "w") as file:
            json.dump([vars(b) for b in bodegas], file)

    @staticmethod
    def cargar_bodegas(filename="bodegas.json"):
        try:
            with open(filename, "r") as file:
                bodegas_data = json.load(file)
                return [Bodega(**data) for data in bodegas_data]
        except FileNotFoundError:
            return []

class BODEGAS:
    def __main__(self, identificador, capacidad, espacio_usado, productos):
        self.identificador = int(identificador)
        self.capacidad = int(capacidad)
        self.espacio_usado = 0 
        self.productos = []

    def buscar_bodega(self,identificador):
        for bodega in self.bodegas:
            if bodega.identificador == identificador:
                return bodega
            else:
                print("Bodega NO encontrada")
                return None

    def __str__(self):
        return f"Identificador:{self.identificador}, Capacidad:{self.capacidad}, Espacio usado:{self.espacio_usado}, Productos:{self.productos}"  

class PANEL_CONTROL:
    def __init__():
        self.bodegas = GESTION.cargar_bodegas()

    def crear_bodega():
        identificador = input("Ingrese su id: ")
        capacidad = input("Ingrese su capacidad: ")
        nueva_bodega = BODEGAS(identificador, capacidad)
        self.bodegas.append(nueva_bodega)
        GESTION.guardar_bodegas(self.bodegas)
        Print("Bodega creada con exito...")

    def eliminar_bodega(identificador):
        bodega = BODEGAS.buscar_bodega(Identificador)
        if bodega:
            self.bodegas.pop(nueva_bodega)
            GESTION.guardar_bodegas(self.bodegas)

    @staticmethod
    def crear_objeto():
        identificador_obj = input("Ingrese el id: ")
        nombre = input("Ingrese el nombre del objeto: ")
        espacio_necesario = float(input("Ingrese el espacio necesario del objeto: "))
        cantidad = int(input("Ingrese la cantidad de este objeto: "))
        objeto = {"Identificador_obj": identificador_obj, "Nombre": nombre, "Espacio_necesario": espacio_necesario}
        return objeto

    def buscar_si_esta_obj_bodega(self, bodega, objeto):
        lista = bodega.productos()
        for obj in lista:
            if obj.get("identificador_obj") == identificador_obj:
                return True
            else:
                return False

    def buscar_obj_bodega(self, bodega, identificador_obj):
        lista = bodega.productos
        for obj in lista:
            if obj.get("identificador_obj") == identificador_obj:
                return obj
            else:
                print("Este objeto no se encuentra en esta bodega")
                return False

    def evaluar_espacio(self, cantidad, bodega, objeto):
        espacio_necesario = objeto["Espacio_necesario"] * cantidad
        espacio_disponible = bodega.capacidad - bodega.espacio_usado
        if espacio_disponible >= espacio_necesario:
            return True
        else:
            print("Espacio insuficiente...")
            return False
        
    def redefinir_espacio_suma(self, cantidad, bodega, objeto):
        espacio_a_agregar = objeto["Espacio_necesario"] * cantidad
        bodega.espacio_usado = bodega.espacio_usado + espacio_a_agregar

    def redefinir_espacio_resta(self, cantidad, bodega, objeto):
        espacio_a_restar = objeto["Espacio_necesario"] * cantidad
        bodega.espacio_usado = bodega.espacio_usado - espacio_a_restar       

    def agregar_objeto(self, Identificador):
        bodega = BODEGAS.buscar_bodega(Identificador)
        objeto = crear_objeto()
        if evaluar_espacio(cantidad, bodega, objeto):
            if buscar_obj_bodega(bodega, objeto):
                decision = input(f"El objeto de nombre {objeto['nombre']} ya existe en esta bodega ¿Desea agregar más cantidad del mismo?")
                if decision == "Y":
                    redefinir_espacio_suma(cantidad, bodega, objeto)
                    print("Su objeto redefinido en la bodega exitosamente...")
            else:
                redefinir_espacio(cantidad, bodega, objeto)
                print("Su objeto ha sido agregado a la bodega exitosamente...")
                bodega.productos.append(objeto)

    def eliminar_objeto(self, Identificador, Identificador_obj):
        bodega = BODEGAS.buscar_bodega(Identificador)
        objeto = buscar_obj_bodega(bodega, identificador_obj)
        if objeto:
            bodega.pop(objeto)
            cantidad = objeto['cantidad']
            redefinir_espacio_resta(cantidad, bodega, objeto)
            print(f"El objeto {objeto['nombre']} ha sido eliminado de la bodega")

    def mostrar_bodega(self, identificador):
        bodega = BODEGAS.buscar_bodega(identificador)
        print(f"Id: {bodega.identificador}")
        print(f"Capacidad: {bodega.capacidad}")
        print(f"Espacio usado: {bodega.espacio_usado}")
        for objeto in bodega.productos:
            print(f"-> {objeto['nombre']} ({objeto['cantidad']}))")

    def mostrar_bodegas(self):
        for bodega in self.bodegas:
            print(f"Id: {bodega.identificador}")
            print(f"Capacidad: {bodega.capacidad}")
            print(f"Espacio usado: {bodega.espacio_usado}")
            for objeto in bodega.productos:
                print(f"-> {objeto['nombre']} ({objeto['cantidad']}))")

    def mostrar_productos_bodega(self, identificador):
        bodega = BODEGAS.buscar_bodega(identificador)
        for objeto in bodega.productos:
            print(f"-> {objeto['nombre']} ({objeto['cantidad']}))")

    def mostrar_producto_bodega(self, identificador, identificador_obj):
        bodega = BODEGAS.buscar_bodega(identificador)
        objeto = buscar_obj_bodega(bodega,identificador_obj)
        if objeto:
            print(f"Id: {objeto['identificador_obj']}")
            print(f"Nombre: {objeto['nombre']}")
            print(f"Espacio por unidad: {objeto['espacio_necesario']}")
            print(f"Cantidad: {objeto['cantidad']}")

    def cambiar_cantidad_objeto(self, identificador, identificador_obj):
        bodega = BODEGAS.buscar_bodega(identificador)
        objeto = buscar_obj_bodega(bodega,identificador_obj)
        if objeto:
            print(f"Actualmente en esta bodega hay {objeto['cantidad']} de {objeto['nombre']}")
            cantidad = int(input("¿A que cantidad desea cambiarlo?"))
            if cantidad < 0:
                print("Dato ingresado invalido")
            else:
                if evaluar_espacio(cantidad, bodega, objeto):
                    total = objeto['cantidad']
                    redefinir_espacio_resta(total, bodega, objeto)
                    redefinir_espacio_suma(cantidad,bodega,objeto)
                    print("Su objeto ha sido redefinido exitosamente....")


def dar_opciones():
    print("Ingrese la opcion que desee trabajar:")
    print("1. Crear bodega")
    print("2. Eliminar bodega")
    print("3. Mostrar información de una bodega")
    print("4. Mostrar información de todas las bodegas")
    print("5. Mostrar información de un producto")
    print("6. Mostrar información de productos")
    print("7. Cambiar cantidad de un producto")
    print("8. Agregar producto a una bodega")
    print("9. Terminar programa")
    eleccion = int(input("Ingrese su elección: "))
    return eleccion
    
def menu():
    while True:
        eleccion = dar_opciones()
        if eleccion == 1:
            PANEL_CONTROL.crear_bodega()

        elif eleccion == 2:
            identificador = input("Ingrese el id de la bodega: ")
            PANEL_CONTROL.eliminar_bodega(identificador)

        elif eleccion == 3:
            identificador = input("Ingrese el id de la bodega: ")
            PANEL_CONTROL.mostrar_bodega(identificador)

        elif eleccion == 4:
            PANEL_CONTROL.mostrar_bodegas()

        elif eleccion == 5:
            identificador_bodega = input("Ingrese el id de la bodega: ")
            identificador_obj = input("Ingrese el id de su objeto: ")
            PANEL_CONTROL.mostrar_producto_bodega(identificador_bodega,identificador_obj)

        elif eleccion == 6:
            identificador = input("Ingrese el id de la bodega: ")
            PANEL_CONTROL.mostrar_productos_bodega(identificador)

        elif eleccion == 7:
            identificador_bodega = input("Ingrese el id de la bodega: ")
            identificador_obj = input("Ingrese el id de su objeto: ")
            PANEL_CONTROL.cambiar_cantidad_objeto(identificador_bodega,identificador_obj)

        elif eleccion == 8:
            identificador_bodega = input("Ingrese el id de la bodega: ")
            PANEL_CONTROL.agregar_objeto(identificador_bodega)

        elif eleccion == 9:
            Print("Programa terminado")
            break

        else:
            print("Elección no valida")        

        
#########################################################################################################################

menu()

