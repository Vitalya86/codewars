def scramble(s1, s2):
    cache_letters = '' # Creating a cache to speed up the result
    for char in s2:
        if char not in cache_letters:
            cache_letters += char
            if s2.count(char) > s1.count(char):
                return False
    return True



from collections import Counter
def scramble(s1,s2):
    return len(Counter(s2) - Counter(s1)) == 0


