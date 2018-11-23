#!/usr/bin/env python3

##
# SixArm Unix shell functions, written as Python.
#
# These are for convenience, to help porting shell scripts to Python.
##

def out(msg):
  print(msg)

def err(msg):
  logging.error(msg)

def die(msg):
  logging.critcal(msg)
  sys.exit(1)

def now():
  return datetime.datetime.utcnow().isoformat() + "Z"

def sec():
  return str(int(time.time()))

def zid():
  return secrets.token_hex(16)

def cmd(name):
  return 0 == subprocess.run(f"command {name}", shell=True, check=True).returncode
