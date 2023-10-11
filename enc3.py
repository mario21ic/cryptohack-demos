import base64

hexs="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
#bytes.hex(b"c") # 63
#bytes.fromhex("63") # c

# Decodificación de la cadena hexadecimal a bytes
bytes_value = bytes.fromhex(hexs)

# Codificación de los bytes a Base64
base64_string = base64.b64encode(bytes_value).decode('utf-8')

# Mostrar la cadena Base64
print(base64_string)
