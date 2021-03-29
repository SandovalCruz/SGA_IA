## Cosas que se van a pedir
## Poblacion inicial
## Maximo de Poblacion
## Numero de Generaciones
## Numero de la cadena de Bits
## Maximo de x
## Minimo de x
## Posibilidad de Mutación por Individuo
## Posibilidad de Mutación por Gen
import os
from Algorithm import Process_SGA

def Def_dx():
    Valx = 0
    for item in range(Bits_size):
        Valx += pow(2,item)
    Valx += 1
    return abs((Max_x - Min_x)/(Valx))

def Def_dy():
    Valy = 0
    for item in range(Bits_size):
        Valy += pow(2,item)
    Valy += 1
    return abs((Max_y - Min_y)/(Valy))

def Def_dz():
    Valz = 0
    for item in range(Bits_size):
        Valz += pow(2,item)
    Valz += 1
    return abs((Max_z - Min_z)/(Valz))

if __name__ == "__main__":
    os.system("clear")
    Init_Population = 0
    Max_Population = 0
    Generations = 0
    Bits_size = 0
    Max_x = 0
    Min_x = 0
    Max_y = 0
    Min_y = 0
    Max_z = 0
    Min_z = 0
    P_Mutation = 0
    P_Mutation_gen = 0
    Dx = 0
    Dy = 0
    Dz = 0
    Address = 0

    print("========================================================================================================================================================================================================================================================================================================================================================================================================================")

    Descicion = int(input("\n Menu de opciones \n 1.- Usar las configuraciones guardadas \n 2.- agregar nuevos datos \n "))
    if Descicion == 1 or Descicion == 2:
        if Descicion == 1:
            Init_Population = 14
            Max_Population = 30
            Generations = 100
            Bits_size = 12
            Max_x = 4.5678766
            Min_x = 4.2340543
            Max_y = 3.1252376
            Min_y = 3.0012422
            Max_z = 2.9531344
            Min_z = 2.4912432
            P_Mutation = .2
            P_Mutation_gen = .12
            Address = 1
        else:
            ##
            Init_Population = int(input("Introduce el numero de individuos al iniciar → "))
            if Init_Population <= 1 or (Init_Population % 2) != 0:
                while True:
                    Init_Population = int(input("Introduce el numero de individuos al iniciar \n ('estos deben ser mayores a 1 y pares') → "))
                    if Init_Population >= 2  and (Init_Population % 2) == 0:
                        break

            ##
            Max_Population = int(input("introduce el numero maximo de poblacion por generacion → "))
            if Max_Population < 10:
                while True:
                    Max_Population = int(input("introduce el numero maximo de poblacion por generacion \n ('De preferencia que sean mayores a 9') → "))
                    if Max_Population >= 10:
                        break

            ##
            Generations = int(input("Introduce el numero de Generaciones para el muestreo → "))
            if Generations < 1:
                while True:
                    Generations = int(input("Introduce el numero de Generaciones para el muestreo → "))
                    if Generations > 1:
                        break

            ##
            Bits_size = int(input("Introduce el numero de Bits que deseas tener para todas las cadenas → "))
            if Bits_size < 8:
                while True:
                    Bits_size = int(input("Introduce el numero de Bits que deseas tener ¡¡¡Valido!!! → "))
                    if Bits_size >= 8:
                        break

            ##
            Max_x = float(input("Introduce un Maximo de X → "))

            ##
            Min_x = float(input("Introduce un Minimo de X → "))
            if Max_x < Min_x:
                while True:
                    Min_x = float(input("Introduce un Minimo de x  menor al Maximo de x → "))
                    if Max_x > Min_x:
                        break

            ##
            Max_y = float(input("Introduce un Maximo de y → "))

            ##
            Min_y = float(input("Introduce un Minimo de y → "))
            if Max_y < Min_y:
                while True:
                    Min_y = float(input("Introduce un Minimo de y  menor al Maximo de y → "))
                    if Max_y > Min_y:
                        break

            ##
            Max_z = float(input("Introduce un Maximo de z → "))

            ##
            Min_z = float(input("Introduce un Minimo de z → "))
            if Max_z < Min_z:
                while True:
                    if Max_z > Min_z:
                        Min_z = float(input("Introduce un Minimo de z  menor al Maximo de z → "))
                        break

            ##
            P_Mutation = float(input("Introduce la probabilidad de que un especimen mute Ejem → 0.008 ó 0.7 → "))
            if P_Mutation < 0 and P_Mutation > 1:
                while True:
                    P_Mutation = float(input("Introduce la probabilidad de que un especimen mute Ejem → 0.008 ó 0.7 → "))
                    if P_Mutation > 0 and P_Mutation < 1:
                        break

            ##
            P_Mutation_gen = float(input("Introduce la probabilidad de que el gen de un especimen mute Ejem → 0.008 ó 0.7 → "))
            if P_Mutation_gen < 0 and P_Mutation_gen > 1:
                while True:
                    P_Mutation_gen = float(input("Introduce la probabilidad de que el gen de un especimen mute Ejem → 0.008 ó 0.7 → "))
                    if P_Mutation_gen > 0 and P_Mutation_gen < 1:
                        break


            Address = int(input('Introduce el camino a elegir en 1.-Maximizar 2.-Minimizar → '))
            if Address != 1 or Address != 2:
                while True:
                    Address = int(input('Introduce el camino a elegir en 1.-Maximizar 2.-Minimizar → '))
                    if Address == 1 or Address == 2:
                        break
        Dx = Def_dx()
        Dy = Def_dy()
        Dz = Def_dz()


        print("============================================== Datos del Ejercicio ==============================================")
        print('{  Poblacion Inicial: ', Init_Population, ' Población Maxima: ', Max_Population, ' Numero de generaciones: ', Generations, ' Tamaño de Bits: ', Bits_size, '  }')
        print('{  Maximo de X: ', Max_x, ' Minimo de X. ', Min_x, 'Maximo de y: ', Max_y, ' Minimo de y. ', Min_y, 'Maximo de z: ', Max_z, ' Minimo de z. ', Min_z, '}')
        print(' Probabilidad de Mutación: ', P_Mutation, ' Probabilidad de Mutacion por Gen: ', P_Mutation_gen, 'Dx: ', Dx, 'Dy: ', Dy, 'Dz: ', Dz, '  }')

        Opcion  = str(input("Deseas Continuar con el ejercicion S Ó N → "))
        if Opcion == "S" or Opcion == "s":
            Process_SGA.Start_SGA(Init_Population, Max_Population, Generations, Bits_size, Max_x, Min_x, Max_y, Min_y, Max_z, Min_z, P_Mutation, P_Mutation_gen, Dx, Dy, Dz, Address)
        else:
            print('prueba de nuevo para hacer las correcciones necesarias :D :) :P')

    else:
        print('Elegiste mal vuelve a intentarlo')