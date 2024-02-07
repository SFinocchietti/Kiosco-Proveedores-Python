import mariadb
import random
import datetime

def generar_numero_remito():
    return random.randint(20, 40) #genera numeros aleatorios para los remitos
lista_nuevos_productos = []
mydb = mariadb.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    autocommit=True
)

#<== creo la BD
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE KIOSCO") 

#<== me conecto a la BD
mydb = mariadb.connect(
    host = "127.0.0.1",
    user = "root",
    password = "root",
    database = "KIOSCO"
)


#<== creacion de tablas
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Proveedor (cuit INT PRIMARY KEY, nombre_proveedor VARCHAR (255), descripcion_producto ENUM('Bebida','Alfajores','Caramelos','Panchos', 'Cigarrillos'), direccion VARCHAR(255), telefono INT, situacion_iva VARCHAR(255) ,estado ENUM('Alta', 'Suspendido'))")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Articulo (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR (255), descripcion_producto ENUM('Bebida','Alfajores','Caramelos','Panchos', 'Cigarrillos'), stock INT, cuit_proveedor INT, FOREIGN KEY (cuit_proveedor) REFERENCES Proveedor(cuit))")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Remito (id_remito INT AUTO_INCREMENT PRIMARY KEY, descripcion_producto VARCHAR (255), cantidad INT, cuit_proveedor INT, FOREIGN KEY (cuit_proveedor) REFERENCES Proveedor(cuit), id_articulo INT, FOREIGN KEY (id_articulo) REFERENCES Articulo(id), nro_remito INT)")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Cliente (id_cliente INT AUTO_INCREMENT PRIMARY KEY, nombre_cliente VARCHAR (255), apellido VARCHAR (255), telefono INT, dni INT, mail VARCHAR (255), situacion_iva VARCHAR (255), estado ENUM('Alta', 'Suspendido', 'Consumidor Final'))")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Devolucion (id_devolucion INT AUTO_INCREMENT PRIMARY KEY, cuit_proveedor INT, estado VARCHAR (255), cantidad INT, num_devolucion INT, FOREIGN KEY (cuit_proveedor) REFERENCES Proveedor(cuit))")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Facturacion (id_facturacion INT AUTO_INCREMENT PRIMARY KEY, id_cliente INT, FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente), total INT, fecha_compra DATE)")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Precio (id INT AUTO_INCREMENT PRIMARY KEY, descripcion_producto VARCHAR (255), precio_producto INT)")


#<===================== AGREGAR DATOS A LA TABLA CREADA ========>
#varchar %S int %D
mycursor = mydb.cursor()
sql = "INSERT INTO Cliente (nombre_cliente, apellido, telefono, dni, mail, situacion_iva, estado) VALUES (%s, %s, %d, %d, %d, %d, %s)"
val = [
    ("Sebastian", "Finocchietti", 4321321, 32998877, "sebastianfino@gmail.com", "Monotributista", "Alta"),
    ("Luisina","Perez", 4877852, 33448866, "luisi@hotmail.com", "Monotributista", "Alta"),
    ("Maria", "Garcia", 15465487, 30134679, "garcia@gmail.com", "Responsable Inscripto", "Alta"),
    ("Lucio", "Romario", 4979121, 39853215, "lucio@gmail.com", "Exento", "Alta"),
    ("Carlos", "Alcaraz", 4987654,  27986532, "charli@hotmail.com", "Exento", "Alta"),
    ("Romina", "Gomez", 154454545, 35786513, "romina@gmail.com", "Monotributista", "Suspendido")]
mycursor.executemany(sql,val)
mydb.commit()  # actualiza la tabla
mycursor = mydb.cursor()
sql = "INSERT INTO Proveedor (cuit, nombre_proveedor, descripcion_producto, direccion, telefono, situacion_iva, estado) VALUES (%d, %s, %s,%s, %d,%s, %s)"
val = [
    (543298657, "Bebidas_SA", "Bebida", "Rivadavia 3265", 4321654, "Responsable Inscripto", "Alta"),
    (127854327, "Alfajores_del_sur","Alfajores","Corrientes 5468", 4877852, "Exento", "Alta"),
    (786532458, "Dulces_Unicos", "Caramelos","Eva Peron 8789", 4789654, "Responsable Inscripto", "Alta"),
    (264783145, "Vienisima","Panchos", "Bermudez 6548", 4979121, "Exento", "Suspendido"),
    (367412986, "Puchito", "Cigarrillos", "Alvares Jonte 12345",4987654, "Responsable Inscripto" ,"Alta")]
mycursor.executemany(sql,val)
mydb.commit()  # actualiza la tabla
mycursor = mydb.cursor()
sql = "INSERT INTO Articulo (nombre, descripcion_producto, stock, cuit_proveedor) VALUES (%s, %s,%d, %d)"
val = [
    ("coca-Cola", "Bebida", 10, 543298657 ),
    ("pepsi","Bebida", 10, 543298657),
    ("agua", "Bebida", 5, 543298657),
    ("tri_shot", "Alfajores", 5, 543298657),
    ("milka", "Alfajores", 8,127854327),
    ("bon_o_bon", "Alfajores", 12,127854327),
    ("tofi", "Alfajores", 7,127854327),
    ("flinpaf", "Caramelos", 50 ,786532458),
    ("sugus", "Caramelos", 70 ,786532458),
    ("pico_dulce", "Caramelos", 80 ,786532458),
    ("paladini", "Panchos", 10 ,264783145),
    ("granja_iris", "Panchos", 5 ,264783145),
    ("malboro", "Cigarrillos", 15 ,367412986),
    ("phillips_morris", "Cigarrillos", 25 ,367412986),
    ("camel", "Cigarrillos", 9 ,367412986)]
mycursor.executemany(sql,val)
mydb.commit()  # actualiza la tabla
mycursor = mydb.cursor()
sql = "INSERT INTO Precio (descripcion_producto, precio_producto) VALUES (%s, %d)"
val = [
    ("Bebida", 500),
    ("Alfajores", 150),
    ("Caramelos", 30),
    ("Panchos", 200),
    ("Cigarrillos", 400)]
mycursor.executemany(sql,val)
mydb.commit()  # actualiza la tabla

class Cliente:
    def __init__(self, nombre_cliente, apellido, telefono, dni, mail, situacion_iva, estado):
        self.nombre_cliente = nombre_cliente
        self.apellido = apellido
        self.telefono = telefono
        self.dni = dni
        self.mail = mail
        self.situacion_iva = situacion_iva
        self.estado = estado
    def insertarClienteBase(self):
        mycursor = mydb.cursor()
        sql = "INSERT INTO Cliente (nombre_cliente, apellido, telefono, dni, mail, situacion_iva, estado) VALUES(%s, %s, %d, %d, %d, %d, %s)"
        values = (self.nombre_cliente, self.apellido, self.telefono, self.dni, self.mail, self.situacion_iva, self.estado)
        mycursor.execute(sql, values)
        mydb.commit()

class Proveedor:
    def __init__(self, cuit, nombre_proveedor, descripcion_producto, direccion, telefono, situacion_iva, estado):
        self.cuit = cuit
        self.nombre_proveedor = nombre_proveedor
        self.descripcion_producto = descripcion_producto
        self.direccion = direccion
        self.telefono = telefono
        self.situacion_iva = situacion_iva
        self.estado = estado
    def insertarProveedorBase(self):
        mycursor = mydb.cursor()
        sql = "INSERT INTO Proveedor (cuit, nombre_proveedor, descripcion_producto, direccion, telefono, situacion_iva, estado) VALUES (%d, %s, %s, %s, %d, %s, %s)"
        values = (self.cuit, self.nombre_proveedor, self.descripcion_producto, self.direccion, self.telefono, self.situacion_iva, self.estado)
        mycursor.execute(sql, values)
        mydb.commit

class Articulo:
    def __init__(self,nombre, descripcion_producto, stock,cuit_proveedor):
        self.nombre = nombre
        self.descripcion_producto = descripcion_producto
        self.stock = stock
        self.cuit_proveedor = cuit_proveedor
    def insertarArticuloBase(self):
        mycursor = mydb.cursor()
        sql = "INSERT INTO Articulo (nombre, descripcion_producto, stock, cuit_proveedor) VALUES (%s, %s, %s, %d)"
        values = (self.nombre, self.descripcion_producto, self.stock, self.cuit_proveedor)
        mycursor.execute(sql, values)
        mydb.commit

class Menu:
    def inicio(self):
        global lista_nuevos_productos
        while True:
            numero_remito = generar_numero_remito()  # numero aleatorio para el remito
            print("********** Kiosco ************* ")
            print("Seleccionar una opcion: ")
            print("1. Proveedores")
            print("2. Clientes")
            print("3. Articulos")
            print("4. Ventas")
            print("5. Salir")

            opcion = input("Ingrese el numero de la opcion deseada: ")
            
            if opcion == "1":
                while True:
                    print("Seleccionar una opcion:")
                    print("1. Alta de Proveedor")
                    print("2. Baja de proveedores")
                    print("3. Modificar datos")
                    print("4. Pedido de reposicion")
                    print("5. Devolucion a proveedor")
                    print("6. Volver al menu principal")
                    opcion_proveedores = input("Ingrese el numero de la opcion deseada: ")
                    
                    # Cargo los datos del proveerdor
                    if opcion_proveedores == "1":
                        try:
                            cuit = int(input("Ingresar el CUIT del nuevo proveedor: "))
                            nombre_proveedor = input("Ingresar el nombre del nuevo proveedor: ")
                            descripcion_producto = input("Que categoria reparte? Bebida /-/ Alfajores /-/ Caramelos /-/ Panchos /-/ Cigarrillos: ")
                            if descripcion_producto.lower() not in ['bebida', 'alfajores', 'caramelos', 'panchos', 'cigarrillos']:
                                raise ValueError("Opciones invalidas para la categoria. Ingrese una opcion valida.")
                            direccion = input("Ingresar direccion del nuevo proveedor: ")
                            telefono = int(input("Ingresar telefono de la persona: "))
                            situacion_iva = input("Ingresar situacion de iva: ")
                            estado = input("Ingresar estado (Alta -- Suspendido): ")
                            if estado.lower() not in ['alta', 'suspendido']:
                                raise ValueError("Opción inválida para el estado. Solo puede ser: Alta o Suspendido.")
                            nuevo_proveedor = Proveedor(cuit, nombre_proveedor, descripcion_producto, direccion, telefono, situacion_iva, estado)
                            nuevo_proveedor.insertarProveedorBase()
                            mydb.commit()
                            print("Proveedor ingresado con exito!!\U0001F600")
                        except ValueError:
                            print("Datos ingresados de forma erronea, \U0000274C volver a cargar los datos por favor")

                    elif opcion_proveedores == "2":
                        cuit = int(input("Ingresar el CUIT del proveedor: "))
                        mycursor = mydb.cursor()
                        sql = "SELECT * FROM Proveedor WHERE cuit = %d"
                        mycursor.execute(sql, (cuit,))
                        myResultado = mycursor.fetchall()
                        if myResultado:
                            # Proveedor encontrado, mostrar detalles y confirmar suspension
                            for provee in myResultado:
                                print(f"CUIT: {provee[0]}, Nombpre proveedor: {provee[1]}, Estado: {provee[6]}")                                                      
                            suspender = input("¿Cambiar a estado suspendido? (si/no): ")
                            if suspender.lower() == "si":
                                sql_update= "UPDATE Proveedor SET estado = 'Suspendido' WHERE cuit = %d"
                                mycursor.execute(sql_update, (cuit,))
                                mydb.commit()
                                print("Proveedor suspendido con éxito.")
                            else:
                                print("No se elimino al proveedor.")
                        else:
                            print("Proveedor no encontrado. No se puede suspender")
                    
                    elif opcion_proveedores == "3":
                         # Modificar el telefono de un proveedor
                            cuit = int(input("Ingresar el CUIT del proveedor: "))
                            mycursor = mydb.cursor()
                            sql = "SELECT * FROM Proveedor WHERE cuit = %d"
                            mycursor.execute(sql, (cuit,))
                            myResultado = mycursor.fetchall()
                            
                            if myResultado:
                                # Proveedor encontrado
                                print("Proveedor encontrado.")
                                nuevo_telefono = int(input("Ingresar el nuevo numero de telefono: "))
                                sql_update = "UPDATE Proveedor SET telefono = %d WHERE cuit = %d"
                                mycursor.execute(sql_update, (nuevo_telefono, cuit))
                                mydb.commit()
                                print("Modificacion con exito.")
                            else:
                                print("Proveedor no encontrada. No te encontramos en nuestro sistema.")

                    elif opcion_proveedores == "4":
                        # Generar el número de remito
                        numero_remito_global = generar_numero_remito()                        
                        nombre_proveedor_usuario = input("Ingrese el nombre del proveedor: ")
                        mycursor = mydb.cursor()
                        sql = "SELECT * FROM Proveedor WHERE nombre_proveedor = %s"
                        mycursor.execute(sql, (nombre_proveedor_usuario,))
                        mycursor = mydb.cursor()
                        sql = """
                            SELECT Articulo.id, Articulo.nombre, Articulo.stock
                            FROM Proveedor
                            JOIN Articulo ON Proveedor.cuit = Articulo.cuit_proveedor
                            WHERE Proveedor.nombre_proveedor = %s
                        """
                        mycursor.execute(sql, (nombre_proveedor_usuario,))
                        myResultado = mycursor.fetchall()

                        if myResultado:
                            print(f"{'Numero producto': ^30} | {'Nombre producto': ^30} | {'Stock': ^10}")
                            print('-' * 73)
                            for resultado in myResultado:
                                print(f"{resultado[0]: ^30} | {resultado[1]: ^30} | {resultado[2]: ^10}")
                            print('-' * 73)
                            while True:
                                id_articulo_str = input("Ingrese el numero del producto: ")                       
                                try:
                                    id_articulo = int(id_articulo_str)
                                    break
                                except ValueError:
                                    print("\U0000274C Ingrese un numero de producto valido.")
                            while True:
                                cantidad_nueva_str = input("Ingrese la cantidad del producto a solicitar:")
                                if cantidad_nueva_str:  # Verificar si la cadena no está vacía
                                    try:
                                        cantidad_nueva = int(cantidad_nueva_str)
                                        break  # Si la conversión fue exitosa, salimos del bucle
                                    except ValueError:
                                        print("\U0000274C Ingrese una cantidad valida.")

                            # Guarda el nuevo producto con el número de remito
                            nuevo_producto = {
                                'id_articulo': id_articulo,
                                'cantidad_nueva': cantidad_nueva,
                                'numero_remito': numero_remito_global
                                    }

                            lista_nuevos_productos.append(nuevo_producto)

                            # Insertar en la tabla Remito
                            sql_insert_remito = "INSERT INTO Remito (descripcion_producto, cantidad, cuit_proveedor, id_articulo, nro_remito) VALUES (%s, %s, (SELECT cuit FROM Proveedor WHERE nombre_proveedor = %s), %s, %s)"
                            values_insert_remito = (nombre_proveedor_usuario, cantidad_nueva, nombre_proveedor_usuario, id_articulo, numero_remito_global)
                            mycursor.execute(sql_insert_remito, values_insert_remito)
                            mydb.commit()

                            print(f"Producto '{id_articulo}' agregado a la lista de nuevos productos.")
                            print(f"El numero de remito generado es: {numero_remito_global} \U0001F44D")
                        else:
                            print(f"\U0000274C No existe proveedor con el siguiente nombre: '{nombre_proveedor_usuario}'.")
                                
                    elif opcion_proveedores == "5":
                       # Mostrar los proveedores y detalles de productos con stock
                            print("Lista de proveedores, descripción de productos y stock:")
                            mycursor = mydb.cursor()
                            sql = """
                                SELECT Proveedor.nombre_proveedor, Proveedor.descripcion_producto, Articulo.nombre, Articulo.stock
                                FROM Proveedor
                                JOIN Articulo ON Proveedor.cuit = Articulo.cuit_proveedor
                            """
                            mycursor.execute(sql)
                            myResultado = mycursor.fetchall()

                            if myResultado:
                                print(f"{'Proveedor': ^30} | {'Descripcion producto': ^30} | {'Nombre producto': ^30} | {'Stock': ^10}")
                                print('-' * 111)
                                for resultado in myResultado:
                                    print(f"{resultado[0]: ^30} | {resultado[1]: ^30} | {resultado[2]: ^30} | {resultado[3]: ^10}")
                                print('-' * 111)
                            else:
                                print("No hay informacion disponible en la base de datos.")

                            nombre_proveedor_usuario = input("Ingrese el nombre del proveedor: ")

                            mycursor = mydb.cursor()
                            sql = """
                                SELECT Articulo.nombre, Articulo.stock
                                FROM Proveedor
                                JOIN Articulo ON Proveedor.cuit = Articulo.cuit_proveedor
                                WHERE Proveedor.nombre_proveedor = %s
                            """
                            mycursor.execute(sql, (nombre_proveedor_usuario,))
                            myResultado = mycursor.fetchall()

                            if myResultado:
                                print(f"{'Nombre producto': ^30} | {'Stock': ^10}")
                                print('-' * 51)
                                for resultado in myResultado:
                                    print(f"{resultado[0]: ^30} | {resultado[1]: ^10}")
                                print('-' * 51)

                                # Verifica si existe el producto
                                nombre_producto = input("Ingrese el nombre del producto a devolver: ")

                                producto_existente = any(nombre_producto.lower() == resultado[0].lower() for resultado in myResultado)

                                if producto_existente:
                                    while True:
                                        cantidad_a_descontar_str = input(f"Ingrese la cantidad a descontar del producto '{nombre_producto}':")
                                        try:
                                            cantidad_a_descontar = int(cantidad_a_descontar_str)
                                            break  # Si la conversión fue exitosa, salimos del bucle
                                        except ValueError:
                                            print("\U0000274C Ingrese una cantidad válida.")
                                        # Verificar que hay suficiente stock para descontar
                                    if cantidad_a_descontar <= myResultado[0][1]:
                                        # Actualizar la tabla para descontar el stock del producto
                                        sql_update = "UPDATE Articulo SET stock = stock - %s WHERE nombre = %s AND cuit_proveedor = (SELECT cuit FROM Proveedor WHERE nombre_proveedor = %s)"
                                        values_update = (cantidad_a_descontar, nombre_producto, nombre_proveedor_usuario)
                                        mycursor.execute(sql_update, values_update)
                                        mydb.commit()

                                        print(f"Se han descontado {cantidad_a_descontar} unidades del producto '{nombre_producto}'.")
                                    else:
                                        print(f"\U0000274C No hay suficiente stock para descontar {cantidad_a_descontar} unidades del producto '{nombre_producto}'.")
                                else:
                                    print(f"\U0000274C El producto '{nombre_producto}' no existe en la lista de productos del proveedor.")
                            else:
                                print(f"\U0000274C No hay información disponible para el proveedor '{nombre_proveedor_usuario}'.")

                    elif opcion_proveedores == "6":
                        # volver al menu principal
                        break
            elif opcion == "2": 
                while True:
                    print("Seleccionar una opcion:")
                    print("1. Alta cliente")
                    print("2. Modificar telefono")
                    print("4. Cambiar estado al cliente")
                    print("5. Volver al menu principal")  
                    opcion_cliente = input("Ingrese el numero de la opcion deseada: ")
                    
                    # Cargo los datos de la persona
                    if opcion_cliente == "1":
                        try:
                            consu_final = input("Sos consumidor final? si/no ")   
                            if consu_final == "si":
                                mycursor = mydb.cursor()
                                sql = "INSERT INTO Cliente (nombre_cliente, apellido, telefono, dni, mail, situacion_iva, estado) VALUES (%s, %s, %d, %d, %d,%d, %s)"
                                val = [(None, None, None, None, None, None, "Consumidor Final"),]  
                                mycursor.executemany(sql,val)
                                mydb.commit()        
                            elif consu_final == "no":
                                nombre_cliente = input("Ingresar nombre del nuevo cliente: ")
                                apellido_cliente = input("Ingresar apellido de la persona del nuevo cliente: ")
                                telefono_cliente = int(input("Ingresar telefono del nuevo cliente: "))
                                dni_cliente = int(input("Ingresar dni del nuevo cliente: "))
                                mail_cliente = input("Ingrese el mail del nuevo cliente: ")
                                situacion_iva_cliente = input("Ingrese la situacion de iva del nuevo cliente: ")
                                estado = input("Ingresar estado (Alta -- Suspendido): ")
                                if estado.lower() not in ['alta', 'suspendido']:
                                    raise ValueError("Opción inválida para el estado. Solo puede ser: Alta o Suspendido.")
                                nueva_persona = Cliente(nombre_cliente, apellido_cliente, telefono_cliente, dni_cliente, mail_cliente, situacion_iva_cliente, estado)
                                nueva_persona.insertarClienteBase()
                                print("Cliente agregado con exito!!\U0001F600")
                        except ValueError:
                            print("Datos ingresados de forma erronea, \U0000274C volver a cargar los datos por favor")
                   
                    elif opcion_cliente == "2":
                            # Modificar el telefono de una persona por DNI
                            dni = int(input("Ingresar el DNI de la persona: "))
                            mycursor = mydb.cursor()
                            sql = "SELECT * FROM Cliente WHERE dni = %s"
                            mycursor.execute(sql, (dni,))
                            myResultado = mycursor.fetchall()
                            
                            if myResultado:
                                # Persona encontrada
                                print("Cliente encontrado.")
                                nuevo_telefono = int(input("Ingresar el nuevo numero de telefono: "))
                                sql_update = "UPDATE Cliente SET telefono = %s WHERE dni = %s"
                                mycursor.execute(sql_update, (nuevo_telefono, dni))
                                mydb.commit()
                                print("Modificacion con exito. \U0001F44D")
                            else:
                                print("Cliente no encontrado. No te encontramos en nuestro sistema.")    
                    
                    elif opcion_cliente == "4":
                        cuit = int(input("Ingresar el DNI del cliente: "))
                        mycursor = mydb.cursor()
                        sql = "SELECT * FROM Cliente WHERE dni = %d"
                        mycursor.execute(sql, (cuit,))
                        myResultado = mycursor.fetchall()
                        if myResultado:
                            # Cliente encontrado, mostrar detalles y confirmar Suspencion
                            for cli in myResultado:
                                print(f"DNI: {cli[3]}, Nombere de Cliente: {cli[1]}, Estado: {cli[7]}")                                                      
                            suspender = input("¿Cambiar a estado suspendido? (si/no): ")
                            if suspender.lower() == "si":
                                sql_update= "UPDATE Cliente SET estado = 'Suspendido' WHERE dni = %d"
                                mycursor.execute(sql_update, (cuit,))
                                mydb.commit()
                                print("Cliente suspendido con exito. \U0001F44D")
                            else:
                                print("No se suspendio al Cliente. \U0000274C")
                        else:
                            print("Cliente no encontrado. No se puede suspender \U0001F6AB")    
                     
                    elif opcion_cliente == "5":
                        # volver al menu principal
                        break
                       
            elif opcion == "3": 
                while True:  
                    print("Seleccionar una opcion:")
                    print("1. Alta Articulo")
                    print("2. Baja Articulo")
                    print("3. Modificar articulo")
                    print("4. Articulos sin stock")
                    print("5. Ingreso de remito por mercaderia de proveedor")
                    print("6. Regresar al menu principal")
                    opcion_articulo = input("Ingrese el numero de la opcion deseada: ")
                    numero_remito_global = None  # numero de remito en 0
                    if opcion_articulo == "1":
                        categorias_validas = ['bebida', 'alfajores', 'caramelos', 'panchos', 'cigarrillos']
                        try:
                            nombre = input("Ingrese el nombre del articulo nuevo: ")
                            while True:
                                descripcion_producto = input("Ingresar la categoria del articulo nuevo: Bebida/-/ Alfajores /-/ Caramelos /-/ Panchos /-/ Cigarrillos ")                               
                                if descripcion_producto.lower() in categorias_validas:
                                    break
                                else:
                                    print("\U0000274C Categoria incorrecta. Ingrese una categoria valida.")
                            # Validar que el stock sea un número
                            while True:
                                try:
                                    stock = int(input("Ingrese la cantidad de stock del nuevo articulo: "))
                                    break  # Salir del bucle si el valor es un número válido
                                except ValueError:
                                    print("\U0000274C Datos incorrectos.")
                            
                            # Validar que el CUIT del proveedor sea un número
                            while True:
                                try:
                                    cuit_proveedor = int(input("Ingrese el CUIT del proveedor: "))
                                    break  # Salir del bucle si el valor es un número válido
                                except ValueError:
                                    print("\U0000274C Datos incorrectos.")

                            # Verificar si el proveedor existe
                            mycursor = mydb.cursor()
                            sql_proveedor = "SELECT * FROM Proveedor WHERE cuit = %s"
                            mycursor.execute(sql_proveedor, (cuit_proveedor,))
                            proveedor_existente = mycursor.fetchone()

                            if proveedor_existente:
                                # Proveedor encontrado
                                sql_articulo = "INSERT INTO Articulo (nombre, descripcion_producto, stock, cuit_proveedor) VALUES (%s, %s, %s, %s)"
                                val_articulo = (nombre, descripcion_producto, stock, cuit_proveedor)
                                mycursor.execute(sql_articulo, val_articulo)
                                mydb.commit()
                                print("Articulo agregado con éxito!!\U0001F600")
                            else:
                                print("Proveedor no encontrado. No se puede agregar producto \U0001F61E")

                        except ValueError:
                            print("Datos ingresados de forma incorrecta. Por favor, vuelva a cargar los datos.")

         
                    elif opcion_articulo == "2":
                        #bajar articulos del stock
                        mycursor = mydb.cursor()
                        sql = """
                            SELECT Proveedor.nombre_proveedor, Proveedor.descripcion_producto, Articulo.nombre, Articulo.stock
                            FROM Proveedor
                            JOIN Articulo ON Proveedor.cuit = Articulo.cuit_proveedor
                            """
                        mycursor.execute(sql)
                        myResultado = mycursor.fetchall()
                        print(f"{'Proveedor': ^30} | {'Descripcion producto': ^30} | {'Nombre producto': ^30} | {'Stock': ^10}")
                        print('-' * 111)
                        for resultado in myResultado:
                            print(f"{resultado[0]: ^30} | {resultado[1]: ^30} | {resultado[2]: ^30} | {resultado[3]: ^10}")
                        print('-' * 111)
                        # Obtener información de stock y nombre del producto para un proveedor especifico
                        nombre_proveedor_usuario = input("Ingrese el nombre del proveedor: ")

                        mycursor = mydb.cursor()
                        sql = """SELECT Articulo.nombre, Articulo.stock
                                FROM Proveedor
                                JOIN Articulo ON Proveedor.cuit = Articulo.cuit_proveedor
                                WHERE Proveedor.nombre_proveedor = %s"""
                        mycursor.execute(sql, (nombre_proveedor_usuario,))
                        myResultado = mycursor.fetchall()

                        if myResultado:
                            print(f"{'Nombre producto': ^30} | {'Stock': ^10}")
                            print('-' * 51)
                            for resultado in myResultado:
                                print(f"{resultado[0]: ^30} | {resultado[1]: ^10}")
                            print('-' * 51)
                            # Verificación de existencia del producto
                            baja_stock = input("Ingrese el nombre del producto a bajar stock: ")

                            producto_existente = any(baja_stock.lower() == resultado[0].lower() for resultado in myResultado)

                            if producto_existente:
                                cantidad_a_descontar = int(input(f"Ingrese la cantidad a descontar del producto '{baja_stock}':"))
                                # Verificar que hay suficiente stock para descontar
                                if cantidad_a_descontar <= myResultado[0][1]:
                                    # Actualizar la tabla para descontar el stock del producto
                                    sql_update = "UPDATE Articulo SET stock = stock - %s WHERE nombre = %s AND cuit_proveedor = (SELECT cuit FROM Proveedor WHERE nombre_proveedor = %s)"
                                    values_update = (cantidad_a_descontar, baja_stock, nombre_proveedor_usuario)
                                    mycursor.execute(sql_update, values_update)
                                    mydb.commit()

                                    print(f"Se descontaron {cantidad_a_descontar} unidades del producto '{baja_stock}'.")
                                else:
                                    print(f"No hay suficiente stock para descontar {cantidad_a_descontar} unidades del producto '{baja_stock}'.")
                            else:
                                print(f"El producto '{baja_stock}' no existe en la lista de productos del proveedor.")
                        else:
                            print(f"No hay informacion disponible para el proveedor '{nombre_proveedor_usuario}'.")                        
                    
                    elif opcion_articulo == "3":
                        # Modificar nombre del articulo
                            articulo = input("Ingresar el nombre del articulo: ")
                            mycursor = mydb.cursor()
                            sql = "SELECT * FROM Articulo WHERE nombre = %d"
                            mycursor.execute(sql, (articulo,))
                            myResultado = mycursor.fetchall()
                            
                            if myResultado:
                                # Articulo encontrado
                                print("Articulo encontrado.")
                                nuevo_nombre = input("Ingresar el nuevo nombre del articulo: ")
                                sql_update = "UPDATE Articulo SET nombre = %d WHERE nombre = %d"
                                mycursor.execute(sql_update, (nuevo_nombre, articulo))
                                mydb.commit()
                                print("Modificacion con exito.\U0001F600")
                            else:
                                print("Articulo no encontrado. No ese articulo en nuestro sistema.\U0001F6AB")
                    
                    elif opcion_articulo == "4":
                        #Articulos sin stock
                        mycursor = mydb.cursor()
                        sql = """
                            SELECT Proveedor.nombre_proveedor, Proveedor.descripcion_producto, Articulo.nombre, Articulo.stock
                            FROM Proveedor
                            JOIN Articulo ON Proveedor.cuit = Articulo.cuit_proveedor
                            WHERE Articulo.stock = 0
                            """
                        mycursor.execute(sql)
                        myResultado = mycursor.fetchall() 
                        if myResultado:
                            print(f"{'Proveedor': ^30} | {'Descripcion producto': ^30} | {'Nombre producto': ^30} | {'Stock': ^10}")
                            print('-' * 111)
                            for resultado in myResultado:
                                print(f"{resultado[0]: ^30} | {resultado[1]: ^30} | {resultado[2]: ^30} | {resultado[3]: ^10}")
                            print('-' * 111)
                        else:
                            print("No hay productos sin stock.")
                     
                    elif opcion_articulo =="5":
                        if numero_remito_global is not None:
                            print(f"El numero de remito generado es: {numero_remito_global}")
                            # Mostrar la lista de nuevos productos pendientes de ingreso
                            if lista_nuevos_productos:
                                print("Productos pendientes de ingreso:")
                                print(f"{'Proveedor': ^30} | {'Numero articulo': ^30} | {'Cantidad': ^10} | {'Numero de Remito': ^15}")
                                print('-' * 95)
                                for producto in lista_nuevos_productos:
                                    print(f"{nombre_proveedor_usuario: ^30} | {producto['id_articulo']: ^15} | {producto['cantidad_nueva']: ^10} | {producto['numero_remito']: ^15}")
                                print('-' * 95)

                                # Confirmar ingreso
                                confirmacion = input("Confirmar ingreso de remito? si/no: ").lower()

                                if confirmacion == "si":
                                    # Actualizar la base de datos con los nuevos productos
                                    for producto in lista_nuevos_productos:
                                        id_articulo = producto['id_articulo']
                                        cantidad_nueva = producto['cantidad_nueva']
                                        numero_remito = producto['numero_remito']

                                        sql_update = "UPDATE Articulo SET stock = stock + %s WHERE id = %s AND cuit_proveedor = (SELECT cuit FROM Proveedor WHERE nombre_proveedor = %s)"
                                        values_update = (cantidad_nueva, id_articulo, nombre_proveedor_usuario)
                                        mycursor.execute(sql_update, values_update)
                                        mydb.commit()

                                    print("Ingreso confirmado. Se agrego la cantidad en la base de datos. \U0001F389")
                                    # Limpiar la lista después de confirmar el ingreso
                                    lista_nuevos_productos = []
                                else:
                                    print("Ingreso no confirmado. \U0000274C")
                            else:
                                print("No hay productos pendientes de ingreso.")
                        else:
                            print("No se genero el numero de remito \U0001F6AB. Por favor, genera el numero en la parte de proveedores.")
                            
                    elif opcion_articulo == "6":
                        # volver al menu principal
                        break      
            
            elif opcion == "4":
                while True:  
                    print("Seleccionar una opcion:")
                    print("1. Realizar compra")
                    print("2. Regresar al menu principal")
                    opcion_ventas = input("Ingrese el numero de la opcion deseada: ")
                    
                    if opcion_ventas == "1":
                        #Muestra los precios y productos
                        print("Lista de productos con precios: ")
                        mycursor = mydb.cursor()
                        sql = """
                            SELECT Articulo.nombre, Articulo.descripcion_producto, Articulo.stock, Precio.precio_producto
                            FROM Articulo
                            JOIN Precio ON Articulo.descripcion_producto = Precio.descripcion_producto
                        """
                        mycursor.execute(sql)
                        myResultado = mycursor.fetchall()
                        lista_compras = []  # Lista para almacenar los productos comprados
                        if myResultado:
                            print(f"{'Nombre producto': ^30} | {'Descrion Producto': ^30} | {'Stock': ^10} | {'Precio': ^18}")
                            print('-' * 100)
                            
                            for resultado in myResultado:
                                print(f"{resultado[0]: ^30} | {resultado[1]: ^30} | {resultado[2]: ^10} | ${resultado[3]: ^15}")

                            while True:
                                dia = input("Indicar el dia de la venta (formato dd/mm/yyyy): ")
                                try:
                                    fecha_compra = datetime.datetime.strptime(dia, "%d/%m/%Y").date()  
                                except ValueError:
                                    print("Formato de fecha incorrecto. Ingresa el siguiente formato dd/mm/yyyy.")
                                    continue
                                
                                fecha_compra = datetime.datetime.strptime(dia, "%d/%m/%Y").date()
                                comprar_articulo = input("Indicar el nombre de producto a comprar: ")
                                
                                if comprar_articulo.lower() == 'fin':
                                    break
                                
                                # Valida la cantidad ingresada
                                cantidad_a_comprar_str = input("Indicar la cantidad a comprar: ")
                                
                                if cantidad_a_comprar_str.isdigit(): 
                                    cantidad_a_comprar = int(cantidad_a_comprar_str)
                                    
                                    # Verificar la cantidad 
                                    stock_disponible = next((resultado[2] for resultado in myResultado if resultado[0].lower() == comprar_articulo.lower()), None)
                                    
                                    if stock_disponible is not None:
                                        if cantidad_a_comprar <= stock_disponible:
                                            precio_unitario = next((resultado[3] for resultado in myResultado if resultado[0].lower() == comprar_articulo.lower()), None)
                                            precio_total = cantidad_a_comprar * precio_unitario
                                            
                                            lista_compras.append({
                                                'nombre_producto': comprar_articulo,
                                                'cantidad': cantidad_a_comprar,
                                                'precio_total': precio_total
                                            })
                                            
                                            print(f"Compra exitosa. Has comprado {cantidad_a_comprar} unidades de {comprar_articulo}. Precio total: ${precio_total}")
                                        else:
                                            print(f"No hay suficiente stock. Stock disponible: {stock_disponible}.")
                                    else:
                                        print(f"El producto {comprar_articulo} no existe en la lista.")
                                else:
                                    print("La cantidad ingresada no es valida. Debe ser un numero entero positivo.")
                                
                                seguir_comprando = input("¿Deseas seguir comprando? (si/no): ").lower()
                                if seguir_comprando != 'si':
                                    break
                        else:
                            print("No hay productos en la base de datos")

                        # Mostrar resumen de la compra
                        if lista_compras:
                            print("Resumen de la compra")
                            print(f"{'Nombre producto': ^30} | {'Cantidad': ^10} | {'Precio Total': ^18}")
                            print('-'* 60)
                            for compra in lista_compras:
                                print(f"{compra['nombre_producto']: ^30} | {compra['cantidad']: ^10} | ${compra['precio_total']: ^18}")
                            precio_total_compra = sum(compra['precio_total'] for compra in lista_compras)
                            print(f"\nPrecio total de la compra: ${precio_total_compra}")
                            while True:
                                facturacion_cliente = input("Asignar a - Opcion 1: Cliente || Opcion 2: Consumidor final: ")
                                if facturacion_cliente == "1" or facturacion_cliente == "2":
                                    break
                                else:
                                    print("Opcion ingresada incorrecta. Por favor, elige 1 o 2.")

                                
                            if facturacion_cliente == "1":
                                dni_cliente = input("Ingrese el DNI del cliente para asignarle factura: ")
                                mycursor = mydb.cursor()
                                sql_cliente = "SELECT * FROM Cliente WHERE dni = %s"
                                mycursor.execute(sql_cliente, (dni_cliente,))
                                cliente_existente = mycursor.fetchone()

                                if cliente_existente:
                                    print(f"Factura asignada al cliente con DNI: {dni_cliente} \U0001F44D")
                                    id_cliente = cliente_existente[0]  
                                    total = sum(compra['precio_total'] for compra in lista_compras)

                                    # Insertar en la tabla Facturacion
                                    sql_insert_facturacion = "INSERT INTO Facturacion (id_cliente, total, fecha_compra) VALUES (%s, %s, %s)"
                                    values_insert_facturacion = (id_cliente, total, fecha_compra)
                                    mycursor.execute(sql_insert_facturacion, values_insert_facturacion)
                                    mydb.commit()
                                    for compra in lista_compras:
                                        nombre_producto = compra['nombre_producto']
                                        cantidad_comprada = compra['cantidad']

                                        #Actualiza la tabla de Articulos
                                        sql_update_productos = "UPDATE Articulo SET stock = stock - %s WHERE nombre = %s"
                                        values_update_productos = (cantidad_comprada, nombre_producto)
                                        mycursor.execute(sql_update_productos, values_update_productos)
                                        mydb.commit()
                                    
                                else:
                                    print(f"No se encontro un cliente con DNI: {dni_cliente}. Por favor, vuelva a realizar la compra.")

                            elif facturacion_cliente == "2":
                                print("Factura asignada como Consumidor Final. \U0001F44D")
                                id_cliente = None  
                                total = sum(compra['precio_total'] for compra in lista_compras)

                                # Insertar en la tabla Facturacion
                                sql_insert_facturacion = "INSERT INTO Facturacion (id_cliente, total, fecha_compra) VALUES (%s, %s, %s)"
                                values_insert_facturacion = (id_cliente, total, fecha_compra)
                                mycursor.execute(sql_insert_facturacion, values_insert_facturacion)
                                mydb.commit()
                                for compra in lista_compras:
                                    nombre_producto = compra['nombre_producto']
                                    cantidad_comprada = compra['cantidad']
                                    #Actualiza la tabla de Articulos
                                    sql_update_productos = "UPDATE Articulo SET stock = stock - %s WHERE nombre = %s"
                                    values_update_productos = (cantidad_comprada, nombre_producto)
                                    mycursor.execute(sql_update_productos, values_update_productos)
                                    mydb.commit()
                                    
                        else:
                            print("No se realizaron compras.")
                        
                    elif opcion_ventas == "2":
                        # volver al menu principal
                        break  
            elif opcion == "5":
                try:
                    mycursor = mydb.cursor()
                    mycursor.execute("DROP DATABASE KIOSCO")
                    print("Gracias por visitar nuestro comercio!!!")
                finally:
                    if mycursor:
                        mycursor.close()
                    mydb.close()
                break             
                             
if __name__ == "__main__":
    menu = Menu()
    menu.inicio()
