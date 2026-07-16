import subprocess
import sys

if len(sys.argv) < 2:
    print("""
Usage:

farm
movement
deforestation
risk

Example:

movement -s SIGMA

farm -s SAGARI

deforestation --years 2024 --source smbyc

risk
""")
    exit(1)

etl = sys.argv[1]
args = sys.argv[2:]

print(f"Running ETL {etl} with args {args}")

commands = {
    "farm": "repos/farm/src/main.py",
    "movement": "repos/movement/src/main.py",
    "deforestation": "repos/deforestation/src/main.py",
    "risk": "repos/risk/src/main.py",
}

if etl not in commands:
    raise Exception(f"Unknown ETL {etl}")

subprocess.run(
    ["python", commands[etl], *args],
    check=True,
)