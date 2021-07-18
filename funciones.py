from pathlib import Path
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def leerArchivo(archivo):
    stream=open(archivo,"rb")
    print(stream.read())

def escribirArchivo(linea,archivo):
    with open(archivo,'a') as file: #argumento "a" es igual a append de agregar
        file.write("\n"+linea)

def cargarClavePrivada():
    return open("Privatekey.pem","rb").read()

def cargarClavePublica():
    return open("Publickey.pem","rb").read()

def claves():
    archivo=r'Privatekey.pem'
    objetoArchivo=Path(archivo)
    archivo2=r'Publickey.pem'
    objetoArchivo2=Path(archivo2)

    key = RSA.generate(2048)
    private_key = key.export_key('PEM')
    public_key = key.publickey().exportKey('PEM')

    if not objetoArchivo.is_file():    

        with open("Privatekey.pem","wb") as key_file:
            key_file.write(private_key)
        
    if not objetoArchivo2.is_file():
        
        with open("Publickey.pem","wb") as key_file2:
            key_file2.write(public_key)

def cifrado(archivo,clave):
    with open(archivo,"rb") as file:
        file_data=file.read()

    rsa_public_key = RSA.importKey(clave)
    rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
    encrypted_text = rsa_public_key.encrypt(file_data)

    with open(archivo,"wb") as file:
        file.write(encrypted_text)

def descifrado(archivo,clave):
    with open(archivo,"rb") as file:
        file_data=file.read()

    rsa_private_key = RSA.importKey(clave)
    rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
    decrypted_text = rsa_private_key.decrypt(file_data)

    with open(archivo,"wb") as file:
        file.write(decrypted_text)
