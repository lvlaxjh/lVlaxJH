from cx_Freeze import setup, Executable
import sys
base = 'WIN32GUI' if sys.platform == "win32" else None


executables = [Executable("ui.py", base=base, icon='1.ico')]

packages = []
options = {
    'build_exe': {
        'packages':packages,
    },

}

setup(
    name = "prog",
    options = options,
    version = "1.0",
    description = 'desc of program',
    executables = executables
)