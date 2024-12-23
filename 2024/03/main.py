import numpy as np
import re


def mul(tuple):
    result = int(tuple[0]) * int(tuple[1])
    return result


pattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
results = []
with open("2024/03/input") as file:
    while line := file.readline():
        targets = re.findall(pattern, line)
        for target in targets:
            results.append(mul(target))

result_1 = np.sum(results)
print(f"Part One Result: {result_1}")

results = []
data = ""
with open("2024/03/input") as file:
    while line := file.readline():
        data += line

targets = re.findall(pattern, data)
do = True
sections = [match.start() for match in re.finditer(pattern, data)]
results.append(mul(targets[0]))
for idx, section in enumerate(sections):
    if idx == 0:
        continue
    start = sections[idx-1]
    snippet = data[start:section]
    # print(snippet)
    if "don't()" in snippet:
        print("dont")
        do = False
    elif "do()" in snippet:
        print("do")
        do=True
    
    if do:
        results.append(mul(targets[idx]))
        do = True

result_2 = np.sum(results)
print(f"Part Two Result: {result_2}")