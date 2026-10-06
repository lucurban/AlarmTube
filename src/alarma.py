'''
Este programa se encarga de representar una alarma individual conociendo el 
dia de la semana y la hora en que se reproduce el video, ademas del estado 
actual.
'''

'''
==============================================================================
                         Definición de la clase Alarma
==============================================================================
'''

class Alarma:
    def __init__(self, dia_semana, hora, estado=False):
        '''
        Constructor de la clase Alarma.
        
        Parametros:
            dia_semana: El día de la semana en que se activa la alarma.
            hora: La hora en que se activa la alarma.
            estado: El estado inicial de la alarma (True para activada, False 
            para desactivada).
        '''
        self.dia_semana = dia_semana
        self.hora = hora
        self.estado = estado

    def activar(self):
        '''
        Método que activa la alarma.
        '''
        self.estado = True

    def desactivar(self):
        '''
        Método que desactiva la alarma.
        '''
        self.estado = False