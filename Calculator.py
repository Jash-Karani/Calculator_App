import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget
from functools import partial
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
        self.menu.addAction('Exit', self.close)
        self.menu.addAction('Help',self.help)
    
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
      super().__init__()
      self.setWindowTitle('Trigo calculator')
      self.trig_layout = QVBoxLayout()
      self.setFixedSize(400,400)
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
      self.font2.setPointSize(12)             
      self.input_box2.setFont(self.font2)
      self.input_box2.setAlignment(Qt.AlignLeft)
      self.input_box2.isReadOnly()
      self.trig_layout.addWidget(self.input_box2)
   
   def button_create2(self):
      self.trig_layout2 = QGridLayout()
      
      self.trig_button1 =QPushButton("tan\u03B8")
      self.trig_button1.setFixedSize(100,60)
      self.trig_button1.setFont(self.font2)

      self.trig_button2 =QPushButton("sin\u03B8")
      self.trig_button2.setFixedSize(100,60)
      self.trig_button2.setFont(self.font2)

      self.trig_button3 =QPushButton("cos\u03B8")
      self.trig_button3.setFixedSize(100,60)
      self.trig_button3.setFont(self.font2)

      self.trig_button4 =QPushButton("cot\u03B8")
      self.trig_button4.setFixedSize(100,60)
      self.trig_button4.setFont(self.font2)

      self.trig_button5 =QPushButton("cosec\u03B8")
      self.trig_button5.setFixedSize(100,60)
      self.trig_button5.setFont(self.font2)

      self.trig_button6 =QPushButton("sec\u03B8")
      self.trig_button6.setFixedSize(100,60)
      self.trig_button6.setFont(self.font2)

      self.trig_button7 =QPushButton("tan⁻¹\u03B8")
      self.trig_button7.setFixedSize(100,60)
      self.trig_button7.setFont(self.font2)

      self.trig_button8 =QPushButton("sin⁻¹\u03B8")
      self.trig_button8.setFixedSize(100,60)
      self.trig_button8.setFont(self.font2)

      self.trig_button9 =QPushButton("cos⁻¹\u03B8")
      self.trig_button9.setFixedSize(100,60)
      self.trig_button9.setFont(self.font2)

      self.trig_button10 =QPushButton("cot⁻¹\u03B8")
      self.trig_button10.setFixedSize(100,60)
      self.trig_button10.setFont(self.font2)

      self.trig_button11 =QPushButton("cosec⁻¹\u03B8")
      self.trig_button11.setFixedSize(100,60)
      self.trig_button11.setFont(self.font2)

      self.trig_button12=QPushButton("sec⁻¹\u03B8")
      self.trig_button12.setFixedSize(100,60)
      self.trig_button12.setFont(self.font2)

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

      
      self.trig_layout.addLayout(self.trig_layout2)

   def control2(self):
      pass


def main():
    calc = QApplication(sys.argv)
    view = Calculator()
    view.show()
    sys.exit(calc.exec_())



if __name__ == '__main__':
    main()

    
