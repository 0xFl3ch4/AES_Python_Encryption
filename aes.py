import os
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random

def getKey(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()
    
def encrypt(key, filename):
    #tamanho do bloco
    chunksize = 64*1024
    outputFile = "enc_"+filename
    filesize = str(os.path.getsize(filename)).zfill(16)

    #vetor de inicialização
    IV = Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    #abertura do ficheiro em modo binário
    with open(filename, 'rb') as infile:
        
        #escreve o ficheiro the output em modo binário
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            #encriptação
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk)%16 != 0:
                    chunk += b' '*(16-(len(chunk)%16))

                outfile.write(encryptor.encrypt(chunk))

def decrypt(key, filename):
    chunksize = 64*1024
    outputFile = filename[11:]

    #abertura do ficheiro em modo binário
    with open(filename, 'rb') as infile:
        filesize = int(infile.read(16))

        #vetor de inicialização
        IV = infile.read(16)
        decryptor= AES.new(key, AES.MODE_CBC, IV)

        #escreve o ficheiro the output em modo binário
        with open(outputFile, 'wb') as outfile:
            
            #desencriptação
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(filesize)



def Main():
    choice = input("(E)Encriptar ou (D)Desencriptar? ")

    if choice == 'E':
        filename = input("Nome ficheiro: ")
        password = input("Palavra-passe: ")
        encrypt(getKey(password), filename)
    elif choice == 'D':
        filename = input("Nome ficheiro: ")
        password = input("Palavra-passe: ")
        decrypt(getKey(password),filename)

    else:
        print("Nenhuma opção valida selecionada")


Main()
