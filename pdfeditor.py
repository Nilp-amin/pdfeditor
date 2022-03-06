import os
import sys
from typing import (
    List
)

import pikepdf
import easygui

from pick import pick

EDITING_OPTIONS = [
    "merge",
    "delete",
]

if __name__ == "__main__":
    # TODO: Change the default to the location from which this program was called
    pdfs = easygui.fileopenbox(multiple=True, default="C:/downloads/*.pdf")
    if not pdfs:
        print(f"ERROR: Please select .pdf file(s) and try again")
        sys.exit(1)

    # pdf editing options
    option, _ = pick(EDITING_OPTIONS, "Choose editing mode", indicator="=>")
    print(option)

    if option.lower() == "merge":
        print("ERROR: This editing mode is yet to be implemented")
    elif option.lower() == "delete":
        pass