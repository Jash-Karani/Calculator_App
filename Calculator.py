import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit,QCheckBox
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget
from functools import partial
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QPoint, QRect, QSize, pyqtSignal
from PyQt5 import QtGui
import copy

class Calculator(QMainWindow):

    def __init__(self):
        self.input_string=""
        self.expression=""
        self.error_list=["1","2","3","4","5","6","7","8","9","0",".","/","*","-","+","(",")"]
        super().__init__()
        self.setWindowTitle('Pogulator')
        self.setFixedSize(400,400)
        self.layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_widget.setLayout(self.layout)
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.input_box_create()
        self.button_create()
        self.menu()
        self.StatusBar()
        self.control()
        self.error_check()
        
    def input_box_create(self):
        self.input_box=QLineEdit()
        self.input_box.setFixedHeight(40)
        self.font = self.input_box.font()      
        self.font.setPointSize(20)             
        self.input_box.setFont(self.font)
        self.input_box.setAlignment(Qt.AlignLeft)
        self.input_box.isReadOnly()
        self.layout.addWidget(self.input_box)

    def button_create(self):
        self.layout2=QGridLayout()

        self.button1=QPushButton('7')
        self.button1.setFont(self.font)
        self.button1.setFixedSize(50,50)

        self.button2=QPushButton('8')
        self.button2.setFont(self.font)
        self.button2.setFixedSize(50,50)
       
        self.button3=QPushButton('9')
        self.button3.setFont(self.font)
        self.button3.setFixedSize(50,50)
        
        self.button4=QPushButton('/')
        self.button4.setFont(self.font)
        self.button4.setFixedSize(50,50)
        
        self.button5=QPushButton('c')
        self.button5.setFont(self.font)
        self.button5.setFixedSize(50,100)

        self.button6=QPushButton('=')
        self.button6.setFont(self.font)
        self.button6.setFixedSize(50,100)

        self.button7=QPushButton('4')
        self.button7.setFont(self.font)
        self.button7.setFixedSize(50,50)

        self.button8=QPushButton('5')
        self.button8.setFont(self.font)
        self.button8.setFixedSize(50,50)

        self.button9=QPushButton('6')
        self.button9.setFont(self.font)
        self.button9.setFixedSize(50,50)

        self.button10=QPushButton('*')
        self.button10.setFont(self.font)
        self.button10.setFixedSize(50,50)

        self.button11=QPushButton('1')
        self.button11.setFont(self.font)
        self.button11.setFixedSize(50,50)

        self.button12=QPushButton('2')
        self.button12.setFont(self.font)
        self.button12.setFixedSize(50,50)       

        self.button13=QPushButton('3')
        self.button13.setFont(self.font)
        self.button13.setFixedSize(50,50)
                
        self.button14=QPushButton('-')
        self.button14.setFont(self.font)
        self.button14.setFixedSize(50,50)

        self.button15=QPushButton('0')
        self.button15.setFont(self.font)
        self.button15.setFixedSize(50,50)        
                       
        self.button16=QPushButton('00')
        self.button16.setFont(self.font)
        self.button16.setFixedSize(50,50)

        self.button17=QPushButton('.')
        self.button17.setFont(self.font)
        self.button17.setFixedSize(50,50)

        self.button18=QPushButton('+')
        self.button18.setFont(self.font)
        self.button18.setFixedSize(50,50)

        self.button19=QPushButton('^')
        self.button19.setFont(self.font)
        self.button19.setFixedSize(50,50)

        self.button20=QPushButton('%')
        self.button20.setFont(self.font)
        self.button20.setFixedSize(50,50)

        self.layout2.addWidget(self.button1, 0, 0)
        self.layout2.addWidget(self.button2, 0, 1)
        self.layout2.addWidget(self.button3, 0, 2)
        self.layout2.addWidget(self.button4, 0, 3)
        self.layout2.addWidget(self.button5, 0, 4, 2, 1)
        self.layout2.addWidget(self.button6, 2, 4, 2, 1)
        self.layout2.addWidget(self.button7, 1, 0)
        self.layout2.addWidget(self.button8, 1, 1)
        self.layout2.addWidget(self.button9, 1, 2)
        self.layout2.addWidget(self.button10, 1, 3)
        self.layout2.addWidget(self.button11, 2, 0)
        self.layout2.addWidget(self.button12, 2, 1)
        self.layout2.addWidget(self.button13, 2, 2)
        self.layout2.addWidget(self.button14, 2, 3)
        self.layout2.addWidget(self.button15, 3, 0)
        self.layout2.addWidget(self.button16, 3, 1)
        self.layout2.addWidget(self.button17, 3, 2)
        self.layout2.addWidget(self.button18, 3, 3)
        self.layout.addLayout(self.layout2)

    def control(self):
        self.button1.clicked.connect(partial(self.input_str,"7"))
        self.button2.clicked.connect(partial(self.input_str,"8"))
        self.button3.clicked.connect(partial(self.input_str,"9"))
        self.button4.clicked.connect(partial(self.input_str,"/"))
        self.button5.clicked.connect(partial(self.input_str,"C"))
        self.button6.clicked.connect(partial(self.input_str,"="))
        self.button7.clicked.connect(partial(self.input_str,"4"))
        self.button8.clicked.connect(partial(self.input_str,"5"))
        self.button9.clicked.connect(partial(self.input_str,"6"))
        self.button10.clicked.connect(partial(self.input_str,"*"))
        self.button11.clicked.connect(partial(self.input_str,"1"))
        self.button12.clicked.connect(partial(self.input_str,"2"))
        self.button13.clicked.connect(partial(self.input_str,"3"))
        self.button14.clicked.connect(partial(self.input_str,"-"))
        self.button15.clicked.connect(partial(self.input_str,"0"))
        self.button16.clicked.connect(partial(self.input_str,"00"))
        self.button17.clicked.connect(partial(self.input_str,"."))
        self.button18.clicked.connect(partial(self.input_str,"+"))
        self.button19.clicked.connect(partial(self.input_str,"^"))
        self.button20.clicked.connect(partial(self.input_str,"%"))

    def input_str(self,string):
        if string in ["C","="]:
            if string == "C":
                self.clearDisplay()
                self.input_string=""
            else:
                self.expression=self.input_box_text()
                answer=self.calculation_brain(self.expression)
                self.clearDisplay()
                self.setDisplayText(answer)
                self.input_string=""

        else:
            self.input_string = self.input_string+ string
            self.setDisplayText(self.input_string)

    def menu(self):
        self.menu = self.menuBar().addMenu("Menu")
        self.menu.addAction('Trigonometry Calculator',self.trigo)
        self.menu.addAction('Help',self.help)
        self.menu.addAction('Exit', self.close)
    
    def StatusBar(self):
        status = QStatusBar()
        status.showMessage("YOURMAMA corp")
        self.setStatusBar(status)
    
    def setDisplayText(self,input):
        self.input_box.setText(input)
        self.input_box.setFocus()

    def input_box_text(self):
        return self.input_box.text()

    def clearDisplay(self):
        self.setDisplayText('')
      
    def keyPressEvent(self,event):
       if event.key() == 16777220 or event.key() == 16777221:
          self.input_str("=")
       if event.key() == 16777216:
          self.input_str("C")

    def calculation_brain(self,expression):
      input_str=expression
      operators={"+":[],"-":[],"*":[],"/":[]} 
      operator_list=["+","-","*","/"]
      operator_index_list=[]
      for i in range(len(input_str)):
         if input_str[i] in operator_list:
            operator_index_list.append(i)
            operators[input_str[i]].append(i)

      if len(operators["*"])!=0:
         for i in operators["*"]:
            before_index=0
            str_to_remove=""
            after_index=len(input_str)

            if operator_index_list.index(i)-1!=-1:
               before_index = int(operator_index_list[operator_index_list.index(i)-1])+1
            if operator_index_list.index(i)+1!=len(operator_index_list):
               after_index = int(operator_index_list[operator_index_list.index(i)+1])

            str_to_remove=(input_str[before_index:after_index])
            j=i
            result=str(float(input_str[before_index:i].rstrip())*float(input_str[i+1:after_index].rstrip()))

            if len(result)<len(str_to_remove):
               mainstr=""
               input_value=len(str_to_remove)-len(result)
               for i in range(input_value):
                  mainstr=mainstr+"0"
               result_final=result+mainstr
            if len(result)>len(str_to_remove):
               result_final=result[:len(str_to_remove)]
               if result_final[len(result_final)-1]==".":
                  result_final0=result_final.replace("."," ")
                  result_final=copy.deepcopy(result_final0)
            if len(result)==len(str_to_remove):
               result_final=result
            input_str2=input_str.replace(str_to_remove,result_final)
            operator_index_list.remove(j)
            input_str=copy.deepcopy(input_str2)

      if len(operators["/"])!=0:
         for i in operators["/"]:
            before_index=0
            str_to_remove=""
            after_index=len(input_str)

            if operator_index_list.index(i)-1!=-1:
               before_index = int(operator_index_list[operator_index_list.index(i)-1])+1
            if operator_index_list.index(i)+1!=len(operator_index_list):
               after_index = int(operator_index_list[operator_index_list.index(i)+1])

            str_to_remove=(input_str[before_index:after_index])
            j=i
            result=str(float(input_str[before_index:i].rstrip())/float(input_str[i+1:after_index].rstrip()))

            if len(result)<len(str_to_remove):
               mainstr=""
               input_value=len(str_to_remove)-len(result)
               for i in range(input_value):
                  mainstr=mainstr+"0"
               result_final=result+mainstr

            if len(result)>len(str_to_remove):
               result_final=result[:len(str_to_remove)]
               if result_final[len(result_final)-1]==".":
                  result_final0=result_final.replace("."," ")
                  result_final=copy.deepcopy(result_final0)
            if len(result)==len(str_to_remove):
               result_final=result
            input_str2=input_str.replace(str_to_remove,result_final)
            operator_index_list.remove(j)
            input_str=copy.deepcopy(input_str2)


      if len(operators["-"])!=0:
         for i in operators["-"]:
            before_index=0
            str_to_remove=""
            after_index=len(input_str)

            if operator_index_list.index(i)-1!=-1:
               before_index = int(operator_index_list[operator_index_list.index(i)-1])+1
            if operator_index_list.index(i)+1!=len(operator_index_list):
               after_index = int(operator_index_list[operator_index_list.index(i)+1])


            str_to_remove=(input_str[before_index:after_index])
            j=i
            result=str(float(input_str[before_index:i].rstrip())-float(input_str[i+1:after_index].rstrip()))
            if len(result)<len(str_to_remove):
               mainstr=""
               input_value=len(str_to_remove)-len(result)
               for i in range(input_value):
                  mainstr=mainstr+"0"
               result_final=result+mainstr
            if len(result)>len(str_to_remove):
               result_final=result[:len(str_to_remove)]
               if result_final[len(result_final)-1]==".":
                  result_final0=result_final.replace("."," ")
                  result_final=copy.deepcopy(result_final0)
            if len(result)==len(str_to_remove):
               result_final=result
            input_str2=input_str.replace(str_to_remove,result_final)
            operator_index_list.remove(j)
            input_str=copy.deepcopy(input_str2)

      if len(operators["+"])!=0:
         for i in operators["+"]:
            before_index=0
            str_to_remove=""
            after_index=len(input_str)

            if operator_index_list.index(i)-1!=-1:
               before_index = int(operator_index_list[operator_index_list.index(i)-1])+1
            if operator_index_list.index(i)+1!=len(operator_index_list):
               after_index = int(operator_index_list[operator_index_list.index(i)+1])

            str_to_remove=(input_str[before_index:after_index])
            j=i
            result=str(float(input_str[before_index:i].rstrip())+float(input_str[i+1:after_index].rstrip()))
            if len(result)<len(str_to_remove):
               mainstr=""
               input_value=len(str_to_remove)-len(result)
               for i in range(input_value):
                  mainstr=mainstr+"0"
               result_final=result+mainstr
            if len(result)>len(str_to_remove):
               result_final=result[:len(str_to_remove)]
               if result_final[len(result_final)-1]==".":
                  result_final0=result_final.replace("."," ")
                  result_final=copy.deepcopy(result_final0)
            if len(result)==len(str_to_remove):
               result_final=result
            input_str2=input_str.replace(str_to_remove,result_final)
            operator_index_list.remove(j)
            input_str=copy.deepcopy(input_str2)
      return(input_str)

    def error_check(self):
       pass

    def help(self):
       print("hi")
       msg = QMessageBox()
       msg.setFixedSize(400,400)
       msg.setWindowTitle("HELP")
       msg.setIcon(QMessageBox.Information)
       msg.setText("This the overview of all help you will need regarding the calculator.")
       msg.setDetailedText("The details are as follows:\nFigure it out yourselves nerds")
       
       msg.exec_()

    def trigo(self):
        print("trigo works")
        self.trigo_object=Trigo_Window()
        self.trigo_object.show()

class Trigo_Window(QMainWindow):
   def __init__(self):
      self.expression_str=""
      self.trig_function_selected = ""
      self.degree_or_radian = ""
      super().__init__()
      self.setWindowTitle('Trigo calculator')
      self.trig_layout = QVBoxLayout()
      self.setFixedSize(880,400)
      self.main_widget2 = QWidget()
      self.setCentralWidget(self.main_widget2)
      self.main_widget2.setLayout(self.trig_layout)
      
      self.input_box_create2()
      self.button_create2()
      self.control2()
   
   def input_box_create2(self):
      self.input_box2=QLineEdit()
      self.input_box2.setFixedHeight(40)
      self.font2 = self.input_box2.font()     
      self.font3 = self.input_box2.font() 
      self.font4 = self.input_box2.font() 
      self.font2.setPointSize(14)
      self.font3.setPointSize(20)  
      self.font4.setPointSize(9)           
      self.input_box2.setFont(self.font2)
      self.input_box2.setAlignment(Qt.AlignLeft)

      self.trig_status = QLabel()
      self.trig_status.setPixmap(QPixmap("initial.png"))      

      self.degree_radian = QLabel()
      self.degree_radian.setPixmap(QPixmap("degree"))
      self.degree_or_radian = "degree"

   def button_create2(self):
      self.trig_layout2 = QGridLayout()
      self.trig_button1 =QPushButton("tanθ")
      self.trig_button1.setFixedSize(100,60)
      self.trig_button1.setFont(self.font2)

      self.trig_button2 =QPushButton("sinθ")
      self.trig_button2.setFixedSize(100,60)
      self.trig_button2.setFont(self.font2)

      self.trig_button3 =QPushButton("cosθ")
      self.trig_button3.setFixedSize(100,60)
      self.trig_button3.setFont(self.font2)

      self.trig_button4 =QPushButton("cotθ")
      self.trig_button4.setFixedSize(100,60)
      self.trig_button4.setFont(self.font2)

      self.trig_button5 =QPushButton("cosecθ")
      self.trig_button5.setFixedSize(100,60)
      self.trig_button5.setFont(self.font2)

      self.trig_button6 =QPushButton("secθ")
      self.trig_button6.setFixedSize(100,60)
      self.trig_button6.setFont(self.font2)

      self.trig_button7 =QPushButton("tan⁻¹θ")
      self.trig_button7.setFixedSize(100,60)
      self.trig_button7.setFont(self.font2)

      self.trig_button8 =QPushButton("sin⁻¹θ")
      self.trig_button8.setFixedSize(100,60)
      self.trig_button8.setFont(self.font2)

      self.trig_button9 =QPushButton("cos⁻¹θ")
      self.trig_button9.setFixedSize(100,60)
      self.trig_button9.setFont(self.font2)

      self.trig_button10 =QPushButton("cot⁻¹θ")
      self.trig_button10.setFixedSize(100,60)
      self.trig_button10.setFont(self.font2)

      self.trig_button11 =QPushButton("cosec⁻¹θ")
      self.trig_button11.setFixedSize(100,60)
      self.trig_button11.setFont(self.font2)

      self.trig_button12=QPushButton("sec⁻¹θ")
      self.trig_button12.setFixedSize(100,60)
      self.trig_button12.setFont(self.font2)

      self.degree_button=QPushButton("degree(θ°)")
      self.radian_button=QPushButton("radian(θᶜ)")

      self.trig_layout2.addWidget(self.trig_button1,0,0)
      self.trig_layout2.addWidget(self.trig_button2,0,1)
      self.trig_layout2.addWidget(self.trig_button3,0,2)
      self.trig_layout2.addWidget(self.trig_button4,1,0)  
      self.trig_layout2.addWidget(self.trig_button5,1,1)  
      self.trig_layout2.addWidget(self.trig_button6,1,2)
      self.trig_layout2.addWidget(self.trig_button7,2,0)
      self.trig_layout2.addWidget(self.trig_button8,2,1)
      self.trig_layout2.addWidget(self.trig_button9,2,2)
      self.trig_layout2.addWidget(self.trig_button10,3,0)  
      self.trig_layout2.addWidget(self.trig_button11,3,1)  
      self.trig_layout2.addWidget(self.trig_button12,3,2) 

      self.vertical_line = QLabel()
      self.vertical_line.setText(" | | | \n | | | \n | | | \n | | | \n | | | \n | | | \n | | | \n | | | \n | | | \n | | | \n | | | \n | | | \n | | | \n | | | \n | | | \n | | | \n | | | \n | | | \n | | | \n | | | \n")   
      self.trig_layout2.addWidget(self.vertical_line,0,3,4,1) 

      self.num_button1 = QPushButton("7")
      self.num_button1.setFixedSize(85,60)
      self.num_button1.setFont(self.font3)  

      self.num_button2 =QPushButton("8")
      self.num_button2.setFixedSize(85,60)
      self.num_button2.setFont(self.font3)

      self.num_button3 =QPushButton("9")
      self.num_button3.setFixedSize(85,60)
      self.num_button3.setFont(self.font3)

      self.num_button4 =QPushButton("4")
      self.num_button4.setFixedSize(85,60)
      self.num_button4.setFont(self.font3)

      self.num_button5 =QPushButton("5")
      self.num_button5.setFixedSize(85,60)
      self.num_button5.setFont(self.font3)

      self.num_button6 =QPushButton("6")
      self.num_button6.setFixedSize(85,60)
      self.num_button6.setFont(self.font3)

      self.num_button7 =QPushButton("1")
      self.num_button7.setFixedSize(85,60)
      self.num_button7.setFont(self.font3)

      self.num_button8 =QPushButton("2")
      self.num_button8.setFixedSize(85,60)
      self.num_button8.setFont(self.font3)

      self.num_button9 =QPushButton("3")
      self.num_button9.setFixedSize(85,60)
      self.num_button9.setFont(self.font3)

      self.num_button10 =QPushButton("0")
      self.num_button10.setFixedSize(85,60)
      self.num_button10.setFont(self.font3)   

      self.num_button11 =QPushButton(".")
      self.num_button11.setFixedSize(85,60)
      self.num_button11.setFont(self.font3)

      self.num_button12 =QPushButton("-")
      self.num_button12.setFixedSize(85,60)
      self.num_button12.setFont(self.font3)        

      self.num_button13 =QPushButton("𝝅")
      self.num_button13.setFixedSize(100,150)
      self.num_button13.setFont(self.font3)  

      self.num_button14 =QPushButton("C")
      self.num_button14.setFixedSize(100,60)
      self.num_button14.setFont(self.font3)  

      self.num_button15 =QPushButton("=")
      self.num_button15.setFixedSize(100,60)
      self.num_button15.setFont(self.font3)   

      self.num_button16 =QPushButton("/")
      self.num_button16.setFixedSize(85,60)
      self.num_button16.setFont(self.font3)   

      self.trig_layout2.addWidget(self.input_box2,0,6,1,3)
      self.trig_layout2.addWidget(self.trig_status,0,5,1,1)
      self.trig_layout2.addWidget(self.degree_radian,0,9,1,2)
      #self.trig_layout2.addWidget(self.radian_button,4,0)
      #self.trig_layout2.addWidget(self.degree_button,4,1)

      self.trig_layout2.addWidget(self.num_button16,1,5)
      self.trig_layout2.addWidget(self.num_button1,1,6)
      self.trig_layout2.addWidget(self.num_button2,1,7)
      self.trig_layout2.addWidget(self.num_button3,1,8)
      self.trig_layout2.addWidget(self.num_button10,4,7)
      self.trig_layout2.addWidget(self.num_button4,2,6)
      self.trig_layout2.addWidget(self.num_button5,2,7)
      self.trig_layout2.addWidget(self.num_button6,2,8)
      self.trig_layout2.addWidget(self.num_button12,4,8)
      self.trig_layout2.addWidget(self.num_button7,3,6)
      self.trig_layout2.addWidget(self.num_button8,3,7)
      self.trig_layout2.addWidget(self.num_button9,3,8)
      self.trig_layout2.addWidget(self.num_button11,4,6)
      self.trig_layout2.addWidget(self.num_button14,1,9,1,2)
      self.trig_layout2.addWidget(self.num_button13,2,9,2,2)
      self.trig_layout2.addWidget(self.num_button15,4,9,1,2)      

      self.trig_layout.addLayout(self.trig_layout2)

   def control2(self):
      self.num_button1.clicked.connect(partial(self.expression_maker,"7"))
      self.num_button2.clicked.connect(partial(self.expression_maker,"8"))
      self.num_button3.clicked.connect(partial(self.expression_maker,"9"))
      self.num_button4.clicked.connect(partial(self.expression_maker,"4"))
      self.num_button5.clicked.connect(partial(self.expression_maker,"5"))
      self.num_button6.clicked.connect(partial(self.expression_maker,"6"))
      self.num_button7.clicked.connect(partial(self.expression_maker,"1"))
      self.num_button8.clicked.connect(partial(self.expression_maker,"2"))
      self.num_button9.clicked.connect(partial(self.expression_maker,"3"))
      self.num_button10.clicked.connect(partial(self.expression_maker,"0"))
      self.num_button13.clicked.connect(partial(self.expression_maker,"𝝅"))
      self.num_button12.clicked.connect(partial(self.expression_maker,"-"))
      self.num_button11.clicked.connect(partial(self.expression_maker,"."))

      self.trig_button1.clicked.connect(partial(self.trigo_brain,"tanθ"))
      self.trig_button2.clicked.connect(partial(self.trigo_brain,"sinθ"))
      self.trig_button3.clicked.connect(partial(self.trigo_brain,"cosθ"))
      self.trig_button4.clicked.connect(partial(self.trigo_brain,"cotθ"))
      self.trig_button5.clicked.connect(partial(self.trigo_brain,"cosecθ"))
      self.trig_button6.clicked.connect(partial(self.trigo_brain,"secθ"))
      self.trig_button7.clicked.connect(partial(self.trigo_brain,"tan⁻¹θ"))
      self.trig_button8.clicked.connect(partial(self.trigo_brain,"sin⁻¹θ"))
      self.trig_button9.clicked.connect(partial(self.trigo_brain,"cos⁻¹θ"))
      self.trig_button10.clicked.connect(partial(self.trigo_brain,"cot⁻¹θ"))
      self.trig_button11.clicked.connect(partial(self.trigo_brain,"cosec⁻¹θ"))
      self.trig_button12.clicked.connect(partial(self.trigo_brain,"sec⁻¹θ"))

      self.num_button15.clicked.connect(self.expression_solver)
      self.num_button14.clicked.connect(self.clear_display)      
      
      self.degree_button.clicked.connect(self.radian_to_degree)
      self.radian_button.clicked.connect(self.degree_to_radian)

   def expression_maker(self,button_pressed):
      self.expression_str = self.expression_str + button_pressed
      print(self.expression_str)
      self.input_box2.setText(self.expression_str)

   def trigo_brain(self,button_pressed):
      print(button_pressed)
      if button_pressed == "sinθ":
         self.trig_status.setPixmap(QPixmap("sin.png"))  
         self.trig_function_selected = "sinθ"
      
      if button_pressed == "cosθ":
         self.trig_status.setPixmap(QPixmap("cos.png"))
         self.trig_function_selected = "cosθ"

      if button_pressed == "tanθ":
         self.trig_status.setPixmap(QPixmap("tan.png"))
         self.trig_function_selected = "tanθ"            

      if button_pressed == "secθ":
         self.trig_status.setPixmap(QPixmap("sec.png"))
         self.trig_function_selected = "secθ"

      if button_pressed == "cosecθ":
         self.trig_status.setPixmap(QPixmap("cosec.png"))
         self.trig_function_selected = "cosecθ"

      if button_pressed == "cotθ":
         self.trig_status.setPixmap(QPixmap("cot.png"))
         self.trig_function_selected = "cotθ"

      if button_pressed == "sin⁻¹θ":
         self.trig_status.setPixmap(QPixmap("sin_inverse.png"))  
         self.trig_function_selected = "sin⁻¹θ"

      if button_pressed == "cos⁻¹θ":
         self.trig_status.setPixmap(QPixmap("cos_inverse.png"))
         self.trig_function_selected = "cos⁻¹θ"

      if button_pressed == "tan⁻¹θ":
         self.trig_status.setPixmap(QPixmap("tan_inverse.png"))
         self.trig_function_selected = "tan⁻¹θ"

      if button_pressed == "sec⁻¹θ":
         self.trig_status.setPixmap(QPixmap("sec_inverse.png"))
         self.trig_function_selected = "sec⁻¹θ"

      if button_pressed == "cosec⁻¹θ":
         self.trig_status.setPixmap(QPixmap("cosec_inverse.png"))
         self.trig_function_selected = "cosec⁻¹θ"

      if button_pressed == "cot⁻¹θ":
         self.trig_status.setPixmap(QPixmap("cot_inverse.png"))   
         self.trig_function_selected = "cot⁻¹θ"

   def degree_to_radian(self):
      self.degree_radian.setPixmap(QPixmap("radians"))
      self.degree_or_radian = "radian"
   
   def radian_to_degree(self):
      self.degree_or_radian = "degree"
      self.degree_radian.setPixmap(QPixmap("degree"))

   def keyPressEvent(self,event):
      if event.key() == 16777220 or event.key() == 16777221:
         self.expression_solver()
      if event.key() == 16777216:
         self.clear_display()
   
   def expression_solver(self):
      pass 

   def clear_display(self):
      self.expression_str = ""
      self.input_box2.setText('')
      self.input_box2.setFocus()
      self.trig_status.setPixmap(QPixmap("initial"))  


      
def main():
    calc = QApplication(sys.argv)
    view = Calculator()
    view.show()
    sys.exit(calc.exec_())



if __name__ == '__main__':
    main()

    
