import os
import platform
import subprocess


if __name__ == "__main__":
    # Try to enable script execution
    powershell64 = os.path.join(os.environ['SystemRoot'],
                                'SysNative' if platform.architecture()[0] == '32bit' else 'System32',
                                'WindowsPowerShell', 'v1.0', 'powershell.exe')

    psxmlgen = subprocess.Popen(f"{powershell64} Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser",
                                cwd=os.getcwd())
    result = psxmlgen.wait()

    venv = None
    if os.path.exists("./venv"):
        venv = "venv"
    elif os.path.exists("./.venv"):
        venv = ".venv"

    cmd = ""

    if venv is None:
        # create virtual environment
        cmd += "python -m venv venv &&"
        venv = "venv"

    # activate virtual environment and install requirements
    activate_script = f".\\{venv}\\Scripts\\activate"
    cmd += f"{activate_script} && pip install -r requirements.txt"

    print(cmd)

    os.system(cmd)
