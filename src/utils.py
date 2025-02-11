from config import *
from colorama import Fore
from datetime import datetime

class Debug:
    save_defaultType: str = "debug"

    def __init__(self, saveFile: str | None, defaultType: str = "debug"):
        global save_defaultType

        self.saveFile = saveFile
        self.defaultType = defaultType

        save_defaultType = defaultType

    def debug(self, msg: str, debType: str = save_defaultType):
        from var import DEV

        COLOR_TYPE: str | None

        match debType:
            case "debug":
                COLOR_TYPE = Fore.MAGENTA

            case "error":
                COLOR_TYPE = Fore.RED

            case "warn":
                COLOR_TYPE = Fore.YELLOW

            case "info":
                COLOR_TYPE = Fore.CYAN

            case _:
                COLOR_TYPE = Fore.RESET

                self.debug("Pass a value at least to param 1", "error")

                return

        debugData = f"[ {datetime.now()} | {debType.capitalize()} | DEV_MODE: {DEV} ] {msg}"

        print(f"{COLOR_TYPE}{debugData}{Fore.RESET}")

        if (self.saveFile is not None):
            with open(self.saveFile, "a") as file:
                file.write(f"{debugData}\n")
                file.flush()

