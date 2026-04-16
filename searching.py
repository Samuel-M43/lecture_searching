import os
import json

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

unordered = read_data("sequential.json", "unordered_numbers")

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


def main():
    data = read_data("sequential.json", "unordered_numbers")
    #print(data)
    wanted_num = 70
    positions = linear_search(data, wanted_num)
    ordered = read_data("sequential.json", "ordered_numbers")
    bin_search = binary_search(ordered, wanted_num)
    print(bin_search)


if __name__ == '__main__':
    main()