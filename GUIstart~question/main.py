from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
from mod1 import *


class Startwindow(QWidget):  # A
    global B
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(800,300,1000,700)   # self.center을 사용할지 고민

        winB = QPushButton('심리테스트 시작하기', self)
        winB.clicked.connect(self.winB_clicked)
        winB.setGeometry(400, 500, 210, 40)
        self.setWindowTitle('유미의 세포들 심리테스트 ⸜(*ˊᗜˋ*)⸝')

        label1 = QLabel('오픈소스 프로그래밍 team2의 유미의 세포들 심리테스트', self)
        label1.move(250, 200)

        self.show()

    def winB_clicked(self):

        self.close()
        B.show()


class question1(QWidget):  # B
    global C
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(800,300,1000,700)
        self.setWindowTitle('질문1')

        self.label1 = QLabel('Q1. 오늘은 소개팅날! 처음 상대를 만나게 되는데, 그 상황에서 당신은?', self)
        self.label1.move(200, 200)

        self.rbtn1 = QRadioButton('주로 질문을 하며 대답을 유도한다.', self) # E
        self.rbtn1.move(300, 300)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(300, 350)
        self.rbtn2.setText('주로 상대방의 질문에 대답한다.') # I

        winB = QPushButton('다음 질문으로', self)
        winB.clicked.connect(self.winB_clicked)
        winB.setGeometry(400, 500, 210, 40)

        
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
        self.setGeometry(800,300,1000,700)
        self.setWindowTitle('질문 2')

        self.label1 = QLabel('Q2. 친구들과 2박 3일로 여행을 가기로 했다. 여행 계획을 세울 때 당신은?', self)
        self.label1.move(170, 200)
     
        self.rbtn1 = QRadioButton('교통편, 숙박시설 뿐만 아니라 경우의 수를 나누어 세부 계획을 짠다.', self)  # J
        self.rbtn1.move(150, 300)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(150, 350)
        self.rbtn2.setText('교통편, 숙박시설 등 필수적인 것만 예약한 후 여행을 가서 상황에 맞게 행동한다.')  # P
       
        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 500, 210, 40)



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
        self.setGeometry(800,300,1000,700)
        self.setWindowTitle('질문 3')

        self.label1 = QLabel('Q3. 동아리에서 사소한 규칙을 어긴 친구에 대한 조치를 취하려고 한다. 당신의 의견은?', self)
        self.label1.move(100, 200)

        self.rbtn1 = QRadioButton('사소한 규칙이라도 사전에 약속된 규칙이기 때문에 적절한 조치를 취해야 한다. ', self)  # J
        self.rbtn1.move(120, 300)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(120, 350)
        self.rbtn2.setText('사소한 규칙은 개인이 재량으로 상황에 따라 유연하게 행동할 수 있다고 생각한다')  # P

        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 500, 210, 40)


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
        self.setGeometry(800, 300, 1000, 700)
        self.setWindowTitle('질문 4')

        self.label1 = QLabel('Q4. 과제들에 공모전, 동아리에 학생회까지! 할 일이 너무 많을 때 당신의 머리속은?', self)
        self.label1.move(120, 200)

        self.rbtn1 = QRadioButton('(다른사람한테 도와달라고 부탁할까 이정도면 시간내에 완벽하게 할 수 있을거같은데) ', self)  # S
        self.rbtn1.move(100, 300)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(100, 350)
        self.rbtn2.setText('(일 안하고 돈벌고싶다. 내가 삼ㅇ전자 회장이었으면 숨만쉬어도 돈이 들어오겠지? ')  # N


        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 500, 210, 40)

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
        self.setGeometry(800, 300, 1000, 700)
        self.setWindowTitle('질문 5')

        self.label1 = QLabel('Q5. 당신이 며칠 동안 열심히 준비한 과제 발표가 끝났다. 친구에게 듣고 싶은 말은?', self)
        self.label1.move(100, 200)

        self.rbtn1 = QRadioButton('잘했어! 이 부분에서 이것만 수정하면 다음엔 더 좋을 발표가 될 것 같아!', self)  # T
        self.rbtn1.move(150, 300)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(150, 350)
        self.rbtn2.setText('열심히 했어~ 넘 고생했어~')  # F


        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 500, 210, 40)

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
        self.setGeometry(800, 300, 1000, 700)
        self.setWindowTitle('질문 6')

        self.label1 = QLabel('Q6. 친구가 취업이 안돼 힘들어하고 있는 상황이다. 당신이라면 어떤 말을 해줄 것인가?', self)
        self.label1.move(100, 200)

        self.rbtn1 = QRadioButton('어떤거 준비하고 있는데? 이력서는 많이 넣어봤어?', self)  # T
        self.rbtn1.move(200, 300)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(200, 350)
        self.rbtn2.setText('(곤란한 질문은 하지 말자) 힘들지 ㅠㅠ')  # F


        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 500, 210, 40)


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
        self.setGeometry(800, 300, 1000, 700)
        self.setWindowTitle('질문 7')

        self.label1 = QLabel('Q7. 어쩌다 새로운 사교모임에 초대되었다. 그곳에서 당신은 어떤 것을 더 기대하는가?', self)
        self.label1.move(100, 200)

        self.rbtn1 = QRadioButton('다양한 사람들과의 대화', self)  # E
        self.rbtn1.move(250, 300)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(250, 350)
        self.rbtn2.setText('사회적인 경험과 유용한 정보 수집')  # I


        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 500, 210, 40)

       

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
        self.setGeometry(800, 300, 1000, 700)
        self.setWindowTitle('질문 8')

        self.label1 = QLabel('Q8. 다음 주까지 해결해야 할 중요한 일이 생겼다. 당신은 이 일을 어떻게 처리할 것인가?', self)
        self.label1.move(100, 200)

        self.rbtn1 = QRadioButton('남은 기간 동안의 계획을 먼저 세운 후 계획에 따라 실천한다.', self)  # J
        self.rbtn1.move(200, 300)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(200, 350)
        self.rbtn2.setText('시간이 나거나, 생각날 때 조금씩 해결한다.')  # P


        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 500, 210, 40)


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
        self.setGeometry(800, 300, 1000, 700)
        self.setWindowTitle('질문 9')

        self.label1 = QLabel('Q9. 맛집을 찾아가려는 데 위치를 안다고 호언장담하던 친구가 못찾고 헤멘다. 이럴 때 당신은?', self)
        self.label1.move(50, 200)

        self.rbtn1 = QRadioButton('얼른 지도 앱 켜봐 이번엔 실패하지말고 후딱 가자.', self)  # s
        self.rbtn1.move(200, 300)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(200, 350)
        self.rbtn2.setText('와 이런데도 있었네 기왕 새로운 길로 온 거 여기 구경하다 가자.')  # N


        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 500, 210, 40)


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
        self.setGeometry(800, 300, 1000, 700)
        self.setWindowTitle('질문 10')

        self.label1 = QLabel('Q10. 친구와 의견차이로 갈등이 생겼다. 이럴 때 당신은?', self)
        self.label1.move(200, 200)

        self.rbtn1 = QRadioButton('친구의 입장과 내 입장을 파악하고 최대한 빨리 해결하고자 한다.', self)  # J
        self.rbtn1.move(200, 300)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(200, 350)
        self.rbtn2.setText('갈등 상황을 충분한 시간을 두고 고민한다. ')  # P


        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 500, 210, 40)


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
        self.setGeometry(800, 300, 1000, 700)
        self.setWindowTitle('질문 11')

        self.label1 = QLabel('Q11. "넌 뭐 제대로 아는게 없는 데 아는 척은 엄청하는 것 같아"라는 말을 들을 때, 당신의 반응은?', self)
        self.label1.move(50, 200)

        self.rbtn1 = QRadioButton('뭐래, 조용히 해. 가만 안둔다.', self)  # T
        self.rbtn1.move(250, 300)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(250, 350)
        self.rbtn2.setText('.......(마음의 상처)')  # F


        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 500, 210, 40)


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
        self.setGeometry(800, 300, 1000, 700)
        self.setWindowTitle('질문 12')

        self.label1 = QLabel('Q12. 친구가 달이 떴다고 전화를 했다. 당신의 반응은?', self)
        self.label1.move(200, 200)

        self.rbtn1 = QRadioButton('달이 떴다고 왜 내생각이 나..?  ', self)  # T
        self.rbtn1.move(200, 300)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(200, 350)
        self.rbtn2.setText('ㅠㅠㅠㅠ 감동이야 ㅠㅠ 고마워 사랑해ㅠㅠㅠ ')  # F


        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 500, 210, 40)

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
        self.setGeometry(800, 300, 1000, 700)
        self.setWindowTitle('질문 13')

        self.label1 = QLabel('Q13. 민감한 주제에 대해 대화를 하게 되었다. 당신의 행동은?', self)
        self.label1.move(200, 200)

        self.rbtn1 = QRadioButton('민감한 주제인 만큼 주의를 기울여 발언한다.', self)  # E
        self.rbtn1.move(250, 300)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(250, 350)
        self.rbtn2.setText('실수를 방지하기 위해 발언을 자제한다.')  # I


        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 500, 210, 40)

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
        self.setGeometry(800, 300, 1000, 700)
        self.setWindowTitle('질문 14')

        self.label1 = QLabel('Q14. 해결하기 어려운 상황에 놓이게 되었다. 이럴 때, 당신의 행동은?', self)
        self.label1.move(150, 200)

        self.rbtn1 = QRadioButton('주위사람들에게 도움을 요청한다', self)  # E
        self.rbtn1.move(300, 300)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(300, 350)
        self.rbtn2.setText('어떻게든 혼자 해결해보고자 한다.')  # I


        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 500, 210, 40)



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
        self.setGeometry(800, 300, 1000, 700)
        self.setWindowTitle('질문 15')

        self.label1 = QLabel('Q15. 혼자 요리를 하는 상황일 때 당신은?', self)
        self.label1.move(250, 200)

        self.rbtn1 = QRadioButton('설탕 두숟가락…? 아니 무슨 숟가락인데 티스푼이야 뭐야, 이렇게 알려주면 어떡하라는건데', self)  # S
        self.rbtn1.move(50, 300)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(50, 350)
        self.rbtn2.setText('설탕 150mg….? 대충 이정도 무게를 150mg이라고 기준으로 정하고 요리하면 되겠지?')  # N


        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 500, 210, 40)

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
        self.setGeometry(800, 300, 1000, 700)
        self.setWindowTitle('질문 16')

        self.label1 = QLabel('Q16. 먼 곳에서 일정을 마치고 혼자 집으로 갈 때 당신의 행동은?', self)
        self.label1.move(200, 200)

        self.rbtn1 = QRadioButton('집에 도착할 때까지 친구와 연락한다.', self)  # E
        self.rbtn1.move(250, 300)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(250, 350)
        self.rbtn2.setText('혼자만의 시간을 즐긴다.')  # I


        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 500, 210, 40)

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
        self.setGeometry(800, 300, 1000, 700)
        self.setWindowTitle('질문 17')

        self.label1 = QLabel('Q17. 새 회사에 첫 출근을 하게 되었다. 모든 것이 낯선 상황에서 당신이 원하는 것은?', self)
        self.label1.move(100, 200)

        self.rbtn1 = QRadioButton('업무에 빠르게 적응할 수 있는 구조화된 환경', self)  # J
        self.rbtn1.move(200, 300)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(200, 350)
        self.rbtn2.setText('낯선 업무를 편하게 물어볼 수 있는 자유로운 환경')  # P


        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 500, 210, 40)


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
        self.setGeometry(800, 300, 1000, 700)
        self.setWindowTitle('질문 18')

        self.label1 = QLabel('Q18. 추리소설을 읽고 있는 당신, 당신의 머릿속은?', self)
        self.label1.move(250, 200)

        self.rbtn1 = QRadioButton('(아무 생각 없이 집중해서 읽음)', self)  # S
        self.rbtn1.move(100, 300)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(100, 350)
        self.rbtn2.setText('(책을 읽다 말고)오….주인공이 A를 이 방에서 이렇게 죽였다고? 그게 가능한가?')  # N


        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 500, 210, 40)

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
        self.setGeometry(800, 300, 1000, 700)
        self.setWindowTitle('질문 19')

        self.label1 = QLabel('Q19. 당신이 회사에서 좋은 성과를 거두었다. 가장 듣고 싶은 칭찬은?', self)
        self.label1.move(130, 200)

        self.rbtn1 = QRadioButton('어떻게 이런 걸 생각했어? 다음에도 너랑 일하고 싶다. 금방 배우네 ', self)  # T
        self.rbtn1.move(150, 300)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(150, 350)
        self.rbtn2.setText('소중해 너는, 늘 고마워, 넌 꼭 필요한 사람이야, 난 널 믿어 ')  # F


        self.winB = QPushButton('다음 질문으로', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 500, 210, 40)


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
        self.setGeometry(800, 300, 1000, 700)
        self.setWindowTitle('질문 20')

        self.label1 = QLabel('Q20. 친구와 여행가기 전날 밤 잠들기 직전에 당신의 머릿속은?', self)
        self.label1.move(200, 200)

        self.rbtn1 = QRadioButton('필요한 준비물 다 챙겼지? 옷이랑…음 됐다 일찍 자자', self)  # S
        self.rbtn1.move(30, 300)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(30, 350)
        self.rbtn2.setText('근데 비 오면 어떡하지? 비 맞고 노는 것도 재밌겠다 근데 그러다 파도에 휩쓸려가서 조난당하면?')  # N


        self.winB = QPushButton('결과 분석하기', self)
        self.winB.clicked.connect(self.winB_clicked)
        self.winB.setGeometry(400, 500, 210, 40)

    def winB_clicked(self):

        adding(1, (self.rbtn1.isChecked()))
        self.close()
        print(mbti_result())
        #V.show()
        


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
# V= progressbar()




sys.exit(app.exec_())