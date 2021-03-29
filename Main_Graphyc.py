import os
from Algorithm import Process_SGA
from tkinter import *
import tkinter as tk

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

def CheckValues(Init_Population, Max_Population, Generations, Bits_size, Max_x, Min_x, Max_y, Min_y, Max_z, Min_z, P_Mutation, P_Mutation_gen, Address):
    error = 0
    Message = ''
    #if Init_Population.e, Max_Population, Generations, Bits_size, Max_x, Min_x, Max_y, Min_y, Max_z, Min_z, P_Mutation, P_Mutation_gen, Address:

    if Init_Population <= 1 or (Init_Population % 2) != 0:
        error +=1
        Message += 'Error de Poblacion inicial\n'
        Message += 'Se introdujo una poblacion inicial menor a la esperada → ' + str(Init_Population) + '. \nSe recomienda que la poblacion sea mayor a 1 y en su defecto que sea par. \n'

    if Max_Population <= 10:
        error += 1
        Message += 'Error de Poblacion Maxima \n'
        Message += 'La Poblacion maxima no puede ser menor a  → ' + str(Max_Population) + ', se espera que esta sea mayor a 10.\n'

    if Generations < 1:
        error += 1
        Message += 'Error de el numero de generaciones\n'
        Message += 'Se recomienda que las generaciones no sean menores a → ' + str(Generations) + '. \n'

    if Bits_size < 8:
        error += 1
        Message += 'Error del Tamaño de bits\n'
        Message += 'El Tamaño de bit propuesto va encontra de los parametros minimos que este programa pide\nse recomieda que este sea mayor o igual a 8. \n'

    if Max_x <= Min_x:
        error += 1
        Message += 'Error de los minimos de x\n'
        Message += 'El maximo de X es menor al minimo de este se recomienda que no sea menor que el minimo propuesto. \n'

    if Max_y <= Min_y:
        error += 1
        Message += 'Error de los minimos de y\n'
        Message += 'El maximo de y es menor al minimo de este se recomienda que no sea menor que el minimo propuesto. \n'

    if Max_z <= Min_z:
        error += 1
        Message += 'Error de los minimos de z\n'
        Message += 'El maximo de z es menor al minimo de este se recomienda que no sea menor que el minimo propuesto. \n'

    if P_Mutation < 0 or P_Mutation > 1:
        error += 1
        Message += 'Error de la mutacion\n'
        Message += 'Se recomienda que la mutacion sea mayor a 0 y menor a 1 . \n'

    if P_Mutation_gen < 0 or P_Mutation_gen > 1:
        error += 1
        Message += 'Error de la mutacion por gen \n'
        Message += 'Se recomienda que la mutacion por gen sea mayor a 0 y menor a 1 . \n'

    if Address == 'Seleccionar..':
        error += 1
        Message += 'Error de la direccion\n'
        Message += 'Solo hay dos caminos maximizar o minimizar \n'

    if error >= 1:
        Message += 'Numero de errores → ' + str(error)

    return error, Message

def Start_Application():
    #result=textExample.get()
    #print(result)
    TextEntry.configure(state='normal')
    Init_Population =int(TextPobInicial.get())
    Max_Population = int(TextPobMax.get())
    Generations = int(TextGeneraciones.get())
    Bits_size = int(TextBitsize.get())
    Max_x = float(TextMaxX.get())
    Min_x = float(TextMinx.get())
    Max_y = float(TextMaxy.get())
    Min_y = float(TextMiny.get())
    Max_z = float(TextMaxz.get())
    Min_z = float(TextMinz.get())
    P_Mutation = float(TextPMutacion.get())
    P_Mutation_gen = float(TextPMutacionGen.get())
    Dx = 0
    Dy = 0
    Dz = 0
    Address = str(variable.get())
    print(Address)

    (result, message) = CheckValues(Init_Population, Max_Population, Generations, Bits_size, Max_x, Min_x, Max_y, Min_y, Max_z, Min_z, P_Mutation, P_Mutation_gen, Address)

    Dx = Def_dx()
    Dy = Def_dy()
    Dz = Def_dz()

    TextEntry.delete(1.0,"end")
    if result == 0:
        listn = []
        Path = 0
        btnRead["state"] = DISABLED
        print("============================================== Datos del Ejercicio ==============================================")
        print('{  Poblacion Inicial: ', Init_Population, ' Población Maxima: ', Max_Population, ' Numero de generaciones: ', Generations, ' Tamaño de Bits: ', Bits_size, '  }')
        print('{  Maximo de X: ', Max_x, ' Minimo de X. ', Min_x, 'Maximo de y: ', Max_y, ' Minimo de y. ', Min_y, 'Maximo de z: ', Max_z, ' Minimo de z. ', Min_z, '}')
        print(' Probabilidad de Mutación: ', P_Mutation, ' Probabilidad de Mutacion por Gen: ', P_Mutation_gen, 'Dx: ', Dx, 'Dy: ', Dy, 'Dz: ', Dz, 'Camino: ', Address, '  }')

        varn = {'Poblacion Inicial': Init_Population, 'Población Maxima': Max_Population, 'Numero de generaciones': Generations, 'Tamaño de Bits': Bits_size },
        listn.extend(varn)
        varn = {'Maximo de X': Max_x, 'Minimo de X': Min_x, 'Maximo de y': Max_y, 'Minimo de y': Min_y, 'Maximo de z': Max_z, 'Minimo de z': Min_z},
        listn.extend(varn)
        varn = {'Probabilidad de Mutación': P_Mutation, 'Probabilidad de Mutacion por Gen': P_Mutation_gen, 'Dx': Dx, 'Dy': Dy, 'Dz': Dz, 'Camino': Address},
        listn.extend(varn)
        if Address == "Minimizar":
            Path = 2
        if Address == "Maximizar":
            Path = 1
        TextEntry.insert(1.0, listn)
        Process_SGA.Start_SGA(Init_Population, Max_Population, Generations, Bits_size, Max_x, Min_x, Max_y, Min_y, Max_z, Min_z, P_Mutation, P_Mutation_gen, Dx, Dy, Dz, Path)
        TextEntry.configure(state='disabled')
    else:
        print('\n\n\n')
        print(message)
        TextEntry.insert(1.0, message)
        TextEntry.configure(state='disabled')


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
    OptionList = [
        "Seleccionar..",
        "Minimizar",
        "Maximizar"
    ]

    root = tk.Tk()

    root.title('SGA Sandoval 173198')

    #Minimo de x
    LableTitle = tk.Label(root, text='Configuración de la Aplicación')
    LableTitle.config(font=('helvetica', 10))
    LableTitle.place(x = 250,y = 5,width=200,height=25)

    #Minimo de x
    LableMinx = tk.Label(root, text='Min X:')
    LableMinx.config(font=('helvetica', 10))
    TextMinx = tk.Entry(root,width=15)
    LableMinx.place(x = 10,y = 50,width=100,height=25)
    TextMinx.place(x = 10,y = 80,width=100,height=20)

    #Maximo de x
    LableMaxX = tk.Label(root, text='Max X:')
    LableMaxX.config(font=('helvetica', 10))
    TextMaxX = tk.Entry(root,width=15)
    LableMaxX.place(x = 130,y = 50,width=100,height=25)
    TextMaxX.place(x = 130,y = 80,width=100,height=20)

    # #Minimo de y
    LableMiny = tk.Label(root, text='Min y:')
    LableMiny.config(font=('helvetica', 10))
    TextMiny = tk.Entry(root,width=15)
    LableMiny.place(x = 250,y = 50,width=100,height=25)
    TextMiny.place(x = 250,y = 80,width=100,height=20)

    # #Maximo de y
    LableMaxy = tk.Label(root, text='Max y:')
    LableMaxy.config(font=('helvetica', 10))
    TextMaxy = tk.Entry(root,width=15)
    LableMaxy.place(x = 370,y = 50,width=100,height=25)
    TextMaxy.place(x = 370,y = 80,width=100,height=20)

    # #Minimo de z
    LableMinz = tk.Label(root, text='Min z:')
    LableMinz.config(font=('helvetica', 10))
    TextMinz = tk.Entry(root,width=15)
    LableMinz.place(x = 490,y = 50,width=100,height=25)
    TextMinz.place(x = 490,y = 80,width=100,height=20)

    # #Maximo de z
    LableMaxz = tk.Label(root, text='Max z:')
    LableMaxz.config(font=('helvetica', 10))
    TextMaxz = tk.Entry(root,width=15)
    LableMaxz.place(x = 610,y = 50,width=100,height=25)
    TextMaxz.place(x = 610,y = 80,width=100,height=20)

    #Poblacion Inicial
    LabelPobInicial = tk.Label(root, text='Poblacion Inicial:')
    LabelPobInicial.config(font=('helvetica', 10))
    TextPobInicial = tk.Entry(root,width=15)
    LabelPobInicial.place(x = 50,y = 110,width=120,height=25)
    TextPobInicial.place(x = 50,y = 140,width=120,height=20)

    # Poblacion Maxima
    LabelpobMax = tk.Label(root, text='Poblacion Maxima:')
    LabelpobMax.config(font=('helvetica', 10))
    TextPobMax = tk.Entry(root,width=15)
    LabelpobMax.place(x = 200,y = 110,width=120,height=25)
    TextPobMax.place(x = 200,y = 140,width=120,height=20)

    #Generaciones
    LabelGeneraciones = tk.Label(root, text='Generaciones:')
    LabelGeneraciones.config(font=('helvetica', 10))
    TextGeneraciones = tk.Entry(root,width=15)
    LabelGeneraciones.place(x = 350,y = 110,width=120,height=25)
    TextGeneraciones.place(x = 350,y = 140,width=120,height=20)

    #Numero de Bits
    LabelBitsize = tk.Label(root, text='Tamño de Bits:')
    LabelBitsize.config(font=('helvetica', 10))
    TextBitsize = tk.Entry(root,width=15)
    LabelBitsize.place(x = 500,y = 110,width=120,height=25)
    TextBitsize.place(x = 500,y = 140,width=120,height=20)

    # P Mutacion
    LabelPMutacion = tk.Label(root, text='P Mutacion:')
    LabelPMutacion.config(font=('helvetica', 10))
    TextPMutacion = tk.Entry(root,width=15)
    LabelPMutacion.place(x = 100,y = 170,width=120,height=25)
    TextPMutacion.place(x = 100,y = 200,width=120,height=20)

    #P Mutacion Gen
    LabelMutacionGen = tk.Label(root, text='P Mutacion Gen:')
    LabelMutacionGen.config(font=('helvetica', 10))
    TextPMutacionGen = tk.Entry(root,width=15)
    LabelMutacionGen.place(x = 250,y = 170,width=120,height=25)
    TextPMutacionGen.place(x = 250,y = 200,width=120,height=20)

    #Path
    LabelPath = tk.Label(root, text='Minimizar o Maximizar:')
    LabelPath.config(font=('helvetica', 10))
    variable = tk.StringVar(root)
    variable.set(OptionList[0])
    SelectPath = tk.OptionMenu(root, variable, *OptionList)
    LabelPath.place(x = 400,y = 170,width=160,height=25)
    SelectPath.place(x = 400,y = 200,width=160,height=20)

    #Result
    LabelEntry = tk.Label(root, text='Resultados Configuracion:')
    LabelEntry.config(font=('helvetica', 10))
    LabelEntry.place(x = 260,y = 230,width=160,height=20)
    TextEntry=tk.Text(root, height=10)
    TextEntry.place(x = 5,y = 260,width=705,height=120)

    btnRead=tk.Button(root, height=1, width=15, text="Iniciar Algoritmo",command=Start_Application)
    btnRead.place(x = 260,y = 400,width=150,height=30)

    # btnRead.pack()
    root.geometry("720x450")
    root.resizable(0,0)
    root.mainloop()