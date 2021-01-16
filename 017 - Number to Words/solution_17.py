"""
HackRank Euler Project #17: Number to Words
"""

number_to_words = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten",
    "11": "Eleven",
    "12": "Twelve",
    "13": "Thirteen",
    "14": "Fourteen",
    "15": "Fifteen",
    "16": "Sixteen",
    "17": "Seventeen",
    "18": "Eighteen",
    "19": "Nineteen",
    "20": "Twenty",
    "30": "Thirty",
    "40": "Forty",
    "50": "Fifty",
    "60": "Sixty",
    "70": "Seventy",
    "80": "Eighty",
    "90": "Ninety"
}

separators = ["", "Thousand", "Million", "Billion", "Trillion"]


def triplet_to_word(triplet):
    """
    Convert given triplet, i.e. 3-digit, into word representation.
    """
    if triplet in number_to_words:
        return number_to_words[triplet]

    if len(triplet) == 2:
        if triplet == "00":
            return ""

        if triplet[0] == "0":
            return number_to_words[triplet[1]]

        return number_to_words[triplet[0] + "0"] + " " + number_to_words[triplet[1]]

    else:
        print('something is wrong\nTriplet:', triplet)


def separate(number):
    """
    Separate the number into parts from each of three digits.
    E.g. 12345678 -> 12_345_678
    """
    number_string = str(number)
    number_separated = []
    while len(number_string):
        number_separated.insert(0, number_string[-3:])
        number_string = number_string[:-3]

    return number_separated


def convert_to_words(number):
    """
    Words representation of given number.
    """
    number_separated = separate(number)
    words = []
    for index, triplet in enumerate(number_separated):

        if triplet == "000":
            continue

        if len(triplet) == 3 and triplet[0] != '0':
            triplet_word_list = [triplet_to_word(triplet[0]) + " Hundred " + triplet_to_word(triplet[1:])]
            triplet_word_list = [s.strip() for s in triplet_word_list]
            triplet_word = ' '.join(triplet_word_list)
        elif len(triplet) == 3 and triplet[0] == '0':
            triplet_word = triplet_to_word(triplet[1:])
        else:
            triplet_word = triplet_to_word(triplet)

        words.append(''.join(triplet_word))
        words.append(separators[len(number_separated) - (index + 1)])

    words_string = ' '.join(words).strip()
    return words_string


with open("test_inputs", "r") as f:
    lines = f.readlines()
    lines = [int(line.strip()) for line in lines]
    for number in lines:
        print("{} : {}".format(number, convert_to_words(number)))
