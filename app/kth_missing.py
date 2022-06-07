'''
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. 
    The 5th missing positive integer is 9.
'''
def validate_data(arr, k):
    if (1 <= len(arr) <= 1000) and (1 <= k <= 1000):
        valid = True
    return valid
                    
        
def kth_missing_positive_number(arr, k):
    '''
    INPUT: List of numbers in increating order & a positive integer k
    OUTPUT: The kth missing number
    '''
    
    valid = False
    max_len = 1000
    missing_ints = []

    valid = validate_data(arr, k)

    if valid:
        for i in range(max_len):
            j = i + 1
            if (j) not in arr:
                missing_ints.append(j)
            
            if len(missing_ints) == k:
                return j
    else:
        return k

list = [2,3,4,7,11]
k = 5
answer = kth_missing_positive_number(list, k)
print(f"Answer: {answer}")