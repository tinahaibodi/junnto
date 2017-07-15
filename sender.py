import random
ans = 0

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
    global ans
    ans = answers.index(1) + 1
    
    n = 1
    for e in answers:
        string += str(n) + ") " + qlist[x][e] + "\n"
        n += 1

    return string

def check(answer):
    #send a response
    if(answer == ans):
        return "You are correct!"
    else:
        return "Incorrect"

print generateText()
