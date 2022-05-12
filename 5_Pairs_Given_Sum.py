'''

This function finds the number of pairs of numbers in a list which add up to a given target. This function takes in a list of whole numbers and a target as parameters. The return value is an integer of the number of pairs.

'''
def validate_data(num_list, target):
    valid_data = False

    if len(num_list) > 0 and target >= 0:
        for num in num_list:
            if isinstance(num, int):
                valid_data = True
        return valid_data

    return valid_data

def pairs_with_given_sum(num_list, target):
    length = len(num_list)
    counter = 0

    valid_data = validate_data(num_list, target)

    # if valid_data:
    #     for i in range(length):
    #         for j in range(i + 1, length):
    #             if num_list[i] + num_list[j] == target:
    #                 counter += 1

    num_dict = {}

    print(f"Target {target}")

# refactor
    for num in num_list:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    print(num_dict)

    for num in num_list:
        difference = target - num
        if difference in num_dict and (num_dict[difference] >= 1 and num_dict[num] >= 1):
            counter += 1
            
            num_dict[num] -= 1
            num_dict[difference] -= 1
# end of refactor
    return counter

num_list = [3, 5, 5, 1, 2, 3]
target = 8

result = pairs_with_given_sum(num_list, target)
print(f"Number of pairs: {result}")