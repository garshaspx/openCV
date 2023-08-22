from subprocess import CalledProcessError, call
from os import chdir, path

packages = {'opencv-python':'4.8.0.76', 'ultralytics':'8.0.154', 'pillow':'10.0.0', 'Nuitka':'1.7.10'}
for package, version in packages.items():
    try:
        call(['pip', 'install', f"{package}=={version}"])
        print(f"Successfully installed {package} version {version}")
    except CalledProcessError:
        print(f"Failed to install {package}")

current_file_path = path.abspath(__file__)
current_directory = path.dirname(current_file_path)
chdir(current_directory)


print("installig ...")

try:
    call(f"python -m nuitka --enable-plugin=tk-inter --disable-console --windows-icon-from-ico=media/icon.ico main_app.py")
    print("-------installination is done")
except:
    print("installination failed.")



# print("shorcut created ")
input("-------press enter to exit ... ")