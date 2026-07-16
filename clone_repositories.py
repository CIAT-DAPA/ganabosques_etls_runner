import os
import yaml
import subprocess

TOKEN = os.environ["GITHUB_TOKEN"]

with open("repos.yml") as f:
    repos = yaml.safe_load(f)

os.makedirs("repos", exist_ok=True)

for name, repo in repos["repositories"].items():

    url = repo["url"]

    branch = repo.get("branch", "main")

    authenticated = url.replace(
        "https://",
        f"https://{TOKEN}@"
    )

    subprocess.run([
        "git",
        "clone",
        "--branch",
        branch,
        authenticated,
        f"repos/{name}"
    ], check=True)