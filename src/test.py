from alarma import Alarma
from gestorAlarmas import GestorAlarmas
from datetime import time

gestor = GestorAlarmas()

alarma1 = Alarma(2, time(6, 30, 0), False)
gestor.agregar_alarma(alarma1)

alarma2 = Alarma(4, time(7, 0, 0), True)
gestor.agregar_alarma(alarma2)

alarma3 = Alarma(0, time(8, 15, 0), True)
gestor.agregar_alarma(alarma3)
'''
for alarma in gestor.listar_alarmas():
    print(f'La alarma sonara el {alarma.dia_semana}, a las {alarma.hora}, y su estado es {alarma.estado}')
'''
lista_alarmas = gestor.listar_alarmas()

for alarma in lista_alarmas:
    print(f'La alarma sonara el {alarma.dia_semana}, a las {alarma.hora}, y su estado es {alarma.estado}')