from levels.ultimate.modules.scrambler import scrambler

code = ["@echo off\n", "echo this is a test\n", "pause\n", "exit"]


t = scrambler(code, "ultimate")

with open("out.bat", "w", encoding="utf8", errors="ignore") as f:
    for array in t:
        for line in array:
            f.write(line)
