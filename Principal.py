# Daniel Morales 15526
# Rodrigo Corona 15102

import sys
import simpy
import random
from Simulacion import *
from sistema_op import *




def main(argv):
	#-- Random para memoria
    cantidadProcesos = 25 #Cantidad de Procesos
    RANDOM_SEED = 42 #Semilla para numeros aleatorios
    random.seed(RANDOM_SEED)
    intervalo = 10 #para random de memoria
    intervalo2 = 10 #para random de instrucciones

    #-- Instanciacion del sistema operativo
    env = simpy.Environment()
    sistema_operativo = LinuxOS(env, 1, 100, 3, 1, 3, 1)

    procesos = []
    #-- Crear los procesos
    for i in range(cantidadProcesos):
        #-- Cantidad de memoria entre 1 y 10
        memory = int(random.expovariate(1.0/intervalo))
        if (memory > 10):
            memory = int(memory/10)
        if (memory < 1):
            memory = memory + 1

        #-- Cantidad de instrucciones entre 1 y 10
        instructions = int(random.expovariate(1.0/intervalo2))
        if (instructions > 10):
            instructions = int(instructions/10)
        if (instructions < 1):
            instructions = instructions + 1

        #-- Crea proceso
        procesos.append(Simulacion(env, "Piercy " + str(i + 1), memory, instructions, sistema_operativo))
    env.run()

    suma = 0
    for procesito in procesos:
        suma += procesito.tiempoTotal
    promedio = suma / cantidadProcesos
    print ("El promedio de ejecucion de los programas fue: {}".format(promedio))
    



# Funcion main
if __name__ == "__main__":
    main(sys.argv)
