totalred = 12
totalgreen = 13
totalblue = 14

def alg(lines):
    total = 0
    for line in lines:
        gamenbr = (int)(line.split(" ")[1][:-1])
        subgame = line.split(": ")[1].split("; ")
        tooMany = False
        blueamount = 0
        redamount = 0
        greenamount = 0
        for subsubgame in subgame:
            percolor = subsubgame.split(", ")
            for colorv in percolor:
                amount = (int)(colorv.split(" ")[0])
                color = colorv.split(" ")[1].replace("\n", "")
                #print(color, amount)
                match color:
                    case "blue":
                        blueamount += amount
                        if amount > totalblue:
                            tooMany = True
                            break
                    case "green":
                        greenamount += amount
                        if amount > totalgreen:
                            tooMany = True
                            break
                    case "red":
                        redamount += amount
                        if amount > totalred:
                            tooMany = True
                            break
                    


        if not tooMany:
            #print(gamenbr)
            total += gamenbr
    return total


def alg2(lines):
    total = 0
    for line in lines:
        gamenbr = (int)(line.split(" ")[1][:-1])
        subgame = line.split(": ")[1].split("; ")
        blueamount = 0
        redamount = 0
        greenamount = 0
        for subsubgame in subgame:
            percolor = subsubgame.split(", ")
            for colorv in percolor:
                amount = (int)(colorv.split(" ")[0])
                color = colorv.split(" ")[1].replace("\n", "")
                #print(color, amount)
                match color:
                    case "blue":
                        blueamount = max(amount, blueamount)
                        
                    case "green":
                        greenamount += amount
                        if amount > totalgreen:
                            tooMany = True
                            break
                    case "red":
                        redamount += amount
                        if amount > totalred:
                            tooMany = True
                            break
                    


        if not tooMany:
            #print(gamenbr)
            total += gamenbr
    return total




file_path = 'input.txt'
try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        total = alg(lines)
        print(total)
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
