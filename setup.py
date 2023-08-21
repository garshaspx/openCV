import subprocess
from os import getcwd

def install_packages(packages):
    

    for package, version in packages.items():
        try:
            x = subprocess.check_output(['pip', 'install', f"{package}=={version}"])
            print(x)
            print(f"Successfully installed {package} version {version}")
        except subprocess.CalledProcessError:
            print(f"Failed to install {package}=={version}")


packages_to_install = {
    'opencv-python':'4.8.0.76',
    'ultralytics':'8.0.154',
    'pillow':'10.0.0',
    'Nuitka':'1.7.10'
}

# install_packages(packages_to_install)




print(f'{getcwd()}\\main.py')
subprocess.Popen(['Nuitka', 'main.py'], bufsize=0)
print("setup completed")

