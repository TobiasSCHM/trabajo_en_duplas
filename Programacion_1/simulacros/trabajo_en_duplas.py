inventario = [

["Chupetin Sable de Luz".upper(), 50, 200],
["Agua La Fuerza".upper(), 35, 3200],
["Gomitas Holocubo".upper(), 25, 990],
["Barritas de cereal Wokiee".upper(), 48, 2500],
["Galletitas R2D2".upper(), 20, 15800]

]

def venta_producto():
    """
    Función que pregunta al usuario el producto que desea comprar, valida si el producto existe en el inventario y valida si la cantidad 
    deseada del producto esté disponible
    """
    producto = input("ingrese el producto que quiere comprar: ").upper()
    cant_producto = int(input("ingrese la cantidad que quiere comprar: "))
    
    for i in inventario:
        if i[0] == producto:  
            if i[1] >= cant_producto:  
                i[1] -= cant_producto  
                print("Producto vendido:", producto)
                print("Cantidad restante:", i[1])
                break
            elif cant_producto > i[1]:
                print("Error, ingresaste una cantidad muy alta. Solo hay", i[1], "disponibles.")
            else:
                print("flaco, no existe eso")


def agregar_producto():
    """
    Función para agregar nombre, cantidad y precio del producto nuevo en forma de lista a la lista inventario 
    """
    nombre = input("Ingrese el nombre del producto: ").upper()
    cantidad = int(input("Ingrese la cantidad disponible del producto: "))
    precio = int(input("Ingrese el precio del producto: "))

    inventario.append([nombre, cantidad, precio])

def validar_menu(): 
    """
    Función para mostrar el menu al usuario, que ingrese su eleccion y que se valide solamentee las 4 opciones del menú
    """
    
    print("1. Agregar producto al inventario\n2. Realizar una venta\n3. Mostrar productos disponibles\n4. Salir del sistema")
    seleccion = int(input("Ingrese el numero de su elección: "))    

    while seleccion != 1 and seleccion != 2 and seleccion != 3 and seleccion !=4:
        seleccion = int(input("Error. Ingrese el numero de su elección: ")) 

    return seleccion    


def mostrar_producto():
    """
    Funcion para mostrar el nombre, cantidad y precio de todos los  productos en el inventario  
    """
    for i in inventario:
        print(f"NOMBRE DEL PRODUCTO: {i[0]}, CANTIDAD: {i[1]}, PRECIO: {i[2]}")


seguir = True

while seguir == True:
    seleccion= validar_menu()

    match seleccion:
        case (1): 
            agregar_producto()
        case (2):
            venta_producto()
        case (3):
            mostrar_producto()
        case (4):
            print("¡Hasta luego!")
            seguir = False
