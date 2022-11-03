count = [0]
def digit_match(l1, l2):
    l1 = str(l1)
    l2 = str(l2)

    if len(l1) == 0 or len(l2) == 0:
        match = ''.join(str(count[0]))
        count[0] = 0
        return int(match)

    if l1[-1] == l2[-1]:
        count[0] += 1

    l1 = l1[:-1]
    l2 = l2[:-1]

    if l1 and l2:
        l1 = int(l1)
        l2 = int(l2)
    
    
    return digit_match(l1, l2)

apples = 1072503891
oranges = 62530841
print(digit_match(apples, oranges)) # 4

apples = 0
oranges = 62530841
print(digit_match(apples, oranges)) # 0

apples = 841
oranges = 62530841
print(digit_match(apples, oranges)) # 3

apples = 0
oranges = 0
print(digit_match(apples, oranges)) # 1

apples = 10
oranges = 20
print(digit_match(apples, oranges)) # 1