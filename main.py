import random
import string


def main() -> None:
    path = input('{:<27}: '.format('File path (.bat)'))
    level = int(input('{:<27}: '.format('Obfuscation level (1 or 2)')))

    with open(path, 'r', encoding='utf-8') as f:
        code = f.read()

    if level == 1:
        with open('out.bat', 'w') as f:
            f.write(methods.one(code))

    elif level == 2:
        with open('out.bat', 'wb') as f:
            f.write(methods.two(code))


class methods:
    def one(code: str) -> str:
        out = ''
        for lines in code:
            for char in lines:
                if char == '\n':
                    out += char

                elif char == '%':
                    out += char
                    while char != '%':
                        char = next(lines)
                        out += char

                else:
                    ran_str = ''.join(random.choice(string.ascii_letters)
                                      for _ in range(random.randint(5, 15)))
                    out += f'{char}%{ran_str}%'

        return out

    def two(code: str) -> str:
        code = bytes(methods.one(code), 'utf-8')

        out = []
        out.extend(['FF', 'FE', '0A', '0D'])
        out.extend(['{:02X}'.format(b) for b in code])
        out = bytes.fromhex(''.join(out))

        return out


if __name__ == '__main__':
    main()
