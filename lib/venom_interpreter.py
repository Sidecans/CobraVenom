class Scanner():
    def __init__(self):
        pass
    def readline(self, lin, total):
        chunks = lin.split(" ")
        if chunks[0] == "var":
            try:
                temp = chunks[1]
                del temp
            except:
                print("Line: " + total)
                print("Error: Errno [6]: Name of Variable not Provided")
                input("Press [Enter]")
            try:
                temp = chunks[2]
                del temp
            except:
                print("Line: " + total)
                print("Error: Errno [7]: Type/Value not Provided")
                input("Press [Enter]")
            token = chunks[2]
            Place = token.split(":")
            if len(Place) == 2:
                pass
            else:
                print("Line: " + total)
                print("Error: Errno [7]: Type:Value not Provided")    
                input("Press [Enter]")
            if Place[0] == "str":
                self.var[chunks[1]] = str(Place[1])
        
        if chunks[0] == "print":
            try:
                temp = chunks[1]
                del temp
            except:
                print("Line: " + total)
                print("Error: Errno [6]: Name of Variable not Provided")
                input("Press [Enter]")
            token = chunks[1]
            Place = token.split(":")
            if len(Place) == 2:
                pass
            else:
                print("Line: " + total)
                print("Error: Errno [7]: Type:Value not Provided")    
                input("Press [Enter]")
            if Place[0] == "var":
                print(self.var[Place[1]])
    def setup(self):
        self.var = dict()

        