'''
Find all of the crypto map entries that are using PFS group2 in the file cisco_ipsec.txt
'''

# Cargar clase CiscoConfParse de libreria ciscoconfparse
from ciscoconfparse import CiscoConfParse

# Abrir fichero de configuracion
config = CiscoConfParse('cisco_ipsec.txt')

# Buscar y guardar linea que contiene cadena buscada
lineas = config.find_objects(r'pfs group2')

# Buscar y encontrar crypto map que utilizan PFS group2
for linea in lineas:
    crypto_map = linea.parent
    print crypto_map.text