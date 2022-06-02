'''
INPUT: Two dimensional list, and number of rows & columns of reshaped matrix
OUTPUT: Reshaped matrix
'''
def reshape_matrix(old_matrix, new_row, new_col):
    new_matrix = []
    old_row = len(old_matrix)
    old_col = len(old_matrix[0])
    col_list = []
    
    all_items = []
    for item in old_matrix:
        all_items.extend(item)

    if (new_row * new_col) == (old_row * old_col):
        for i in range(new_row):
            for j in range(new_col):
                col_list.append(all_items[j])
            all_items = all_items[new_col:]
            new_matrix.append(col_list)
            col_list = []
    else:
        return old_matrix
    
    return new_matrix

print(reshape_matrix([[1,2],[3,4], [5, 6], [7, 8]], 2, 4))    