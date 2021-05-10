import sys
from cx_Freeze import setup, Executable


# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Pogulator",
    version = "0.1",
    description = "A calculator that contains trigo and quadratic solving features!",
    executables = [Executable("Calculator.py", base=base)]
)