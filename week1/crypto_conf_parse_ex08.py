'''
The script should find all of the crypto map entries in the file cisco_ipsec.txt
(lines that begin with 'crypto map CRYPTO') and for each crypto map 
entry print out its children.
'''
# Abrir fichero de configuracion
from ciscoconfparse import CiscoConfParse
config = CiscoConfParse('cisco_ipsec.txt')

# Buscar y guardar lineas que empiezan por 'crypto map'
lineas_crypto = config.find_objects(r'^crypto map')
print lineas_crypto

# Buscar y capturar lineas hijas de cada bloque 'crypto map'
for linea_padre in lineas_crypto:
    hijas = linea_padre.children
    print linea_padre.text
    for linea_hija in hijas:
       print linea_hija.text
