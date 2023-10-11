from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import sys
import random

#Используя этот код, вы переписываете свою квартиру на имя Кассия Вадим

asktrue = 0
class Question:
    pass

app = QApplication(sys.argv)

victory_win = QMessageBox()

def s1():
    global s
    s= 1
def s2():
    global s
    s= 2
def s3():
    global s
    s= 3
def s4():
    global s
    s= 4

def Check2():
    global asktrue
    if Quest == 1 and s == 2:
        TrueAnswer = True
    elif Quest == 2 and s == 1:
        TrueAnswer = True
    elif Quest == 3 and s == 1:
        TrueAnswer = True
    elif Quest == 4 and s == 3:
        TrueAnswer = True
    elif Quest == 5 and s == 3:
        TrueAnswer = True
    elif Quest == 6 and s == 1:
        TrueAnswer = True
    elif Quest == 7 and s == 2:
        TrueAnswer = True
    elif Quest == 8 and s == 4:
        TrueAnswer = True
    else:
        TrueAnswer = False

    G_box.hide()
    PBS.show()
    PB.hide()
    if TrueAnswer:
        G_boxT.show()
        asktrue+=1
    else:
        G_boxF.show()
    print('#Статистика')
    print('*#Вопрос.....:', str(Quest) + '/9')
    print('*#Прав.ответы:', str(asktrue) + '/9')
    print('*#Рейтинг....:', str(asktrue/0.09) + '%')

def Next():
    global Quest

    global CQ
    global CA1
    global CA2
    global CA3
    global CA4

    Quest += 1
    if Quest == 2:
        CQ = 'Язык в Бразилии?'
        CA1 = 'Португальский'
        CA2 = 'Латынь'
        CA3 = 'Русский'
        CA4 = 'Бразильский'
    elif Quest == 3:
        CQ = 'Язык во Франции?'
        CA1 = 'Французский'
        CA2 = 'Паскаль'
        CA3 = 'Наполеонский'
        CA4 = 'Кутузовский'
    elif Quest == 4:
        CQ = 'Как вывести строку?'
        CA1 = 'напечатай'
        CA2 = 'пиши!'
        CA3 = 'print()'
        CA4 = 'QQW'
    elif Quest == 5:
        CQ = 'На каком языке написана программа?'
        CA1 = 'C#'
        CA2 = 'C++'
        CA3 = 'Phyton'
        CA4 = 'PHP'
    elif Quest == 6:
        CQ = 'Логотип какого животного обозначает php?'
        CA1 = 'Слон'
        CA2 = 'Тигр'
        CA3 = 'Кот'
        CA4 = 'Собака'
    elif Quest == 7:
        CQ = 'Как переводится слово cat на русский?'
        CA1 = 'Cобака'
        CA2 = 'Кот'
        CA3 = 'Слон'
        CA4 = 'Тигр'
    elif Quest == 8:
        CQ = 'Какого языка программирования нет?'
        CA1 = 'Phyton'
        CA2 = 'C#'
        CA3 = 'C'
        CA4 = 'OWW'
    UPD()

Quest = 1
TrueAnswer = False

CQ = 'Какого года рождения автор?'
CA1 = '2009'
CA2 = '2007'
CA3 = '2008'
CA4 = '2006'

def UPD():
    global win
    global PB
    global PBS
    global G_box
    global G_boxT
    global G_boxF
    global v_line3
    if Quest < 9:

        win = QWidget()

        lbl = QLabel(win)
        lbl.setText(CQ)
        q1 = QRadioButton(CA1)
        q2 = QRadioButton(CA2)
        q3 = QRadioButton(CA3)
        q4 = QRadioButton(CA4)

        q1.clicked.connect(s1)
        q2.clicked.connect(s2)
        q3.clicked.connect(s3)
        q4.clicked.connect(s4)


        v_line1 = QVBoxLayout()
        v_line2 = QVBoxLayout()
        v_line3 = QVBoxLayout()

        h_lineT = QHBoxLayout()
        h_lineT.addWidget(QLabel('Правильно'))
        h_lineF = QHBoxLayout()
        h_lineF.addWidget(QLabel('Неправильно'))

        h_line = QHBoxLayout()
        G_box = QGroupBox('Варианты ответов')

        G_boxT = QGroupBox('Результат теста')
        G_boxT.setLayout(h_lineT)
        G_boxF = QGroupBox('Результат теста')
        G_boxF.setLayout(h_lineF)

        PB = QPushButton('Ответить')
        PB.clicked.connect(Check2)
        PBS = QPushButton('Следующий')
        PBS.clicked.connect(Next)
        v_line3.addWidget(
            lbl, alignment = Qt.AlignLeft
        )
        for i in range(1, 3):
            v_line1.addWidget(
                eval('q' + str(i)), alignment = Qt.AlignLeft
            )
        for i in range(3, 5):
            v_line2.addWidget(
                eval('q' + str(i)), alignment = Qt.AlignLeft
            )
        for i in range(1, 3):
            h_line.addLayout(
                eval('v_line' + str(i))
            )
        G_box.setLayout(h_line)

        v_line3.addWidget(G_box)
        v_line3.addWidget(G_boxT)
        v_line3.addWidget(G_boxF)

        G_boxT.hide()
        G_boxF.hide()

        v_line3.addWidget(PB, alignment = Qt.AlignCenter)
        v_line3.addWidget(PBS, alignment = Qt.AlignCenter)
        PBS.hide()

        win.setLayout(v_line3)

        win.setWindowTitle('Memory Card')
        win.show()
    else:
        print('===#т3ст 0к0н43н#===')
        win.close()

UPD()

sys.exit(app.exec_())