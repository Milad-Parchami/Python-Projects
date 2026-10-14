import math
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Calculator import Ui_Form

class CalculatorApp(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.first_num = 0      
        self.operator = ""      
        self.new_input = True   

        self.connect_buttons()

    def connect_buttons(self):

        self.b1.clicked.connect(lambda: self.digit_clicked(1))      
        self.b2.clicked.connect(lambda: self.digit_clicked(2))
        self.b3.clicked.connect(lambda: self.digit_clicked(3))
        self.b4.clicked.connect(lambda: self.digit_clicked(4))
        self.b5.clicked.connect(lambda: self.digit_clicked(5))
        self.b6.clicked.connect(lambda: self.digit_clicked(6))
        self.b7.clicked.connect(lambda: self.digit_clicked(7))
        self.b8.clicked.connect(lambda: self.digit_clicked(8))
        self.b9.clicked.connect(lambda: self.digit_clicked(9))
        self.b10.clicked.connect(lambda: self.digit_clicked(0))

        self.b11.clicked.connect(lambda: self.operator_clicked("+"))
        self.b12.clicked.connect(lambda: self.operator_clicked("-"))
        self.b13.clicked.connect(lambda: self.operator_clicked("*"))
        self.b14.clicked.connect(lambda: self.operator_clicked("/"))
        self.b18.clicked.connect(lambda: self.operator_clicked("%"))
        self.b19.clicked.connect(lambda: self.operator_clicked("Pi"))
        self.b20.clicked.connect(lambda: self.operator_clicked("^"))
        self.b21.clicked.connect(lambda: self.operator_clicked("sqrt"))
        self.b22.clicked.connect(lambda: self.operator_clicked("log"))
        self.b23.clicked.connect(lambda: self.operator_clicked("sin"))
        self.b24.clicked.connect(lambda: self.operator_clicked("cos"))
        self.b25.clicked.connect(lambda: self.operator_clicked("tan"))
        self.b27.clicked.connect(lambda: self.operator_clicked("1/x"))
        self.b28.clicked.connect(lambda: self.operator_clicked("X!"))
        self.b29.clicked.connect(lambda: self.operator_clicked("e"))
       
       
        self.b26.clicked.connect(self.add_decimal)
        self.b17.clicked.connect(self.alamat)
        self.b15.clicked.connect(self.calculate)   
        self.b16.clicked.connect(self.clear_all)  

    def digit_clicked(self, digit):
        if self.new_input == True:
            self.input1.setText(str(digit))
            self.new_input = False  
        else:
            current_text = self.input1.text()
            self.input1.setText(current_text + str(digit))

    def operator_clicked(self, op):
        try:
            self.first_num = float(self.input1.text())
           
            self.operator = op
           
            self.new_input = True
        except ValueError:
            self.input1.setText("Error")

    def calculate(self):
        try:
            second_num = float(self.input1.text())

            if self.operator == "+":
                result = self.first_num + second_num
            elif self.operator == "-":
                result = self.first_num - second_num
            elif self.operator == "*":
                result = self.first_num * second_num
            elif self.operator == "%":
                result = self.first_num / 100
            elif self.operator == "^":
                result = math.pow(self.first_num,second_num)
            elif self.operator == "Pi":
                result = self.first_num * math.pi
            elif self.operator == "sqrt":
                result = math.sqrt(self.first_num)
            elif self.operator == "log":
                result = math.log10(self.first_num)
            elif self.operator == "sin":
                result = math.sin(math.radians(self.first_num))
            elif self.operator == "cos":
                result = math.cos(math.radians(self.first_num))
            elif self.operator == "tan":
                result = math.tan(math.radians(self.first_num))
            elif self.operator == "1/x":
                result = 1 / self.first_num
            elif self.operator == "X!":
                result = math.factorial(self.first_num)
            elif self.operator == "e":
                result = self.first_num * math.e
            elif self.operator == "/":
                if second_num == 0:
                    self.input1.setText("Cannot divide by zero")
                    return
                result = self.first_num / second_num
            else:


                result = second_num

            self.input1.setText(str(result))
            self.first_num = result
            self.new_input = True

        except ValueError:
            self.input1.setText("Error")

    def clear_all(self):
        self.input1.clear()     
        self.first_num = 0      
        self.operator = ""       
        self.new_input = True    

    def alamat(self):
       
            a_text = self.input1.text()

            if a_text == "" or a_text == "0":
                return

            a_num  = int(a_text)
        
            b = a_num * -1

            self.input1.setText(str(b))
    
    def add_decimal(self):
        num =self.input1.text()

        if num == "":
            self.input1.setText("0.")
            self.new_input = False
            return
          
        if "." in num :
            return

        self.input1.setText(num + ".")
        self.new_input = False

            




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())