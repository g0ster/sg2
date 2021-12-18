import random

ADV = ['aggressively', 'fastly', 'clumsily']
ADJ = ['aggressive', 'fast', 'clumsy', 'black']
NOUN = ['I', 'Some cows', 'People', 'Some things', 'My friends']
ARTICLE = ['the', 'a', 'an']
ACTV = ['are doing', 'did', 'will', 'should', 'would', 'could']
POSV = ['have']
VBE = ['are', 'was', 'were', 'will be', 'would be', 'shall be', 'have been']
VRB = ['run', 'jump', 'dance', 'flip']

x = random.randrange(0, len(NOUN))
y = VBE[random.randrange(0, len(VBE))]
if x == 0:
    y = 'am'

ACTION_SENTENCE = NOUN[x] + ' ' + ACTV[random.randrange(0, len(ACTV))] + ' ' + ADV[
    random.randrange(0, len(ADV))] + ' ' + VRB[random.randrange(0, len(VRB))] + '.'

BEING_SENTENCE = NOUN[x] + ' ' + y + ' ' + ADJ[random.randrange(0, len(ADJ))] + '.'

SENTENCE_TYPES = [ACTION_SENTENCE, BEING_SENTENCE]
print(SENTENCE_TYPES[random.randrange(0, len(SENTENCE_TYPES)-1)])
