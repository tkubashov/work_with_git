a = {'sap_code': '9061', 'cluster_name': 'Кластер Волга 18 Новокуйбышевск', 'cluster_sapid': '52901676',
 'macroregion_name': 'Макрорегион Волга', 'macroregion_sapid': '52880599'}

b = {'cluster_name': None, 'aaaaa': 'aaaaa'}


re = a.items() & b.items()
print(re)