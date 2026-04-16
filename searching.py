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

def main():
    data = read_data("sequential.json", "unordered_numbers")
    print(data)
    wanted_num = 9
    positions = linear_search(data, wanted_num)
    print(positions)


if __name__ == '__main__':
    main()