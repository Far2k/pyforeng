# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface     FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
result = '''
Protocol:           {prot}
Prefix:             {pref}
AD/Metric:          {metr}
Next-Hop:           {hop}
Last update         {upd}
Outbond Interface   {int}
'''
print(result.format(prot='OSPF', pref='10.0.24.0/24', metr='110/41', hop='10.0.13.3', upd='3d18h', int='FastEthernet0/0'))
