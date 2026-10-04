'''
Este programa se encarga de proporcionar la hora actual utilizando la libreria
datetime de python.
'''

#---Importar paquetes---
from datetime import datetime

'''
==============================================================================
                         Definición de la clase Reloj
==============================================================================
'''

class Reloj:
    #---Metodo para obtener la hora actual---
    def obtener_hora_actual(self):
        '''
        Método que obtiene la hora actual utilizando la libreria datetime de python.
        
        Retorna:
            datetime: La fecha y hora actual.
        '''
        hora_actual = datetime.now()

        return hora_actual