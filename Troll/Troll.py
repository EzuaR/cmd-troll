import subprocess
import time

def run_cmd():
    with subprocess.Popen(["cmd", "/k"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_CONSOLE) as cmd_process:
        time.sleep(5)

    cmd_process.terminate()

run_cmd()
