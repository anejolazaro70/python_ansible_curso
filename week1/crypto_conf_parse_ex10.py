'''
Using ciscoconfparse find in cisco_ipsec.txt the crypto maps that are not using AES (based-on the transform set name). 
Print these entries and their corresponding transform set name.
'''

# Incorporar clase CiscoConfParse de libreria ciscoconfparse
from ciscoconfparse import CiscoConfParse

# Abrir y leer fichero de configuracion
config = CiscoConfParse('cisco_ipsec.txt')

# Buscar crypto maps que no utilizan AES
lineas_buscadas = config.find_objects(r'\sset transform-set .*')
linea_patron = ' set transform-set AES-SHA'
for linea in lineas_buscadas:
    linea_text = linea.text.rstrip()
    if linea_text != linea_patron:
        crypto_map = linea.parent
        print crypto_map.text
        print linea.text
    