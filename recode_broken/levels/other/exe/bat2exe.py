import os


class bat2exe:
    def __init__(self, file, *args, **kwargs) -> None:
        self.file = file
        self.bat2exe()

    def bat2exe(self):
        """The insperation for this was either from a github repo (90% sure) or a stackoverflow comment. Either way credit to the person who discovered this method. (NOTE: I also had to edit this a bit to work better with somalifuscator)"""
        code = r"""[Version]
Class=IEXPRESS
SEDVersion=3
[Options]
PackagePurpose=InstallApp
ShowInstallProgramWindow=0
HideExtractAnimation=1
UseLongFileName=1
InsideCompressed=0
CAB_FixedSize=0
CAB_ResvCodeSigning=0
RebootMode=N
InstallPrompt=%InstallPrompt%
DisplayLicense=%DisplayLicense%
FinishMessage=%FinishMessage%
TargetName=%TargetName%
FriendlyName=%FriendlyName%
AppLaunched=%AppLaunched%
PostInstallCmd=%PostInstallCmd%
AdminQuietInstCmd=%AdminQuietInstCmd%
UserQuietInstCmd=%UserQuietInstCmd%
SourceFiles=SourceFiles

[Strings]
InstallPrompt=
DisplayLicense=
FinishMessage=
FriendlyName=-
PostInstallCmd=<None>
AdminQuietInstCmd=
"""
        current_dir = os.getcwd()
        bat_file_name = os.path.basename(self.file)
        exe_name = bat_file_name[:-4] + ".exe"

        app_launched = "AppLaunched=cmd /c " + '"' + bat_file_name + '"'
        target = f"TargetName={exe_name}"
        file_0 = f"FILE0={bat_file_name}"
        source_files = f"[SourceFiles]\nSourceFiles0={current_dir}"
        extra = f"[SourceFiles0]\n%FILE0%="

        to_write = [app_launched, target, file_0, source_files, extra]
        with open("setup.sed", "a+") as f:
            f.write(code)
            for item in to_write:
                f.write(item + "\n")
        os.system("iexpress /n /q /m setup.sed")
        os.remove("setup.sed")
        print(f"Exe file saved as {exe_name}")
