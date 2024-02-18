import copy
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QLineEdit, QVBoxLayout, QWidget, QGridLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys


def promising(word, dictionary):
    for w in dictionary:
        if w.startswith(word):
            return True
    return False

def checkIfInDictionary(word, dictionary):
    for w in dictionary:
        if w == word:
            return True
    return False

def traverse(i, j, word, usedCoordinates, cutDictionary, answers, grid):

    # check manually all possible directions
    
    if (i + 1, j) not in usedCoordinates and i + 1 < 4:
        if promising(word + grid[i + 1][j], cutDictionary):
            usedCoordinates.append((i + 1, j))
            traverse(i + 1, j, word + grid[i + 1][j], usedCoordinates, copy.deepcopy(cutDictionary), answers, grid)
            usedCoordinates.remove((i + 1, j))

    if (i - 1, j) not in usedCoordinates and i - 1 >= 0:
        if promising(word + grid[i - 1][j], cutDictionary):
            usedCoordinates.append((i - 1, j))
            traverse(i - 1, j, word + grid[i - 1][j], usedCoordinates, copy.deepcopy(cutDictionary), answers, grid)
            usedCoordinates.remove((i - 1, j))

    if (i, j + 1) not in usedCoordinates and j + 1 < 4:
        if promising(word + grid[i][j + 1], cutDictionary):
            usedCoordinates.append((i, j + 1))
            traverse(i, j + 1, word + grid[i][j + 1], usedCoordinates, copy.deepcopy(cutDictionary), answers, grid)
            usedCoordinates.remove((i, j + 1))

    if (i, j - 1) not in usedCoordinates and j - 1 >= 0:
        if promising(word + grid[i][j - 1], cutDictionary):
            usedCoordinates.append((i, j - 1))
            traverse(i, j - 1, word + grid[i][j - 1], usedCoordinates, copy.deepcopy(cutDictionary), answers, grid)
            usedCoordinates.remove((i, j - 1))

    if (i + 1, j + 1) not in usedCoordinates and i + 1 < 4 and j + 1 < 4:
        if promising(word + grid[i + 1][j + 1], cutDictionary):
            usedCoordinates.append((i + 1, j + 1))
            traverse(i + 1, j + 1, word + grid[i + 1][j + 1], usedCoordinates, copy.deepcopy(cutDictionary), answers, grid)
            usedCoordinates.remove((i + 1, j + 1))

    if (i - 1, j - 1) not in usedCoordinates and i - 1 >= 0 and j - 1 >= 0:
        if promising(word + grid[i - 1][j - 1], cutDictionary):
            usedCoordinates.append((i - 1, j - 1))
            traverse(i - 1, j - 1, word + grid[i - 1][j - 1], usedCoordinates, copy.deepcopy(cutDictionary), answers, grid)
            usedCoordinates.remove((i - 1, j - 1))

    if (i + 1, j - 1) not in usedCoordinates and i + 1 < 4 and j - 1 >= 0:
        if promising(word + grid[i + 1][j - 1], cutDictionary):
            usedCoordinates.append((i + 1, j - 1))
            traverse(i + 1, j - 1, word + grid[i + 1][j - 1], usedCoordinates, copy.deepcopy(cutDictionary), answers, grid)
            usedCoordinates.remove((i + 1, j - 1))

    if (i - 1, j + 1) not in usedCoordinates and i - 1 >= 0 and j + 1 < 4:
        if promising(word + grid[i - 1][j + 1], cutDictionary):
            usedCoordinates.append((i - 1, j + 1))
            traverse(i - 1, j + 1, word + grid[i - 1][j + 1], usedCoordinates, copy.deepcopy(cutDictionary), answers, grid)
            usedCoordinates.remove((i - 1, j + 1))

    if checkIfInDictionary(word, cutDictionary) and word not in answers:
        if not any(answer['word'] == word for answer in answers):
            answers.append({'word': word, 'coordinates': copy.deepcopy(usedCoordinates), 'index': len(answers)})

    return

def checkInput(input):
    if len(input) != 16:
        return False

    for letter in input:
        if not letter.isalpha():
            return False

    return True

def solve(letters):
    with (open("/Users/ramygad/Vs Code/Word Hunt/processedDictionary.txt", "r")) as f:
            dictionary = f.read().splitlines()
    grid = [['' for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            grid[i][j] = letters[i * 4 + j]

    answers = []
    for i in range(4):
        for j in range(4):
            
            # usedCoordinates is a list of coordinates that we have already used
            usedCoordinates = []
            usedCoordinates.append((i, j))
            word = ""
            word += grid[i][j]
            # remove all words from possibleWords that don't start with this letter.
            cutDictionary = copy.deepcopy(dictionary)
            cutDictionary = [w for w in cutDictionary if w.startswith(word)]
            traverse(i, j, word, usedCoordinates, copy.deepcopy(cutDictionary), answers, grid)
            # Sort by longest words at the bottom.
            answers.sort(key=lambda x: (len(x['word']), x['index']), reverse=True)

    return answers

class MainWindow(QMainWindow):

    def __init__(self, windowSize=600, grid=[[]]):

        with (open("/Users/ramygad/Vs Code/Word Hunt/processedDictionary.txt", "r")) as f:
            self.dictionary = f.read().splitlines()
        
        self.answers = []

        super(MainWindow, self).__init__()
        self.setWindowTitle("Word Hunt Solver")
        self.State = "Input"    
        # change background color to beige
        #self.setStyleSheet("background-color: beige")

        screenRes = QDesktopWidget().screenGeometry()
        self.setGeometry(int((screenRes.width() - windowSize)/2), int((screenRes.height() - windowSize)/2),
                          windowSize, windowSize)
        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)
        self.layout.setSpacing(10)

        # Input prompt
        self.inputPromptFont = QFont("Arial", 20, QFont.Bold)
        self.inputPrompt = QtWidgets.QLabel("Enter the letters", self)
        self.inputPrompt.setFont(self.inputPromptFont)
        self.layout.addWidget(self.inputPrompt, alignment=Qt.AlignCenter)

        # Text input box
        self.inputBox = QLineEdit()
        self.inputBox.setAlignment(Qt.AlignCenter)  
        self.layout.addWidget(self.inputBox, alignment=Qt.AlignCenter)

        # Invalid input message
        self.invalidInput = QtWidgets.QLabel("Invalid input", self)
        self.invalidInput.setStyleSheet("color: red")
        self.layout.addWidget(self.invalidInput, alignment=Qt.AlignCenter)
        self.invalidInput.hide()

        self.show()

    def keyPressEvent(self, event):

        if (self.State == "Input"):
            if event.key() == Qt.Key_Return:
                self.letters = self.inputBox.text().upper()
                if(checkInput(self.letters)): 
                    self.inputPrompt.hide()
                    self.invalidInput.hide()
                    self.inputBox.hide()
                    self.State = "Game"
                    self.wordIndex = 0
                    self.answers = solve(self.letters)
                    self.game(self.letters)
                else:
                    self.invalidInput.show()

        elif(self.State == "Game"):
            if(event.key() == Qt.Key_Return):
                self.clearWindow()
                self.wordIndex += 1
                self.game(self.letters)

    def game(self, letters):
        grid = [['' for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                grid[i][j] = letters[i * 4 + j]

        letters = letters.upper()
        gridLayout = QGridLayout()

        # Current word
        self.currentWord = QtWidgets.QLabel(self.answers[self.wordIndex]['word'], self)
        self.currentWord.setFont(self.inputPromptFont)
        self.layout.addWidget(self.currentWord, alignment=Qt.AlignCenter)

        for i in range(4):
            for j in range(4):
                letterLabel = QLabel(grid[i][j])
                letterLabel.setAlignment(Qt.AlignCenter)
                if (i, j) in self.answers[self.wordIndex]['coordinates']:
                    if (self.answers[self.wordIndex]['coordinates'].index((i, j)) == 0):
                        # is there dark green?
                        letterLabel.setStyleSheet("background-color: green; border: 1px solid black; font-size: 20px; text-align: center;")
                        
                    else:
                        letterLabel.setStyleSheet("background-color: darkgreen; border: 1px solid black; font-size: 20px; text-align: center;")
                else:
                    letterLabel.setStyleSheet("background-color: ##8C5535; border: 1px solid black; font-size: 20px; text-align: center;")
                gridLayout.addWidget(letterLabel, i, j)

        self.layout.addLayout(gridLayout)
        self.layout.setStretch(self.layout.count()-2, 1)  # word
        self.layout.setStretch(self.layout.count()-1, 3)  # grid

    def clearWindow(self):
        for i in reversed(range(self.layout.count())):
            item = self.layout.itemAt(i)
            if item.widget():
                item.widget().setParent(None)
            elif item.layout():
                self.clearLayout(item.layout())

    def clearLayout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
            elif item.layout():
                self.clearLayout(item.layout())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = MainWindow(windowSize=600)


    sys.exit(app.exec_())
