import os
import shutil
login = str(os.getlogin())
loc = "C:\\Users\\" + login + "\\"
if os.path.exists(loc + "SSS"):
  os.mkdir(loc + "SSS")
if os.path.exists(loc + "SSS\\SidecansSoftware"):
  os.mkdir(loc + "SSS\\SidecansSoftware")
if os.path.exists(loc + "SSS\\SidecansSoftware\\CobraVenom"):
  os.mkdir(loc + "SSS\\SidecansSoftware\\CobraVenom")

