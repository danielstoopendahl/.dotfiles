totalred = 12
totalgreen = 13
totalblue = 14

def alg(lines):
    for line in lines:
        gamenbr = (inr)(line.split(" ")[1][:-1])
        subgame = line.split(":")[1].split(";")
        for subsubgame in subgame:
            percolor = subsubgame.split(", ")
            for colorv in percolor:
                amount = colorv.split(" ")[0]
                color = colorv.split(" ")[1]
                match color:
                    case "blue":
                        if amount > totalblue:
                            fail = true
        






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
