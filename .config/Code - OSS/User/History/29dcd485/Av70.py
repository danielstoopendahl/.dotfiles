# Open a file in read mode ('r')
file_path = 'input.txt'
digitnames = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# 4, 3, 3, 5, 4, 4, 3, 5, 5, 4
def alg(list):
    total = 0
    for line in list:
        digits = "".join(d for d in line if d.isdigit())
        linevalue = 10 * (int)(digits[0]) +  (int)(digits[-1])
        total += linevalue
    return total

def valueOfChars(line, i):
    value = -1
    substr = line[i:]
    for i in range(len(digitnames)):
        digitname = digitnames[i]
        lendigit = len(digitname)
        if substr[0:lendigit] == digitname:
            value = i
    return value


    

def alg2(list):
    total = 0
    for line in list:
        digits = []
        lenline = len(line)
        for i in range(lenline):
            if line[i].isdigit():
                digits.append(line[i])
            elif lenline - i >= 3:
                v = valueOfChars(line, i)
                if v != -1:
                    digits.append(v)

        
        linevalue = 10 * (int)(digits[0]) +  (int)(digits[-1])
        total += linevalue
    return total



try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        total = alg2(lines)
        print(total)
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
