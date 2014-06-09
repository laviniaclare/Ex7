"""Open and read file (command line argument).
Make a dictionary with words as keys and times seen as values.
Order keys by values.
"""
from sys import argv
import operator

words_in_txt = {}
input_file = argv[1]

def main():
    with open(input_file) as f:
        contents = f.read().lower().replace("\n"," ").split(" ")

        for i in contents:
            if i.isalpha():
                if i not in words_in_txt:
                    words_in_txt[i] = 1
                else:
                    words_in_txt[i] += 1

    # sort words in txt alphabetically then highest to lowest frequency
    sorted_values = sorted(words_in_txt.iteritems(), key = operator.itemgetter(0))
    sorted_values = sorted(sorted_values, key = operator.itemgetter(1), reverse = True)

    for item in sorted_values:
        print item[0], item[1]                    

if __name__ == "__main__":
    main()