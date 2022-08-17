import os
import shutil
login = str(os.getlogin())
loc = "C:\\Users\\" + login + "\\"
if os.path.exists(loc + "SSS") == False:
  os.mkdir(loc + "SSS")
if os.path.exists(loc + "SSS\\SidecansSoftware") == False:
  os.mkdir(loc + "SSS\\SidecansSoftware")
if os.path.exists(loc + "SSS\\SidecansSoftware\\CobraVenom") == False:
  os.mkdir(loc + "SSS\\SidecansSoftware\\CobraVenom")

