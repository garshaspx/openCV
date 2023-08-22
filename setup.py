import subprocess
import os



def install_packages(packages):
    for package, version in packages.items():
        try:
            subprocess.call(['pip', 'install', f"{package}=={version}"])
            print(f"Successfully installed {package} version {version}")
        except subprocess.CalledProcessError:
            print(f"Failed to install {package}")
packages_to_install = {
    'opencv-python':'4.8.0.76',
    'ultralytics':'8.0.154',
    'pillow':'10.0.0',
    'Nuitka':'1.7.10'
}

install_packages(packages_to_install)


current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
os.chdir(current_directory)





print("installig ...")

subprocess.call(f"python -m nuitka main_app.py")

print("-------installination is done")
input("-------press enter to exit ... ")