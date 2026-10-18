from alarma import Alarma
from gestorAlarmas import GestorAlarmas
from datetime import time

gestor = GestorAlarmas()

alarma1 = Alarma(0, time(6, 30, 0), 'Alarma 1', True)
alarma2 = Alarma(0, time(7, 00, 0), 'Alarma 2', False)
alarma3 = Alarma(0, time(8, 15, 0), 'Alarma 2', True)
alarma4 = Alarma(0, time(9, 45, 0), 'Alarma 4', False)
alarma5 = Alarma(0, time(12, 00, 0), 'Alarma 5', False)
alarma6 = Alarma(0, time(5, 15, 0), 'Alarma 3', True)

alarmas = [alarma1, alarma2, alarma3, alarma4, alarma5, alarma6]

for alarma in alarmas:
    nueva_alarma = gestor.agregar_alarma(alarma)

    while nueva_alarma is False:
        var_nombre = False
                
        while var_nombre == False:
            print(f'La alarma {alarma.nombre} ya existe en la lista de alarmas.')
            print('Elije la opción 1 para dar un nombre personalizado a la alarma')
            print('Elije la opción 2 para que el programa le asigne un nombre ' \
                'a la alarma')

            opcion = int(input('tu elección: '))

            if opcion == 1 or opcion == 2:
                if opcion == 1:
                    alarma.nombre = input('Ingresa el nombre de la alarma: ')

                    var_nombre = gestor.agregar_alarma(alarma)

                    if var_nombre:
                        nueva_alarma = True
                
                elif opcion == 2:
                    alarma.nombre = None

                    gestor.obtener_nombre(alarma)
                        
                    print(f'El nombre de la alarma es: {alarma.nombre}')

                    var_nombre = gestor.agregar_alarma(alarma)

                    if var_nombre:
                        nueva_alarma = True

                else:
                    print('Elección inválida. Por favor, elige la opción 1 o 2.')

    print(f'La alarma {alarma.nombre} ha sido agregada exitosamente.')

lista_alarmas = gestor.listar_alarmas()

print(f'')
print(f'La lista de alarmas es: ')
print(f'')

for alarma in lista_alarmas:
    mensaje = f'La alarma {alarma.nombre} sonara el {alarma.dia_semana}, a '\
              f'las {alarma.hora} y su estado es {alarma.estado}'
    
    print(mensaje)

print('')
print(gestor.eliminar_alarma(alarma2))
print('')
print(f'Luego de eliminar la alarma {alarma2.nombre}, la nueva lista de '\
      f'alarmas es: ')
print('')

lista_alarmas = gestor.listar_alarmas()

for alarma in lista_alarmas:
    mensaje = f'La alarma {alarma.nombre} sonara el {alarma.dia_semana}, a '\
              f'las {alarma.hora} y su estado es {alarma.estado}'
    
    print(mensaje)