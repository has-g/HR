'''
"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False

even number of letters
 then each letter must have even number of occurrences

 if (val%2): return False

odd number of letters
    then one letter is allowed odd number of occurrences
    AND every other letter must have even number of occurrences
    if (val%2 == 1)
        if (oddFlag == 1)
            return False
        else:
            oddFlag = 1
    else:


edge cases
    0 list is True
    list of 1 is also true

        if (string_len//2):
        # is odd
    else:
        # is even

'''

def has_palindrome_permutation(the_string):
    string_len = len(the_string)

    if (string_len == 0) or (string_len == 1): return True

    # build a dict
    str_dict = dict()
    for i in range(len(the_string)):
        el = the_string[i]
        if (el in str_dict):
            value = str_dict[el]
            str_dict[el] = value + 1
        else:
            str_dict[el] = 1
    print(str_dict)

    oddFlag = False
    for key in str_dict.keys():
        if (str_dict[key]%2):
            # value of this key is odd
            if (oddFlag == True):
                # ive just found a second key which is also odd
                return False
            else:
                oddFlag = True
    return True


print(has_palindrome_permutation('civil')) # false
print(has_palindrome_permutation('civic')) # true
print(has_palindrome_permutation('livci')) # false
print(has_palindrome_permutation('boohoo')) # false



#{'l': 1, 'i': 2, 'v': 1, 'c': 1} = false
#{'b': 1, 'o': 4, 'h': 1} = false


