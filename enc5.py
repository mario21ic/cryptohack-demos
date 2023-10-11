# Cadena original
original_string = 'label'

# Inicializar la nueva cadena
new_string = ''

# Iterar a través de cada carácter en la cadena original
for char in original_string:
    # Obtener el valor ASCII del carácter
    ascii_value = ord(char)
    # Realizar la operación XOR con 13
    xor_value = ascii_value ^ 13
    # Convertir el resultado de vuelta a un carácter y agregarlo a la nueva cadena
    new_string += chr(xor_value)

# Formatear la cadena de acuerdo al formato de la bandera
flag = f'crypto{{{new_string}}}'

# Mostrar la bandera
print(flag)

