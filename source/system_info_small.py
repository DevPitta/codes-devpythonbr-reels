"""
This code uses the psutil
and platform libraries
and outputs operating system and computer information.

-> Requirements:
    . pip install psutil
    . pip install platform
"""

import psutil as ps 
import platform as pl 

print(f'Nome do Computador: {pl.node()}')
print(f'Sistema Operacional: {pl.system()}')
print(f'Kernel do Sistema: {pl.release()}')
print(f'Plataforma da Máquina: {pl.machine()}')
print(f'Plataforma do Processador: {pl.processor()}')
print(f'Cores do CPU: {ps.cpu_count()}')
print(f'Frequência Mínima do CPU: {ps.cpu_freq().min}')
print(f'Frequência Máxima do CPU: {ps.cpu_freq().max}')
print(f'Memória RAM: {round(ps.virtual_memory().total/1000000000, 2)} GB')
