import os
from time import sleep


d_juegos = {
'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
}

d_inventario  = {
'G001': [9990, 7],
'G002': [19990, 0],
'G003': [42990, 3],
'G004': [14990, 5],
'G005': [17990, 9],
'G006': [39990, 2],
}

def leer_opcion():
    
    try:
        opcion = int(input("Elija una opcion: "))
        
        if opcion < 1 or opcion > 6:
            return -1
        
        return opcion
    
    except ValueError:
        print("Por favor ingrese un numero valido.")
        sleep(3)

def stock_plataforma(plataforma, diccionario_juegos,diccionario_inventario):
    
    total = 0
    
    for juego in diccionario_juegos:
        nombre, plataforma_b, genero, clasificacion, multiplayer, editor = diccionario_juegos[f"{juego}"]
        if plataforma in plataforma_b.lower():
            total += diccionario_inventario[f"{juego}"][1]
            #print(juego)
            
    
    if total != 0:
        print(f"Juegos encontrados para la plataforma '{plataforma}': {total}")
        sleep(3)
        
    elif total == 0:
        print(f"No se encontraron juegos disponibles para la plataforma: {plataforma}")
        sleep(3)

def busqueda_precio(p_min, p_max, diccionario_juegos,diccionario_inventario):
    
    lista_juegos = []
    
    for juego in diccionario_inventario:
        if diccionario_inventario[f"{juego}"][0] >= p_min and diccionario_inventario[f"{juego}"][0] <= p_max and diccionario_inventario[f"{juego}"][1] != 0:
            lista_juegos.append(f"{diccionario_juegos[f"{juego}"][0]}--{juego}")
            
    if len(lista_juegos) == 0:
        print("Actualmente no hay juegos disponibles dentro de ese rango.")
        sleep(3)
        return
            
    s_lista_juegos = sorted(lista_juegos)
    os.system('cls')
    
    print("Juego--codigo:")
    for i in s_lista_juegos:
        print(i)
        
    input()

def buscar_codigo(codigo,diccionario_inventario):
    
    if codigo in diccionario_inventario:
        return True
    else: return False
    
def actualizar_precio(codigo, nuevo_precio, diccionario_inventario):
    
    check = buscar_codigo(codigo,diccionario_inventario)
    
    if check:
        diccionario_inventario[f"{codigo}"][0] = nuevo_precio
        return True
        
    elif not check:
        print("Al verificar el codigo, se retorno que no existe.")
        return False
    
def check_codigo(codigo, diccionario_juegos):
    
    if codigo == "":
        return False
    if codigo in diccionario_juegos:
        return False
    
    return True

def check_titulo(titulo):
    
    if titulo == "":
        return False
    return True

def check_plataforma(plataforma):
    
    if plataforma == "":
        return False
    
    return True

def check_genero(genero):
    
    if genero == "":
        return False
    
    return True

def check_clasificacion(clasificacion):
    
    if clasificacion == "E" or clasificacion == "T" or clasificacion == "M":
        return True
    else:
        return False

def check_multiplayer(multiplayer):
    
    if multiplayer == "s":
        return True
    elif not multiplayer == "n":
        return False

def check_editor(editor):
    
    if editor == "":
        return False
    
    return True

def check_precio(precio):
    
    if precio <= 0:
        return False
    return True

def check_stock(stock):
    if stock < 0:
        return False
    
    return True
    
def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, diccionario_juegos, diccionario_inventario):
    
    if buscar_codigo(codigo,diccionario_inventario):
        return False
    
    diccionario_juegos.update({f"{codigo}": [titulo,plataforma,genero,clasificacion,multiplayer,editor]})
    diccionario_inventario.update({f"{codigo}": [precio,stock]})
    
def eliminar_juego(codigo, diccionario_juegos,diccionario_inventario):
    check = buscar_codigo(codigo,diccionario_inventario)
    
    if check:
        diccionario_juegos.popitem(codigo)
        diccionario_inventario.popitem(codigo)
        return True
    elif not check:
        return False


while True:
    os.system('cls')
    
    print("""
========== MENÚ PRINCIPAL ==========
1. Stock por plataforma
2. Búsqueda de juegos por rango de precio
3. Actualizar precio de juego
4. Agregar juego
5. Eliminar juego
6. Salir
=====================================
""")
    
    match leer_opcion():
        
        case 1:
            busqueda = input("Nombre de la plataforma?: ").strip()
            stock_plataforma(busqueda,d_juegos,d_inventario)
        case 2:
            
            try:
                minimo = int(input("Precio minimo?: "))
                
                if minimo < 0:
                    print("El precio minimo no puede ser menor que 0.")
                    sleep(3)
                    continue
                
                maximo = int(input("Precio maximo?: "))
                
                if maximo < 0:
                    print("El precio maximo no puede ser menor que 0.")
                    sleep(3)
                    continue
                
                if maximo < minimo or minimo > maximo:
                    print("El precio menor no puede ser mayor que el maximo y viseversa.")
                    sleep(3)
                    continue
                
                busqueda_precio(minimo, maximo, d_juegos,d_inventario)
                
            except ValueError:
                print("Debe ingresar valores enteros, no letras o caracteres especiales.")
                sleep(3)
                continue
            
        case 3:
            while True:
                codigo_a_buscar = input("Cual es el codigo del juego? ('GXXX'): ").strip().upper()
                
                status = buscar_codigo(codigo_a_buscar,d_inventario)
                
                if status:
                    nuevo_valor = int(input(("El codigo existe. Cual es el nuevo valor del producto?: ")))
                    
                    resultado = actualizar_precio(codigo_a_buscar,nuevo_valor,d_inventario)
                    
                    if resultado:
                        print(f"Precio actualizado.")
                    elif not resultado:
                        print(f"El codigo no existe")
                        
                    again = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
                    
                    if again == "s":
                        continue
                    elif again == "n":
                        break
                    
                elif not status:
                    print("El codigo ingresado no existe.")
                    continue
            
        case 4:
            while True:
                try:

                    codigo = input("Codigo del juego?: ").strip().upper()
                    c_codigo = check_codigo(codigo,d_juegos)

                    if c_codigo:
                        pass
                    elif not c_codigo:
                        print("El codigo no puede tener/ser solo espacios en blanco o ya esta registrado.")
                        sleep(2)
                        break
                    
                    titulo = input("Titulo del juego?: ").strip()
                    c_titulo = check_titulo(titulo)
                    
                    if c_titulo:
                        pass
                    elif not c_titulo:
                        print("El titulo no puede estar vacio o ser solo espacios en blanco.")
                        sleep(2)
                        break
                    
                    plataforma = input("Plataforma del juego?: ").strip()
                    c_plat = check_plataforma(plataforma)
                    
                    if c_plat:
                        pass
                    elif not c_plat:
                        print("El nombre de la plataforma no puede estar vacio o ser solo espacios en blanco.")
                        sleep(2)
                        break
                    
                    genero = input("Genero del juego?: ").strip()
                    c_genero = check_genero(genero)
                    
                    if c_genero:
                        pass
                    elif not c_genero:
                        print("El nombre del genero no puede estar vacio o ser solo espacios en blanco.")
                        sleep(2)
                        break
                    
                    clasificacion = input("Clasificacion del juego?: ").strip().upper()
                    c_clasificacion = check_clasificacion(clasificacion)
                    
                    if c_clasificacion:
                        pass
                    elif not c_clasificacion:
                        print("La clasificacion no es valida. Tiene que ser 'E', 'T' o 'M' ")
                        sleep(2)
                        break
                    
                    multiplayer = input("El juego es multijugador? (s/n): ").strip().lower()
                    c_multiplayer = check_multiplayer(multiplayer)
                    
                    editor = input("Editor del juego?: ").strip()
                    c_editor = check_editor(editor)
                    
                    if c_editor:
                        pass
                    elif not c_editor:
                        print("El nombre del editor no puede estar vacio o ser solo espacios en blanco.")
                        sleep(2)
                        break
                    
                    precio = int(input("Precio del juego?: "))
                    c_precio = check_precio(precio)
                    
                    if c_precio:
                        pass
                    elif not c_precio:
                        print("El precio tiene que ser mayor a 0.")
                        sleep(2)
                        break
                    
                    stock = int(input("Stock del juego?: "))
                    c_stock = check_stock(stock)
                    
                    if c_stock:
                        pass
                    elif not c_stock:
                        print("El stock tiene que ser igual o mayor a 0.")
                        sleep(2)
                        break
                    
                    add = agregar_juego(codigo,titulo,plataforma,genero,clasificacion,multiplayer,editor,precio,stock,d_juegos,d_inventario)
                    
                    if add:
                        print("Juego agregado.")
                        sleep(2)
                        break
                    elif not add:
                        print("El codigo ya existe.")
                        sleep(2)
                        break
                    
                except ValueError:
                    print("El dato ingresado no es valido en su tipo.")
                    sleep(2)
                    continue
                
        case 5:
            codigo = input("El codigo del juego a eliminar?: ").strip().upper()
            
            check = buscar_codigo(codigo,d_inventario)
            
            if check:
                e_check = eliminar_juego(codigo,d_juegos,d_inventario)
                if e_check:
                    print("Juego eliminado.")
                    sleep(2)
                    continue
                elif not e_check:
                    print("El codigo no existe.")
                    sleep(2)
                    continue
            elif not check:
                print("El codigo no existe.")
                sleep(2)
                continue

        case 6:
            break
            
        case -1:
            print("La opcion ingresada esta fuera de rango. Intentelo de nuevo.")
            sleep(3)
            continue
        
print("Programa finalizado.")