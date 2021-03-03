from typeCheck import mapDic

testdb = {"E" : 0 , "I" : 0, "F" : 0, "T" : 0, "P" : 0, "J" : 0, "S" : 0, "N" : 0}

class Logic:
    def setName(self,name):
        self.playerName = name

    def getName(self):
        return self.playerName

    def storeTestResult(self, selection):
        for k in selection:
            testdb[mapDic[k]] += 1
        self.inspectMBTI()


    def inspectMBTI(self):
        self.result = []
        if testdb['E'] > testdb['I']:
            self.result.append('E')
        else:
            self.result.append('I')
        if testdb['S'] > testdb['N']:
            self.result.append('S')
        else:
            self.result.append('N')
        if testdb['F'] > testdb['T']:
            self.result.append('F')
        else:
            self.result.append('T')
        if testdb['J'] > testdb['P']:
            self.result.append('J')
        else:
            self.result.append('P')
        self.myMBTI = "".join(self.result)

    def getMyMBTI(self):
        return self.myMBTI


