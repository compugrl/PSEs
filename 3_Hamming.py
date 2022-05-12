def hamming_distance(strand1, strand2):
    # if the strings aren't the same length
    # raise a ValueError
    if len(strand1) != len(strand2):
        raise ValueError("Strings aren't the same length.")
    else:
        # zip takes a consecutive value from each list
        # and adds it to a tuple output
        # In the syntax below, it only does the zip
        # if the two items aren't equal
        diff = [l1 for l1, l2 in zip(strand1, strand2) if l1 != l2]
        return len(diff)
        
strand1 = "GAG"
strand2 = "AGE"

result = hamming_distance(strand1, strand2)
print(f"{result=}")