# -*- coding: utf-8 -*-
'''
Задание 6.1

Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX.
Однако, в оборудовании cisco MAC-адреса используются в формате XXXX.XXXX.XXXX.

Создать скрипт, который преобразует MAC-адреса в формат cisco
и добавляет их в новый список mac_cisco

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco= []
for result in mac:
    mac_cisco.append(result.replace(':','.'))
print(mac_cisco)
