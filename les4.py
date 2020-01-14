#code utf-8
import os
import psutil
import shutil
import platform
import locale

def show_menu():
    print("""
[1] - Show file list
[2] - Show current pids
[3] - Show sys info
[4] - Duplicate all files
[5] - Your file duplicating in
[6] - Delete duplicate files in directory
""")

def sys_info():
    print('SYSTEMINFO: \nOS: '
    + platform.uname().system + ' ' + platform.uname().release
    + ' (Code page: '+ locale.getpreferredencoding()
    + ')'
    + '\nBuild: '+ str(platform.uname().version)
    + '\nCPU Count: '+ str(psutil.cpu_count()) + ' (' + platform.uname().machine
    + ' ' +str(int(psutil.cpu_freq().max)) + 'MHz)'
    + '\nMemory: Total:'+ str(psutil.virtual_memory().total)
    + ' (Used:' + str(psutil.virtual_memory().percent) + '%)'
    + '\nCurrent Login: ' + os.getlogin() + ' (PID: '+ str(os.getpid()) + ')'
    + '\nCurrent Directory: ' + os.path.dirname(os.path.realpath(__file__))
    )

sys_info()
