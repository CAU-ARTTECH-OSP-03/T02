import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Result(QWidget):

    global etc

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MBTI with UMI's Cells")
        self.setWindowIcon(QIcon('icon.png')) # 임시로 만든 게임아이콘, main.py와 같은 hierarchy에 위치
        self.resize(1000, 750)
        self.center()
        self.loadcell()

        btn_next = QPushButton('다음', self)
        btn_next.move(850, 670)
        btn_next.clicked.connect(self.next)

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def loadcell(self):

        pixmap1 = QPixmap()
        cell_txt = QLabel()

        # mbti 결과 반환인자를 result라고 가정
        result = 7 # 임의로 istj 지정

        if result == 7:
            pixmap1.load('./cell/istj.jfif') # 세포 이미지 위치, main.py 아래에 cell 폴더 만들어 .jfif 형식의 이미지 저장
            cell_txt.setText("실제 사실에 대해 정확하고 체계적으로 기억하며, 일처리에 있어도 신충하고 책임감 있는 당신!\n\n"
                             "변화보단 반복을 좋아하는 당신의 머리 속의 가장 중요한 세포는\n\n"
                             "바로 다른 이들에게 항상완벽한 모습으로 예의를 지키는 “예의세포” 입니다~!")
        elif result == 1:
            pixmap1.load('./cell/infj.jfif')
            cell_txt.setText("항상 상대방을 위해 배려하고 진심 어린 공감을 해주는 당신!\n\n"
                             "하지만 평상시에 생각이 너무 많아 걱정이 많은 당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "안 좋은 상황을 미리 걱정하고 세포들에게 대비할 수 있도록 도움을 주는 “불안 세포”입니다~!")
        elif result == 3:
            pixmap1.load('./cell/intj.jfif')
            cell_txt.setText("계획적이고 효율적이면 혼자 있는 것을 좋아하는 당신!\n\n"
                             "분석력 또한 매우 뛰어난 편인 당신의머리 속의 가장 중요한 세포는 바로\n\n"
                             "상황을 분석하고 추리해내는 능력이 뛰어나지만, 잘못 분석하는 경우가 있어 허당미가 있는 “명탐정 세포” 입니다~!")
        elif result == 6:
            pixmap1.load('./cell/istp.jfif')
            cell_txt.setText("호불호가 강하고 자기주장도 강한 당신!\n\n"
                             "내성적이면서도 냉철한 이성주의자인 당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "이유 없이 화내진 않지만, 할 말을 다 못하면 잠재되어 있던 분노가 격하게 치밀어 오르는 “히스테리우스” 입니다~!")
        elif result == 4:
            pixmap1 = QPixmap('./cell/isfp.jfif')
            cell_txt.setText("집에 있는 게 가장 좋고 누워서 무언가를 하는 게 가장 좋은 당신!\n\n"
                             "당신의 머리 속의 가장 중요한 세포는 바로 세포들의 휴식과 숙면을 책임지는 중요한 역할을 하지만\n\n"
                             "항상 겸손하고, 순하고 따뜻하며 정이 많은 “자장자장 세포” 입니다~!")
        elif result == 0:
            pixmap1.load('./cell/infp.jfif')
            cell_txt.setText("조용한 힐링과 낭만을 즐기고, 섬세하며 감성적인 당신!\n\n"
                             "당신의 머리 속의 가장 중요한 세포는 바로 호기심이 많고 온화하지만\n\n"
                             "이적이고 상상력이 풍부하며 다양한 감정을 느끼는 낭만적인 “감성세포” 입니다~!")
        elif result == 2:
            pixmap1.load('./cell/intp.jfif')
            cell_txt.setText("아이디어가 풍부하며, 끊임없이 새로운 지식에 목바른 비평적인 관점을 뛰어난 전략가인 당신!\n\n"
                             "당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "평상시에는 세상에 별 관심이 없다가 중요한 순간에 등장해\n\n"
                             "독창적이고 돌직구적인 아이디어로 문제를 해결해주는 “신의 한수” 입니다~!")
        elif result == 5:
            pixmap1.load('./cell/isfj.jfif')
            cell_txt.setText("상상력과 타고난 섬세함으로 상대방의 가슴을 진심으로 울리는데 천부적인 소질이 있는 당신!\n\n"
                             "정이 많고 남용하지 않고, 솔직하지만 조용한 당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "세포들의 마음의 평화를 찾아주지만 화가 쌓기면 확 터트리는 “마음의 평화 사절단” 입니다~!")
        elif result == 14:
            pixmap1.load('./cell/estp.jfif')
            cell_txt.setText("경쟁, 내기, 스릴있고 즉흥적인 것들을 좋아하는 당신!\n\n"
                             "선입견도 없고 개방적인 당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "생각보다 행동이 우선이고, 항상 적극적이고 열정적인 본능에 충실해\n\n"
                             "많은 세포들의 관심을 받고 있는 “응큼세포” 입니다~!")
        elif result == 12:
            pixmap1.load('./cell/esfp.jfif')
            cell_txt.setText("붙임성이 좋고 사교적이며 낙천적인 성격으로 적극적으로 사랑을 표현하는 당신!\n\n"
                             "당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "자유롭고 밝지만 화가 나면 쉽게 감정에 휩싸이는\n\n"
                             "깜짝 이벤트를 좋아하는 사랑꾼의 역할을 하는 “사랑세포”입니다~!")
        elif result == 8:
            pixmap1.load('./cell/enfp.jfif')
            cell_txt.setText("긍정적이며 낙천적이고 인싸 기질이 다분한 당신!\n\n"
                             "많은 쾌활한 성격과 때로는 어린아이 같은 면이 있는 당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "자유를 추구하고 리액션이 좋아 많은 세포들과 친한 “설레발 세포”입니다~!")
        elif result == 10:
            pixmap1.load('./cell/entp.jfif')
            cell_txt.setText("본인의 잘난 맛에 살아가고 지는 건 절대 용납 못하는 당신!\n\n"
                             "당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "평상시에는 쿨하지만, 자존심을 긁히는 일이 생긴다면\n\n"
                             "화가 나고 열받아서 절대 지지 않는 “자존심 세포” 입니다~!")
        elif result == 15:
            pixmap1.load('./cell/estj.jfif')
            cell_txt.setText("매우 현실적이고 이성적이며 직설적으로 내면이 단단하고 강단있는 당신!\n\n"
                             "당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "자존감이 높아 주변의 유혹에 쉽게 흔들리지 않고 맡은 일은 책임감 있게 완수하는 능력자이지만,\n\n"
                             "남의 말을 귀담아 듣지 않고 공감능력이 조금 떨어지는 “이성세포” 입니다~!")
        elif result == 13:
            pixmap1.load('./cell/esfj.jfif')
            cell_txt.setText("밝은 표정으로 매사에 열정적이며 칭찬 자판기인 당신! \n\n"
                             "당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "뛰어난 패션감각으로 외모를 꾸며주는 중요한 역할을 하지만\n\n"
                             "가끔은 남의 시선을 많이 의식해 힘들기도 한 “패션 세포” 입니다~!")
        elif result == 9:
            pixmap1.load('./cell/enfj.jfif')
            cell_txt.setText("강한 책임감과 열정을 가지고 있고 세계평화를 꿈꾸고 있는 당신!\n\n"
                             "당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "뛰어난 카리스마로 세포들의 평화를 책임지고 있는 중요한 역할을 하고 있지만\n\n"
                             "고집이 강해 종종 마음 먹은 대로 성급한 결정을 하기도 하는 “판사세포” 입니다~!")
        elif result == 11:
            pixmap1.load('./cell/entj.jfif')
            cell_txt.setText("자기애가 강하고 논리적이며 항상 준비가 철저한 워커홀릭 기질의 당신!\n\n"
                             "당신의 머리 속의 가장 중요한 세포는 바로\n\n"
                             "꼼꼼한의 정석으로 다이어리, 노트필기 등의 정리와 계획세우는 것을 좋아하고\n\n"
                             "즉흥적인 것을 싫어해 때로는 너무 철저한 계획으로 피곤하기도 한 “스케줄 세포” 입니다~!")

        cell_img = QLabel()
        cell_img.setPixmap(pixmap1)
        cell_img.setAlignment(Qt.AlignCenter)
        cell_txt.setAlignment(Qt.AlignCenter)
        font1 = cell_txt.font()
        font1.setPointSize(11)
        cell_txt.setFont(font1)

        vbox = QVBoxLayout()
        vbox.addWidget(cell_img)
        vbox.addWidget(cell_txt)

        self.setLayout(vbox)

    def next(self):
        self.close()
        etc.show()


class Etc(QWidget):

    global game

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MBTI with UMI's Cells")
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(1000, 750)
        self.center()

        btn_share = QPushButton('공유하기', self)
        btn_save = QPushButton('결과화면 캡쳐 및 저장', self)
        btn_game = QPushButton('다음 콘텐츠로', self)

        btn_share.setFixedSize(250, 50)
        btn_save.setFixedSize(250, 50)
        btn_game.setFixedSize(250, 50)

        vbox = QVBoxLayout()
        vbox.addWidget(btn_share, alignment=Qt.AlignCenter)
        vbox.addWidget(btn_save, alignment=Qt.AlignCenter)
        vbox.addWidget(btn_game, alignment=Qt.AlignCenter)

        self.setLayout(vbox)

        btn_share.clicked.connect(self.share)
        btn_save.clicked.connect(self.save)
        btn_game.clicked.connect(self.next)

        # self.show() -> 3개의 창이 동시에 뜨는 문제 해결

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def share(self):
        # sdfsdfd
        exit()

    def save(self):
        # 스크린샷 저장
        exit()

    def next(self): # 뒤에 이어질 컨텐츠
        self.close()
        game.show()


class Game(QWidget): # 뒤에 이어질 컨텐츠 일단 소개페이지정도만 만듦....

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MBTI with UMI's Cells")
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(1000, 750)
        self.center()

        txt = QLabel('추후 완성 예정', self)
        txt.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(txt)

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

        # self.show() -> 3개의 창이 동시에 뜨는 문제 해결

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


app = QApplication(sys.argv)

result = Result()
etc = Etc()
game = Game() # 뒤에 이어질 컨텐츠

sys.exit(app.exec_())
