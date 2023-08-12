import sys
import os
from cx_Freeze import Executable, setup

# Get the script filename
script = sys.argv[1] 

# Setup cx_Freeze options
exe_options = {
    'script': script,
    'icon': 'icon.ico',
    'optimize': 2,
    'compressed': True,
    'include_files': [('data.txt', 'data.txt')] 
}

# Configure cx_Freeze setup
setup(
    name = "MyApp",
    version = "0.1",
    description = "Sample cx_Freeze script",
    options = {'build_exe': exe_options},
    executables = [Executable(**exe_options)]
)

# Build the .exe file
os.system("python setup.py build")