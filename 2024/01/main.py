import pandas as pd
import numpy as np

data = pd.read_csv("2024/01/input.csv", header=None, delimiter=r"   ")
list_a = np.array(data[0])
list_b = np.array(data[1])

list_a_sorted = np.sort(list_a)
list_b_sorted = np.sort(list_b)

deviation = np.abs(list_a_sorted - list_b_sorted)

result_1 = np.sum(deviation)

print(f"Part One Result: {result_1}")

result_2 = 0
for value in list_a_sorted:
    result_2 += value * np.sum(list_b_sorted==value)

print(f"Part Two Result: {result_2}")

