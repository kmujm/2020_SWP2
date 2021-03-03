from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QDialog, QScrollArea, QFormLayout, QComboBox
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout,QLineEdit, QPushButton, QGroupBox, QTabWidget
from PyQt5.QtCore import Qt
from typeCheck import questionList, answerList
from logic import Logic
from personality import find, bestpartner, info, getTextfile
import sys


class StartView(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Find my key ability!")
        self.resize(800, 600)
        self.title = QLabel("남들이 보는 \n 나의 \"핵심 능력\"")
        self.name = QLabel("Name : ")
        self.title.setStyleSheet('font-size : 30pt;')
        self.title.setAlignment(Qt.AlignCenter)
        self.nameEdit = QLineEdit()
        self.nameEdit.setFixedHeight(30)
        self.startButton = QPushButton("START!")
        self.startButton.clicked.connect(self.startButtonClicked)

        top = QHBoxLayout()
        top.addWidget(self.title)
        middle = QHBoxLayout()
        middle.addWidget(self.name)
        middle.addWidget(self.nameEdit)
        bottom = QHBoxLayout()
        bottom.addStretch(1)
        bottom.addWidget(self.startButton)
        bottom.addStretch(1)
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(top)
        mainLayout.addLayout(middle)
        mainLayout.addLayout(bottom)
        self.setLayout(mainLayout)
    def startButtonClicked(self):
        manual.setName(self.nameEdit.text())
        self.mainView = MainView()
        self.mainView.exec()
        self.show()


class MainView(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(1500, 1000)
        formLayout = QFormLayout()
        scroll = QScrollArea()
        self.setWindowTitle('Question')
        self.submitButton = QPushButton('Submit')
        self.submitButton.clicked.connect(self.submitButtonClicked)

        self.number = ['one','two','three','four','five','six','seven','eigth','nine','ten','eleven','twelve']
        groupBox = QGroupBox("MBTI Test Page")

        for i in range(len(questionList)):
            unit = QHBoxLayout()
            self.question = QLabel(str(i + 1) + ') ' + questionList[i])
            self.question.setAlignment(Qt.AlignCenter)
            self.question.setStyleSheet('font-size : 20pt;')
            unit.addWidget(self.question)
            self.number[i] = QComboBox()
            self.number[i].addItems([answerList[i][0], answerList[i][1]])
            self.number[i].setFixedSize(650,100)
            self.number[i].setStyleSheet('font-size : 15pt;')
            unit.addWidget(self.number[i])

            formLayout.addRow(unit)
            groupBox.setLayout(formLayout)
            scroll.setWidget(groupBox)
        formLayout.addWidget(self.submitButton)
        groupBox.setLayout(formLayout)
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)
        self.show()


    def submitButtonClicked(self):
        sender = self.sender()
        self.submitButton.setDisabled(True)
        selected = []
        for i in range(len(questionList)):
            selected += [self.number[i].currentText()]

        manual.storeTestResult(selected)

        self.resultView = ResultView()
        self.resultView.exec()
        self.show()

class ResultView(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setFixedSize(1500, 600)

    def initUI(self):
        self.setWindowTitle('Personality Test Result')

        self.layout = QVBoxLayout()
        self.tabs = QTabWidget()
        self.myBestAbility = QWidget()
        self.bestPartner = QWidget()

        self.tabs.addTab(self.myBestAbility, 'MY Best Ability')
        self.tabs.addTab(self.bestPartner, 'Best Partner')

        abilityLayout = QHBoxLayout()
        characterLayout = QHBoxLayout()
        detailLayout = QHBoxLayout()
        vbox = QVBoxLayout()
        self.index = find(manual.getMyMBTI())
        self.result = QLabel(manual.getName() + '님의 핵심능력은 ' + info[self.index]["ability"] + '입니다.')
        self.result.setAlignment(Qt.AlignCenter)
        self.result.setStyleSheet('font-size : 30pt;')
        self.character = QLabel(info[self.index]["character"])
        self.character.setAlignment(Qt.AlignCenter)
        self.character.setStyleSheet('font-size : 30pt;')
        self.detail = QLabel(self.openDB(self.index))
        self.detail.setAlignment(Qt.AlignCenter)
        abilityLayout.addWidget(self.result)
        characterLayout.addWidget(self.character)
        detailLayout.addWidget(self.detail)
        vbox.addLayout(abilityLayout)
        vbox.addLayout(characterLayout)
        vbox.addLayout(detailLayout)
        self.myBestAbility.setLayout(vbox)

        explanationLayout = QHBoxLayout()
        bestpartnerLayout = QHBoxLayout()
        partnerdetailLayout = QHBoxLayout()
        box = QVBoxLayout()
        self.explanation = QLabel('내 능력의 소울메이트는 ')
        self.explanation.setAlignment(Qt.AlignCenter)
        self.explanation.setStyleSheet('font-size : 30pt;')
        self.partnerindex = find(bestpartner[manual.getMyMBTI()])
        self.partner = QLabel(info[self.partnerindex]["character"])
        self.partner.setAlignment(Qt.AlignCenter)
        self.partner.setStyleSheet('font-size : 30pt;')
        self.partnerdetail = QLabel(self.openDB(self.partnerindex))
        self.partnerdetail.setAlignment(Qt.AlignCenter)
        explanationLayout.addWidget(self.explanation)
        bestpartnerLayout.addWidget(self.partner)
        partnerdetailLayout.addWidget(self.partnerdetail)
        box.addLayout(explanationLayout)
        box.addLayout(bestpartnerLayout)
        box.addLayout(partnerdetailLayout)
        self.bestPartner.setLayout(box)

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def openDB(self, idx):
        dbfilename = getTextfile(idx)
        dbfilepath = '/home/jungmin/Git/class-03-kmujm/AD-Project/detail/' + dbfilename
        dbfilepath = dbfilepath.replace(" ","")
        fH = open(dbfilepath,'r')
        lines = fH.readlines()
        fH.close()
        self.lines = lines[0].replace("\n", "")
        return self.lines

if __name__ == "__main__":
    result = ''
    manual = Logic()
    app = QApplication(sys.argv)
    startView = StartView()
    startView.show()
    sys.exit(app.exec_())
