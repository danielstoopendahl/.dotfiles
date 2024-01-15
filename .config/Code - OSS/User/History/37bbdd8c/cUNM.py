# 1st: 25 min
# 2nd: länge min

def allcurrentsatend(currents):
    notatend = 0
    for c in currents:
        if c[2] != 'Z':
            notatend += 1
    return notatend <= 0


def alg(lines):
    stepamount = 0
    directions = lines[0][:-1]
    directionindex = 0
    map = {}
# 307
    # print(len(directions))
    for line in lines[2:]:
        k = line.split(" = ")[0]
        va = line.split(" = ")[1]
        v = (va[1:4], va[6:9])
        map[k] = v

    currents = []
    for (k, v) in map.items():
        if k[2] == 'A':
            currents.append(k)
    cs0 = []

    cyclelengths = [20569, 18727, 14429, 13201, 18113, 22411]
    cycleZindeces = [20569, 18727, 14429, 13201, 18113, 22411]

    # len 20876
    # cycle starts after 307 and has len 20569

    currentit = cycleZindeces
    while True:
        print(currentit[0])
        minindex = 0
        minim = min(currentit)
        for i in range(len(currentit)):
            if currentit[i] == minim:
                minindex = i
        currentit[minindex] += cyclelengths[minindex]

        if all(e == currentit[0] for e in currentit):
            break
    print(currentit)

    while True:
        if stepamount % 20569 == 0:
            print(currents[0])

        elif directionindex == 0:
            cs0.append(currents[0])
        vp = map[currents[0]]
        if directions[directionindex] == 'L':
            currents[0] = vp[0]
        else:
            currents[0] = vp[1]

        directionindex = (directionindex + 1) % len(directions)
        stepamount += 1

    # print(cs0, currents[1])
    # print(cycleZindeces)
    # while not allcurrentsatend(currents):
    #     newcurrents = []
    #     for i in range(len(currents)):
    #         if directionindex == 0:
    #             if currents[0] in c0s:
    #                 print(stepamount, len(c0s))
    #             else:
    #                 c0s.append(currents[i])
    #         vp = map[currents[i]]
    #         if directions[directionindex] == 'L':
    #             newcurrents.append(vp[0])
    #         else:
    #             newcurrents.append(vp[1])
    #     currents = newcurrents
    #
    #     directionindex = (directionindex + 1) % len(directions)
    #     stepamount += 1

    return stepamount


file_path = 'input.txt'
try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        total = alg(lines)
        # print(total)
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
