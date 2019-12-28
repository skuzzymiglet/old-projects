import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32": base = "Win32GUI"
opts = {"include_files": ["audio/*", "fonts/*"], "includes": ["re", "pygame"]}
setup(
    name="Face the Numbers",
    version="0.1",
    description="A Reaction Game for the Keyboard-Minded",
    author="Rafik Harrington",
    options = {"bouild_exe": opts},
    executables = [Executable("main0.py", base=base)]
    )
