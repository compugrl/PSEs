def clean_string(string):
    clean_str = ""

    for char in string :
        if char.isalpha():
            char = char.lower()
            clean_str += char

    return clean_str

def palindrome(s):
    clean_str = clean_string(s)
    rev_str = "".join(reversed(clean_str))

    if clean_str == rev_str:
        return True
    return False

string = "kay2  Ak!"
result = palindrome(string)
print(result)