import random, tqdm
import numpy as np
import pandas as pd


def check_piece(data_piece):
    violations = {}
    violation = False
    for idx_number, number in enumerate(data_piece):
        if number in rules:
            violations[idx_number] = []
            rule = rules[number]
            # forward = data_piece[idx_number+1:]
            backward = data_piece[:idx_number]
            # for idx_element, element in enumerate(forward):
            #     if element not in rule:
            #         violation = True
            #         violations[idx_number].append(idx_number + idx_element+1)
            for idx_element, element in enumerate(backward):
                if element in rule:
                    violation = True
                    violations[idx_number].append(idx_element)

        else:
            raise Exception("Number not in rules")
    return violation, violations


def sort_piece(data_piece, violation_idxs):
    violation = True
    while violation:
        # print(f"data piece: {data_piece}")
        # print(f"indexes that violate rules: {violation_idxs}")
        
        # Get index with fewest violations but not zero
        fewest_violations = float("inf")
        index_with_fewest_violations = 0
        for idx, _ in enumerate(violation_idxs.values()):
            if (len(_) > 0) and (len(_) <= fewest_violations):
                fewest_violations = len(_)
                index_with_fewest_violations = max(idx, index_with_fewest_violations)

        target_index = violation_idxs[index_with_fewest_violations][-1]
        data_piece[index_with_fewest_violations], data_piece[target_index] = data_piece[target_index], data_piece[index_with_fewest_violations] 
        violation, violation_idxs = check_piece(data_piece)
    return data_piece


with open("2024/05/input") as file:
    # Read rules
    rules = {}
    # Read data
    data = []
    for i in tqdm.tqdm(range(1368)):
        line = file.readline().rstrip()
        print(line)
        if "|" in line:
            A = int(line.split("|")[0])
            B = int(line.split("|")[1])
            if A in rules.keys():
                rules[A].append(B)
            else:
                rules[A] = [B]
        elif len(line) > 0:
            line = [int(i) for i in line.split(",")]
            data.append(line)
        else:
            print("invalid line")

result_1 = []
result_2 = []
for idx, data_piece in tqdm.tqdm(enumerate(data)):
    violation, violation_idxs = check_piece(data_piece)
    if not violation:
        result_1.append(data_piece[round(len(data_piece)/2-0.5)])
    else:
        sorted_data_piece = sort_piece(data_piece, violation_idxs)
        result_2.append(sorted_data_piece[round(len(data_piece)/2-0.5)])
    
result_1 = sum(result_1)
result_2 = sum(result_2)

print(f"Part One Result: {result_1}")
print(f"Part Two Result: {result_2}")
print("finish")