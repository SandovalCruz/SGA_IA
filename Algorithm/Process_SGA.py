##
# Importar librerias necesarias para la ejecución de el algoritmo
# #
import random
import math
from matplotlib import pyplot as plt
import cmath

Global_Population = []
Result_finish = []
posGeneration = 0
pos = 0


def Result_finished():
    print('--------------------------------------------------------------------------------------------------------------------------------')
    print('---------------------------------------------------Result Finish','---------------------------------')
    for i in range(len(Result_finish)):
        print(Result_finish[i])

def Fitness_Calculation(val_x, val_y, val_z):
    try:
        return round(abs(( math.cos(val_x) + math.sin(2* pow(val_z,2)) ) / ( cmath.sqrt(9 - pow(val_x,2) - pow(val_y,2) - pow(val_z,2))) ),7) # 1.4289 / f(x,y,z)=(cos(x)+sin(2 z^(2)))/(sqrt(9-x^(2)-y^(2)-z^(2)))
    except:
        print('error')

def Genotype_to_Phenotype(Bits_cadene, Max_x, Min_x, Max_y, Min_y, Max_z, Min_z):
    phenotype_dx = 0
    phenotype_dy = 0
    phenotype_dz = 0

    range_dx = abs(Max_x - Min_x)
    range_dy = abs(Max_y - Min_y)
    range_dz = abs(Max_z - Min_z)
    #print(len(Bits_cadene[0]), ' : ', int(Bits_cadene[0]))
    Dx = range_dx / math.pow(2,len(Bits_cadene[0]))
    Value_dx = int(Bits_cadene[0],2)
    #print(Value_dx, ' : ', math.pow(2,len(Bits_cadene[0])))

    Dy = range_dy / math.pow(2,len(Bits_cadene[1]))
    Value_dy = int(Bits_cadene[1],2)

    Dz = range_dx / math.pow(2,len(Bits_cadene[2]))
    Value_dz = int(Bits_cadene[2],2)

    if(Min_x > Max_x):
        phenotype_dx = Max_x + ( Value_dx * Dx)#de binario se convierte a decimal y se multiploca por Dx, luego se suma a la valor inicial de x
    else:
        phenotype_dx = Min_x + ( Value_dx * Dx)#de binario se convierte a decimal y se multiploca por Dx, luego se suma a la valor inicial de x

    if(Min_y > Max_y):
        phenotype_dy = Max_y + ( Value_dy * Dy)#de binario se convierte a decimal y se multiploca por Dx, luego se suma a la valor inicial de x
    else:
        phenotype_dy = Min_y + ( Value_dy * Dy)#de binario se convierte a decimal y se multiploca por Dx, luego se suma a la valor inicial de x

    if(Min_z > Max_z):
        phenotype_dz = Max_z + ( Value_dz * Dz)#de binario se convierte a decimal y se multiploca por Dx, luego se suma a la valor inicial de x
    else:
        phenotype_dz = Min_z + ( Value_dz * Dz)#de binario se convierte a decimal y se multiploca por Dx, luego se suma a la valor inicial de x

    return round(phenotype_dx,4), round(phenotype_dy,4), round(phenotype_dz,4)

def Global_pop():
    print('--------------------------------------------------------------------------------------------------------------------------------')
    print('---------------------------------------------------Actual Population'  ,'---------------------------------')
    for i in range(len(Global_Population)):
        print(Global_Population[i])

def Crossover(Max_Population, Bits_size, Max_x, Min_x, Max_y, Min_y, Max_z, Min_z):
    global pos
    string_bit_1 = ''
    string_bit_2 = ''

    aux_string_bit1 = ''
    aux_string_bit2 = ''
    Son1 = []
    Son2 = []
    num = len(Global_Population)
    list_population_aux = []

    for i in range(int(len(Global_Population) / random.randint(2,4))):
        (F1_position, F2_position ) = Fathers()
        crossoverPoint = (random.randint(2,Bits_size - 1)) #genera punto de cruza
        #print('Crossover → {', 'F1 : ', Global_Population[F1_position].get('Mating pool'), 'Pos', F1_position , ' } { F2: ', Global_Population[F2_position].get('Mating pool'), 'Pos', F2_position, ' } { Crossover Point: ', crossoverPoint, ' }')
        Global_Population[F1_position].update({'Crossover Point' : crossoverPoint})
        Global_Population[F2_position].update({'Crossover Point' : crossoverPoint})
        Father_1 =  Global_Population[F1_position].get('Mating pool')
        Father_2 =  Global_Population[F2_position].get('Mating pool')
        Son1 = []
        Son2 = []
        for item in range(len(Father_1)):
            string_bit_1 = ''
            string_bit_2 = ''
            aux_string_bit1 = ''
            aux_string_bit2 = ''

            string_bit_1 = Father_1[item][0:crossoverPoint]
            string_bit_2 = Father_2[item][0:crossoverPoint]
            aux_string_bit1 = Father_1[item][crossoverPoint: len(Father_1[item])]
            aux_string_bit2 = Father_2[item][crossoverPoint:len(Father_2[item])]
            string_bit_1 = string_bit_1 + aux_string_bit2
            string_bit_2 = string_bit_2 + aux_string_bit1

            #print(Father_1[item], ' : ', Father_2[item])
            #print(string_bit_1, '← →', string_bit_2)

            Son1.append(string_bit_1)
            Son2.append(string_bit_2)
        list_population_aux.append(Son1)
        list_population_aux.append(Son2)
        #print(Son1, ' : ', Son2)
        #print(list_population_aux)

    #print(list_population_aux)

    for i in range(len(list_population_aux)):
        #print(list_population_aux[i])
        pos += 1
        dicIndividues1 = {'Ind' : pos, 'Mating pool': list_population_aux[i], 'Crossover Point' : 0, 'P Mutation': 0, 'X Value' : 0, 'Y Value' : 0, 'Z Value' : 0,'Fitness' : 0},
        print(dicIndividues1)
        Global_Population.extend(dicIndividues1)
    #Global_pop()

def Fathers():
    Father_position_1 = (random.randint(1,len(Global_Population) - 1))
    Father_position_2 = (random.randint(1,len(Global_Population) - 1))
    if Father_position_1 == Father_position_2:
        while True:
            Father_position_2 = 0
            Father_position_2 = (random.randint(1,len(Global_Population) - 1))
            if Father_position_1 != Father_position_2:
                break

    return Father_position_1, Father_position_2

def Mutation(Max_Population, P_Mutation, P_Mutation_gen, Max_x, Min_x, Max_y, Min_y, Max_z, Min_z):

    aux_individue_mut = ''
    aux_individue = []
    Mutation_Pas = Global_Population[0].get('P Mutation')
    print(' P Mutacion Max Generation → ', Mutation_Pas, '   Generation → ', posGeneration - 1, )
    for item in range(len(Global_Population)):
        Global_Population[item].update({'P Mutation' : random.random()})

    if posGeneration > 1:
        if Global_Population[0].get('P Mutation') < P_Mutation:
            print(Global_Population[0].get('P Mutation'))
            while True:
                Global_Population[0].update({'P Mutation' : random.random()})
                if Global_Population[0].get('P Mutation') > P_Mutation:
                    break
    print(' P Mutacion → ',  Global_Population[0].get('P Mutation'), '   Generation → ', posGeneration , )

    for item in range(len(Global_Population)):

        if Global_Population[item].get('P Mutation') <= P_Mutation:
            individue = Global_Population[item].get('Mating pool')
            #print('Mutation → {', 'Ind : ', Global_Population[item].get('Mating pool'), 'Pos', item , ' }' )
            aux_individue = []
            for data in range(len(individue)):
                aux_individue_mut = ''
                #print(individue[data])
                for i in range(len(individue[data])):
                    if random.random() <= P_Mutation_gen:
                        #print(individue[data][i], ' : ', i)
                        if individue[data][i] == '1':
                            #print('change → ', 0)
                            aux_individue_mut += '0'
                        elif individue[data][i] == '0':
                            #print('change → ', 1)
                            aux_individue_mut += '1'
                        else:
                            print('error')
                            break
                    else:
                        aux_individue_mut += individue[data][i]
                #print('mutado → ',aux_individue_mut)
                aux_individue.append(aux_individue_mut)
            #print('New individue mut → ', aux_individue, ' : ', Global_Population[item].get('Mating pool'))
            Global_Population[item].update({'Mating pool':aux_individue})
            print(Global_Population[item])
    #Global_pop()

def Generate_Init_Population(Init_Population, Bits_size):
    cadena_bits = ''
    list_individuos = [[] for i in range(Init_Population)]

    for item in range(Init_Population):
        for n in range(3):
            cadena_bits = ''
            for i in range(Bits_size):
                cadena_bits += str(random.randint(0,1) )
            list_individuos[item].append(cadena_bits)
    #print(list_individuos)
    return list_individuos

def Get_Fitness_General(Max_Population):
    global posGeneration
    Max_fitness = 0
    Min_fitness = 0
    all_fitness = 0
    prom_fitness = 0
    pos_Max = 0
    pos_Min = 0
    for item in range(len(Global_Population)):
        fitness_Cal = Global_Population[item].get('Fitness')
        #Global_Population[item].update({'Exent': 'N'})
        #print(item, ' : ', fitness_Cal)
        if item == 0:
            Max_fitness = fitness_Cal
            Min_fitness = fitness_Cal
            all_fitness += fitness_Cal
            pos_Max = item
            pos_Min = item
        else:
            all_fitness += fitness_Cal
            if fitness_Cal > Max_fitness:
                Max_fitness = fitness_Cal
                pos_Max = item
            if fitness_Cal < Min_fitness:
                Min_fitness = fitness_Cal
                pos_Min = item
    #Global_Population[pos_Max].update({'Exent': 'S'})
    dicResult = {'Generation' : posGeneration, 'Max Fitness' : Max_fitness, 'Indi Max' : Global_Population[pos_Max].get('Ind') , 'Min Fitness' : Min_fitness, 'Pos Min' : Global_Population[pos_Min].get('Ind') , 'Prom Fitness' : all_fitness/len(Global_Population) }
    #print(dicResult)
    Result_finish.append(dicResult)

def Fitness_Population_Get(Address):
    list_Fitness = []
    for item in range(len(Global_Population)):
        list_Fitness.append(Global_Population[item].get('Fitness'))
    #print('Fitnesss 1 → ',list_Fitness)
    if Address == 1:
        list_Fitness.sort(reverse=True)
    else:
        list_Fitness.sort(reverse=False)
    return list_Fitness

def Out_All_individues(Position):
    True_Individues = []
    for item in Position:
        dicfitness = Global_Population[item]
        True_Individues.append(dicfitness)
    #print('####################################################')
    Global_Population.clear()
    for i in range(len(True_Individues)):
        #print(True_Individues[i])
        Global_Population.append(True_Individues[i])
    Global_pop()

def Poda(Max_Population, Address):
    list_Fitness_Pop = []
    Position = []
    (list_Fitness_Pop) = Fitness_Population_Get(Address)
    #print(list_Fitness_Pop)
    if posGeneration == 1:
        for i in range(Max_Population):
            for item in range(len(Global_Population)):
                if Global_Population[item].get('Fitness') == list_Fitness_Pop[i]:
                    #print(Global_Population[item].get('Fitness'), ' pos → ', item)
                    if i == 0:
                        Position.append(item)
                    else:
                        if item in Position:
                            break
                        else:
                            Position.append(item)
        Out_All_individues(Position)
        #print(Position)
        #print('num Max → ', len(Position))
    else:
        #print('************** -------- →→→→→→→→→→→→→',posGeneration)
        for i in range(Max_Population):
            for item in range(len(Global_Population)):
                if Global_Population[item].get('Fitness') == list_Fitness_Pop[i]:
                    #print(Global_Population[item].get('Fitness'), ' pos → ', item)
                    #if list_Fitness_Pop[i] < Result_finish[len(Result_finish) - 1].get('Max Fitness'):
                    #    break
                    #else:
                    if i == 0:
                        Position.append(item)
                    else:
                        if item in Position:
                            break
                        else:
                            Position.append(item)
        Out_All_individues(Position)

def Evaluation(Max_Population, Bits_size, Max_x, Min_x, Max_y, Min_y, Max_z, Min_z,Address):
    for item in range(len(Global_Population)):
        Bits_cadene = Global_Population[item].get('Mating pool')
        (x_value, y_value, z_value) = Genotype_to_Phenotype(Bits_cadene, Max_x, Min_x, Max_y, Min_y, Max_z, Min_z)
        Global_Population[item].update({'X Value' : x_value})
        Global_Population[item].update({'Y Value' : y_value})
        Global_Population[item].update({'Z Value' : z_value})
        fitness = Fitness_Calculation(x_value, y_value, z_value)
        Global_Population[item].update({'Fitness' : fitness})
    Global_pop()

    if len(Global_Population) > Max_Population:
        Poda(Max_Population, Address)
        Get_Fitness_General(Max_Population)
    else:
        Get_Fitness_General(Max_Population)

def Create_Initial_List(Init_Population, Bits_size, Max_x, Min_x, Max_y, Min_y, Max_z, Min_z ):
    global Global_Population
    global pos

    list_individues =  Generate_Init_Population(Init_Population, Bits_size)
    for i  in range (Init_Population):
        pos += 1
        dicIndividues = {'Ind' : pos, 'Mating pool': list_individues[i], 'Crossover Point' : 0, 'P Mutation': 0, 'X Value' : 0, 'Y Value' : 0, 'Z Value' : 0,'Fitness' : 0},

        Global_Population.extend(dicIndividues)
#
# Creaion de la Grafica y muestreo de los fitness
# #
def Graphyc():
    lis_Max = []
    lis_Min = []
    lis_Prom = []
    generations = []
    for item in range(len(Result_finish)):
        lis_Max.append(Result_finish[item].get('Max Fitness'))
        lis_Min.append((Result_finish[item].get('Min Fitness')))
        lis_Prom.append((Result_finish[item].get('Prom Fitness')))
        generations.append(item + 1)
    #print(lis_Max)
    plt.title("Fitness")
    plt.legend()
    plt.plot(generations, lis_Max, color="red", linewidth=2, linestyle="-", label="maximos")
    plt.plot(generations, lis_Min,  color="green", linewidth=2, linestyle="-", label="minimos")
    plt.plot(generations, lis_Prom,  color="blue", linewidth=2, linestyle="--", label="promedio")
    plt.legend(loc='upper left')
    plt.xlabel('Generaciones')
    plt.ylabel('Fitness')
    plt.rcParams['toolbar'] = 'None'
    plt.grid(b=None, which='major', axis='both')
    plt.legend()
    plt.show()



#
# Inicio del Proceso para el algoritmo
# #
def Start_SGA(Init_Population, Max_Population, Generations, Bits_size, Max_x, Min_x, Max_y, Min_y, Max_z, Min_z, P_Mutation, P_Mutation_gen, Dx, Dy, Dz, Address):
    global posGeneration
    print('====================================== Inicio de el programa ======================================')
    Create_Initial_List(Init_Population, Bits_size, Max_x, Min_x, Max_y, Min_y, Max_z, Min_z )
    Global_pop()

    for item in range(Generations):
        posGeneration += 1
        print('--------------------------------------------------------------------------------------------------------------------------------')
        print('---------------------------------------------------List CROSSOVER GENERATION ',item + 1,'---------------------------------')
        Crossover(Max_Population, Bits_size, Max_x, Min_x, Max_y, Min_y, Max_z, Min_z)
        print('--------------------------------------------------------------------------------------------------------------------------------')
        print('----------------------------------------------------List MUTATION GENERATION ', item + 1,'---------------------------------')
        Mutation(Max_Population,P_Mutation, P_Mutation_gen,Max_x, Min_x, Max_y, Min_y, Max_z, Min_z)
        print('--------------------------------------------------------------------------------------------------------------------------------')
        print('---------------------------------------------------List SELECTION GENERATION ', item + 1 ,'---------------------------------')
        Evaluation(Max_Population, Bits_size, Max_x, Min_x, Max_y, Min_y, Max_z, Min_z, Address)
        print('-----------------------------*******************************************************************************-----------------------------')
        print(Result_finish[len(Result_finish) - 1])

    Result_finished()
    Graphyc()