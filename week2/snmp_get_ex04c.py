'''
Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and prints out both the MIB2 sysName and sysDescr.
'''

from snmp_helper import snmp_get_oid, snmp_extract

pynet_rtr1 = ('184.105.247.70', 'galileo', 161)
pynet_rtr2 = ('184.105.247.71', 'galileo', 161)
lista_nodos = [pynet_rtr1, pynet_rtr2]

sysName = '1.3.6.1.2.1.1.5.0'
sysDescr = '1.3.6.1.2.1.1.1.0'

lista_var_snmp = [sysName, sysDescr]

for nodo in lista_nodos:
    print "Nombre de nodo: ", nodo[0]
    for var_snmp in lista_var_snmp:
        snmp_data = snmp_get_oid(nodo, oid=var_snmp, display_errors=True)
        output = snmp_extract(snmp_data)
        print output
