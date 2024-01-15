# 1st: 25 min
# 2nd: 26 min

def allcurrentsatend(currents):
    notatend = 0
    for c in currents:
        if c[2] != 'Z':
            notatend += 1
    return notatend <= 0


def alg(lines):
    stepamount = 0
    directions = lines[0]
    directionindex = 0
    map = {}

    for line in lines[2:]:
        k = line.split(" = ")[0]
        va = line.split(" = ")[1]
        v = (va[1:4], va[6:9])
        map[k] = v

    currents = []
    for (k, v) in map.items():
        if k[2] == 'A':
            currents.append(k)
    allacurrents = []
    while not allcurrentsatend(currents):
        newcurrents = []
        #print(currents)
        for c in currents:
            vp = map[c]
            if directions[directionindex] == 'L':
                newcurrents.append(vp[0])
            else:
                newcurrents.append(vp[1])
        currents = newcurrents
        # if currents in allacurrents:
        #     print(stepamount)
        # else:
        #     allacurrents.append(currents)

        directionindex = (directionindex + 1) % (len(directions) - 1)
        stepamount += 1

    return stepamount


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
