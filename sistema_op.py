# Daniel Morales 15526
# Rodrigo Corona 15102

import simpy
class LinuxOS(object):
    def __init__(self, env, cap, mem, vel, velMemoria, velWait, velAlojamiento):
        self.procesador = simpy.Resource(env, capacity=cap) # Procesador
        self.memoria_ram = simpy.Container(env, init=mem, capacity=mem) # Memoria
        self.io = simpy.Resource(env, capacity=1) # Cola de IO
        self.velprocesador = vel # Velocidad de instrucciones por ciclo del procesador
        self.velMemoria = velMemoria # Velocidad de la memoria
        self.velWait = velWait # Tiempo del Wait
        self.velAlojamiento = velAlojamiento # Velocidad que se tarda en alojar
