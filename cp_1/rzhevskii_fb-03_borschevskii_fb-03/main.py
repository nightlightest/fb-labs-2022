import re
import itertools

alletters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й'
             , 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф'
             , 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


def cleantextfunc():
    uncleantext = open("sourcetext.txt", encoding='utf-8').read()
    cleantext = re.sub('[^ А-Яа-я\nёЁ]+', '', uncleantext)
    cleantext = cleantext.replace('\n', ' ')
    cleantext = re.sub(' +', ' ', cleantext)
    cleantext = cleantext.lower()
    open('refactoredtext.txt', 'w').write(cleantext)


def countletterfrequency():
    letterfrequency = dict.fromkeys(alletters, 0)
    text = open("refactoredtext.txt").read()
    for i in text:
        if i in alletters:
            letterfrequency[i] += 1

    totaloccurences = sum(letterfrequency.values())
    for k, v in dict(reversed(sorted(letterfrequency.items(), key=lambda item: item[1]))).items():
        pct = round((v * 100.0 / totaloccurences), 3)
        print(k, str(pct) + '%')

    # print(dict(sorted(letterfrequency.items(), key=lambda item: item[1])))


def countbigramsoverlapping():
    allbigrams = []
    templist = [alletters, alletters]
    for element in itertools.product(*templist):
        allbigrams.append(''.join(element))

    bigramfrequency = dict.fromkeys(allbigrams, 0)
    text = open("refactoredtext.txt").read()
    for count, value in enumerate(text):
        if value != ' ' and text[count+1] != ' ':
            bigramfrequency[value + text[count+1]] += 1

    totaloccurences = sum(bigramfrequency.values())
    # percentages = []
    for k, v in dict(reversed(sorted(bigramfrequency.items(), key=lambda item: item[1]))).items():
        pct = round((v / totaloccurences), 5)
        print(k, str(pct))
        # percentages.append(pct)
    # print(percentages)


def countbigrams_nooverlapping():
    allbigrams = []
    templist = [alletters, alletters]
    for element in itertools.product(*templist):
        allbigrams.append(''.join(element))

    bigramfrequency = dict.fromkeys(allbigrams, 0)
    text = open("refactoredtext.txt").read()
    for count, value in enumerate(text):
        if value != ' ' and text[count + 1] != ' ':
            bigramfrequency[value + text[count + 1]] += 1

    totaloccurences = sum(bigramfrequency.values())
    # percentages = []
    for k, v in dict(reversed(sorted(bigramfrequency.items(), key=lambda item: item[1]))).items():
        pct = round((v / totaloccurences), 5)
        print(k, str(pct))
        # percentages.append(pct)
    # print(percentages)


if __name__ == "__main__":
    # cleantextfunc()
    countletterfrequency()
    # countbigramsoverlapping()
    # countbigrams_nooverlapping()