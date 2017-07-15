def questions():
    f = open('questions.txt', 'rU')
    s = f.read()
    qlist = s.split('\n\n')

    for i in range(len(qlist)):
        q = qlist[i]
        qlist[i] = q.split('\n')
    return qlist
