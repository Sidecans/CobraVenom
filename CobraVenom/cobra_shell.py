import time
import os

with open("destination.txt", 'rb') as f:
    login = f.read()
class Scanner():
    def __init__(self, chunks):
        self.keyword = chunks[0]
        try:    
            self.command = chunks[1]
            self.exe_command()
        except:
            print("Error: Errno [1]: Command Not Provided")
    def exe_command(self):
        if self.keyword == "cd":
            if os.path.exists(login + "\\" + self.command):
                with open("destination.txt") as F:
                    F.write(login + "\\" + self.command)
            

while True:
    with open("destination.txt", 'rb') as f:
        login = f.read()
    print(login)
    text = input("Cobra > ")
    chunks = text.split(' ')
    Scanner(chunks)
    time.sleep(5)
    os.system('cls')
    
    
    
    