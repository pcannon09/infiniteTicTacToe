from config import *
from colorama import Fore
from datetime import datetime

import json

class Debug:
    save_defaultType: str = "debug"

    def __init__(self, saveFile: str | None, defaultType: str = "debug"):
        global save_defaultType

        self.saveFile = saveFile
        self.defaultType = defaultType ; save_defaultType = defaultType

    def debug(self, msg: str, debType: str = save_defaultType):
        COLOR_TYPE: str | None

        match debType:
            case "debug":
                COLOR_TYPE = Fore.MAGENTA

            case "error":
                COLOR_TYPE = Fore.RED

            case "warning":
                COLOR_TYPE = Fore.YELLOW

            case _:
                COLOR_TYPE = None

                self.debug("Pass a value at least to param 1", "error")

                return

        debugData = f"[ {datetime.now()} | {COLOR_TYPE.capitalize()} ]" + COLOR_TYPE + msg + Fore.RESET

        print(debugData)

        if (self.saveFile is not None):
            with open(self.saveFile, "a") as file:
                file.write(debugData)
                file.flush()

