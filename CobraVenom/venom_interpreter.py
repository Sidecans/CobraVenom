class Scanner():
    def __init__(self):
        pass
    def readline(self, lin):
        chunks = lin.split(" ")
        if chunks[0] == "var":
            try:
                temp = chunks[1]
                del temp
            except:
                print("Error: Errno [6]: Name of Variable not Provided")
            try:
                temp = chunks[2]
                del temp
            except:
                print("Error: Errno [7]: Type/Value not Provided")
            
            token = chunks[2]
            Place = token.split(":")
                
            
            # self.var[chunks[1]] 
    def setup(self):
        self.var = dict()

        