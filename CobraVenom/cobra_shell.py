import time
import os
class Scanner():
    def __init__(self, chunks):
        self.__class__keyword = chunks[0]
        try:    
            self.command = chunks[1]

        except:
            print("Error: Errno [1]: Command Not Provided")

        
            
with open("destination.txt", 'rb') as f:
    login = f.read()
while True:
    print(login)
    text = input("Cobra > ")
    chunks = text.split(' ')
    Scanner(chunks)
    time.sleep(5)
    os.system('cls')
    
    
    
    