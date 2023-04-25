class level3:
    def __init__(self, file, *args, **kwargs) -> None:
        super().__init__()
        self.file = file
        self.main()

    def main(self):
        out_hex = []

        # lowkey overkill lmao
        out_hex.extend(["FF", "FE", "0A", "0D"])
        with open(f"{self.file}", "rb") as f:
            penis = f.read()

        out_hex.extend(["{:02X}".format(b) for b in penis])

        with open(f"{self.file}.level3.bat", "wb") as f:
            for i in out_hex:
                f.write(bytes.fromhex(i))
