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
call(f"python -m nuitka --enable-plugin=tk-inter --disable-console --windows-icon-from-ico=media/icon.ico main_app.py")
print("-------installination is done")





# executable_path = "main_app.exe"
# # Get the desktop directory
# desktop_directory = path.join(path.expanduser("~"), "Desktop")
# # Create a shortcut file name
# shortcut_name = "item_detector.lnk"
# # Create the command to create the shortcut
# command = 'powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut(\'{0}\');$s.TargetPath=\'{1}\';$s.Save()"'.format(
#     path.join(desktop_directory, shortcut_name),
#     path.abspath(executable_path)
# )
# # Create the shortcut using subprocess
# call(command, shell=True)




input("-------press enter to exit ... ")