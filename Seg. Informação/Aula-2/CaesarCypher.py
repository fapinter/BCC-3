import random

def cripto(mensagem, chave):
    cripto = ""
    for c in mensagem:
        codigo = ord(c) + chave
        cripto += chr(codigo)
    return cripto

def decripto(mensagem,chave):
    cripto = ""
    for c in mensagem:
        codigo = ord(c) - chave
        cripto += chr(codigo)
    return cripto

def analise_frequencia(cipher):
    codigo = [ ord(c) for c in cipher ]
    freq = {}
    for c in codigo:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] = freq[c] + 1  

    print(freq)
    return sorted(freq.items(), key=lambda item: item[1])

def forca_bruta(cipher, espaco):
    for i in range(1,espaco):
        cripto = ""
        mensagem = cipher
        for c in mensagem:
            codigo = ord(c) - i
            cripto += chr(codigo)
        print(f"{i} = {cripto}")
            

plain = 'Nada de novo no front'
N = 16 #Numero de bits
espaco = 2** N #Espaco de chaves possiveis

chave = random.randint(1,espaco)
print(chave)
cipher = cripto(plain, chave)
print(cipher)

mensagem = "Sfif%ij%st{t%st%kwtsy"

forca = forca_bruta(cipher,espaco)
print(forca)

#res =analise_frequencia(cipher)
#print(res)

#print(res[-1][0] - ord(' '))
#print(res[-1][0] - ord('a'))
#print(res[-1][0] - ord('o'))

#print(res[-2][0] - ord(' '))
#print(res[-2][0] - ord('a'))
#print(res[-2][0] - ord('o'))










