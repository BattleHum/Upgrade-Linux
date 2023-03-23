#!/bin/python3
import subprocess

def upgrade():
    subprocess.call(["apt-get", "update", "-y"])
    subprocess.call(["apt-get", "upgrade", "-y"])
    subprocess.call(["apt-get", "dist-upgrade", "-y"])
    
if __name__ == '__main__':
    upgrade()
