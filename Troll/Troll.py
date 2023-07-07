import subprocess
import time

def run_cmd():

    cmd_process = subprocess.Popen(["cmd", "/k"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_CONSOLE)


    time.sleep(5)


    cmd_process.terminate()

run_cmd()
