"""
Find the matching word in given sentence across given dictionary
v1.0 Supports only single words
"""

import re


def find(sentence, dictionary):
    sentence = sentence.strip()
    sentence = re.sub(r'\s+', '', sentence)
    sentence = re.sub(r'[^a-zA-Z]', '', sentence)
    sentence = sentence.lower()
    n = len(sentence)
    found = False
    result = "Not found"
    for i in range(n):
        s = ""
        for j in range(i, n):
            s += sentence[j]
            if s in dictionary:
                found = True
                break
        if found:
            result = s
            break
    return result


def main():
    dictionary = set([x.strip().lower() for x in open('dict.txt').readlines()])
    inputs = open('input.txt').readlines()
    i = 1
    for sentence in inputs:
        ans = find(sentence, dictionary)
        print('{i}. {ans}'.format(i=i, ans=ans.capitalize()))
        i += 1


if __name__ == '__main__':
    main()
