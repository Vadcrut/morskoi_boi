import sys

from PyQt5.QtGui import QPainter, QColor

import check_user1
import structure

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QButtonGroup, QLabel, QPushButton
from PyQt5.QtCore import Qt
from structure import a1 as a
from structure import a2 as acomp
from structure import a3 as aplayer
from pprint import pprint

razmer_window = 300
razmer_window1 = 900
razmer = 30
otstup = 50

comp = -1


class MyWidget(QWidget):
    def __init__(self):
        self.f = True
        super().__init__()
        uic.loadUi('UI\start form.ui', self)
        self.setWindowTitle('menu')
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.startdouble)
        self.pushButton_3.clicked.connect(self.show_spravka)

    def show_spravka(self):
        self.hide()
        ex1.show()

    def run(self):
        global comp
        comp = 0
        self.hide()
        ex2.show()

    def startdouble(self):
        global comp
        comp = 1
        self.hide()
        ex5.show()


class Spravka(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI\spravka.ui', self)
        self.setWindowTitle('spravka')
        self.resize(900, 900)
        try:
            with open('spravka.txt', 'rt', encoding='utf-8') as f:
                s = f.readlines()
        except Exception:
            pass
        self.listWidget.addItems(s)

    def closeEvent(self, QCloseEvent):
        ex.show()

    def resizeEvent(self, QResizeEvent):
        self.listWidget.resize(self.size())


class Insert(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI\insert_login_parol.ui', self)
        self.setWindowTitle('checking you')
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.pushButton.clicked.connect(self.go)

    def go(self):
        user = self.lineEdit.text()
        password = self.lineEdit_2.text()
        a = check_user1.check(user, password)
        if a == 'make_new':
            ex3.show()
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            self.hide()
        elif a == 'Yes':
            self.hide()
            ex5.show()

    def closeEvent(self, QCloseEvent):
        ex.show()


class Newuser(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI\ANew_user.ui', self)
        self.setWindowTitle('adding user')
        self.pushButton.clicked.connect(self.run)

    def run(self):
        ex4.show()
        self.hide()


class Adduser(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI\insert_login_parol.ui', self)
        self.setWindowTitle('adding user')
        self.pushButton.clicked.connect(self.run)
        self.hide()
        print('OK')

    def run(self):
        check_user1.add_user(self.lineEdit.text(), self.lineEdit_2.text())
        self.hide()
        ex5.show()


class Battlefield(QWidget):
    def __init__(self):
        self.f = False
        self.d = {4: 1, 3: 2, 2: 3, 1: 4}
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(razmer_window, razmer_window, razmer_window1, razmer_window1)
        self.setWindowTitle('game')

        self.rb = QRadioButton('четырехпалубный', self)
        self.rb.move(500, 50)
        self.rb.setChecked(True)

        self.rb1 = QRadioButton('трехпалубный', self)
        self.rb1.move(500, 100)

        self.rb2 = QRadioButton('двухпалубный', self)
        self.rb2.move(500, 150)

        self.rb3 = QRadioButton('однопалубный', self)
        self.rb3.move(500, 200)

        self.rb4 = QRadioButton('вертикально', self)
        self.rb4.move(50, 500)
        self.rb4.setChecked(True)

        self.rb5 = QRadioButton('горизонтально', self)
        self.rb5.move(200, 500)

        self.group1 = QButtonGroup(self)
        self.group1.addButton(self.rb)
        self.group1.addButton(self.rb1)
        self.group1.addButton(self.rb2)
        self.group1.addButton(self.rb3)

        self.group2 = QButtonGroup(self)
        self.group2.addButton(self.rb4)
        self.group2.addButton(self.rb5)

        self.lb = QLabel(self)
        self.lb.resize(500, razmer)
        self.lb.setText('')
        self.lb.move(450, 450)

        self.btn = QPushButton(self)
        self.btn.resize(100, razmer)
        self.btn.setText('Далее')
        self.btn.move(50, 600)
        self.btn.clicked.connect(self.nextstep)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if event.x() >= otstup and event.x() <= 350 and event.y() >= otstup and event.y() <= 350:
                self.f = True
                kolp = 0
                napr = 0
                if self.rb.isChecked():
                    kolp = 4
                if self.rb1.isChecked():
                    kolp = 3
                if self.rb2.isChecked():
                    kolp = 2
                if self.rb3.isChecked():
                    kolp = 1
                if self.rb4.isChecked():
                    napr = 1
                if self.rb5.isChecked():
                    napr = 2
                x = (event.x() - otstup) // razmer
                y = (event.y() - otstup) // razmer
                if self.d[kolp] > 0:
                    self.f = structure.check(x, y, kolp, napr, structure.a1)
                    if not self.f:
                        self.lb.setText('Некорректные координаты')
                    else:
                        self.d[kolp] -= 1
                else:
                    self.lb.setText('Максимальное количество кораблей данного типа достигнуто')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawfield(qp)
        qp.end()

    def drawfield(self, qp):
        for j in range(11):
            qp.drawLine(otstup + j * razmer, otstup, otstup + j * razmer, otstup + 10 * razmer)
            qp.drawLine(otstup, otstup + j * razmer, otstup + 10 * razmer, otstup + j * razmer)
        for i in range(10):
            for j in range(10):
                if a[i][j] == 4:
                    qp.drawLine(otstup + j * razmer, otstup + i * razmer, otstup + razmer + j * razmer,
                                otstup + razmer + i * razmer)
                    qp.drawLine(otstup + j * razmer, otstup + razmer + i * razmer, otstup + razmer + j * razmer,
                                otstup + i * razmer)
                if a[i][j] == 3:
                    qp.drawEllipse(otstup + j * razmer + razmer // 2, otstup + razmer // 2 + i * razmer, 1, 1)
        self.update()

    def nextstep(self):
        f = True
        for key in self.d.keys():
            if self.d[key] != 0:
                self.lb.setText('Расставлены не все корабли')
                f = False
        if f:
            if comp == 0:
                ex6.show()
                self.hide()
            if comp == 1:
                ex11.show()
                self.hide()

    def closeEvent(self, QCloseEvent):
        ex.show()


class PlayerField_2(QWidget):
    def __init__(self):
        self.f = False
        self.d = {4: 1, 3: 2, 2: 3, 1: 4}
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(razmer_window, razmer_window, razmer_window1, razmer_window1)
        self.setWindowTitle('game')

        self.rb = QRadioButton('четырехпалубный', self)
        self.rb.move(500, 50)
        self.rb.setChecked(True)

        self.rb1 = QRadioButton('трехпалубный', self)
        self.rb1.move(500, 100)

        self.rb2 = QRadioButton('двухпалубный', self)
        self.rb2.move(500, 150)

        self.rb3 = QRadioButton('однопалубный', self)
        self.rb3.move(500, 200)

        self.rb4 = QRadioButton('вертикально', self)
        self.rb4.move(50, 500)
        self.rb4.setChecked(True)

        self.rb5 = QRadioButton('горизонтально', self)
        self.rb5.move(200, 500)

        self.group1 = QButtonGroup(self)
        self.group1.addButton(self.rb)
        self.group1.addButton(self.rb1)
        self.group1.addButton(self.rb2)
        self.group1.addButton(self.rb3)

        self.group2 = QButtonGroup(self)
        self.group2.addButton(self.rb4)
        self.group2.addButton(self.rb5)

        self.lb = QLabel(self)
        self.lb.resize(500, razmer)
        self.lb.setText('')
        self.lb.move(450, 450)

        self.btn = QPushButton(self)
        self.btn.resize(100, razmer)
        self.btn.setText('Далее')
        self.btn.move(50, 600)
        self.btn.clicked.connect(self.nextstep)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if event.x() >= otstup and event.x() <= 350 and event.y() >= otstup and event.y() <= 350:
                self.f = True
                kolp = 0
                napr = 0
                if self.rb.isChecked():
                    kolp = 4
                if self.rb1.isChecked():
                    kolp = 3
                if self.rb2.isChecked():
                    kolp = 2
                if self.rb3.isChecked():
                    kolp = 1
                if self.rb4.isChecked():
                    napr = 1
                if self.rb5.isChecked():
                    napr = 2
                x = (event.x() - 50) // 30
                y = (event.y() - 50) // 30
                if self.d[kolp] > 0:
                    self.f = structure.check(x, y, kolp, napr, structure.a3)
                    if not self.f:
                        self.lb.setText('Некорректные координаты')
                    else:
                        self.d[kolp] -= 1
                else:
                    self.lb.setText('Максимальное количество кораблей данного типа достигнуто')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawfield(qp)
        qp.end()

    def drawfield(self, qp):
        for j in range(11):
            qp.drawLine(otstup + j * razmer, otstup, otstup + j * razmer, otstup + 10 * razmer)
            qp.drawLine(otstup, otstup + j * razmer, otstup + 10 * razmer, otstup + j * razmer)
        for i in range(10):
            for j in range(10):
                if aplayer[i][j] == 4:
                    qp.drawLine(otstup + j * razmer, otstup + i * razmer, otstup + razmer + j * razmer,
                                otstup + razmer + i * razmer)
                    qp.drawLine(otstup + j * razmer, otstup + razmer + i * razmer, otstup + razmer + j * razmer,
                                otstup + i * razmer)
                if aplayer[i][j] == 3:
                    qp.drawEllipse(otstup + j * razmer + razmer // 2, otstup + razmer // 2 + i * razmer, 1, 1)
        self.update()

    def nextstep(self):
        ex9.show()
        self.hide()


class DoubleBattlefieldComp(QWidget):
    def __init__(self):
        self.player = -1
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(razmer_window, razmer, razmer_window1, razmer_window1)
        self.setWindowTitle('game')
        structure.makerasstanovka()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.player == -1:
                if event.x() >= 450 and event.x() <= 750 and event.y() >= 50 and event.y() <= 350:
                    x = (event.x() - 450) // 30
                    y = (event.y() - 50) // 30
                    f = False
                    if acomp[y][x] == 4:
                        k, d = structure.dead(x, y, acomp)
                        print(k, d)
                        m = 0
                        for key in k.keys():
                            if k[key] > 0:
                                f = True
                                break
                        if f:
                            acomp[y][x] = 2
                        if not f:
                            if d['xl'] > 0 or d['xr'] > 0:
                                structure.fillneardead(x - d['xl'], y, 2, d['xl'] + d['xr'] + 1, acomp)
                            elif d['yu'] > 0 or d['yd'] > 0:
                                structure.fillneardead(x, y - d['yu'], 1, d['yu'] + d['yd'] + 1, acomp)
                            elif d['xl'] == 0 and d['xr'] == 0 and d['yu'] == 0 and d['yd'] == 0:
                                structure.fillneardead(x, y - d['yu'], 1, d['yu'] + d['yd'] + 1, acomp)
                            for key in d.keys():
                                if d[key] >= 0:
                                    for i in range(d[key] + 1):
                                        if key == 'yd':
                                            acomp[y + i][x] = 5
                                        if key == 'yu':
                                            acomp[y - i][x] = 5
                                        if key == 'xr':
                                            acomp[y][x + i] = 5
                                        if key == 'xl':
                                            acomp[y][x - i] = 5
                            for i in range(10):
                                for j in range(10):
                                    if acomp[i][j] == 5:
                                        m += 1
                            if m == 20:
                                self.hide()
                                ex7.show()
                    elif acomp[y][x] == 2 or acomp[y][x] == 1 or acomp[y][x] == 5:
                        pass
                    else:
                        acomp[y][x] = 1
                        self.player *= -1
            else:
                p = 0
                for i in range(10):
                    for j in range(10):
                        if acomp[i][j] == 5:
                            p += 1
                if p == 20:
                    self.hide()
                    ex10.show()
                f = structure.comphod()
                while f:
                    f = structure.comphod()
                self.player *= -1
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawfield(qp)
        qp.end()

    def drawfield(self, qp):
        for j in range(11):
            qp.drawLine(50 + j * 30, 50, 50 + j * 30, 350)
            qp.drawLine(50, 50 + j * 30, 350, 50 + j * 30)
            qp.drawLine(450 + j * 30, 50, 450 + j * 30, 350)
            qp.drawLine(450, 50 + j * 30, 750, 50 + j * 30)
        for i in range(10):
            for j in range(10):
                if acomp[i][j] == 2:
                    qp.drawLine(450 + j * 30, 50 + i * 30, 480 + j * 30, 80 + i * 30)
                    qp.drawLine(450 + j * 30, 80 + i * 30, 480 + j * 30, 50 + i * 30)
                if acomp[i][j] == 1:
                    qp.drawEllipse(450 + j * 30 + 15, 65 + i * 30, 1, 1)
                if acomp[i][j] == 5:
                    qp.setBrush(QColor(0, 0, 0))
                    qp.drawRect(450 + j * 30, 50 + i * 30, 30, 30)
                if a[i][j] == 2:
                    qp.drawLine(50 + j * 30, 50 + i * 30, 80 + j * 30, 80 + i * 30)
                    qp.drawLine(50 + j * 30, 80 + i * 30, 80 + j * 30, 50 + i * 30)
                if a[i][j] == 1:
                    qp.drawEllipse(50 + j * 30 + 15, 65 + i * 30, 1, 1)
                if a[i][j] == 5:
                    qp.setBrush(QColor(0, 0, 0))
                    qp.drawRect(50 + j * 30, 50 + i * 30, 30, 30)


class DoubleField(QWidget):
    def __init__(self):
        self.player = -1
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 900, 900)
        self.setWindowTitle('game')

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.player == -1:
                if event.x() >= 450 and event.x() <= 750 and event.y() >= 50 and event.y() <= 350:
                    x = (event.x() - 450) // 30
                    y = (event.y() - 50) // 30
                    f = False
                    if acomp[y][x] == 4:
                        k, d = structure.dead(x, y, aplayer)
                        print(k, d)
                        m = 0
                        for key in k.keys():
                            if k[key] > 0:
                                f = True
                                break
                        if f:
                            aplayer[y][x] = 2
                        if not f:
                            if d['xl'] > 0 or d['xr'] > 0:
                                structure.fillneardead(x - d['xl'], y, 2, d['xl'] + d['xr'] + 1, aplayer)
                            elif d['yu'] > 0 or d['yd'] > 0:
                                structure.fillneardead(x, y - d['yu'], 1, d['yu'] + d['yd'] + 1, aplayer)
                            elif d['xl'] == 0 and d['xr'] == 0 and d['yu'] == 0 and d['yd'] == 0:
                                structure.fillneardead(x, y - d['yu'], 1, d['yu'] + d['yd'] + 1, aplayer)
                            for key in d.keys():
                                if d[key] >= 0:
                                    for i in range(d[key] + 1):
                                        if key == 'yd':
                                            aplayer[y + i][x] = 5
                                        if key == 'yu':
                                            aplayer[y - i][x] = 5
                                        if key == 'xr':
                                            aplayer[y][x + i] = 5
                                        if key == 'xl':
                                            aplayer[y][x - i] = 5
                            for i in range(10):
                                for j in range(10):
                                    if aplayer[i][j] == 5:
                                        m += 1
                            if m == 20:
                                self.hide()
                                ex12.show()
                    elif aplayer[y][x] == 2 or aplayer[y][x] == 1 or aplayer[y][x] == 5:
                        pass
                    else:
                        aplayer[y][x] = 1
                        self.player *= -1
            else:
                if event.x() >= 50 and event.x() <= 350 and event.y() >= 50 and event.y() <= 350:
                    x = (event.x() - 50) // 30
                    y = (event.y() - 50) // 30
                    f = False
                    if a[y][x] == 4:
                        k, d = structure.dead(x, y, a)
                        print(k, d)
                        m = 0
                        for key in k.keys():
                            if k[key] > 0:
                                f = True
                                break
                        if f:
                            a[y][x] = 2
                        if not f:
                            if d['xl'] > 0 or d['xr'] > 0:
                                structure.fillneardead(x - d['xl'], y, 2, d['xl'] + d['xr'] + 1, a)
                            elif d['yu'] > 0 or d['yd'] > 0:
                                structure.fillneardead(x, y - d['yu'], 1, d['yu'] + d['yd'] + 1, a)
                            elif d['xl'] == 0 and d['xr'] == 0 and d['yu'] == 0 and d['yd'] == 0:
                                structure.fillneardead(x, y - d['yu'], 1, d['yu'] + d['yd'] + 1, a)
                            for key in d.keys():
                                if d[key] >= 0:
                                    for i in range(d[key] + 1):
                                        if key == 'yd':
                                            a[y + i][x] = 5
                                        if key == 'yu':
                                            a[y - i][x] = 5
                                        if key == 'xr':
                                            a[y][x + i] = 5
                                        if key == 'xl':
                                            a[y][x - i] = 5
                            for i in range(10):
                                for j in range(10):
                                    if a[i][j] == 5:
                                        m += 1
                            if m == 20:
                                self.hide()
                                ex13.show()
                    elif a[y][x] == 2 or a[y][x] == 1 or a[y][x] == 5:
                        pass
                    else:
                        a[y][x] = 1
                        self.player *= -1
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawfield(qp)
        qp.end()

    def drawfield(self, qp):
        for j in range(11):
            qp.drawLine(50 + j * 30, 50, 50 + j * 30, 350)
            qp.drawLine(50, 50 + j * 30, 350, 50 + j * 30)
            qp.drawLine(450 + j * 30, 50, 450 + j * 30, 350)
            qp.drawLine(450, 50 + j * 30, 750, 50 + j * 30)
        for i in range(10):
            for j in range(10):
                if aplayer[i][j] == 2:
                    qp.drawLine(450 + j * 30, 50 + i * 30, 480 + j * 30, 80 + i * 30)
                    qp.drawLine(450 + j * 30, 80 + i * 30, 480 + j * 30, 50 + i * 30)
                if aplayer[i][j] == 1:
                    qp.drawEllipse(450 + j * 30 + 15, 65 + i * 30, 1, 1)
                if aplayer[i][j] == 5:
                    qp.setBrush(QColor(0, 0, 0))
                    qp.drawRect(450 + j * 30, 50 + i * 30, 30, 30)
                if a[i][j] == 2:
                    qp.drawLine(50 + j * 30, 50 + i * 30, 80 + j * 30, 80 + i * 30)
                    qp.drawLine(50 + j * 30, 80 + i * 30, 80 + j * 30, 50 + i * 30)
                if a[i][j] == 1:
                    qp.drawEllipse(50 + j * 30 + 15, 65 + i * 30, 1, 1)
                if a[i][j] == 5:
                    qp.setBrush(QColor(0, 0, 0))
                    qp.drawRect(50 + j * 30, 50 + i * 30, 30, 30)


class win(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI\win.ui', self)


class lose(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI\lose.ui', self)


class For_2_players(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI\For two players.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.hide()
        ex8.show()


class win_2(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI\p2_win.ui', self)


class win_1(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI\p1_win.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    ex1 = Spravka()
    ex1.hide()
    ex2 = Insert()
    ex2.hide()
    ex3 = Newuser()
    ex3.hide()
    ex4 = Adduser()
    ex4.hide()
    ex5 = Battlefield()
    ex5.hide()
    ex6 = DoubleBattlefieldComp()
    ex6.hide()
    ex7 = win()
    ex7.hide()
    ex8 = PlayerField_2()
    ex8.hide()
    ex9 = DoubleField()
    ex9.hide()
    ex10 = lose()
    ex10.hide()
    ex11 = For_2_players()
    ex11.hide()
    ex12 = win_1()
    ex12.hide()
    ex13 = win_2()
    ex13.hide()
    sys.exit(app.exec_())
