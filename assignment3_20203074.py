import pickle

dbfilename = 'test3_4.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()


    for p in scdb:
        p['Score'] = int(p['Score'])
        p['Age'] = int(p['Age'])
    return scdb

# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
            except IndexError as ie:  # add 뒤 정보를 누락할 때
                print(ie, " >> One or more information is missing. \" add <Name> <Age> <Score>\"")
            except ValueError as ve: # 입력 type이 맞지 않을 때
                print(ve, " >> Please input <Name> as string type, <Age> and <Score> as integer type")
            else:
                scdb += [record]
        elif parse[0] == 'del':
            try:
                for p in scdb[:]:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
            except IndexError as ie:   # name을 입력하지 않았을 때
                print(ie, ">> Please follow input form \'del <Name>\'" )
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            try:
                showScoreDB(scdb, sortKey)
            except:  # 'show '라고 입력할 때
                if parse[1] == "":
                    showScoreDB(scdb, 'Name')
        elif parse[0] == 'quit':
            break
        elif parse[0] == 'find':
            lst = []
            for p in scdb:
                try:
                    if p['Name'] == parse[1]:
                        lst.append(p)
                        showScoreDB(lst,'Name')
                except IndexError as ie:  # name을 입력하지 않았을 때
                    print(ie, ">> Please follow input form \'find <Name>\'")
        elif parse[0] == 'inc':
            for p in scdb:
                try:
                    if p['Name'] == parse[1]:
                        p['Score'] += int(parse[2])
                except IndexError as ie:  # name과 amount를 모두 입력하지 않았을 때
                    print(ie,">> Please follow input form \'inc <Name> <amount>\'")
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]), end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
