from random import randint
import random, codecs, string, os

file = input("What is the exact file name or path of file you want to obfuscate? (with file extension pls) -> ")

code = """@echo off
SETLOCAL EnableDelayedExpansion&set "n=a" &set "o=b" &set "p=c" &set "q=d" &set "r=e" &set "s=f" &set "t=g" &set "u=h" &set "v=i" &set "w=j" &set "x=k" &set "y=l" &set "z=m" &set "a=n" &set "b=o" &set "c=p" &set "d=q" &set "e=r" &set "f=s" &set "g=t" &set "h=u" &set "i=v" &set "j=w" &set "k=x" &set "l=y" &set "m=z" &set "N1=A" &set "O1=B" &set "P1=C" &set "Q1=D" &set "R1=E" &set "S1=F" &set "T1=G" &set "U1=H" &set "V1=I" &set "W1=J" &set "X1=K" &set "Y1=L" &set "Z1=M" &set "A1=N" &set "B1=O" &set "C1=P" &set "D1=Q" &set "E1=R" &set "F1=S" &set "G1=T" &set "H1=U" &set "I1=V" &set "J1=W" &set "K1=X" &set "L1=Y" &set "M1=Z"
"""


def obfuscate(file):
    try:
        os.remove(f'{file}.obfuscated.bat')
        os.remove(f'{file}.obfuscated.super.bat')
    except:
        pass
    switch = False
    with open(f'{file}', 'r+', encoding='utf-8') as original:
        for lines in original:
            for char in lines:
                if switch == False:
                    if '\n' in char:
                        with open(f'{file}.obfuscated.bat', 'a+', encoding='utf-8') as f:
                            f.write("\n")
                    elif "%" in char:
                        with open(f'{file}.obfuscated.bat', 'a+', encoding='utf-8') as f:
                            f.write("%")
                            switch = True #thx baum for making this work :sob:
                    else:
                        random_num = randint(5, 12)
                        random_string = ''.join(random.choice('☞☟☠☡☢☣☤☥☦☧☰☱☲☳☴☵☶☷☸♕☻♡☹♆♔♅♖♘♗♙♚♛♜♝♞♟♠♡♢♣♤♥♦♧♨♩♪♫♬♭♮♯♰♱♲♳♴♵♶♶♸♹♻♼♽♾⚀⚁⚂⚃⚄⚅⚆⚇⚈⚉⚊⚋⚌⚍⚎⚏⚐⚑⚒⚔⚕⚖⚗⚘⚙⚚⚛⚜⚝⚞⚟') for kdot in range(random_num))
                        with open(f'{file}.obfuscated.bat', 'a+', encoding='utf-8') as f:
                            if char in string.ascii_letters:
                                if char.islower():
                                    coded0 = codecs.encode(char, 'rot_13')
                                    coded = coded0.replace(coded0, f"%{coded0}%")
                                    f.write(f"{coded}%{random_string}%")
                                else:
                                    coded0 = codecs.encode(char, 'rot_13').upper()
                                    coded = coded0.replace(coded0, f'%{coded0}1%')
                                    f.write(f"{coded}%{random_string}%")
                            else:
                                f.write(f"{char}%{random_string}%")

                else:
                    if "%" in char:
                        with open(f'{file}.obfuscated.bat', 'a+', encoding='utf-8') as f:
                            f.write("%")
                            switch = False
                    elif '\n' in char:
                        with open(f'{file}.obfuscated.bat', 'a+', encoding='utf-8') as f:
                            f.write("\n")
                    else:
                        with open(f'{file}.obfuscated.bat', 'a+', encoding='utf-8') as f:
                            f.write(char) # spent like 2 hours trying to fix this and found baums again :sob: https://github.com/baum1810/batchobfuscator

    with open(f'{file}.obfuscated.bat', 'r+', encoding='utf-8') as f:
        everything = f.read()
    with open(f'{file}.obfuscated.bat', 'w+', encoding='utf-8') as f:
        f.write(f"{code}\n{everything}")

    out_hex = []

    out_hex.extend(["FF", "FE", "26", "63", "6C", "73", "0D", "0A", "FF", "FE", "0A", "0D"])
    with open(f'{file}.obfuscated.bat','rb') as f:
            penis = f.read()

    out_hex.extend(['{:02X}'.format(b) for b in penis])

    with open(f'{file}.obfuscated.super.bat', 'wb') as f:
        for i in out_hex:
            f.write(bytes.fromhex(i))

if __name__ == '__main__':
    obfuscate(file)
