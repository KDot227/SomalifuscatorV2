from util.common import *
from util.cesar import *
from ultimate.modules.gen_obf import obf_oneline
import string


def ran1(char):
    # caesar cipher rotation shi
    choices = [make_random_string(), make_random_string()]
    randomed = random.choice(choices)
    if char in string.ascii_letters:
        if char.islower():
            coded0 = caesar_cipher_rotation(char)
            coded = coded0.replace(coded0, f"%{coded0}%")
            return f"{coded}%{randomed}%"
        else:
            coded0 = caesar_cipher_rotation_UPPER(char)
            coded = coded0.replace(coded0, f"%{coded0}1%")
            return f"{coded}%{randomed}%"
    else:
        return f"{char}%{randomed}%"


def ran2(char, random_order, carrot: bool):
    # fasho could have used dict for this but idc its already done
    public = r"C:\Users\Public"
    weird = r"C:\Program Files (x86)\Common Files"
    program_1 = r"C:\Program Files"
    program_2 = r"C:\Program Files (x86)"
    psmodule_path = r"C:\Program Files\WindowsPowerShell\Modules;C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules"
    driver_stuff = r"C:\Windows\System32\Drivers\DriverData"
    comspec = r"C:\WINDOWS\system32\cmd.exe"
    pathext = r".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
    session_name = r"Console"
    program_data = r"C:\ProgramData"
    alluserprofile = r"C:\ProgramData"
    ProgramW6432 = r"C:\Program Files"
    SystemDrive = r"C:"
    SystemRoot = r"C:\WINDOWS"
    windir = r"C:\WINDOWS"
    # not adding the comspec exploit yet
    ComSpec = r"C:\WINDOWS\system32\cmd.exe"
    CommonProgramFiles = r"C:\Program Files\Common Files"
    CommonProgramFiles_x86 = r"C:\Program Files (x86)\Common Files"
    CommonProgramW6432 = r"C:\Program Files\Common Files"
    DriverData = r"C:\Windows\System32\Drivers\DriverData"

    list_of_all = [
        public,
        weird,
        program_1,
        program_2,
        psmodule_path,
        driver_stuff,
        comspec,
        pathext,
        session_name,
        program_data,
        alluserprofile,
        ProgramW6432,
        SystemDrive,
        SystemRoot,
        windir,
        ComSpec,
        CommonProgramFiles,
        CommonProgramFiles_x86,
        CommonProgramW6432,
        DriverData,
    ]

    corosponding = [
        "PUBLIC",
        "COMMONPROGRAMFILES(X86)",
        "PROGRAMFILES",
        "PROGRAMFILES(X86)",
        "PSMODULEPATH",
        "DRIVERDATA",
        "COMSPEC",
        "PATHEXT",
        "SESSIONNAME",
        "PROGRAMDATA",
        "ALLUSERPROFILE",
        "PROGRAMW6432",
        "SYSTEMDRIVE",
        "SYSTEMROOT",
        "WINDIR",
        "COMSPEC",
        "COMMONPROGRAMFILES",
        "COMMONPROGRAMFILES(X86)",
        "COMMONPROGRAMW6432",
    ]

    new_lists = []

    for i in list_of_all:
        if char in i:
            new_lists.append(i)

    # random_posotive_negative = random.choice([True, False])
    if len(new_lists) > 0:
        if char == " ":
            return char
        new = random.choice(new_lists)
        if char in new:
            # if random_posotive_negative:
            #    if new == psmodule_path:
            #        index = new.index(char)
            #        new = corosponding[list_of_all.index(new)]
            #        return f"{self.random_single_carrot(carrot)}%{self.random_capitalization(new)}:~{index},1%"
            #    else:
            #        # index = new.index(char)
            #        # new = corosponding[list_of_all.index(new)]
            #        # length = len(new)
            #        # neg_index = length - index
            #        index = new.index(char)
            #        new = corosponding[list_of_all.index(new)]
            #        negative_index = index - len(new)
            #        print(
            #            f"{self.random_single_carrot(carrot)}%{self.random_capitalization(new)}:~{negative_index},1% {char}"
            #        )
            #        return f"{self.random_single_carrot(carrot)}%{self.random_capitalization(new)}:~{negative_index},1%"
            # else:
            if new == psmodule_path:
                index = new.index(char)
                new = corosponding[list_of_all.index(new)]
                return f"{random_single_carrot(carrot)}%{random_capitalization(new)}:~{index},1%"
            else:
                index = new.index(char)
                new = corosponding[list_of_all.index(new)]
                return f"{random_single_carrot(carrot)}%{random_capitalization(new)}:~{index},1%"
    else:
        if char in string.ascii_letters:
            var = f"{random_single_carrot(carrot)}%{random_capitalization('KDOT')}:~{random_order.index(char)},1%"
            return var
        else:
            return char


def ran3(line):
    random_letter = random.choice(string.ascii_letters)
    random_number = random.randint(1, 99)
    return f"for /l %%{random_letter} in ( {random_number}, {random_number}, {random_number} ) do ( {line} )\n"


def echo(line: str, errorlevel_state: bool) -> str:
    choices = {
        "for_loop": for_loop,
        "mshta": mshta,
        "powershell": powershell,
    }
    if not errorlevel_state:
        pick = random.choice(list(choices.keys()))
        return choices.get(pick)(line)
    else:
        return obf_oneline(line)


def mshta(line):
    line = line.split(" ", 1)[1]
    chars = [ord(c) for c in line]
    chars = " & ".join([f"Chr({c})" for c in chars])
    return obf_oneline(
        f'mshta vbscript:execute("CreateObject(""Scripting.FileSystemObject"").GetStandardStream(1).Write({chars}):Close")|more'
    )


def powershell(line):
    everything_after_first_line = line.split(" ", 1)[1]
    print(
        f"""powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -Command "Write-Host {everything_after_first_line}" """
    )
    return f"""powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -Command "Write-Host {everything_after_first_line}" """


def for_loop(self, line, errorlevel_check: bool):
    options_all = {
        ".cdxml": ".cdxml=Microsoft.PowerShellCmdletDefinitionXML.1",
        ".cmd": ".cmd=cmdfile",
        ".ps1xml": ".ps1xml=Microsoft.PowerShellXMLData.1",
        ".psc1": ".psc1=Microsoft.PowerShellConsole.1",
    }
    types = [
        "findstr",
        "assoc",
    ]
    # for loop base = for /f "tokens=1,2 delims= " %%a in ('assoc .cdxml') do (echo %%a)
    # delimiters go to the first occurrence of any part of the dilimiter then but before that part and not including.
    # for example for /f "tokens=1 delims=she" %%a in ('assoc .cdxml') do (echo %%a) will output .cdxml=Micro since the first occurence of the dilimiter is s
    # tokens get each chunk of each line that is being seperated by the delimiters

    random_type = random.choice(types)
    if random_type == "assoc":
        tokens = "1,2"
        out = f'{self.random_carrots("for", obf=True, commas=True)} /f '
    else:
        out = f'{self.random_carrots("for", obf=True, commas=True)} /f '


def set_(self, line: str) -> str:
    # all of these are finished im just too lazy to upload. (basically all except like half lmao)
    return line


def setlocal(self, line: str) -> str:
    return line


def if_(self, line: str) -> str:
    return line


def for_(self, line: str) -> str:
    return line


def goto(self, line: str) -> str:
    return line


def call(self, line: str) -> str:
    return line


def pause(self, line: str) -> str:
    return line


def exit(self, line: str) -> str:
    return line
