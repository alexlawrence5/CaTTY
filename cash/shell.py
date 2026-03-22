#!/usr/bin/python3
import subprocess
import time
from colorama import Fore, init

init()

while True:
  cmd = input(Fore.RED + "$ ")

  if cmd.lower() == "quit":
    print("Huh? Where are you going?")
    exit()

  if cmd.startswith("sleep "):
#!/usr/bin/python3
import subprocess
import time
from colorama import Fore, init

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

  elif cmd == "install":
    inst = input("Enter package name (pacman): ")
    subprocess.run(["sudo", "pacman", "-Syu", inst], text=True)

  else:
    print("Huh!? C-command not found... Maybe we will add this command on the next update!")
