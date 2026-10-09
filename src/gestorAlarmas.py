'''
Este prgrama se encarga de gestionar un conjunto de alarmas, permitiendo 
agregar, eliminar y listar alarmas individuales.
'''

'''
==============================================================================
                     Definición de la clase GestorAlarmas
==============================================================================
'''

class GestorAlarmas:
    def __init__(self):
        '''
        Constructor de la clase GestorAlarmas.
        
        Inicializa una lista vacía de alarmas.
        '''
        self.alarmas = []

    def agregar_alarma(self, alarma):
        '''
        Método que agrega una alarma a la lista de alarmas.
        
        Parametros:
            alarma: Una instancia de la clase Alarma que se desea agregar.
        '''
        self.alarmas.append(alarma)

    def eliminar_alarma(self, alarma):
        '''
        Método que elimina una alarma de la lista de alarmas.
        
        Parametros:
            alarma: Una instancia de la clase Alarma que se desea eliminar.
        '''
        if alarma in self.alarmas:
            self.alarmas.remove(alarma)

    def listar_alarmas(self):
        '''
        Método que devuelve la lista de alarmas.
        
        Retorna:
            Una lista con todas las instancias de la clase Alarma.
        '''
        return self.alarmas