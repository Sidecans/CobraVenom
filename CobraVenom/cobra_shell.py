import time
import os

with open("destination.txt", 'r') as f:
    login = str(f.read())
class Scanner():
    def __init__(self, chunks):
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
                    F.write(login + "\\" + self.command)
        elif self.keyword == "mkdir":
            if os.path.exists(login + "\\" + self.command) == False:
                os.mkdir(self.command)
        else:
            print("Error: Errno[2]: Unkown Command")
    def exception(self):
        if self.keyword == "cls":
            os.system('cls')
            cobra_shell()
def cobra_shell():
    with open("destination.txt", 'r') as f:
        login = str(f.read())
    print(str(login))
    text = input("Cobra > ")
    chunks = text.split(' ')
    Scanner(chunks)
while True:
    cobra_shell()

    
    
    
    