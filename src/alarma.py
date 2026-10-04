'''
Este programa se encarga de representar una alarma individual conociendo la 
hora de activación y su estado actual.
'''

'''
==============================================================================
                         Definición de la clase Alarma
==============================================================================
'''

class Alarma:
    #---Constructor de la clase Alarma---
    def __init__(self, hora_activacion):
        '''
        Constructor de la clase Alarma.
        
        Parametros:
            hora_activacion: La hora de activación de la alarma.
        '''
        self.hora_activacion = hora_activacion
        self.estado = False  # Estado inicial de la alarma (inactiva)

    #---Metodo para activar la alarma---
    def activar(self):
        '''
        Método que activa la alarma.
        '''
        self.estado = True

    #---Metodo para desactivar la alarma---
    def desactivar(self):
        '''
        Método que desactiva la alarma.
        '''
        self.estado = False

    #---Metodo para verificar si la alarma está activa---
    def esta_activa(self):
        '''
        Método que verifica si la alarma está activa.
        
        Returna:
            bool: True si la alarma está activada, False en caso contrario.
        '''
        return self.estado