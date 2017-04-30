'''
Write a Python program that creates a list. 
One of the elements of the list should be a dictionary with at least two keys. 
Write this list out to a file using both YAML and JSON formats. 
The YAML file should be in the expanded form.
'''
import json
import yaml

lista = range(1,10)
print lista
raw_input('Pulsa tecla para seguir...')
diccionario = dict()
diccionario['nombre'] = 'Jose Antonio'
diccionario['apellidos'] = 'Lazaro Lazaro'
diccionario['edad'] = 47
print diccionario
raw_input('Pulsa tecla para seguir...')
lista.append(diccionario)
print lista
raw_input('Pulsa tecla para seguir...')

# escritura en fichero JSON
fh = open('lista.json', 'w')
lista_json = json.dumps(lista)
raw_input('Pulsa tecla para seguir...')
print lista_json
json.dump(lista, fh)


# escritura en fichero YAML
lista_dump = yaml.dump(lista, default_flow_style = False)
print lista_dump
raw_input('Pulsa tecla para seguir...')
fh = open('lista.yml', 'w')
fh.write(lista_dump)
