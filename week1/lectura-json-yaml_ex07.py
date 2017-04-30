'''
7. Write a Python program that reads both the YAML file and the JSON file 
created in exercise6 and pretty prints the data structure that is returned.
'''

import json
import yaml
import pprint

# lectura y conversion fichero JSON
fichero = raw_input('Introduce nombre fichero JSON (.json): ')
fh = open(fichero)
lista = json.load(fh)
pprint.pprint(lista)

# lectura y conversion fichero YAML
fichero = raw_input('Introduce nombre fichero YAML (.yml): ')
fh = open(fichero)
lista = yaml.load(fh)
pprint.pprint(lista)