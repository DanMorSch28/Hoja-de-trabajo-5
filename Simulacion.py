# Daniel Morales 15526
# Rodrogo Corona 15102

from random import randint

class Proceso(object):
    
    # Constructor del sistema operativo
    def __init__(self, env, id_proceso, memoria, instrucciones, os):
        self.env = env
        self.id_proceso = id_proceso
        self.memoria = memoria
        self.instrucciones = instrucciones
        self.os = os
        self.tiempoTotal = 0
        self.env.process(self.ejecutar())
    
    def ejecutar(self):
        #------------ ESTADO NEW ------------
        yield self.env.timeout(self.os.velMemoria)#Valor de llegada a memoria
        self.tiempoTotal = self.os.velMemoria
        print ("Tiempo_i: {:<10}; Proceso: '{proceso_id}' encolado;"\
               " (Memoria = {memoria}, Instrucciones = {instrucciones})"
               .format(self.env.now, proceso_id = self.id_proceso,
                memoria = self.memoria, instrucciones = self.instrucciones))
        yield self.env.timeout(self.os.velWait)#VALOR VARIABLE
        print ("Esperando memoria para el proceso '{0}'".format(self.id_proceso))
        yield self.os.memoria_ram.get(self.memoria) 
        #------------ ESTADO NEW ------------

        #------------ ESTADO READY ------------
        yield self.env.timeout(self.os.velAlojamiento)
        print ("Proceso '{0}' memoria alocada en: {1} "
               .format(self.id_proceso, self.env.now))
        #------------ ESTADO READY ------------
        while (self.instrucciones > 0): # Ready
            #------------ ESTADO RUNNING ------------
            with self.os.procesador.request() as procesador: 
                yield procesador
                print ("Proceso '{0}' ejecutando en: {1}" 
                       .format(self.id_proceso, self.env.now))
                self.instrucciones = self.instrucciones - self.os.velprocesador
                yield self.env.timeout(1)
                random_io = randint(1, 2) 
                if (random_io == 1):  # Wait
                    with self.os.io.request() as cola_io:
                        yield cola_io
                        print ("Proceso '{0}' realizo una operacion de I/O en {1}"
                               .format(self.id_proceso, self.env.now))
                        yield self.env.timeout(1)
            #------------ ESTADO RUNNING ------------
        yield self.env.timeout(1) # TERMINATED
        print ("Liberando memoria del proceso '{0}' en: {1}"
               .format(self.id_proceso, self.env.now))
        self.tiempoTotal = self.env.now - self.tiempoTotal
        self.os.memoria_ram.put(self.memoria) # Liberar memoria_ram
        print ("Ejecucion del proceso '{0}' terminada en: {1} unidades de tiempo"
               .format(self.id_proceso, self.tiempoTotal))


            
        
                
              
