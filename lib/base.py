from cobra_interpreter import Scanner as Cobra
from venom_interpreter import Scanner as Venom
from cobra_venom_interpreter import Scanner as CobraVenom

def runC(file):
    extensi = file.split(".")
    extens = extensi[1]
    if extens == "CodeCobra":
        Scan = Cobra()
    elif extens == "CodeVenom":
        Scan = Venom()
    elif extens == "CobraVenom":
        Scan = CobraVenom()
    else:
        print("Error: Errno[5]: Invalid File Extension")
        input("Press [Enter]")
    with open(file, 'r') as f:
        for count, line in enumerate(f):
            pass
        count += 1
        total_lines = count
        Scan.setup()
        for x in range(1, total_lines):
            lin = f.readline(x)
            Scan.readline(lin, total_lines)
        