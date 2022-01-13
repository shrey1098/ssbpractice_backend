import random

wat_lines = 3378
srt_lines = 475


def getWat():
    word_indexes = generateIndex(type_test=1)
    words = {}
    counter = 0

    for index in word_indexes:
        counter += 1
        with open("backend/ssb_wat.txt", 'r') as f:
            word = f.readlines()[index]
            words[counter] = word.strip()
    return words

def getSrt():
    situation_indexes = generateIndex(type_test=2)
    situations = {}
    counter = 0
    for index in situation_indexes:
        counter +=1
        with open("backend/ssb_srt.txt", 'r') as f:
            situation = f.readlines()[index]
            situations[counter] = situation.strip()
    return situations

def generateIndex(type_test):
    """
    type_test: wat = 1; srt = 2;
    :param type_test:
    :return: list of randomly generated line numbers
    """
    indexes = []
    if type_test == 1:
        for i in range(0, 60):
            indexes.append(random.randint(1, wat_lines))

    elif type_test == 2:
        for i in range(0, 60):
            indexes.append(random.randint(1, srt_lines))

    return indexes
