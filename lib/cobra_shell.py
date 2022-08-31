import time
import os
import cobra_interpreter as Cobra
import venom_interpreter as Venom
import cobra_venom_interpreter as CobraVenom
with open("destination.txt", 'r') as f:
    login = str(f.read())
class Scanner:
    def __init__(self, chunks):
        try:
            self.mode = chunks[2]
        except:
            pass
        self.keyword = chunks[0]
        self.exception()
        try:    
            self.command = chunks[1]
            self.exe_command()
        except:
            print("Error: Errno [1]: Command Not Provided")
    
    def exe_command(self):
        if self.keyword == "cd":
            if os.path.exists(login + "\\" + self.command):
                with open("destination.txt", 'w+') as F:
                    F.write(login + "\\" + "\\" + self.command)
        elif self.keyword == "mkdir":
            if os.path.exists(login + "\\" + self.command) == False:
                os.mkdir(self.command)
        elif self.keyword == "run":
            if os.path.exists(login + "\\" + self.command) == True:
                if self.mode.lower() == "cobra":
                    Cobra.run(login + "\\" + self.command)
                elif self.mode.lower() == "venom":
                    pass
                elif self.mode.lower() == "cobravenom":
                    pass
                else:
                    print("Error: Errno[4]: Mode not Provided")
            else:
                print("Error: Errno[3]: Location Not Found")
        else:
            print("Error: Errno[2]: Unkown Command")
    def exception(self):
        if self.keyword == "cls":
            os.system('cls')
            cobra_shell()
        elif self.keyword == "dfltdir":
            with open("destination.txt", 'w+') as f:

                f.write("C:\\Users")
def cobra_shell():
    with open("destination.txt", 'r') as f:
        login = str(f.read())
    print(str(login))
    text = input("Cobra > ")
    chunks = text.split(' ')
    new = Scanner(chunks)
while True:
    cobra_shell()

    
    
    
    