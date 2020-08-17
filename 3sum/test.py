

def get_positions(my_list):
    positions_dict = {}
    for index in range(len(my_list)):
        if my_list[index] not in positions_dict:
            positions_dict[my_list[index]] = set()
        positions_dict[my_list[index]].add(index)

    for follower in range(len(my_list)):
        for leader in range(follower + 1, len(my_list)):
            target = -my_list[follower] - my_list[leader]
            if target in positions_dict:
                #make sure not picking itself as a potential result
                positions = list(filter(
                    lambda item: item != follower and item != leader, positions_dict[target]))
                if positions:
                    return follower + 1, leader + 1, positions[0] + 1


def main():
    with open("test.txt", "r") as my_file:
        text_data = my_file.readlines()
        int_array = []
        for array in text_data[1:]:
            int_array.append([int(text) for text in array.split()])

        result = []
        for sub_list in int_array:
            indices = get_positions(sub_list)
            if indices:
                list(indices).sort()
                result.append(indices)
            else:
                result.append(-1)


if '__main()__':
    main()
