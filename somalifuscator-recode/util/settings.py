import json, time, os, string

class Settings:
    def __init__(self, settings_file: str) -> None:
        self.settings_file = settings_file
    
    def get_settings(self) -> dict:
        with open(self.settings_file, "r") as f:
            settings = f.read()
        return json.loads(settings)
    
settings = Settings("settings.json").get_settings()

try:
    chinese = settings["chinese"]
    pogdog_fun = settings["pogdog"]
    hell = settings["hell"]
    eicar = settings["eicar"]
    unicode = settings["unicode"]
    utf_16_bom = settings["utf_16_bom"]
    ads = settings["ads"]
    random_spacing = settings["random_spacing"]
    auto_update = settings["auto_update"]
    echo_weird = settings["echo_weird"]
    anti_vm = settings["anti_vm"]
    for_loop = settings["for_loop"]
    scramble_labels = settings["scramble_labels"]
    echo_check = settings["echo_check"]
    double_click_check = settings["double_click_check"]
    recursive_xor = settings["recursive_xor"]
except:
    print(
        "Your settings.json file has been update! Please redownload somalifuscator and try again"
    )
    time.sleep(30)
    os._exit(1)

settings2 = [
    f"Chinese = {chinese}",
    f"Pogdog = {pogdog_fun}",
    f"Hell = {hell}",
    f"Eicar = {eicar}",
    f"Unicode = {unicode}",
    f"UTF-16-BOM = {utf_16_bom}",
    f"ADS = {ads} (Experimental)",
    f"Random Spacing = {random_spacing}",
    f"Echo Weird = {echo_weird} (Experimental)",
    f"Auto Update = {auto_update}",
    f"Anti VM = {anti_vm}",
    f"For Loop Obfuscation = {for_loop} (Experimental)",
    f"Scramble Labels = {scramble_labels} (Experimental)",
    f"Echo Check = {echo_check}",
    f"Double Click Check = {double_click_check}",
    f"Recursive Xor = {recursive_xor} (Experimental)",
]

if chinese:
    chinese_characters = "苑范腕勝滕贖值債價償責直真賭哀衰衷袁忠棄業停亨享亭亮閏闊閒闌聞門閂閃閉開閑間閘閡閣閥閨閩閱閹閻闃闔闕闖關闡募幕慕壞壤讓鑲"
else:
    chinese_characters = string.ascii_letters + string.digits