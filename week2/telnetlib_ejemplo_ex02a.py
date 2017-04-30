'''
2. telnetlib

a. Write a script that connects using telnet to the pynet-rtr1 router. Execute the 'show ip int brief' command on the router and return the output.

Try to do this on your own (i.e. do not copy what I did previously). You should be able to do this by using the following items:

telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
remote_conn.read_until(<string_pattern>, TELNET_TIMEOUT)
remote_conn.read_very_eager()
remote_conn.write(<command> + '\n')
remote_conn.close()
'''

import telnetlib
import time

# Definicion de variables

ip = '184.105.247.70'
TELNET_PORT = 23
TELNET_TIMEOUT = 30

user = 'pyclass'
pasw = '88newclass'

comando = 'show ip interface brief'

# Establecer sesion telnet con equipo

sesion_telnet = telnetlib.Telnet(ip, TELNET_PORT, TELNET_TIMEOUT)
sesion_telnet.read_until('sername:', 5)
sesion_telnet.write(user + '\n')
time.sleep(1)
sesion_telnet.read_until('ssword:', 5)
sesion_telnet.write(pasw + '\n')
time.sleep(1)

# Permitir la salida de mas lineas que las permitidas por el tamanno del terminal
sesion_telnet.write('term len 0\n\n')
time.sleep(1)

# Enviar comando al equipo y presentar en pantalla el resultado de su ejecucion

sesion_telnet.write(comando + '\n')
time.sleep(1)
output = sesion_telnet.read_very_eager()
print output

sesion_telnet.close()

