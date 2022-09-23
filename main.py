from random import randint
import random

file = input("What is the exact file name or path of file you want to obfuscate? (with file extension pls) -> ")


def obfuscate(file):
    switch = False
    with open(f'{file}', 'r+', encoding='utf-8') as original:
        for lines in original:
            for char in lines:
                if switch == False:
                    if '\n' in char:
                        with open(f'{file}obfuscated.bat', 'a+', encoding='utf-8') as f:
                            f.write("\n")
                    elif "%" in char:
                        with open(f'{file}obfuscated.bat', 'a+', encoding='utf-8') as f:
                            f.write("%")
                            switch = True #thx baum for making this work :sob:
                    else:
                        random_num = randint(5, 15)
                        random_string = ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ☞☟☠☡☢☣☤☥☦☧☰☱☲☳☴☵☶☷☸♕☻♡☹♆♔♅♖♘♗♙♚♛♜♝♞♟♠♡♢♣♤♥♦♧♨♩♪♫♬♭♮♯♰♱♲♳♴♵♶♶♸♹♻♼♽♾⚀⚁⚂⚃⚄⚅⚆⚇⚈⚉⚊⚋⚌⚍⚎⚏⚐⚑⚒⚔⚕⚖⚗⚘⚙⚚⚛⚜⚝⚞⚟") for kdot in range(random_num))
                        with open(f'{file}obfuscated.bat', 'a+', encoding='utf-8') as f:
                            f.write(f"{char}%{random_string}%")

                else:
                    if "%" in char:
                        with open(f'{file}obfuscated.bat', 'a+', encoding='utf-8') as f:
                            f.write("%")
                            switch = False
                    elif '\n' in char:
                        with open(f'{file}obfuscated.bat', 'a+', encoding='utf-8') as f:
                            f.write("\n")
                    else:
                        with open(f'{file}obfuscated.bat', 'a+', encoding='utf-8') as f:
                            f.write(char) # spent like 2 hours trying to fix this and found baums again :sob: https://github.com/baum1810/batchobfuscator
    out_hex = []

    out_hex.extend(["FF", "FE", "0A", "0D"])
    with open(f'{file}obfuscated.bat','rb') as f:
            penis = f.read()

    out_hex.extend(['{:02X}'.format(b) for b in penis])

    with open(f'{file}obfuscated.super.bat', 'wb') as f:
        for i in out_hex:
            f.write(bytes.fromhex(i))

if __name__ == '__main__':
    obfuscate(file)
