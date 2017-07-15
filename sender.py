import random

def questions():
    f = open('questions.txt', 'rU')
    s = f.read()
    qlist = s.split('\n\n')

    for i in range(len(qlist)):
        q = qlist[i]
        qlist[i] = q.split('\n')
    return qlist

def generateText():
    qlist = questions()
    x = random.randrange(len(qlist))
    string = qlist[x][0] + "\n"
    answers = [1,2,3,4]
    random.shuffle(answers)

    for e in answers:
        string += qlist[x][e] + "\n"

    return string
