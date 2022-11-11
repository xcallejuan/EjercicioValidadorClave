import os
import platform
import subprocess

if __name__ == "__main__":
    # Try to enable script execution
    powershell64 = os.path.join(os.environ['SystemRoot'],
                                'SysNative' if platform.architecture()[0] == '32bit' else 'System32',
                                'WindowsPowerShell', 'v1.0', 'powershell.exe')

    psxmlgen = subprocess.Popen(f"{powershell64} Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine",
                                cwd=os.getcwd())
    result = psxmlgen.wait()

    venv = None
    if os.path.exists("./venv"):
        venv = "venv"
    elif os.path.exists("./.venv"):
        venv = ".venv"

    if venv is None:
        # create virtual environment
        os.system("python -m venv venv")
        venv = "venv"

    # activate virtual environment
    activate_this_file = f"{venv}/Scripts/activate_this.py"
    with open(activate_this_file) as f:
        exec(f.read(), dict(__file__=activate_this_file))

    # install requirements
    os.system("pip install -r requirements.txt")
