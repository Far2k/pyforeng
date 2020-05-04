# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
result_template = '''
Protocol:           {prot}
Prefix:             {pref}
AD/Metric:          {metr}
Next-Hop:           {hop}
Last update         {upd}
Outbond Interface   {int}
'''

with open('ospf.txt') as src, open('resault.txt', 'w') as dest:
    for var in src:
        if var == 'O':
            print('OSPF')
    else:
        pass
