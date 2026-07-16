from pathlib import Path
import subprocess

for req in Path("repos").rglob("requirements.txt"):

    print(req)

    subprocess.run([
        "pip",
        "install",
        "-r",
        str(req)
    ], check=True)