import time
import os

with open("destination.txt", 'r') as f:
    login = str(f.read())
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
                with open("destination.txt", 'w+') as F:
                    F.write(login + "\\" + self.command)
            

while True:
    with open("destination.txt", 'r') as f:
        login = str(f.read())
    print(str(login))
    text = input("Cobra > ")
    chunks = text.split(' ')
    Scanner(chunks)

    
    
    
    