from typing import ChainMap
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
import time, random, math
import pygame
from pygame import freetype

import sys, os


from MBTI_Ninja import MainMenu
from MBTI_Ninja import main

from mod1 import *

class Startwindow(QWidget):  # A
    global B

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MBTI with UMI's Cells")
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(1000, 750)

        winB = QPushButton('심리테스트 시작하기', self)
        winB.clicked.connect(self.winB_clicked)
        winB.setGeometry(400, 550, 210, 40)

        bgImage = QImage('startbg.png')
        size = bgImage.scaled(QSize(1000,750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)
        self.center()

        label1 = QLabel('오픈소스 프로그래밍 team2의', self)
        label1.move(350, 200)
        label1.setFont(QFont("맑은고딕", 10))  # 한글 폰트 깨지는 문제 발생 -> 시각적으로 보기 좋은 폰트로 수정
        label1.setStyleSheet("Color : white")
        label2 = QLabel('유미의 세포들 심리테스트에', self)
        label2.move(360, 250)
        label2.setFont(QFont("맑은고딕", 10))
        label2.setStyleSheet("Color : white")
        label3 = QLabel('오신 걸 환영합니다!', self)
        label3.move(390, 300)
        label3.setFont(QFont("맑은고딕", 10))
        label3.setStyleSheet("Color : white")
        label4 = QLabel('아래 버튼을 눌러주세요', self)
        label4.move(370, 350)
        label4.setFont(QFont("맑은고딕", 10))
        label4.setStyleSheet("Color : white")

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def winB_clicked(self):
        self.close()
        B.show()


class question1(QWidget):  # B
    global C

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("질문 1")
        self.setWindowIcon(QIcon('winicon.png'))
        self.resize(1000, 750)

        bgImage = QImage('questionbg.PNG')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)
        self.center()

        self.label1 = QLabel('Q1. 오늘은 소개팅날! 처음 상대를 만나게 되는데, 그 상황에서 당신은?', self)
        self.label1.move(170, 180)

        self.rbtn1 = QRadioButton('주로 질문을 하며 대답을 유도한다.', self)  # E
        self.rbtn1.move(320, 270)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(320, 330)
        self.rbtn2.setText('주로 상대방의 질문에 대답한다.')  # I

        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 550, 210, 40)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def winB_clicked(self):
        adding(0, (self.rbtn1.isChecked()))
        self.close()
        C.show()


class question2(QWidget):  # C
    global D

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("질문 2")
        self.setWindowIcon(QIcon('winicon.png'))
        self.resize(1000, 750)

        bgImage = QImage('questionbg.PNG')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)
        self.center()

        self.label1 = QLabel('Q2. 친구들과 2박 3일로 여행을 가기로 했다. 여행 계획을 세울 때 당신은?', self)
        self.label1.move(170, 180)

        self.rbtn1 = QRadioButton('교통편, 숙박시설 뿐만 아니라 경우의 수를 나누어 세부 계획을 짠다.', self)  # J
        self.rbtn1.move(150, 270)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(150, 330)
        self.rbtn2.setText('교통편, 숙박시설 등 필수적인 것만 예약한 후 여행을 가서 상황에 맞게 행동한다.')  # P

        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 550, 210, 40)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def winB_clicked(self):
        adding(3, (self.rbtn1.isChecked()))
        self.close()
        D.show()


class question3(QWidget):  # D
    global E

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("질문 3")
        self.setWindowIcon(QIcon('winicon.png'))
        self.resize(1000, 750)

        bgImage = QImage('questionbg.PNG')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)
        self.center()

        self.label1 = QLabel('Q3. 동아리에서 사소한 규칙을 어긴 친구에 대한 조치를 취하려고 한다. 당신의 의견은?', self)
        self.label1.move(100, 180)

        self.rbtn1 = QRadioButton('사소한 규칙이라도 사전에 약속된 규칙이기 때문에 적절한 조치를 취해야 한다. ', self)  # J
        self.rbtn1.move(120, 270)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(120, 330)
        self.rbtn2.setText('사소한 규칙은 개인이 재량으로 상황에 따라 유연하게 행동할 수 있다고 생각한다')  # P

        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 550, 210, 40)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def winB_clicked(self):
        adding(3, (self.rbtn1.isChecked()))
        self.close()
        E.show()


class question4(QWidget):  # E
    global F

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("질문 4")
        self.setWindowIcon(QIcon('winicon.png'))
        self.resize(1000, 750)

        bgImage = QImage('questionbg.PNG')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)
        self.center()

        self.label1 = QLabel('Q4. 과제들에 공모전, 동아리에 학생회까지! 할 일이 너무 많을 때 당신의 머리속은?', self)
        self.label1.move(120, 180)

        self.rbtn1 = QRadioButton('(다른사람한테 도와달라고 부탁할까 이정도면 시간내에 완벽하게 할 수 있을거같은데) ', self)  # S
        self.rbtn1.move(100, 270)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(100, 330)
        self.rbtn2.setText('(일 안하고 돈벌고싶다. 내가 삼ㅇ전자 회장이었으면 숨만쉬어도 돈이 들어오겠지? ')  # N

        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 550, 210, 40)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def winB_clicked(self):
        adding(1, (self.rbtn1.isChecked()))
        self.close()
        F.show()


class question5(QWidget):  # F
    global G

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("질문 5")
        self.setWindowIcon(QIcon('winicon.png'))
        self.resize(1000, 750)

        bgImage = QImage('questionbg.PNG')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)
        self.center()

        self.label1 = QLabel('Q5. 당신이 며칠 동안 열심히 준비한 과제 발표가 끝났다. 친구에게 듣고 싶은 말은?', self)
        self.label1.move(100, 180)

        self.rbtn1 = QRadioButton('잘했어! 이 부분에서 이것만 수정하면 다음엔 더 좋을 발표가 될 것 같아!', self)  # T
        self.rbtn1.move(170, 270)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(170, 330)
        self.rbtn2.setText('열심히 했어~ 넘 고생했어~')  # F

        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 550, 210, 40)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def winB_clicked(self):
        adding(2, (self.rbtn1.isChecked()))
        self.close()
        G.show()


class question6(QWidget):  # G
    global H

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("질문 6")
        self.setWindowIcon(QIcon('winicon.png'))
        self.resize(1000, 750)

        bgImage = QImage('questionbg.PNG')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)
        self.center()

        self.label1 = QLabel('Q6. 친구가 취업이 안돼 힘들어하고 있는 상황이다. 당신이라면 어떤 말을 해줄 것인가?', self)
        self.label1.move(100, 180)

        self.rbtn1 = QRadioButton('어떤거 준비하고 있는데? 이력서는 많이 넣어봤어?', self)  # T
        self.rbtn1.move(240, 270)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(240, 330)
        self.rbtn2.setText('(곤란한 질문은 하지 말자) 힘들지 ㅠㅠ')  # F

        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 550, 210, 40)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def winB_clicked(self):
        adding(2, (self.rbtn1.isChecked()))
        self.close()
        H.show()


class question7(QWidget):  # H
    global I

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("질문 7")
        self.setWindowIcon(QIcon('winicon.png'))
        self.resize(1000, 750)

        bgImage = QImage('questionbg.PNG')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)
        self.center()

        self.label1 = QLabel('Q7. 어쩌다 새로운 사교모임에 초대되었다. 그곳에서 당신은 어떤 것을 더 기대하는가?', self)
        self.label1.move(100, 180)

        self.rbtn1 = QRadioButton('다양한 사람들과의 대화', self)  # E
        self.rbtn1.move(320, 270)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(320, 330)
        self.rbtn2.setText('사회적인 경험과 유용한 정보 수집')  # I

        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 550, 210, 40)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def winB_clicked(self):
        adding(0, (self.rbtn1.isChecked()))
        self.close()
        I.show()


class question8(QWidget):  # I
    global J

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("질문 8")
        self.setWindowIcon(QIcon('winicon.png'))
        self.resize(1000, 750)

        bgImage = QImage('questionbg.PNG')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)
        self.center()

        self.label1 = QLabel('Q8. 다음 주까지 해결해야 할 중요한 일이 생겼다. 당신은 이 일을 어떻게 처리할 것인가?', self)
        self.label1.move(100, 180)

        self.rbtn1 = QRadioButton('남은 기간 동안의 계획을 먼저 세운 후 계획에 따라 실천한다.', self)  # J
        self.rbtn1.move(200, 270)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(200, 330)
        self.rbtn2.setText('시간이 나거나, 생각날 때 조금씩 해결한다.')  # P

        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 550, 210, 40)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def winB_clicked(self):
        adding(3, (self.rbtn1.isChecked()))
        self.close()
        J.show()


class question9(QWidget):  # J
    global K

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("질문 9")
        self.setWindowIcon(QIcon('winicon.png'))
        self.resize(1000, 750)

        bgImage = QImage('questionbg.PNG')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)
        self.center()

        self.label1 = QLabel('Q9. 맛집을 찾아가려는 데 위치를 안다고 호언장담하던 친구가 못찾고 헤멘다.', self)
        self.label1.move(140, 160)
        self.label2 = QLabel('이럴 때 당신은?', self)
        self.label2.move(450, 200)

        self.rbtn1 = QRadioButton('얼른 지도 앱 켜봐 이번엔 실패하지말고 후딱 가자.', self)  # s
        self.rbtn1.move(200, 270)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(200, 330)
        self.rbtn2.setText('와 이런데도 있었네 기왕 새로운 길로 온 거 여기 구경하다 가자.')  # N

        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 550, 210, 40)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def winB_clicked(self):
        adding(1, (self.rbtn1.isChecked()))
        self.close()
        K.show()


class question10(QWidget):  # K
    global L

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("질문 10")
        self.setWindowIcon(QIcon('winicon.png'))
        self.resize(1000, 750)

        bgImage = QImage('questionbg.PNG')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)
        self.center()

        self.label1 = QLabel('Q10. 친구와 의견차이로 갈등이 생겼다. 이럴 때 당신은?', self)
        self.label1.move(230, 180)

        self.rbtn1 = QRadioButton('친구의 입장과 내 입장을 파악하고 최대한 빨리 해결하고자 한다.', self)  # J
        self.rbtn1.move(200, 270)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(200, 330)
        self.rbtn2.setText('갈등 상황을 충분한 시간을 두고 고민한다. ')  # P

        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 550, 210, 40)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def winB_clicked(self):
        adding(3, (self.rbtn1.isChecked()))
        self.close()
        L.show()


class question11(QWidget):  # L
    global M

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("질문 11")
        self.setWindowIcon(QIcon('winicon.png'))
        self.resize(1000, 750)

        bgImage = QImage('questionbg.PNG')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)
        self.center()

        self.label1 = QLabel('Q11. "넌 뭐 제대로 아는게 없는 데 아는 척은 엄청하는 것 같아"', self)
        self.label1.move(240, 170)
        self.label2 = QLabel('라는 말을 들을 때, 당신의 반응은?', self)
        self.label2.move(360, 210)

        self.rbtn1 = QRadioButton('뭐래, 조용히 해. 가만 안둔다.', self)  # T
        self.rbtn1.move(350, 280)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(350, 330)
        self.rbtn2.setText('.......(마음의 상처)')  # F

        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 550, 210, 40)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def winB_clicked(self):
        adding(2, (self.rbtn1.isChecked()))
        self.close()
        M.show()


class question12(QWidget):  # M
    global N

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("질문 12")
        self.setWindowIcon(QIcon('winicon.png'))
        self.resize(1000, 750)

        bgImage = QImage('questionbg.PNG')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)
        self.center()

        self.label1 = QLabel('Q12. 친구가 달이 떴다고 전화를 했다. 당신의 반응은?', self)
        self.label1.move(250, 180)

        self.rbtn1 = QRadioButton('달이 떴다고 왜 내생각이 나..?  ', self)  # T
        self.rbtn1.move(280, 270)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(280, 330)
        self.rbtn2.setText('ㅠㅠㅠㅠ 감동이야 ㅠㅠ 고마워 사랑해ㅠㅠㅠ ')  # F

        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 550, 210, 40)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def winB_clicked(self):
        adding(2, (self.rbtn1.isChecked()))
        self.close()
        N.show()


class question13(QWidget):  # N
    global O

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("질문 13")
        self.setWindowIcon(QIcon('winicon.png'))
        self.resize(1000, 750)

        bgImage = QImage('questionbg.PNG')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)
        self.center()

        self.label1 = QLabel('Q13. 민감한 주제에 대해 대화를 하게 되었다. 당신의 행동은?', self)
        self.label1.move(250, 180)

        self.rbtn1 = QRadioButton('민감한 주제인 만큼 주의를 기울여 발언한다.', self)  # E
        self.rbtn1.move(280, 270)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(280, 330)
        self.rbtn2.setText('실수를 방지하기 위해 발언을 자제한다.')  # I

        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 550, 210, 40)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def winB_clicked(self):
        adding(0, (self.rbtn1.isChecked()))
        self.close()
        O.show()


class question14(QWidget):  # O
    global P

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("질문 14")
        self.setWindowIcon(QIcon('winicon.png'))
        self.resize(1000, 750)

        bgImage = QImage('questionbg.PNG')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)
        self.center()

        self.label1 = QLabel('Q14. 해결하기 어려운 상황에 놓이게 되었다. 이럴 때, 당신의 행동은?', self)
        self.label1.move(200, 180)

        self.rbtn1 = QRadioButton('주위사람들에게 도움을 요청한다', self)  # E
        self.rbtn1.move(330, 270)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(330, 330)
        self.rbtn2.setText('어떻게든 혼자 해결해보고자 한다.')  # I

        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 550, 210, 40)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def winB_clicked(self):
        adding(0, (self.rbtn1.isChecked()))
        self.close()
        P.show()


class question15(QWidget):  # P
    global Q

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("질문 15")
        self.setWindowIcon(QIcon('winicon.png'))
        self.resize(1000, 750)

        bgImage = QImage('questionbg.PNG')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)
        self.center()

        self.label1 = QLabel('Q15. 혼자 요리를 하는 상황일 때 당신은?', self)
        self.label1.move(300, 180)

        self.rbtn1 = QRadioButton('설탕 두숟가락…? 아니 무슨 숟가락인데 티스푼이야 뭐야, 이렇게 알려주면 어떡하라는건데', self)  # S
        self.rbtn1.move(80, 270)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(80, 330)
        self.rbtn2.setText('설탕 150mg….? 대충 이정도 무게를 150mg이라고 기준으로 정하고 요리하면 되겠지?')  # N

        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 550, 210, 40)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def winB_clicked(self):
        adding(1, (self.rbtn1.isChecked()))
        self.close()
        Q.show()


class question16(QWidget):  # Q
    global R

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("질문 16")
        self.setWindowIcon(QIcon('winicon.png'))
        self.resize(1000, 750)

        bgImage = QImage('questionbg.PNG')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)
        self.center()

        self.label1 = QLabel('Q16. 먼 곳에서 일정을 마치고 혼자 집으로 갈 때 당신의 행동은?', self)
        self.label1.move(200, 180)

        self.rbtn1 = QRadioButton('집에 도착할 때까지 친구와 연락한다.', self)  # E
        self.rbtn1.move(320, 270)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(320, 330)
        self.rbtn2.setText('혼자만의 시간을 즐긴다.')  # I

        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 550, 210, 40)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def winB_clicked(self):
        adding(0, (self.rbtn1.isChecked()))
        self.close()
        R.show()


class question17(QWidget):  # R
    global S

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("질문 17")
        self.setWindowIcon(QIcon('winicon.png'))
        self.resize(1000, 750)

        bgImage = QImage('questionbg.PNG')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)
        self.center()

        self.label1 = QLabel('Q17. 새 회사에 첫 출근을 하게 되었다. 모든 것이 낯선 상황에서 당신이 원하는 것은?', self)
        self.label1.move(120, 180)

        self.rbtn1 = QRadioButton('업무에 빠르게 적응할 수 있는 구조화된 환경', self)  # J
        self.rbtn1.move(260, 270)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(260, 330)
        self.rbtn2.setText('낯선 업무를 편하게 물어볼 수 있는 자유로운 환경')  # P

        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 550, 210, 40)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def winB_clicked(self):
        adding(3, (self.rbtn1.isChecked()))
        self.close()
        S.show()


class question18(QWidget):  # S
    global T

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("질문 18")
        self.setWindowIcon(QIcon('winicon.png'))
        self.resize(1000, 750)

        bgImage = QImage('questionbg.PNG')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)
        self.center()

        self.label1 = QLabel('Q18. 추리소설을 읽고 있는 당신, 당신의 머릿속은?', self)
        self.label1.move(290, 180)

        self.rbtn1 = QRadioButton('(아무 생각 없이 집중해서 읽음)', self)  # S
        self.rbtn1.move(130, 270)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(130, 330)
        self.rbtn2.setText('(책을 읽다 말고)오….주인공이 A를 이 방에서 이렇게 죽였다고? 그게 가능한가?')  # N

        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 550, 210, 40)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def winB_clicked(self):
        adding(1, (self.rbtn1.isChecked()))
        self.close()
        T.show()


class question19(QWidget):  # T
    global U

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("질문 19")
        self.setWindowIcon(QIcon('winicon.png'))
        self.resize(1000, 750)

        bgImage = QImage('questionbg.PNG')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)
        self.center()

        self.label1 = QLabel('Q19. 당신이 회사에서 좋은 성과를 거두었다. 가장 듣고 싶은 칭찬은?', self)
        self.label1.move(200, 180)

        self.rbtn1 = QRadioButton('어떻게 이런 걸 생각했어? 다음에도 너랑 일하고 싶다. 금방 배우네 ', self)  # T
        self.rbtn1.move(180, 270)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(180, 330)
        self.rbtn2.setText('소중해 너는, 늘 고마워, 넌 꼭 필요한 사람이야, 난 널 믿어 ')  # F

        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 550, 210, 40)


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def winB_clicked(self):
        adding(2, (self.rbtn1.isChecked()))
        self.close()
        U.show()


class question20(QWidget):  # U
    global V

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("질문 20")
        self.setWindowIcon(QIcon('winicon.png'))
        self.resize(1000, 750)

        bgImage = QImage('questionbg.PNG')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)
        self.center()

        self.label1 = QLabel('Q20. 친구와 여행가기 전날 밤 잠들기 직전에 당신의 머릿속은?', self)
        self.label1.move(210, 180)

        self.rbtn1 = QRadioButton('필요한 준비물 다 챙겼지? 옷이랑…음 됐다 일찍 자자', self)  # S
        self.rbtn1.move(30, 270)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(30, 330)
        self.rbtn2.setText('근데 비 오면 어떡하지? 비 맞고 노는 것도 재밌겠다 근데 그러다 파도에 휩쓸려가서 조난당하면?')  # N

        self.winB = QPushButton('결과 분석하기', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 550, 210, 40)


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def winB_clicked(self):
        adding(1, (self.rbtn1.isChecked()))
        self.close()
        character.__init__()
        character.show()

    def winB_clicked(self):
        self.close()
        character.__init__()
        character.show()
        
        

class Result(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle("MBTI with UMI's Cells")
        self.setWindowIcon(QIcon('icon.png')) # 임시로 만든 게임아이콘, main.py와 같은 hierarchy에 위치
        self.resize(1000, 750)

        bgImage = QImage('cellresult.png')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))

        self.setPalette(palette)

        self.center()
        self.loadcell()

        btn_next = QPushButton('다음 콘텐츠로', self)
        btn_next.setGeometry(400, 670, 210, 40)
        btn_next.clicked.connect(self.next)

        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        

    def loadcell(self):


        pixmap1 = QPixmap()
        cell_txt = QLabel()
        cell_txt.setAlignment(Qt.AlignCenter)
        self.result = mbti_result()
        #print(self.result)

         #mbti 결과 반환인자를 result라고 가정


        if self.result == 7:
            pixmap1.load('./cell/istj.png') # 세포 이미지 위치, main.py 아래에 cell 폴더 만들어 .png 형식의 이미지 저장
            scaleChangedImage = pixmap1.scaled(300, 300, Qt.KeepAspectRatio)
            cell_txt.setText("실제 사실에 대해 정확하고 체계적으로 기억하며, 일처리에 있어도 신충하고 책임감 있는 당신!\n\n"
                             "변화보단 반복을 좋아하는 당신의 머리 속의 가장 중요한 세포는\n\n"
                             "바로 다른 이들에게 항상완벽한 모습으로 예의를 지키는 “예의세포” 입니다~!")
        elif self.result == 1:
            pixmap1.load('./cell/infj.png')
            scaleChangedImage = pixmap1.scaled(300, 300, Qt.KeepAspectRatio)
            cell_txt.setText("항상 상대방을 위해 배려하고 진심 어린 공감을 해주는 당신!\n\n"
                             "하지만 평상시에 생각이 너무 많아 걱정이 많은 당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "안 좋은 상황을 미리 걱정하고 세포들에게 대비할 수 있도록 도움을 주는 “불안 세포”입니다~!")
        elif self.result == 3:
            pixmap1.load('./cell/intj.png')
            scaleChangedImage = pixmap1.scaled(300, 300, Qt.KeepAspectRatio)
            cell_txt.setText("계획적이고 효율적이면 혼자 있는 것을 좋아하는 당신!\n\n"
                             "분석력 또한 매우 뛰어난 편인 당신의머리 속의 가장 중요한 세포는 바로\n\n"
                             "상황을 분석하고 추리해내는 능력이 뛰어나지만, 잘못 분석하는 경우가 있어 허당미가 있는 “명탐정 세포” 입니다~!")
        elif self.result == 6:
            pixmap1.load('./cell/istp.png')
            scaleChangedImage = pixmap1.scaled(300, 300, Qt.KeepAspectRatio)
            cell_txt.setText("호불호가 강하고 자기주장도 강한 당신!\n\n"
                             "내성적이면서도 냉철한 이성주의자인 당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "이유 없이 화내진 않지만, 할 말을 다 못하면 잠재되어 있던 분노가 격하게 치밀어 오르는 “히스테리우스” 입니다~!")
        elif self.result == 4:
            pixmap1.load('./cell/isfp.png')
            scaleChangedImage = pixmap1.scaled(300, 300, Qt.KeepAspectRatio)
            cell_txt.setText("집에 있는 게 가장 좋고 누워서 무언가를 하는 게 가장 좋은 당신!\n\n"
                             "당신의 머리 속의 가장 중요한 세포는 바로 세포들의 휴식과 숙면을 책임지는 중요한 역할을 하지만\n\n"
                             "항상 겸손하고, 순하고 따뜻하며 정이 많은 “자장자장 세포” 입니다~!")
        elif self.result == 0:
            pixmap1.load('./cell/infp.png')
            scaleChangedImage = pixmap1.scaled(300, 300, Qt.KeepAspectRatio)
            cell_txt.setText("조용한 힐링과 낭만을 즐기고, 섬세하며 감성적인 당신!\n\n"
                             "당신의 머리 속의 가장 중요한 세포는 바로 호기심이 많고 온화하지만\n\n"
                             "이적이고 상상력이 풍부하며 다양한 감정을 느끼는 낭만적인 “감성세포” 입니다~!")
        elif self.result == 2:
            pixmap1.load('./cell/intp.png')
            scaleChangedImage = pixmap1.scaled(300, 300, Qt.KeepAspectRatio)
            cell_txt.setText("아이디어가 풍부하며, 끊임없이 새로운 지식에 목바른 비평적인 관점을 뛰어난 전략가인 당신!\n\n"
                             "당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "평상시에는 세상에 별 관심이 없다가 중요한 순간에 등장해\n\n"
                             "독창적이고 돌직구적인 아이디어로 문제를 해결해주는 “신의 한수” 입니다~!")
        elif self.result == 5:
            pixmap1.load('./cell/isfj.png')
            scaleChangedImage = pixmap1.scaled(300, 300, Qt.KeepAspectRatio)
            cell_txt.setText("상상력과 타고난 섬세함으로 상대방의 가슴을 진심으로 울리는데 천부적인 소질이 있는 당신!\n\n"
                             "정이 많고 남용하지 않고, 솔직하지만 조용한 당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "세포들의 마음의 평화를 찾아주지만 화가 쌓기면 확 터트리는 “마음의 평화 사절단” 입니다~!")
        elif self.result == 14:
            pixmap1.load('./cell/estp.png')
            scaleChangedImage = pixmap1.scaled(300, 300, Qt.KeepAspectRatio)
            cell_txt.setText("경쟁, 내기, 스릴있고 즉흥적인 것들을 좋아하는 당신!\n\n"
                             "선입견도 없고 개방적인 당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "생각보다 행동이 우선이고, 항상 적극적이고 열정적인 본능에 충실해\n\n"
                             "많은 세포들의 관심을 받고 있는 “응큼세포” 입니다~!")
        elif self.result == 12:
            pixmap1.load('./cell/esfp.png')
            scaleChangedImage = pixmap1.scaled(300, 300, Qt.KeepAspectRatio)
            cell_txt.setText("붙임성이 좋고 사교적이며 낙천적인 성격으로 적극적으로 사랑을 표현하는 당신!\n\n"
                             "당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "자유롭고 밝지만 화가 나면 쉽게 감정에 휩싸이는\n\n"
                             "깜짝 이벤트를 좋아하는 사랑꾼의 역할을 하는 “사랑세포”입니다~!")
        elif self.result == 8:
            pixmap1.load('./cell/enfp.png')
            scaleChangedImage = pixmap1.scaled(300, 300, Qt.KeepAspectRatio)
            cell_txt.setText("긍정적이며 낙천적이고 인싸 기질이 다분한 당신!\n\n"
                             "많은 쾌활한 성격과 때로는 어린아이 같은 면이 있는 당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "자유를 추구하고 리액션이 좋아 많은 세포들과 친한 “설레발 세포”입니다~!")
        elif self.result == 10:
            pixmap1.load('./cell/entp.png')
            scaleChangedImage = pixmap1.scaled(300, 300, Qt.KeepAspectRatio)

            cell_txt.setText("본인의 잘난 맛에 살아가고 지는 건 절대 용납 못하는 당신!\n\n"
                             "당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "평상시에는 쿨하지만, 자존심을 긁히는 일이 생긴다면\n\n"
                             "화가 나고 열받아서 절대 지지 않는 “자존심 세포” 입니다~!")
        elif self.result == 15:
            pixmap1.load('./cell/estj.png')
            scaleChangedImage = pixmap1.scaled(300, 300, Qt.KeepAspectRatio)
            cell_txt.setText("매우 현실적이고 이성적이며 직설적으로 내면이 단단하고 강단있는 당신!\n\n"
                             "당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "자존감이 높아 주변의 유혹에 쉽게 흔들리지 않고 맡은 일은 책임감 있게 완수하는 능력자이지만,\n\n"
                             "남의 말을 귀담아 듣지 않고 공감능력이 조금 떨어지는 “이성세포” 입니다~!")
        elif self.result == 13:
            pixmap1.load('./cell/esfj.png')
            scaleChangedImage = pixmap1.scaled(300, 300, Qt.KeepAspectRatio)
            cell_txt.setText("밝은 표정으로 매사에 열정적이며 칭찬 자판기인 당신! \n\n"
                             "당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "뛰어난 패션감각으로 외모를 꾸며주는 중요한 역할을 하지만\n\n"
                             "가끔은 남의 시선을 많이 의식해 힘들기도 한 “패션 세포” 입니다~!")
        elif self.result == 9:
            pixmap1.load('./cell/enfj.png')
            scaleChangedImage = pixmap1.scaled(300, 300, Qt.KeepAspectRatio)
            cell_txt.setText("강한 책임감과 열정을 가지고 있고 세계평화를 꿈꾸고 있는 당신!\n\n"
                             "당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "뛰어난 카리스마로 세포들의 평화를 책임지고 있는 중요한 역할을 하고 있지만\n\n"
                             "고집이 강해 종종 마음 먹은 대로 성급한 결정을 하기도 하는 “판사세포” 입니다~!")
        elif self.result == 11:
            pixmap1.load('./cell/entj.png')
            scaleChangedImage = pixmap1.scaled(300, 300, Qt.KeepAspectRatio)
            cell_txt.setText("자기애가 강하고 논리적이며 항상 준비가 철저한 워커홀릭 기질의 당신!\n\n"
                             "당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "꼼꼼한의 정석으로 다이어리, 노트필기 등의 정리와 계획세우는 것을 좋아하고\n\n"
                             "즉흥적인 것을 싫어해 때로는 너무 철저한 계획으로 피곤하기도 한 “스케줄 세포” 입니다~!")

        cell_img = QLabel()
        cell_img.setPixmap(scaleChangedImage)
        cell_img.setAlignment(Qt.AlignCenter)
        font1 = cell_txt.font()
        font1.setFamily('맑은 고딕')
        font1.setPointSize(9)

        vbox = QVBoxLayout()
        vbox.addStretch(2)
        vbox.addWidget(cell_img)
        vbox.addWidget(cell_txt)
        vbox.addStretch(4)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vbox)
        hbox.addStretch(1)

        self.setLayout(hbox)

    def next(self):
        self.close()
        etc.__init__()
        etc.show()


class Etc(QWidget): # 게임 설명

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MBTI with UMI's Cells")
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(1000, 750)

        bgImage = QImage('intro.png')
        size = bgImage.scaled(QSize(1000, 750))
        palette = QPalette()
        palette.setBrush(10, QBrush(size))
        self.setPalette(palette)
        self.center()
        self.loadcell()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def loadcell(self):
        
        pixmap1 = QPixmap()
        self.icon = mbti_result()
        #print(self.icon)

        btn_game = QPushButton('게임 시작!', self)
        btn_game.setGeometry(400, 520, 210, 40)
        btn_game.clicked.connect(self.game)

        # mbti 결과 반환인자를 result라고 가정

        if self.icon == 7:
            pixmap1.load('./icon/istj.png')  # 세포 이미지 위치, main.py 아래에 icon 폴더 만들어 .png 형식의 이미지 저장
            scaleChangedImage = pixmap1.scaled(210, 70, Qt.KeepAspectRatio)

        elif self.icon == 1:
            pixmap1.load('./icon/infj.png')
            scaleChangedImage = pixmap1.scaled(210, 70, Qt.KeepAspectRatio)

        elif self.icon == 3:
            pixmap1.load('./icon/intj.png')
            scaleChangedImage = pixmap1.scaled(210, 70, Qt.KeepAspectRatio)

        elif self.icon == 6:
            pixmap1.load('./icon/istp.png')
            scaleChangedImage = pixmap1.scaled(210, 70, Qt.KeepAspectRatio)

        elif self.icon == 4:
            pixmap1.load('./icon/isfp.png')
            scaleChangedImage = pixmap1.scaled(210, 70, Qt.KeepAspectRatio)

        elif self.icon == 0:
            pixmap1.load('./icon/infp.png')
            scaleChangedImage = pixmap1.scaled(210, 70, Qt.KeepAspectRatio)

        elif self.icon == 2:
            pixmap1.load('./icon/intp.png')
            scaleChangedImage = pixmap1.scaled(210, 70, Qt.KeepAspectRatio)

        elif self.icon == 5:
            pixmap1.load('./icon/isfj.png')
            scaleChangedImage = pixmap1.scaled(210, 70, Qt.KeepAspectRatio)

        elif self.icon == 14:
            pixmap1.load('./icon/estp.png')
            scaleChangedImage = pixmap1.scaled(210, 70, Qt.KeepAspectRatio)

        elif self.icon == 12:
            pixmap1.load('./icon/esfp.png')
            scaleChangedImage = pixmap1.scaled(210, 70, Qt.KeepAspectRatio)

        elif self.icon == 8:
            pixmap1.load('./icon/enfp.png')
            scaleChangedImage = pixmap1.scaled(210, 70, Qt.KeepAspectRatio)

        elif self.icon == 10:
            pixmap1.load('./icon/entp.png')
            scaleChangedImage = pixmap1.scaled(210, 70, Qt.KeepAspectRatio)

        elif self.icon == 15:
            pixmap1.load('./icon/estj.png')
            scaleChangedImage = pixmap1.scaled(210, 70, Qt.KeepAspectRatio)

        elif self.icon == 13:
            pixmap1.load('./icon/esfj.png')
            scaleChangedImage = pixmap1.scaled(210, 70, Qt.KeepAspectRatio)

        elif self.icon == 9:
            pixmap1.load('./icon/enfj.png')
            scaleChangedImage = pixmap1.scaled(210, 70, Qt.KeepAspectRatio)

        elif self.icon == 11:
            pixmap1.load('./icon/entj.png')
            scaleChangedImage = pixmap1.scaled(210, 70, Qt.KeepAspectRatio)


        cell_img = QLabel()
        cell_img.setPixmap(scaleChangedImage)
        cell_img.setAlignment(Qt.AlignCenter)
        cell_img.move(485, 350)

        txt1 = QLabel("당신의 성격을 잘 나타내는 아이콘을 모으세요!", self)
        txt1.setAlignment(Qt.AlignCenter)
        font1 = txt1.font()
        font1.setPointSize(18)
        txt2 = QLabel("당신의 MBTI는 보통 다음과 같은 성격을 나타냅니다. \n\n 폭탄을 피해서 당신의 성격에 해당하는 아이콘을 클릭하세요!", self)
        txt2.setAlignment(Qt.AlignCenter)
        font1 = txt1.font()
        font1.setPointSize(18)

        vbox = QVBoxLayout()
        vbox.addStretch(4)
        vbox.addWidget(txt1)
        vbox.addStretch(1)
        vbox.addWidget(txt2)
        vbox.addStretch(1)
        vbox.addWidget(cell_img)
        vbox.addStretch(5)

        self.setLayout(vbox)

    def game(self) :
        self.close()
        MainMenu.HomeScreen(self.icon)


app = QApplication(sys.argv)
A = Startwindow()
B = question1()
C = question2()
D = question3()
E = question4()
F = question5()
G = question6()
H = question7()
I = question8()
J = question9()
K = question10()
L = question11()
M = question12()
N = question13()
O = question14()
P = question15()
Q = question16()
R = question17()
S = question18()
T = question19()
U = question20()

character = Result()
etc = Etc()

if __name__ == '__main__':
   
   sys.exit(app.exec_())
   os.system('pause')
