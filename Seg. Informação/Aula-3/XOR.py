def tabela_logica():
    dados = [ [0b0,0b0], [0b0,0b1], [0b1, 0b0], [0b1, 0b1]]

    for x in dados:
       print(x, "AND", x[0] & x[1])
       print(x, "OR", x[0] | x[1])
       print(x, "XOR", x[0] ^ x[1])

#tabela_logica()

def xor_cipher(plain, key):
    cipher = ''
    cipher_bytes = []
    for c in plain:
        x = ord(c) ^ key
        cipher += chr(x)
        cipher_bytes.append(x)

    return cipher, cipher_bytes
    

while True: 
    key = input('entre com a chave: ')
    if not key:
        print("saindo..")
        break
    else:
        key = int(key)
        plain = input("entre com a mensagem: ")
        cipher, cipher_bytes  = xor_cipher(plain,key)
        print("cipher_bytes: ", cipher_bytes)
        print("cripto: ", cipher)
        print("decripto: ", xor_cipher(cipher,key))