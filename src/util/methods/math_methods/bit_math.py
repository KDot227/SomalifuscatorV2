import random
import primefac


class Bit_Math:
    def generate_math_problem(self, answer: int) -> tuple:
        # return 1 = problem, 2 = answer

        answer_nums = list(primefac.primefac(answer))

        for index, num in enumerate(answer_nums):
            if num > 200:
                answer_nums[index] = str(self.random_pick(num=num, hex_check=True))

        num1 = answer_nums[0]
        count = answer_nums.count(num1)

        if count >= 6:
            # remove all occurences of num1
            for _ in range(count):
                answer_nums.remove(num1)
            num1 = num1**count
            answer_nums = [num1] + answer_nums

        result = " * ".join(str(i) for i in answer_nums)

        result = result.replace(" ", "")

        return (result, answer)

    def random_pick(self, num, hex_check=True) -> str:
        choices = [
            self.make_xor,
            self.make_not,
            # self.shift_left,
            # self.shift_right,
        ]
        return random.choice(choices)(num, hex_check=hex_check)

    @staticmethod
    def make_xor(number: int, hex_check: bool = True) -> str:
        """makes xor key"""
        ans = number

        if ans < 0:
            return random_oct_hex(ans)

        binary_string = bin(ans)[2:]

        choices = [0, 1]

        random_binary = [random.choice(choices) for i in range(len(binary_string))]

        random2 = "".join(str(i) for i in random_binary)
        random2 = int(random2, 2)

        # me asf when xor dont wanna be bae
        fixed2 = random2 ^ ans
        if hex_check:
            return f"({random_oct_hex(random2)} ^^ {random_oct_hex(fixed2)})"
        else:
            return f"({hex(random2)} ^^ {hex(fixed2)})"

    @staticmethod
    def make_not(number: int, hex_check: bool = True) -> str:
        """makes and key"""

        ans = number

        if ans < 0:
            return random_oct_hex(number)

        num_return = -ans - 1
        return f"~{num_return}"

    # @staticmethod
    # def shift_left(number: int, hex_check: bool = True) -> str:
    #    """makes shift left key"""


#
#    ans = number
#
#    if ans < 0:
#        return random_oct_hex(number)
#
#    num_return = ans << 1
#    return f"{num_return}"


def random_oct_hex(ans: int):
    choices = [hex(ans), oct(ans)]
    decided = random.choice(choices)
    if decided == oct(ans):
        return f"0{str(decided[2:])}"
    elif decided == hex(ans):
        if random.choice([True, False]):
            return f'"{str(decided)}"'
        return decided
    else:
        return decided


if __name__ == "__main__":
    numbers = list(range(100000, 10000000))
    hundred_random = random.choices(numbers, k=10000)
    for i in hundred_random:
        equation = Bit_Math().generate_math_problem(i)
        evaulated = eval(equation[0])
        if i != evaulated:
            print(equation)
            print(evaulated)
            print("ERROR")
            break
