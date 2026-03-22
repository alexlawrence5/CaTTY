#!/usr/bin/python3
import subprocess
import time
import os
from colorama import Fore, init

subprocess.run(["figlet", "CaSH"], text=True)
print("CaSH: Basic lightweight shell")
init()

while True:
  cmd = input(Fore.RED + "$ ")

  if cmd.lower() == "quit":
    print("Huh? Where are you going?")
    exit()

  if cmd.startswith("sleep "):
    try:
      sec = float(cmd[6:])
      time.sleep(sec)
    except ValueError:
      print("Invalid number!")
    continue

  elif cmd.startswith("echo "):
    print(cmd[5:])

  elif cmd.startswith("mkdir "):
    os.mkdir(cmd[6:])
    
  elif cmd.startswith("rmdir "):
    os.rmdir(cmd[6:])

  elif cmd == "install":
    inst = input("Enter package name (pacman): ")
    subprocess.run(["sudo", "pacman", "-Syu", inst], text=True)

  else:
    print("Huh!? C-command not found... Maybe we will add this command on the next update!")
