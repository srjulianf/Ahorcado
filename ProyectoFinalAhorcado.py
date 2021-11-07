import random
print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
print("█░░ ▲H☼RCAD☼ G▲ME  ░░█")
print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")

print("  ───▄█▌─▄─▄─▐█▄")
print("  ───██▌▀▀▄▀▀▐██")
print("  ───██▌─▄▄▄─▐██")
print("  ───▀██▌▐█▌▐██▀")
print("  ▄██████─▀─██████▄")

pic = ["╬", "▓" , "█" ]

def picture(word):
    for i in range(0, len(word)):
        print( i * random.choice(pic),"    " ,word[i] )

def picture2(word):
    for i in reversed(range(0, len(word))):
        print( i * random.choice(pic),"    " ,word[i] )

picture2("PLAY")   
print("&                               This game is made by Julian Peña Reyes")  
picture("ENJOY")


print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
print("█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█")
print("█░░║║║╠─║─║─║║║║║╠─░░█")
print("█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█")
print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")

lista= []  
with open("./data.txt", "r", encoding = "utf-8") as f:
    for i in f:
        i = i.replace("\n", "")
        # i = i.encode('utf-8')
        lista.append(i)

word = random.choice(lista)
word = str(word)
word = word.replace("á","a")
word = word.replace("é","e")
word = word.replace("í","i")
word = word.replace("ó","o")
word = word.replace("ú","u")

keep = [" _ "] * len(word)
indice = []
dictionar = {}
contador = 0
def palabra():
    char1 = input("█░░ WRITE A LETTER : →→→→ ")
    if char1 in word:
        pos = word.find(char1)
        contador = 0
        if word.count(char1) > 1:
            for i in word:
                if i == char1:
                    keep[contador] = i
                contador = contador +1 
        else: 
            keep[pos] = char1
        print(keep)      
    else:
        print(" ♦ THIS LETTER ISN'T ON WORD, PLEASE CHOOSE ANOTHER: ")


def ahorcado():
    print("▄███████▄.▲.▲▲▲▲▲▲▲▲ YOUR WORD HAS " + str(len(word)) + " LETTERS")
    print( [" _ "] * len(word))
    print("► BE CAREFUL, YOU HAVE JUST 7 LIVES ♥♥♥♥♥♥♥")
    vidas = 10 
    while " _ " in keep:
        print("YOU HAVE ",  vidas * "♥", "LIVES REMAINING " )
        palabra()
        vidas -= 1
        if vidas == 0:
            print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
            print("█░░   GAME OVER    ░░█")
            print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
            print("■   WORD WAS: ", word ,  "   ■")
            break 
    if " _ " not in keep:
        print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
        print("█░░    YOU WIN     ░░█")
        print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
        

    

    



    
 

def run():
    ahorcado()

if __name__ == '__main__' : 
    run()
