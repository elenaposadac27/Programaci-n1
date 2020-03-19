#--------MENSAJES-------
MENSAJE_BIENVENIDA ="""Bienvenido Señor Comprador,
Para realizar compras en nuestra plataforma contamos con un simple proceso de 4 pasos"""
PREGUNTA_EDAD_USUARIO = "Para una mejor experiencia ingrese su edad porfavor \n"
MENSAJE_18 = "COMENCEMOS CON LA COMPRA"
MENSAJE_30 = "USTED POSEE UN DESCUENTO DEL 30%"
MENSAJE_60 = "USTED POSEE UN DESCUENTO DEL "
MENSAJE_NEGATIVO = "LO SENTIMOS, PARA INGRESAR A NUESTRO SITIO DEBES SER MAYOR DE 18 AÑOS"
PREGUNTA_COMPRAS = "¿DESEA AÑADIR NUEVOS PRODUCTOS AL CARRITO? \n"
MENSAJE_INGRESO_ARTICULOS= "INGRESE LOS PRODUCTOS QUE DESEA AÑADIR UNO A UNO \n"
PREGUNTA_ELIMINAR = "¿DESEA ELIMINAR ALGUN PRODUCTO DEL CARRITO? \n"
MENSAJE_PRODUCTO_ELIMINADO = "INGRESE LA POSICION EN LA LISTA DEL PRODUCTO QUE DESEA ELIMINAR COMENZANDO CON EL 0(CERO) \n"
MENSAJE_SALIDA = "GRACIAS POR USAR NUESTRO SISTEMA DE COMPRAS ONLINE"
#--------ENTRADAS-------
_edadUsuario = 0
_comprasCarrito = ""
_eliminarProductos = ""
_posicionProductoEliminado = 0

#-------LISTAS-----
lista_compras = []


#-------CODIGO-------
_menu = int(input("""
    Ingrese el paso de compra en el que se encuentra:
    1- Inicio
    2- Seleccion de productos
    3- Verificación de compra
    4- Modificacion de compra
    5- Salir \n
"""))
while (_menu != 5) :
    if (_menu == 1) :
        _edadUsuario = int(input(PREGUNTA_EDAD_USUARIO))
        if _edadUsuario >= 18 and _edadUsuario < 30:
            print (MENSAJE_18)
        elif _edadUsuario >= 30 and  _edadUsuario < 60 :
            print (MENSAJE_30)
        elif _edadUsuario >= 60 :
            print (MENSAJE_60 , _edadUsuario, "%")
        else:
            print (MENSAJE_NEGATIVO)
    elif (_menu == 2) :
        _comprasCarrito = input(PREGUNTA_COMPRAS)
        while (_comprasCarrito == "si") :
            lista_compras.append(input(MENSAJE_INGRESO_ARTICULOS))
            _comprasCarrito = input(PREGUNTA_COMPRAS)
        print ("USTED HA AÑADIDO AL CARRITO : ", lista_compras)
    elif(_menu == 3) :
        print ("¡ESTAMOS LISTOS PARA PAGAR! SU CARRITO CUENTA CON :", lista_compras, "(PARA REALIZAR MODIFICACIONES AVANZA AL SIGUIENTE PASO)")
    elif(_menu == 4) :
        _eliminarProductos = input(PREGUNTA_ELIMINAR)
        while (_eliminarProductos == "si") :
            _posicionProductoEliminado = int(input(MENSAJE_PRODUCTO_ELIMINADO))
            lista_compras.pop(_posicionProductoEliminado)
            print ("¡ESTAMOS LISTOS PARA PAGAR! SU CARRITO CUENTA CON :", lista_compras)
            _eliminarProductos = input(PREGUNTA_ELIMINAR)
        print ("¡ESTAMOS LISTOS PARA PAGAR! SU CARRITO CUENTA CON :", lista_compras)
    else :
        print ("INGRESE UN PASO DISPONIBLE DENTRO DEL PROCESO DE COMPRA")
        
    _menu = int(input("""
    Ingrese el paso de compra en el que se encuentra:
    1- Inicio
    2- Seleccion de productos
    3- Verificación de compra
    4- Modificacion de compra
    5- Salir \n
    """))
print(MENSAJE_SALIDA)
