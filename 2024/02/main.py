import pandas as pd
import numpy as np


sum = 0
with open("2024/02/input.csv") as file:
    while line := file.readline():
        line = line.rstrip()
        line = line.split(" ")
        line = [int(i) for i in line]
        line = np.array(line)
        line = pd.Series(line, dtype=int)
        if ((line.diff()<0).iloc[1:].all()) or ((line.diff().iloc[1:]>0).all()):
            if min(np.abs(line.diff().iloc[1:])) < 1:
                continue
            elif max(np.abs(line.diff().iloc[1:])) > 3:
                continue
            else:
                sum += 1

result_1 = np.copy(sum)
print(f"Part One Result: {result_1}")

def falsify(line):
    if not(((line.diff()<0).iloc[1:].all()) or ((line.diff().iloc[1:]>0).all())):
        return True
    elif min(np.abs(line.diff().iloc[1:])) < 1:
        return True
    elif max(np.abs(line.diff().iloc[1:])) > 3:
        return True
    
sum = 0
with open("2024/02/input.csv") as file:
    while line := file.readline():
        line = line.rstrip()
        line = line.split(" ")
        line = [int(i) for i in line]
        line = np.array(line)
        line = pd.Series(line, dtype=int)
        if falsify(line):
            for i in range(len(line)):
                if falsify(line.drop(i)):
                    continue
                else:
                    sum += 1
                    break
        else:
            sum += 1

result_2 = np.copy(sum)
print(f"Part Two Result: {result_2}")