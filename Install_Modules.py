import subprocess

modules = ['requests', 'pyautogui', 'ecdsa', 'pickle']


for module in modules:
    try:
        subprocess.check_call(['pip', 'install', module])
        print(f"Successfully installed {module}")
    except subprocess.CalledProcessError:
        print(f"Failed to install {module}")