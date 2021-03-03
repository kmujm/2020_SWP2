import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB(self.scoredb)

    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        name = QLabel('Name :')
        age = QLabel('Age :')
        score = QLabel('Score :')
        amount = QLabel('Amount :')
        result = QLabel('Result :')
        key = QLabel('Key :')

        addButton = QPushButton("Add", self)
        delButton = QPushButton("Del", self)
        findButton = QPushButton("Find", self)
        incButton = QPushButton("Inc", self)
        showButton = QPushButton("Show", self)

        self.nameEdit = QLineEdit(self)
        self.ageEdit = QLineEdit(self)
        self.scoreEdit = QLineEdit(self)
        self.amountEdit = QLineEdit(self)
        self.resultEdit = QTextEdit(self)

        self.keyEdit = QComboBox()
        self.keyEdit.addItems(['Name', 'Score', 'Age'])

        hbox1 = QHBoxLayout()
        hbox1.addWidget(name)
        hbox1.addWidget(self.nameEdit)
        hbox1.addWidget(age)
        hbox1.addWidget(self.ageEdit)
        hbox1.addWidget(score)
        hbox1.addWidget(self.scoreEdit)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(2)
        hbox2.addWidget(amount)
        hbox2.addWidget(self.amountEdit)
        hbox2.addWidget(key)
        hbox2.addWidget(self.keyEdit)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(addButton)
        hbox3.addWidget(delButton)
        hbox3.addWidget(findButton)
        hbox3.addWidget(incButton)
        hbox3.addWidget(showButton)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(result)
        hbox4.addStretch(5)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.resultEdit)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)

        addButton.clicked.connect(self.addButtonClicked)
        delButton.clicked.connect(self.delButtonClicked)
        findButton.clicked.connect(self.findButtonClicked)
        incButton.clicked.connect(self.incButtonClicked)
        showButton.clicked.connect(self.showButtonClicked)

        self.setLayout(vbox)
        self.show()

    def addButtonClicked(self):
        if self.nameEdit.text() != '' and self.ageEdit.text() != '' and self.scoreEdit.text() != '':
            try:
                record = {'Name' : self.nameEdit.text(), 'Age' : int(self.ageEdit.text()), 'Score' :int(self.scoreEdit.text())}
                self.scoredb += [record]
                self.showScoreDB(self.scoredb)
            except ValueError:
                self.resultEdit.setPlainText('Invalid data type : Age and Score as integer type')
        else:
            self.resultEdit.setPlainText('Please input all data')


    def delButtonClicked(self):
        if self.nameEdit.text().strip() != '':
            for i in range(len(self.scoredb)-1,-1,-1):
                p = self.scoredb[i]
                if p['Name'] == self.nameEdit.text():
                    self.scoredb.remove(p)
            self.showScoreDB(self.scoredb)
        else:
            self.resultEdit.setText('Please input Name')

    def findButtonClicked(self):
        lst = []
        if self.nameEdit.text().strip != '':
            for p in self.scoredb:
                if p['Name'] == self.nameEdit.text():
                    lst.append(p)
            if not lst:
                self.resultEdit.setText("Not found")
            else:
                self.showScoreDB(lst)

    def incButtonClicked(self):
        if self.nameEdit.text().strip != '' and self.amountEdit.text().strip != '':
            try:
                for p in self.scoredb:
                    if p['Name'] == self.nameEdit.text():
                        p['Score'] += int(self.amountEdit.text())
                self.showScoreDB(self.scoredb)
            except ValueError:
                self.resultEdit.setText("Please input Score as integer type")

    def showButtonClicked(self):
        self.showScoreDB(self.scoredb)

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self,scdb):
        self.db = ''
        keyname = self.keyEdit.currentText()
        self.nameEdit.clear()
        self.scoreEdit.clear()
        self.ageEdit.clear()
        self.amountEdit.clear()

        for p in sorted(scdb, key = lambda person: person[keyname]):
            for attr in sorted(p):
                self.db += attr + '=' + str(p[attr]) + '  '
            self.db += '\n'
        self.resultEdit.setText(self.db)


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
