import re
import itertools
import math
import csv
from itertools import *

alletters1 = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й',
              'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
              'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']
popular_bigrams = ['ст', 'но', 'то', 'на', 'ен']


def countletterfrequency(text):
    alletters = alletters1
    # text = open("refactoredtext.txt").read()
    letterfrequency = dict.fromkeys(alletters, 0)
    for i in text:
        if i in alletters:
            letterfrequency[i] += 1

    # header = ['Letter', 'Frequency']
    # with open('singleletters_nospace.csv', 'w', encoding='UTF8', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(header)
    #     for items in reversed(sorted(letterfrequency.items(), key=lambda item: item[1])):
    #         print(items)
    #         writer.writerow(items)

    percentages = []
    totaloccurences = sum(letterfrequency.values())
    for k, v in dict(reversed(sorted(letterfrequency.items(), key=lambda item: item[1]))).items():
        pct = round((v / totaloccurences), 3)
        print(k, str(pct))
        percentages.append(pct)
    return percentages


def countbigrams(text):
    alletters = alletters1
    step = 2
    # text = open("refactoredtext.txt").read()
    allbigrams = []
    templist = [alletters, alletters]
    text = text.replace(' ', '')
    for element in itertools.product(*templist):
        allbigrams.append(''.join(element))

    bigramfrequency = dict.fromkeys(allbigrams, 0)
    for i in range(0, len(text) - 1, step):
        bigramfrequency[str(text[i]) + str(text[i + 1])] += 1

    # header = ['Bigram', 'Frequency']
    # with open('bi_noover_nospace.csv', 'w', encoding='UTF8', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(header)
    #     for items in reversed(sorted(bigramfrequency.items(), key=lambda item: item[1])):
    #         print(items)
    #         writer.writerow(items)

    totaloccurences = sum(bigramfrequency.values())
    percentages = []
    for k, v in dict(reversed(sorted(bigramfrequency.items(), key=lambda item: item[1]))).items():
        pct = round((v / totaloccurences), 5)
        # print(k, str(pct))
        # percentages.append(pct)
        percentages.append(k)
    # print(percentages[:5])
    return percentages[:5]


def gcdextended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdextended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def linearmodulequation(a, b, n):
    gcd, x, y = gcdextended(a, n)
    if gcd == 1:
        return (x * b) % n
    else:
        if b % gcd != 0:
            return 'Розв`язків немає'
        else:
            gcd_b, x_b, y_b = gcdextended(b, n)
            result = linearmodulequation(a / gcd_b, b / gcd_b, n / gcd_b)
            solution = []
            while result < n:
                solution.append(result)
                result += n / gcd_b
            return solution


def hit_index_count(text):
    alletters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й',
                 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']
    letterfrequency = dict.fromkeys(alletters, 0)
    for i in text:
        if i in alletters:
            letterfrequency[i] += 1
    hit_index = 0
    # for k, v in dict(reversed(sorted(letterfrequency.items(), key=lambda item: item[1]))).items():
    #     hit_index += (v * (v + 1)) / (len(text) * (len(text) + 1))
    for k, v in dict(reversed(sorted(letterfrequency.items(), key=lambda item: item[1]))).items():
        hit_index += v * (v - 1)
    hit_index = hit_index / (len(text) * (len(text) - 1))
    # print(hit_index)
    # print(frequency)
    return hit_index


def convert_bigram_to_number(bigram_list):
    alletters = alletters1
    # result = alletters.index(bigram[0]) * len(alletters) + alletters.index(bigram[1])
    result = []
    for i in bigram_list:
        result.append(alletters.index(i[0]) * len(alletters) + alletters.index(i[1]))
    return result


def convert_number_to_bigram(number_list):
    alletters = alletters1
    result = []
    for i in number_list:
        letter_1 = alletters[i // 31]
        letter_2 = alletters[i % 31]
        result.append(letter_1 + letter_2)
    return result


def find_key(x1, x2, y1, y2):
    key = []
    x_h = (x1 - x2) % (31 ** 2)
    y_h = (y1 - y2) % (31 ** 2)
    first_part_key = linearmodulequation(x_h, y_h, 31 ** 2)
    key.append(first_part_key)
    if type(first_part_key) == int or type(first_part_key) == float:
        second_part_key = linearmodulequation(1, (y1 - first_part_key * x1) % 31 ** 2, 31 ** 2)
        key.append(second_part_key)
    if type(first_part_key) == list:
        second_part_key = []
        for i in first_part_key:
            second_part_key.append(linearmodulequation(1, (y1 - i * x1) % 31 ** 2, 31 ** 2))
        key.append(second_part_key)
    return key


def decryption(text, key):
    bigram_list_enc = []
    number_list_dec = []
    for i in range(0, len(text) - 1, 2):
        bigram_list_enc.append(text[i] + text[i + 1])
    number_list_enc = convert_bigram_to_number(bigram_list_enc)
    for i in number_list_enc:
        number_list_dec.append(linearmodulequation(key[0], (i - key[1]) % 31 ** 2, 31 ** 2))
    bigram_list_dec = convert_number_to_bigram(number_list_dec)
    dec_text = "".join(bigram_list_dec)
    return dec_text


def key_pairs(text_bigrams):
    popular_bigrams = ['ст', 'но', 'то', 'на', 'ен']
    a = convert_bigram_to_number(popular_bigrams)
    b = convert_bigram_to_number(text_bigrams)
    pairs = [list(item) for item in product(a, b)]
    all_keys = [list(item) for item in product(pairs, pairs)]
    return all_keys


def key_guessing(sourcetext):
    key_guess_list = []
    for i in key_pairs(countbigrams(sourcetext)):
        key_guess_list.append(find_key(i[0][0], i[0][1], i[1][0], i[1][1]))
        # key_guess_list.append(find_key(i[0][0], i[1][0], i[0][1], i[1][1]))
    key_guess_list[:] = [x for i, x in enumerate(key_guess_list) if i == key_guess_list.index(x)]  # убираю повторы
    return key_guess_list


def key_validating(sourcetext):
    valid_key_list = []
    for i in key_guessing(sourcetext):
        text_index = hit_index_count(decryption(sourcetext, i))
        # print(text_index)
        if 0.045 <= text_index <= 0.059:
            valid_key_list.append(i)
    for i in valid_key_list:
        print(decryption(sourcetext, i))
    return valid_key_list


# print(gcdExtended(2, 16))
# print(LinearModulEquation(2, 3, 7))
sourcetext = open("V4", encoding='utf-8').read()
# print(sourcetext)
print(countbigrams(sourcetext))
print(convert_bigram_to_number(countbigrams(sourcetext)))
print(popular_bigrams)
print(convert_bigram_to_number(popular_bigrams))
print(find_key(545, 802, 417, 162))
print(convert_number_to_bigram([0, 222, 111, 444, 555, 666, 777, 888]))
print(decryption(sourcetext, [788, 524]))
# a = convert_bigram_to_number(popular_bigrams)
# b = convert_bigram_to_number(countbigrams(sourcetext))
# pair = [list(item) for item in product(a, b)]
# print(pair)
# print(*[(a, b) for a in A for b in B])
# print(list(product(A, B)))
print(key_validating(sourcetext))