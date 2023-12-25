import random
import primefac


class Bit_Math:
    def generate_math_problem(self, answer: int) -> tuple:
        answer_nums = list(primefac.primefac(answer))

        for index, num in enumerate(answer_nums):
            if num > 200:
                answer_nums[index] = str(self.random_pick(num=num, hex_check=True))

        num1 = answer_nums[0]
        count = answer_nums.count(num1)

        if count >= 6:
            answer_nums = [num1**count] + answer_nums[count:]

        answer_nums = [random_oct_hex(int(item)) if isinstance(item, int) else item for item in answer_nums]

        result = " * ".join(str(i) for i in answer_nums)
        result = result.replace(" ", "")

        return (result, answer)

    def random_pick(self, num, hex_check=True) -> str:
        choices = [
            self.make_xor,
            self.make_not,
            self.random_bit_shift,
        ]
        return random.choice(choices)(num, hex_check=hex_check)

    @staticmethod
    def make_xor(number: int, hex_check: bool = True) -> str:
        ans = number

        if ans < 0:
            return random_oct_hex(ans)

        binary_string = bin(ans)[2:]
        random_binary = [random.choice([0, 1]) for _ in range(len(binary_string))]
        random2 = int("".join(str(i) for i in random_binary), 2)
        fixed2 = random2 ^ ans

        if hex_check:
            return f"({random_oct_hex(random2)} ^^ {random_oct_hex(fixed2)})"
        else:
            return f"({hex(random2)} ^^ {hex(fixed2)})"

    @staticmethod
    def make_not(number: int, *args, **kwargs) -> str:
        ans = number

        if ans < 0:
            return random_oct_hex(number)

        num_return = -ans - 1
        return f"~{random_oct_hex(num_return)}"

    @staticmethod
    def random_bit_shift(number: int, hex_check: bool = True) -> str:
        ans = number

        if ans < 0:
            return random_oct_hex(number)

        random_number_through = random.choice(list(range(2, 10)))
        generated = ans << random_number_through

        if generated > 25:
            generated = Bit_Math.make_xor(generated, hex_check=True)

        return f"({generated} ^>^> {random_number_through})"


def random_oct_hex(ans: int):
    if ans < 3:
        return str(ans)
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
