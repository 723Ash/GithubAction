# lint.py

import subprocess

def run_flake8():
    result = subprocess.run(['flake8', '.'], capture_output=True, text=True)
    if result.returncode != 0:
        print("Flake8 found issues:\n")
        print(result.stdout)
    else:
        print("No linting issues found!")

if __name__ == "__main__":
    run_flake8()
