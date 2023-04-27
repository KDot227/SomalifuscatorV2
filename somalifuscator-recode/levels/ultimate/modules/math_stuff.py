import random

from util.settings import *


def generate_math_problem(self, answer: int):
    """Entire point of this is to make a math problem for the set /a. We do this cause kids need a calculator but once they see that there are octals and hexadecimals they'll prolly give up lmao"""
    # no division since we don't want floats BUT we can use division in the answer since its how you undo multiplication
    # but im not gonna do this cause it still makes floats and im slow
    operators = ["+", "-"]
    opp1 = random.choice(operators)
    opp2 = random.choice(operators)
    num1 = random.randint(10000, 10000000)
    num2 = random.randint(10000, 10000000)

    # maybe add division and multiplication to the problem using even dividers and getting remainder to check if zero.

    problem = f"{answer} {opp1} {num1} {opp2} {num2}"
    ans = eval(problem)

    # make new problem from original answer

    if opp1 == "+":
        opp1 = "-"
    else:
        opp1 = "+"

    if opp2 == "+":
        opp2 = "-"
    else:
        opp2 = "+"

    # randomly do hex or oct to ans instead of all just hex
    choices = [True, False]
    problem2 = f"{self.random_oct_hex(ans) if random.choice(choices) else self.make_xor(ans)} {opp1} {self.random_oct_hex(num1) if random.choice(choices) else self.make_xor(num1)} {opp2} {self.random_oct_hex(num2) if random.choice(choices) else self.make_xor(num2)}"
    problem23 = f"{ans} {opp1} {num1} {opp2} {num2}"

    ans2 = eval(problem23)

    while ans < 0:
        operators = ["+", "-"]
        opp1 = random.choice(operators)
        opp2 = random.choice(operators)
        num1 = random.randint(10000, 10000000)
        num2 = random.randint(10000, 10000000)

        problem = f"{answer} {opp1} {num1} {opp2} {num2}"
        ans = eval(problem)

        # make new problem from original answer

        if opp1 == "+":
            opp1 = "-"
        else:
            opp1 = "+"

        if opp2 == "+":
            opp2 = "-"
        else:
            opp2 = "+"

        # for some reason if number is negative only hex will work idk why and im not tryna figure it out
        # mental health > octals
        problem2 = f"{hex(ans)} {opp1} {self.random_oct_hex(num1)} {opp2} {self.random_oct_hex(num2)}"
        problem23 = f"{ans} {opp1} {num1} {opp2} {num2}"

        ans2 = eval(problem23)

    return problem2, ans2


def make_xor(self, number: int, hex_check: bool = True):
    """makes xor key"""
    ans = number

    if ans < 0:
        return self.random_oct_hex(ans)

    binary_string = bin(ans)[2:]

    choices = [0, 1]

    random_binary = [random.choice(choices) for i in range(len(binary_string))]

    random2 = "".join(str(i) for i in random_binary)
    random2 = int(random2, 2)

    max_fixed = int("1" * len(binary_string), 2)
    # me asf when xor dont wanna be bae
    fixed2 = random2 ^ ans
    while fixed2 > max_fixed:
        random_binary = [random.choice(choices) for i in range(len(binary_string))]
        random2 = "".join(str(i) for i in random_binary)
        random2 = int(random2, 2)
        fixed2 = random2 ^ ans

    if hex_check:
        random_tf = random.randint(1, 3)
        if not recursive_xor:
            random_tf = 2
        try:
            if random_tf != 1:
                return (
                    f"({self.random_oct_hex(random2)} ^^ {self.random_oct_hex(fixed2)})"
                )
            else:
                return f"({self.make_xor(random2)} ^^ {self.make_xor(fixed2)})"
        except RecursionError:
            return f"({self.random_oct_hex(random2)} ^^ {self.random_oct_hex(fixed2)})"
    else:
        return f"({hex(random2)} ^^ {hex(fixed2)})"
