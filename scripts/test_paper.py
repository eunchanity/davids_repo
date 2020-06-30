from collections import Counter

string1 = 'ask a bunch get a bunch'
def count_words(string1):
    lst = string1.split()
    dic = Counter()

    for word in lst:
        dic[word] += 1
        
    return dic

print(count_words(string1))