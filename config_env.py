import os


if __name__ == "__main__":
    # Enable script execution
    os.system("Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine")

    venv = None
    if os.path.exists("./venv"):
        venv = "venv"
    elif os.path.exists("./.venv"):
        venv = ".venv"

    if venv is None:
        # create virtual environment
        os.system("python -m venv .venv")
        venv = ".venv"

    # activate virtual environment
    os.system(f"./{venv}/Scripts/activate")

    # install requirements
    os.system("pip install -r requirements.txt")
