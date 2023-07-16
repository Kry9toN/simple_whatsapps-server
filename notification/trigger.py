import platform
import subprocess

def sendMessageWA(id, message):
    startupinfo = None
    if platform.system() == 'Windows':
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        subprocess.check_output(['C:/Program Files/nodejs/npx.cmd', 'mudslide', 'send', id, message], shell = False, startupinfo=startupinfo).decode()
    if platform.system() == 'Linux':
        subprocess.check_output(['npx', 'mudslide', 'send', id, message], shell = False, startupinfo=startupinfo).decode()
    return True