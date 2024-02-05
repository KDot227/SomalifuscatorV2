import random
import string


class NullParse:
    def __init__(self) -> None:
        self.buffer = random.randint(10, 100)

    def apply_obf(self, code: list) -> list:
        out_block = []
        for index, string in enumerate(code):
            if index == len(code) - 1:
                appending_code = ""
                appending_code += self.make_random_string(self.buffer) + string.rstrip()
                appending_code += "\x00" * self.buffer
                out_block.append(appending_code)
            elif index == 0:
                out_block.append(string + "\n")
            elif string == "\n":
                out_block.append("")
            elif string.startswith(":") and not string.startswith("::"):
                out_block.append(string + "\n\n")
            else:
                out_block.append(
                    self.make_random_string(self.buffer) + string.rstrip() + "\n"
                )
        return out_block

    def write_code_null_parse(self, code, file: str) -> bool:
        with open(file, "wb") as f:
            for array in code:
                for string in array:
                    f.write(string.encode("utf-8"))
        return True

    def make_random_string(self, length: int) -> str:
        """Generate random characters."""
        return "".join(random.choice(string.ascii_letters) for i in range(length))


if __name__ == "__main__":
    test_code = r"""@echo off
echo this is a test lul
%test%echo this is a test lul
REM fuhciuhiuhiuhk
echo this is a test1"""
    test_code = test_code.splitlines()
    null_parse = NullParse()
    out_code = null_parse.apply_obf(test_code)
    null_parse.write_code_null_parse(out_code, "test.bat")
