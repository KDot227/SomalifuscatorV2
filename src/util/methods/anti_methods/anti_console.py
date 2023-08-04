from util.obfuscation.obf_oneline import Obfuscate_Single


class AntiConsole:
    def __init__(self) -> None:
        pass

    @staticmethod
    def main(code: list) -> list:
        vbs_code = """if defined redo goto :KDOTUP
set "redo=1"
echo CreateObject("Wscript.Shell").Run "%~f0", 0, True > temp.vbs
cscript //nologo temp.vbs
del temp.vbs
exit
:KDOTUP
"""
        vbs_code = vbs_code.splitlines()
        for index, line in enumerate(vbs_code):
            code.insert(index, Obfuscate_Single(line).out() + "\n")
        return code