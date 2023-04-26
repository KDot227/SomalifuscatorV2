from util.settings import *
import random


def obf_oneline(self, line):
    final_string = ""
    for word in line.split(" "):
        if word.startswith("%"):
            final_string += word + " "
            continue
        if word.find("%~") != -1:
            final_string += word + " "
            continue
        if word.startswith("^"):
            final_string += word + " "
            continue
        if word.startswith("::"):
            final_string += word + " "
            continue
        else:
            for char in word:
                # fasho could have used dict for this but idc its already done
                public = r"C:\Users\Public"
                weird = r"C:\Program Files (x86)\Common Files"
                program_1 = r"C:\Program Files"
                program_2 = r"C:\Program Files (x86)"
                psmodule_path = r"C:\Program Files\WindowsPowerShell\Modules;C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules"
                driver_stuff = r"C:\Windows\System32\Drivers\DriverData"
                comspec = r"C:\WINDOWS\system32\cmd.exe"
                pathext = r".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"

                list_of_all = [
                    public,
                    weird,
                    program_1,
                    program_2,
                    psmodule_path,
                    driver_stuff,
                    comspec,
                    pathext,
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
                ]

                new_lists = []

                for i in list_of_all:
                    if char in i:
                        new_lists.append(i)

                if len(new_lists) > 0:
                    if char == " ":
                        final_string += char
                    new = random.choice(new_lists)
                    if char in new:
                        if new == psmodule_path:
                            index = new.index(char)
                            new = corosponding[list_of_all.index(new)]
                            final_string += (
                                f"%{self.random_capitalization(new)}:~{index},1%"
                            )
                        else:
                            index = new.index(char)
                            new = corosponding[list_of_all.index(new)]
                            final_string += (
                                f"%{self.random_capitalization(new)}:~{index},1%"
                            )
                else:
                    if unicode:
                        final_string += f"%‮%{char}%‮%"
                    else:
                        random_string = "".join(
                            random.choice(string.ascii_letters)
                            for _ in range(random.randint(5, 7))
                        )
                        final_string += f"%{random_string}%{char}%{random_string}%"
            final_string += " "

    return final_string
