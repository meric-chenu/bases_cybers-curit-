#!python3

import sys
import os
import binascii
import math

from Crypto.Util.Padding import pad
from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.Cipher import AES


def encrypt_file(path, passphrase):
    with open(path, 'rb') as f:
        plaintext = f.read()

    # Remplissage pour avoir un multiple de la taille de bloc
    plaintext = pad(plaintext, AES.block_size)

    # Conversion du mot de passe en clé de chiffrement de 256 bits
    passphrase = passphrase.encode('UTF-8')
    crc1 = binascii.crc32(passphrase)
    crc2 = binascii.crc32(passphrase[::-1])
    seed = (crc2>>math.factorial(4))|((crc1^0x7ed5^crc1^0x3c7f)<< 16)|((crc1&(16**8-4**12))>>2**4)
    key = SHA256.new(seed.to_bytes(256, byteorder='big')).digest()

    # Génération aléatoire du vecteur d’initialisation
    iv = Random.new().read(AES.block_size)

    # Chiffrement avec AES-256 en mode CBC
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = iv + cipher.encrypt(plaintext)

    # Enregistrement du fichier chiffré
    with open(path + '.enc', 'wb') as f:
        f.write(ciphertext)

    # Suppression du fichier clair
    os.remove(path)


if __name__ == '__main__':
    print('Bienvenue dans CryptoSecureFile 3000 !')
    print('LA solution sécurisée pour chiffrer vos fichiers de façon disruptive.\n')
    
    if len(sys.argv) < 2 or sys.argv[1].strip() == '':
        print('Utilisation : passer le fichier à chiffrer en argument du script.')
    else:
        path = sys.argv[1]
        passphrase = input('Mot de passe : ')
        encrypt_file(path, passphrase)
