"""-----------------------------Chiffrement de Vigenere appliqué au premier message de niveau 0----------------------------------"""
"""------------------------------------- La clé est D, le message déchiffré est le suivant : 
----------------------------------------APPARU CENT ANS AVANT JC, JE SUIS LE PREMIER FLAG-------------------------------
------------------------------------J'AI DONNE MON NOM A CE CHIFFRE, MAIS C'EST UNE RIGOLADE----------------------------"""

file = open("Level 0/message.txt",'r')
"""N'ayant aucune redondance dans le mot chiffré, nous en déduisons que la clé ne contient qu'un seul caractère"""
message_encrypted = file.read()
file.close()
array_alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
array_alphabet_letter = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
print("message encrypted : ",message_encrypted)
key = 0
while key < 26:
    print("La clé actuelle est : ",array_alphabet[key])
    message_decrypted = ""
    #On parcourt notre message_crypté
    for i in range(len(message_encrypted)):
        letter_decrypted = ""
        #Si la lettre ciblé n'est pas un caractère spécial
        if(message_encrypted[i] in array_alphabet):
            index_letter_encrypted = 0
            while(array_alphabet[index_letter_encrypted] != message_encrypted[i]):
                index_letter_encrypted+=1

            """A ce stade, nous avons l'index de la lettre crypté, et donc son numéro. Nous pouvons donc la soustraire à la clé
            et trouver la lettre décryptée"""
            #Detection de la lettre décryptée
            """On rajoute +1 à la key, car par exemple si notre clé est A elle a pour index 0 ce qui ne change
            rien à l'index_letter_decrypted si l'on soutrait 0 --> la clé A doit avoir pour index 1"""
            index_letter_decrypted = array_alphabet_letter[index_letter_encrypted] - (key)
            """Si on est dans les négatifs, on est dérrière A donc on rajouter 25 pour aller à la fin de l'alphabet
            (l'index de  la dernière lettre de l'alphabet est 25)."""
            if(index_letter_decrypted < 0):
                index_letter_decrypted+=25
            message_decrypted+= array_alphabet[index_letter_decrypted]
        else:
            message_decrypted+= message_encrypted[i]
    print("Affichage du message décrypté \n",message_decrypted)
    key+=1
