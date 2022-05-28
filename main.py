# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(str1, str2):

    len_1 = len(str1)
    len_2 = len(str2)

    if len_1 != len_2:
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    for i  in range(0,len_1):
        if str1[i] != str2[i]:
            return False
    return True

print(find_anagram("street", "light")) 
print(find_anagram("heart", "earth")) 


