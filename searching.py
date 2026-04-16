import os
import json
import time
import matplotlib.pyplot as plt
from generators import *

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as file:
        data = json.load(file)
        if field in data.keys():
            return data[field]
        else:
            return None


def linear_search(sequence, number):
    positions = []
    for idx, num in enumerate(sequence):
        if num == number:
            positions.append(idx)

    count = len(positions)
    positions_dict = {"Pozicie:": positions, "Pocet vyskytov:": count}
    return positions_dict


def binary_search(sequence, number):
    left = 0
    right = len(sequence) - 1
    while left <= right:
        middle = (left + right) // 2
        value = sequence[middle]
        if value == number:
            return middle
        elif value < number:
            left = middle + 1
        else:
            right = middle - 1
    return None

def measure_linear(seq, target, repeats=5):
    total = 0
    for _ in range(repeats):
        start = time.perf_counter()
        linear_search(seq, target)
        end = time.perf_counter()
        total += (end - start)
    return total / repeats


def measure_binary(seq, target, repeats=5):
    total = 0
    for _ in range(repeats):
        start = time.perf_counter()
        binary_search(seq, target)
        end = time.perf_counter()
        total += (end - start)
    return total / repeats


def pattern_search(sequence, pattern):
    positions = set()
    seq_len = len(sequence)
    pattern_len = len(pattern)
    for i in range(seq_len - pattern_len + 1):
        if sequence[i:i + pattern_len] == pattern:
            positions.add(i)
    return positions



def main():
    sizes = [100, 500, 1000, 5000, 10000]
    lin_times = []
    bin_times = []
    dna_seq = read_data("sequential.json", "dna_sequence")
    positions = pattern_search(dna_seq, "GA")
    print(positions)
    wanted_num = 70
    ordered_seq = ordered_sequence()

    for n in sizes:
        seq = ordered_sequence()
        lin_t = measure_linear(seq, wanted_num)
        bin_t = measure_binary(seq, wanted_num)
        lin_times.append(lin_t)
        bin_times.append(bin_t)
        print(f"Linear = {lin_t:.8f}s, Bin = {bin_t:.8f}s")

    plt.figure(figsize = (10,6))
    plt.plot(sizes, lin_times, label="Linearne vyhladavanie")
    plt.plot(sizes, bin_times, label="Binarne vyhladavanie")
    plt.xlabel("Velkost vstupu")
    plt.ylabel("Cas [s]")
    plt.title("Porovnanie vyhladavani")
    plt.legend()
    plt.grid(True)
    plt.show()




if __name__ == '__main__':
    main()