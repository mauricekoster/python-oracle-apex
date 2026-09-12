from invoke import task

@task
def build(c, version="0.0"):
    print(f"BUILD! version: {version}")