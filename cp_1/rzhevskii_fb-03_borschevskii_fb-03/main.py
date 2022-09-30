import re
import itertools
import math

alletters1 = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
              'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
              'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


def cleantextfunc():
    uncleantext = open("sourcetext.txt", encoding='utf-8').read()
    cleantext = re.sub('[^ А-Яа-я\nёЁ]+', '', uncleantext)
    cleantext = cleantext.replace('\n', ' ')
    cleantext = re.sub(' +', ' ', cleantext)
    cleantext = cleantext.lower()
    open('refactoredtext.txt', 'w').write(cleantext)


def countletterfrequency(spaces):
    alletters = alletters1
    text = open("refactoredtext.txt").read()
    if spaces is True:
        alletters.append(' ')
    letterfrequency = dict.fromkeys(alletters, 0)
    for i in text:
        if i in alletters:
            letterfrequency[i] += 1

    percentages = []
    totaloccurences = sum(letterfrequency.values())
    for k, v in dict(reversed(sorted(letterfrequency.items(), key=lambda item: item[1]))).items():
        pct = round((v / totaloccurences), 3)
        print(k, str(pct))
        percentages.append(pct)
    return percentages

    # print(dict(sorted(letterfrequency.items(), key=lambda item: item[1])))


def countbigrams_overlapping(spaces):
    alletters = alletters1
    text = open("refactoredtext.txt").read()
    allbigrams = []
    if spaces is True:
        alletters.append(' ')
        templist = [alletters, alletters]
    else:
        templist = [alletters, alletters]
        text = text.replace(' ', '')
    for element in itertools.product(*templist):
        allbigrams.append(''.join(element))

    bigramfrequency = dict.fromkeys(allbigrams, 0)
    for i in range(len(text) - 1):
        bigramfrequency[str(text[i]) + str(text[i + 1])] += 1

    totaloccurences = sum(bigramfrequency.values())
    percentages = []
    for k, v in dict(reversed(sorted(bigramfrequency.items(), key=lambda item: item[1]))).items():
        pct = round((v / totaloccurences), 5)
        print(k.replace(' ', '_'), str(pct))
        percentages.append(pct)
    print(percentages)
    return percentages


def countbigrams_nooverlapping(spaces):
    alletters = alletters1
    text = open("refactoredtext.txt").read()
    allbigrams = []
    if spaces is True:
        alletters.append(' ')
        templist = [alletters, alletters]
    else:
        templist = [alletters, alletters]
        text = text.replace(' ', '')
    for element in itertools.product(*templist):
        allbigrams.append(''.join(element))

    bigramfrequency = dict.fromkeys(allbigrams, 0)
    for i in range(0, len(text) - 1, 2):
        bigramfrequency[str(text[i]) + str(text[i + 1])] += 1

    totaloccurences = sum(bigramfrequency.values())
    percentages = []
    for k, v in dict(reversed(sorted(bigramfrequency.items(), key=lambda item: item[1]))).items():
        pct = round((v / totaloccurences), 5)
        print(k.replace(' ', '_'), str(pct))
        percentages.append(pct)
    print(percentages)
    return percentages


def entropy_calc(probability_list):
    entropy = 0
    for letter in probability_list:
        if letter != 0:
            entropy += -(letter * math.log(letter, 2))
    print(entropy)


if __name__ == "__main__":
    # cleantextfunc()
    # countletterfrequency(spaces=True)
    # countbigrams_overlapping(spaces=True)
    # countbigrams_nooverlapping(spaces=True)
    entropy_calc(countbigrams_overlapping(spaces=False))
