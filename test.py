
file = open("cocor.txt", "r")

lines = file.readlines()

chars = []
keys = []
tokens = []

modo = ""
for line in lines:
    if (line.split(" ")[0] == "TOKENS"):
        modo = "tokens"
    
    elif (line.split(" ")[0] == "PRODUCTIONS"):
        modo = "productions"

    elif (line.split(" ")[0] == "CHARACTERS"):
        modo = "characters"
    
    elif (line.split(" ")[0] == "KEYWORDS"):
        modo = "keywords"
    

    else:    
        if(modo == "tokens"):
            try:

                print(line.split(" ")[0], end = " = ")
                print(line.split(" ")[2])
            except:
                print("No token")
    # print(line.split(" "))