import numpy as np

i = 0
with open("2024/04/input") as file:
    while line := file.readline():
        line = line.rstrip()
        print(line)
        if i == 0:
            xmas_matrix = np.array(list(line))
        else:
            xmas_matrix = np.vstack([xmas_matrix, list(line)])
        i += 1

"""
4 by 4 window
x... .x..
.m.. xmax
..a. .a..
...s .s..
"""
def detect(piece, type):
    if type == "diag":
        number = 0
        string = piece[0, 0] + piece[1, 1] + piece[2, 2] + piece [3, 3]
        if (string == "XMAS") or (string == "SAMX"):
            number += 1
        string = piece[3, 0] + piece[2, 1] + piece[1, 2] + piece[0, 3]
        if (string == "XMAS") or (string == "SAMX"):
            number += 1 
        return number
        
    elif type == "horizontal":
        number = 0
        for line in range(len(piece)):
            string = "".join(piece[line])
            if (string == "XMAS") or (string == "SAMX"):
                number += 1
            else:
                continue
        return number

    elif type == "vertical":
        number = 0
        for col in range(np.shape(piece)[1]):
            string = "".join(piece[:, col])
            if (string == "XMAS") or (string == "SAMX"):
                number += 1
            else:
                continue
        return number
    
    elif type == "mas":
        flag_1 = False
        flag_2 = False
        string = piece[0, 0] + piece[1, 1] + piece[2, 2]
        if (string == "MAS") or (string == "SAM"):
            flag_1 = True
        string = piece[2, 0] + piece[1, 1] + piece[0, 2]
        if flag_1 and ((string == "MAS") or (string == "SAM")):
            return 1
        else:
            return 0
           
        
m = 4
n = 4
number = 0
for i in range(np.shape(xmas_matrix)[1]-m+1):
    for j in range(np.shape(xmas_matrix)[0]-n+1):
        piece = xmas_matrix[i:i+m, j:j+n]
        # print(piece)
        number += detect(piece, "diag")
        if i%m == 0:
            number += detect(piece, "horizontal")
        if j%n == 0:
            number += detect(piece, "vertical")

result_1 = np.copy(number)
print(f"Part One Result: {result_1}")

m = 3
n = 3
number = 0
for i in range(np.shape(xmas_matrix)[1]-m+1):
    for j in range(np.shape(xmas_matrix)[0]-n+1):
        piece = xmas_matrix[i:i+m, j:j+n]
        print(piece)
        number += detect(piece, "mas")

result_2 = np.copy(number)
print(f"Part Two Result: {result_2}")

print("finish")