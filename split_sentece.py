import re

def split_sentence():
    re_split = '[．.。]'
    str_1 = input("string:")
    print("return:\n", re.split(re_split, str_1))

split_sentence()