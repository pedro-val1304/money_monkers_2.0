#Estas son las listas.
nameList = ["EMILIANO", "ALLISON", "NAOMI", "NATALIA", "PEDRO", "JOSE", "DIEGO", "ABRIL", "GRECIA", "MISAEL", "ALBERTO", "ELIAS", "ANGEL","GLORIA"]
surList = ["BECERRA", "FACIO", "JIMENEZ", "RODRIGUEZ", "GUTIERREZ", "VALENZUELA", "VIDRIO", "MORA", "VALDIVIA", "IBARRA", "ORNELAS", "ZEPEDA", "GRANADOS", "ALVAREZ"]
codeList = ["224164515", "219439208", "220520973", "221925365", "221453145", "221568619", "224164513", "221964573", "216548448", "224164491", " 218466716", "220571586", " 218220776", "221851264"]
pList = [80, 90, 90, 70, 50, 100, 85, 95, 77, 98, 50, 65, 79, 100] #Programación
fList = [60, 100, 70, 80, 83, 100, 94, 65, 97, 85, 100, 90, 100, 100 ] #Física
qList = [70, 80, 100, 90, 100, 90, 100, 80, 100, 90, 100, 100, 90, 100] #Química
cList = [90, 70, 95, 73, 90, 100, 55, 69, 100, 100, 84, 89, 88, 90] #CB
asisList = [15, 36, 40, 33, 19, 5, 10, 34, 18, 20, 23, 26, 38, 39] #Asistencia
absList = [25, 4, 0, 7, 21, 35, 30, 6, 22, 20, 17, 14, 2, 1] #Faltas
ageList = [19, 20, 22, 18, 18, 18, 19, 18, 24, 18, 21, 19, 22, 18] #Edad
carList = ["LTBI", "LTBI", "LTBI","LTBI","LTBI","LTBI","LTBI","LTBI","LTBI","LTBI","LTBI","LTBI","LTBI","LTBI",] #Carrera
Listade = ["LC", "LCD", "LIACD", "LIFN", "LTB"]
    
#Definiendo función para checar
def validar_input(mensaje, tipo="alfabetico", rango=None):
    while True:
        valor = input(mensaje).upper() if tipo == "alfabetico" else input(mensaje)
        if tipo == "alfabetico":
            if valor.isalpha():
                return valor
            else:
                print("La entrada debe contener solo letras.")
        elif tipo == "numerico":
            try:
                valor = int(valor)
                return valor
            except ValueError:
                print("La entrada debe ser un número.")
        elif tipo == "numerostr":
            if valor.isnumeric():
                return valor
            else:
                print("La entrada debe contener solo números.")
        elif tipo == "rango":
            try:
                valor = float(valor)
                if rango[0] <= valor <= rango[1]:
                    return valor
                else:
                    print(f"La entrada debe estar entre {rango[0]} y {rango[1]}.")
            except ValueError:  
                print("Por favor, ingrese un número válido.")
        else:
            print("Tipo de validación no soportado.")
#Variables para cuando agregamos calificaciones o borramos a alguien
borrar = str
caP = float
caf = float
caQ = float
caC = float
med = float
mod = int
asis = int

#Loop while True, mientras que no escogemos la opción de salir.
while True:
    try:
        try:
            print ("1: Agregar nuevo estudiante")
            print ("2: Datos de estudiante")
            print ("3: Eliminar estudiante")
            print ("4: Modificar información de estudiante")
            print ("5: Mostrar lista de estudiantes")
            print ("6: Almacenar las notas de un estudiante")
            print ("7: Promedio de estudiante")
            print ("8: Generar un reporte de notas de un estudiante")
            print ("9: Almacenar asistencia de un estudiante")
            print ("10: Generar un reporte de asistencia de un estudiante")
            print ("11: Para cerrar el programa")
            print ("")
            opcion = int(input("¿Qué desea hacer?: "))

        #Agregar nuevo 1
            if opcion == 1:
                nameList.append(str(input("Ingrese su nombre: ")).upper()) #Lo que hace esto es que va a guardar todo en la posición que sigue, esa es la función de .append
                surList.append(str(input("Ingrese su apellido: ")).upper()) # .upper hace que el valor sin importar como lo escriban se registre en mayúsculas nomas.
                codeList.append(str(input("Ingrese su código: ")))
                ageList.append(str(input("Ingrese su edad: ")))
                carList.append(str(input("Ingrese su carrera (LTBI, LCD, LDIA, LCS, LIF): ")).upper())
                pList.append(float(input("Ingrese su calificación de Programación 1 (0 - 100): ")))
                fList.append(float(input("Ingrese su calificación de Física (0 - 100): ")))
                qList.append(float(input("Ingrese su calificación de Química (0 - 100): ")))
                cList.append(float(input("Ingrese su calificación de Ciencias Biológicas (0 - 100): ")))
                asisList.append(int(input("Ingrese las asistencias del estudiante (0 - 100): ")))
                absList.append(int(input("Ingrese las faltas del estudiante: ")))

        #Identificar 2
            elif opcion == 2:
                ident = input("Ingresa el identificador: ").upper() #ident es la variable que es un identificador, puede ser nombre, apellido, codigo.
                if ident in nameList: # Si esta en el nombre
                     print("Su nombre es:", nameList[nameList.index(ident)]) #nameList[nameList.index(ident)] Hace que en la lista de nombres se imprima el de la posición del nombre o código que se pone
                     print("Su apellido es:", surList[nameList.index(ident)]) #ident es la variable que se utiliza para saber la posición en la que está el input. Osea, allison es la posición 1
                     print("Su código es:", codeList[nameList.index(ident)]) # entonces se va a imprimir todo lo de las bases de datos de la posición 1
                     print("Su edad es:", ageList[nameList.index(ident)])
                     print("Su carrera es:", carList[nameList.index(ident)])
                elif ident in surList:
                     print("Su nombre es:", nameList[surList.index(ident)])
                     print("Su apellido es:", surList[surList.index(ident)])
                     print("Su código es:", codeList[surList.index(ident)])
                     print("Su edad es:", ageList[surList.index(ident)])
                     print("Su carrera es:", carList[surList.index(ident)])
                elif ident in codeList:
                     print("Su nombre es:", nameList[codeList.index(ident)])
                     print("Su apellido es:", surList[codeList.index(ident)])
                     print("Su código es:", codeList[codeList.index(ident)])
                     print("Su edad es:", ageList[codeList.index(ident)])
                     print("Su carrera es:", carList[codeList.index(ident)])
                else:
                    print("El estudiante no se encuentra en la lista")

        #Eliminar 3
            elif opcion == 3:
                ident = input("Ingresa el identificador: ").upper()
                if ident in nameList: #Si el input esta en la lista de nombres, entonces arrancar el programa
                    print("El estudiante:", nameList[nameList.index(ident)], surList[nameList.index(ident)], "ha sido borrado")
                    borrar = nameList.index(ident) #Esta variable se iguala al de la posición de la lista en la que ident se encuentra, es decir. Si ident encuentra a Emiliano en la posición 0, borrar sera igual a 0 y por ende borrara todos los valores de toda la lista en la posición 0
                    nameList.pop(borrar) #.pop es para borrar en la lista, justamnete usando borrar coo
                    surList.pop(borrar)
                    codeList.pop(borrar)
                    pList.pop(borrar)
                    fList.pop(borrar)
                    qList.pop(borrar)
                    cList.pop(borrar)
                    asisList.pop(borrar)
                    absList.pop(borrar)
                    ageList.pop(borrar)
                    carList.pop(borrar)

                elif ident in surList: #Si no, entonces buscar en los apellidos
                    print("El estudiante:", nameList[surList.index(ident)], surList[surList.index(ident)], "ha sido borrado")
                    borrar = surList.index(ident) #Hace lo mismo, pero en la lista de apellidos
                    nameList.pop(borrar)
                    surList.pop(borrar)
                    codeList.pop(borrar)
                    pList.pop(borrar)
                    fList.pop(borrar)
                    qList.pop(borrar)
                    cList.pop(borrar)
                    asisList.pop(borrar)
                    absList.pop(borrar)
                    ageList.pop(borrar)
                    carList.pop(borrar)

                elif ident in codeList: #Si no buscar en los códigos
                    print("El estudiante:", nameList[codeList.index(ident)], surList[codeList.index(ident)], "ha sido borrado")
                    borrar = codeList.index(ident) #Lo mismo pero busca en la lista de códigos
                    nameList.pop(borrar)
                    surList.pop(borrar)
                    codeList.pop(borrar)
                    pList.pop(borrar)
                    fList.pop(borrar)
                    qList.pop(borrar)
                    cList.pop(borrar)
                    asisList.pop(borrar)
                    absList.pop(borrar)
                    ageList.pop(borrar)
                    carList.pop(borrar)

                else: #Ya si deplano no, no se encuentra en la lista
                    print("El estudiante no se encuentra en la lista")

        #Modificar 4
            elif opcion == 4:
                ident = input("Ingresa el identificador: ").upper()
                if ident in nameList: #Funciona igual en todos los programas
                    mod=nameList.index(ident)
                    nameList[mod]=input(str("Ingrese nuevo nombre: ").upper()) #Va a modificar todo lo de la posicón en la que esta el ident. Mod es una variable que se iguala a la posición en la
                    surList[mod]=input(str("Ingrese nuevo apellido: ").upper()) #que se encuentra el ident. Es decir, si el input esta en la posición 2, se van a modificar todas las listas
                    codeList[mod]=input(str("Ingrese nuevo código: ")) #en la posición 2. Se va a modificar la carrera de la posición 2, el nombre de la posición 2 y todas las listas de la posición 2
                    ageList[mod]=input(int("Ingrese su nueva edad: "))
                    carList[mod]=input(str("Ingrese su nueva carrera: ").upper())
                    pList[mod]=float(input("Ingrese nueva calificación de Programación 1 (0 - 100):  "))
                    fList[mod]=float(input("Ingrese nueva calificación de Física (0 - 100): "))
                    qList[mod]=float(input("Ingrese nueva calificación de Química (0 - 100): "))
                    cList[mod]=float(input("Ingrese nueva calificación de Biología (0 - 100): "))
                    asisList[mod]=int(input("Ingrese nuevas asistencias: "))
                    absList[mod]=int(input("Ingrese nuevas faltas: "))
                elif ident in surList:
                    mod=surList.index(ident)
                    nameList[mod]=input(str("Ingrese nuevo nombre: ").upper()) #Lo mismo, pero busca la posición en la lista de apellidos, es decir, si becerra esta en la posición 0, se van a modificar la posición 0 de todas las listas
                    surList[mod]=input(str("Ingrese nuevo apellido: ").upper())
                    codeList[mod]=input(str("Ingrese nuevo código: "))
                    ageList[mod]=input(int("Ingrese su nueva edad: "))
                    carList[mod]=input(str("Ingrese su nueva carrera: ").upper())
                    pList[mod]=float(input("Ingrese nueva calificación de Programación 1 (0 - 100): "))
                    fList[mod]=float(input("Ingrese nueva calificación de Física (0 - 100): "))
                    qList[mod]=float(input("Ingrese nueva calificación de Química (0 - 100): "))
                    cList[mod]=float(input("Ingrese nueva calificación de Biología (0 - 100): "))
                    asisList[mod]=int(input("Ingrese nuevas asistencias: "))
                    absList[mod]=int(input("Ingrese nuevas faltas: "))
                elif ident in codeList:
                    mod=codeList.index(ident)
                    nameList[mod]=input(str("Ingrese nuevo nombre: ").upper()) #Lo mismo, pero en el código
                    surList[mod]=input(str("Ingrese nuevo apellido: ").upper())
                    codeList[mod]=input(str("Ingrese nuevo código: "))
                    ageList[mod]=input(int("Ingrese su nueva edad: "))
                    carList[mod]=input(str("Ingrese su nueva carrera: ").upper())
                    pList[mod]=float(input("Ingrese nueva calificación de Programación 1 (0 - 100): "))
                    fList[mod]=float(input("Ingrese nueva calificación de Física (0 - 100): "))
                    qList[mod]=float(input("Ingrese nueva calificación de Química (0 - 100): "))
                    cList[mod]=float(input("Ingrese nueva calificación de Biología (0 - 100): "))
                    asisList[mod]=int(input("Ingrese nuevas asistencias: "))
                    absList[mod]=int(input("Ingrese nuevas faltas: "))
                else:
                    print("El estudiante no se encuentra en la lista")

        #Lista de estudiantes 5
            elif opcion == 5:
                nombre_completo = [f"{nombre} {apellido}" for nombre, apellido in zip(nameList, surList)] #nombre_completo es una lista anidada que muestra en paralelo.
                print(nombre_completo)
                
        #Almacenar calificaciones 6
            elif opcion == 6:
                ident = input("Ingresa el identificador: ").upper()
                if ident in nameList:
                    mod=nameList.index(ident) #Es una variable que se va a igualar a la posición en la que ident encuentre a su simil. Es decir, el usuario pone Emiliano, Emiliano en la lista esta en la posición 0. Mod se va a igualar a 0
                    print("Almacenando calificaciones del estudiante:", nameList[nameList.index(ident)], surList[nameList.index(ident)])
                    pList[mod]=float(input("Ingrese nueva calificación de Programación 1 (0 - 100): ")) #Va a almacenar las calificación en la posición en la que ident encuentre en la base de datos, es decir, va a modificar todas las posiciones 0 si ident esta en la posición 0
                    fList[mod]=float(input("Ingrese nueva calificación de Física (0 - 100): "))
                    qList[mod]=float(input("Ingrese nueva calificación de Química (0 - 100): "))
                    cList[mod]=float(input("Ingrese nueva calificación de Biología (0 - 100): "))
                elif ident in surList:
                    mod=surList.index(ident)
                    print("Almacenando calificaciones del estudiante:", nameList[surList.index(ident)], surList[surList.index(ident)])
                    pList[mod]=float(input("Ingrese nueva calificación de Programación 1 (0 - 100): "))
                    fList[mod]=float(input("Ingrese nueva calificación de Física (0 - 100): "))
                    qList[mod]=float(input("Ingrese nueva calificación de Química (0 - 100): "))
                    cList[mod]=float(input("Ingrese nueva calificación de Biología (0 - 100): "))
                elif ident in codeList:
                    mod=codeList.index(ident)
                    print("Almacenando calificaciones del estudiante:", nameList[codeList.index(ident)], surList[codeList.index(ident)])
                    pList[mod]=float(input("Ingrese nueva calificación de Programación 1 (0 - 100): "))
                    fList[mod]=float(input("Ingrese nueva calificación de Física (0 - 100): "))
                    qList[mod]=float(input("Ingrese nueva calificación de Química (0 - 100): "))
                    cList[mod]=float(input("Ingrese nueva calificación de Biología (0 - 100): "))
                else:
                    print("El estudiante no se encuentra en la lista")
                    
        #Promedio de estudiante 7
            elif opcion == 7:
                ident = input("Ingresa el identificador: ").upper()
                if ident in nameList:
                    caP = pList[nameList.index(ident)] #Aquí son variables que se igualan a la calificación, definida por la posición en la que el ident encuentra. Como ha estado funcionando el código en general
                    caF = fList[nameList.index(ident)]
                    caQ = qList[nameList.index(ident)]
                    caC = cList[nameList.index(ident)]
                    med = (caP+caF+caQ+caC)/4
                    print("El promedio de", nameList[nameList.index(ident)], surList[nameList.index(ident)], "es:") 
                    print(med)
                elif ident in surList:
                    caP = pList[surList.index(ident)]
                    caF = fList[surList.index(ident)]
                    caQ = qList[surList.index(ident)]
                    caC = cList[surList.index(ident)]
                    med = (caP+caF+caQ+caC)/4
                    print("El promedio de", nameList[surList.index(ident)], surList[surList.index(ident)], "es:")
                    print(med)    
                elif ident in codeList:
                    caP = pList[codeList.index(ident)]
                    caF = fList[codeList.index(ident)]
                    caQ = qList[codeList.index(ident)]
                    caC = cList[codeList.index(ident)]
                    med = (caP+caF+caQ+caC)/4
                    print("El promedio de", nameList[codeList.index(ident)], surList[codeList.index(ident)], "es:")
                    print(med)
                else:
                    print("El estudiante no se encuentra en la lista")

        #Generar reporte 8
            elif opcion == 8:
                ident = input("Ingresa el identificador: ").upper()
                if ident in nameList:
                    print("Reporte de calificaciones del estudiante:", nameList[nameList.index(ident)], surList[nameList.index(ident)]) #Funciona igual que lo que dice abajo
                    print("Su calificación de programación 1 es:", pList[nameList.index(ident)]) #Va a buscar en la lista de calificaciones de programación, que valor esta en la posición en la que esta ident, es decir, si ident es igual a Emiliano y  
                    print("Su calificación de Física es:", fList[nameList.index(ident)]) #este esta en la posición 0, se va a imprimir de la lista de calificaciones lo que está en la posicion 0.
                    print("Su calificación de Química es:", qList[nameList.index(ident)])
                    print("Su calificación de Ciencias Biológicas es:", cList[nameList.index(ident)])
                elif ident in surList:
                    print("Reporte de calificaciones del estudiante:", nameList[surList.index(ident)], surList[surList.index(ident)])
                    print("Su calificación de programación 1 es:", pList[surList.index(ident)])
                    print("Su calificación de Física es:", fList[surList.index(ident)])
                    print("Su calificación de Química es:", qList[surList.index(ident)])
                    print("Su calificación de Ciencias Biológicas es:", cList[surList.index(ident)])
                elif ident in codeList:
                    print("Reporte de calificaciones del estudiante:", nameList[codeList.index(ident)], surList[codeList.index(ident)])
                    print("Su calificación de programación 1 es:", pList[codeList.index(ident)])
                    print("Su calificación de Física es:", fList[codeList.index(ident)])
                    print("Su calificación de Química es:", qList[codeList.index(ident)])
                    print("Su calificación de Ciencias Biológicas es:", cList[codeList.index(ident)])
                else:
                    print("El estudiante no se encuentra en la lista")

        # Asistencia 9
            elif opcion == 9:
                ident = input("Ingresa el identificador: ").upper()
                if ident in nameList:
                    asis = nameList.index(ident)
                    print("Almacenando asistencias del estudiante:", nameList[nameList.index(ident)], surList[nameList.index(ident)])
                    asistencias = int(input("Ingrese nuevas asistencias: "))
                    inasistencias = int(input("Ingrese nuevas faltas: "))
                    if asistencias+inasistencias <= 40:
                        asisList[asis] = asistencias
                        absList[asis] = inasistencias
                    else:
                        print("El límite de asistencias es 40 y el de inasistencias es 6.")
                elif ident in surList:
                    asis = surList.index(ident)
                    print("Almacenando asistencias del estudiante:", nameList[surList.index(ident)], surList[surList.index(ident)])
                    asistencias = int(input("Ingrese nuevas asistencias: "))
                    inasistencias = int(input("Ingrese nuevas faltas: "))
                    if asistencias+inasistencias <= 40:
                        asisList[asis] = asistencias
                        absList[asis] = inasistencias
                    else:
                        print("El límite de asistencias es 40 y el de inasistencias es 6.")
                elif ident in codeList:
                    asis = codeList.index(ident)
                    print("Almacenando asistencias del estudiante:", nameList[codeList.index(ident)], surList[codeList.index(ident)])
                    asistencias = int(input("Ingrese nuevas asistencias: "))
                    inasistencias = int(input("Ingrese nuevas faltas: "))
                    if asistencias+inasistencias <= 40:
                        asisList[asis] = asistencias
                        absList[asis] = inasistencias
                    else:
                        print("El límite de asistencias es 40 y el de inasistencias es 6.")
                else:
                    print("El estudiante no se encuentra en la lista")

        #Reporte de Asistencia 10
            elif opcion == 10: #Funciona igual que las calificaciones 
                ident = input("Ingresa el identificador: ").upper()
                if ident in nameList:
                    print("Reporte de asistencias del estudiante:", nameList[nameList.index(ident)], surList[nameList.index(ident)])
                    print("Sus asistencias son:", asisList[nameList.index(ident)])
                    print("Sus faltas son:", absList[nameList.index(ident)])
                    if absList[nameList.index(ident)] >= 6:
                        print("El estudiante ha reprobado por faltas")
                    else:
                        print("El estudiante sigue en el curso")
                elif ident in surList:
                    print("Reporte de asistencias del estudiante:", nameList[surList.index(ident)], surList[surList.index(ident)])
                    print("Sus asistencias son:", asisList[surList.index(ident)])
                    print("Sus faltas son:", absList[surList.index(ident)])
                    if absList[nameList.index(ident)] >= 6:
                        print("El estudiante ha reprobado por faltas")
                    else:
                        print("El estudiante sigue en el curso")
                elif ident in codeList:
                    print("Reporte de asistencias del estudiante:", nameList[codeList.index(ident)], surList[codeList.index(ident)])
                    print("Sus asistencias son:", asisList[codeList.index(ident)])
                    print("Sus faltas son:", absList[codeList.index(ident)])
                    if absList[nameList.index(ident)] >= 6:
                        print("El estudiante ha reprobado por faltas")
                    else:
                        print("El estudiante sigue en el curso")
        #Cerrar
            elif opcion == 11:
                print("¡Hasta luego!")
                break

            print("---------------------------------------------------------------------")
        
        except IndexError:
            print("No estan hay suficientes datos de este estudiante")
            print("---------------------------------------------------------------------")

    except ValueError:
        print("Elija un valor valido")
        print("---------------------------------------------------------------------")
