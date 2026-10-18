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
        self.contador_alarmas = 0

    def agregar_alarma(self, alarma):
        '''
        Método que agrega una alarma a la lista de alarmas.
        
        Parametros:
            alarma: Una instancia de la clase Alarma que se desea agregar.
        '''
        for alarma_existente in self.alarmas:
            if alarma_existente.nombre == alarma.nombre:
                return False

        self.alarmas.append(alarma)

        self.contador_alarmas += 1

        return True

    def obtener_nombre(self, alarma):
            '''
            Método que obtiene el nombre de una alarma.
            
            Parametros:
                alarma: Una instancia de la clase Alarma.
            '''
            if alarma.nombre is None:
                alarma.nombre = 'Alarma '+ str(self.contador_alarmas + 1)

    def eliminar_alarma(self, alarma):
        '''
        Método que elimina una alarma de la lista de alarmas.
        
        Parametros:
            alarma: Una instancia de la clase Alarma que se desea eliminar.
        '''
        if alarma in self.alarmas:
            self.alarmas.remove(alarma)
            
            return f'La alarma {alarma.nombre} ha sido eliminada'

    def listar_alarmas(self):
        '''
        Método que devuelve la lista de alarmas.
        
        Retorna:
            Una lista con todas las instancias de la clase Alarma.
        '''
        return self.alarmas