# Листинг программы

from tkinter import *
import math

class Calculator(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self): 
        def sin():
            # в радианах
            label['text']+='math.sin('
        
        def sin_m_one():
            # в радианах
            label['text']+='math.asin('
        
        def pi():
            label['text']+='pi'

        def factorial_b():
            label['text']+='fact('
        
        def cos():
            label['text']+='math.cos('

        def cos_m_one():
            label['text']+='math.acos('
        
        def exp():
            label['text']+='exp('

        def degree_two():
            label['text']+='^2'

        def tan():
            label['text']+='math.tan('

        def tan_m_one_f():
            label['text']+='math.atan('

        def ln():
            label['text']+='ln('

        def degree_three():
            label['text']+='^3'

        def sinh():
            label['text']+='math.sinh('

        def sinh_m_one():
            label['text']+='math.asinh('

        def log():
            label['text']+='log('

        def y_degree_x():
            label['text']+='^'
            if (label['text'] == ''):
                label['text']='0^'

        def cosh():
            label['text']+='math.cosh('

        def cosh_m_one():
            label['text']+='math.acosh('
        
        def y_degree_log_X():
            label['text']+='log('

        def root_of_x():
            label['text']+='sqrt('

        def tanh():
            label['text']+='math.tanh('

        def tanh_m_one():
            label['text']+='math.atanh('
        
        def x_degree_ten():
            label['text']+='^10'

        def y_degree_root_of_x_f():
            label['text']+='yrootx('

        def backspace():
            if (label['text'] == ''):
                label['text']='0'
                return
            s=list(label['text'])
            s.pop(len(label['text'])-1)
            label['text']=label['text'].replace('00', '0')
            label['text']="".join(s)

        def all_clear():
            label['text']=''

        def abs():
            label['text']+='abs('
        def mod():
            label['text']+='mod'
        
        def equal():
            flag=0
            result=''
            for i in range(len(label['text'])):
                if (label['text'][i] == 'n'):
                    flag=1
            label['text']=label['text'].replace('yrootx', 'math.pow')
            strs=list(label['text'])
            for i in range(len(strs)):
                if(strs[i] == ','):
                    strs[i+1]='1/'+strs[i+1]
            strs="".join(strs)
            strs=str(strs)
            label['text']=strs
            if (label['text'][0].isdigit() == False and len(label['text']) <= 4):
                result='0'
            label['text']=label['text'].replace('mod', '%')
            label['text']=label['text'].replace('^', '**')
            label['text']=label['text'].replace('pi', 'math.pi')
            label['text']=label['text'].replace('fact', 'math.factorial')
            label['text']=label['text'].replace('exp', 'math.exp')
            if (flag == 1):
                label['text']=label['text'].replace('ln', 'math.log')
            else:
                label['text']=label['text'].replace('log', 'math.log')
            label['text']=label['text'].replace('sqrt', 'math.sqrt')
            result=eval(str(label['text']))
            label['text']=result

        def plus_minus():
            if (label['text'] == ''):
                label['text']='+'
            elif (label['text'][0] == '+'):
                label['text']='-' + label['text']
            elif (label['text'][0] == '-'):
                label['text']='+' + label['text']
            label['text']=label['text'].replace('-+', '-')
            label['text']=label['text'].replace('+-', '+')
            return

        def left_bracket():
            label['text']+='('
            if (label['text'][len(label['text'])-1] == '-'):
                return
            if (label['text'][len(label['text'])-1] == '+'):
                return
            if (label['text'][len(label['text'])-1] == '*'):
                return
            if (label['text'][len(label['text'])-1] == '/'):
                return
            if (label['text'][len(label['text'])-1] == ','):
                return

        def comma():
            if (label['text'] == ''):
                return
            if (label['text'][len(label['text'])-1] == '-'):
                return
            if (label['text'][len(label['text'])-1] == '+'):
                return
            if (label['text'][len(label['text'])-1] == '*'):
                return
            if (label['text'][len(label['text'])-1] == '/'):
                return
            if (label['text'][len(label['text'])-1] == '('):
                return
            if (label['text'][len(label['text'])-1] == ')'):
                return
            label['text']+=','
            label['text']=label['text'].replace(',,', ',')

        def right_bracket():
            label['text']+=')'
            if (label['text'][len(label['text'])-1] == '-'):
                return
            elif (label['text'][len(label['text'])-1] == '+'):
                return
            elif (label['text'][len(label['text'])-1] == '*'):
                return
            elif (label['text'][len(label['text'])-1] == '/'):
                return
            elif (label['text'][len(label['text'])-1] == ','):
                return

        def divide():
            if (label['text'] == ''):
                return
            if (label['text'][len(label['text'])-1] == '-'):
                return
            if (label['text'][len(label['text'])-1] == '+'):
                return
            if (label['text'][len(label['text'])-1] == '*'):
                return
            if (label['text'][len(label['text'])-1] == '/'):
                return
            label['text']+='/'

        def multiply():
            if (label['text'] == ''):
                return
            if (label['text'][len(label['text'])-1] == '-'):
                return
            if (label['text'][len(label['text'])-1] == '+'):
                return
            if (label['text'][len(label['text'])-1] == '*'):
                return
            if (label['text'][len(label['text'])-1] == '/'):
                return
            label['text']+='*'

        def minus():
            if (label['text'][len(label['text'])-1] == '-'):
                return
            if (label['text'][len(label['text'])-1] == '+'):
                return
            if (label['text'][len(label['text'])-1] == '*'):
                return
            if (label['text'][len(label['text'])-1] == '/'):
                return
            label['text']+='-'

        def plus():
            if (label['text'][len(label['text'])-1] == '-'):
                return
            if (label['text'][len(label['text'])-1] == '+'):
                return
            if (label['text'][len(label['text'])-1] == '*'):
                return
            if (label['text'][len(label['text'])-1] == '/'):
                return
            label['text']+='+'

        def dot():
            label['text']+='.'

        def number_zero():
            flag=0
            label['text']+='0'
            for i in range(len(label['text'])):
                if (label['text'][i] == '.'):
                    flag=1
            if (flag != 1):
                label['text']=label['text'].replace('00', '0')

        def number_one():
            label['text']+='1'

        def number_two():
            label['text']+='2'

        def number_three():
            label['text']+='3'

        def number_four():
            label['text']+='4'

        def number_five():
            label['text']+='5'

        def number_six():
            label['text']+='6'

        def number_seven():
            label['text']+='7'

        def number_eight():
            label['text']+='8'

        def number_nine():
            label['text']+='9'

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)
        self.columnconfigure(4, pad=3)
        self.columnconfigure(5, pad=3)
        self.columnconfigure(6, pad=3)
        self.columnconfigure(7, pad=3)
        self.columnconfigure(8, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        self.rowconfigure(5, pad=3)
        self.rowconfigure(6, pad=3)
        self.rowconfigure(7, pad=3)

        label= Label(self, bg='black', fg='white')
        label.grid(row=1, columnspan=9, sticky=W+E, padx=5, pady=5)
        sin_button=Button(self, text='sin', width=5, command=sin)
        sin_button.grid(row=2, column=0)
        sin_m_one_button=Button(self, text='sin^-1', width=5, command=sin_m_one)
        sin_m_one_button.grid(row=2, column=1)
        pi_button=Button(self, text='π', width=5, command=pi)
        pi_button.grid(row=2, column=2)
        factorial_button=Button(self, text='n!', width=5, command=factorial_b)
        factorial_button.grid(row=2, column=3)
        cos_button=Button(self, text='cos', width=5, command=cos)
        cos_button.grid(row=3, column=0)
        cos_m_one__button=Button(self, text='cos^-1', width=5, command=cos_m_one)
        cos_m_one__button.grid(row=3, column=1)
        exp_button=Button(self, text='exp', width=5, command=exp)
        exp_button.grid(row=3, column=2)
        degree_two_x_button=Button(self, text='x^2', width=5, command=degree_two)
        degree_two_x_button.grid(row=3, column=3)
        left_bracket_button=Button(self, text='(', width=5, command=left_bracket)
        left_bracket_button.grid(row=3, column=4)
        comma_button=Button(self, text=',', width=5, command=comma)
        comma_button.grid(row=3, column=5)
        right_bracket_button=Button(self, text=')', width=5, command=right_bracket)
        right_bracket_button.grid(row=3, column=6)
        backspace_button=Button(self, text='<--', width=5, command=backspace)
        backspace_button.grid(row=3, column=7)
        all_clear_button=Button(self, text='AC', width=5, command=all_clear)
        all_clear_button.grid(row=3, column=8)
        tan_button=Button(self, text='tan', width=5, command=tan)
        tan_button.grid(row=4, column=0)
        tan_m_one=Button(self, text='tan^-1', width=5, command=tan_m_one_f)
        tan_m_one.grid(row=4, column=1)
        ln_button=Button(self, text='ln', width=5, command=ln)
        ln_button.grid(row=4, column=2)
        degree_three_x_button=Button(self, text='x^3', width=5, command=degree_three)
        degree_three_x_button.grid(row=4, column=3)
        sinh_button=Button(self, text='sinh', width=5, command=sinh)
        sinh_button.grid(row=5, column=0)
        sinh_m_one_button=Button(self, text='sinh^-1', width=5, command=sinh_m_one)
        sinh_m_one_button.grid(row=5, column=1)
        log_button=Button(self, text='log', width=5, command=log)
        log_button.grid(row=5, column=2)
        degree_y_x_button=Button(self, text='x^y', width=5, command=y_degree_x)
        degree_y_x_button.grid(row=5, column=3)
        cosh_button=Button(self, text='cosh', width=5, command=cosh)
        cosh_button.grid(row=6, column=0)
        cosh_m_one_button=Button(self, text='cosh^-1', width=5, command=cosh_m_one)
        cosh_m_one_button.grid(row=6, column=1)
        log_y_X_button=Button(self, text='log^y X', width=5, command=y_degree_log_X)
        log_y_X_button.grid(row=6, column=2)
        root_of_x_button=Button(self, text='√x', width=5, command=root_of_x)
        root_of_x_button.grid(row=6, column=3)
        tanh_button=Button(self, text='tanh', width=5, command=tanh)
        tanh_button.grid(row=7, column=0)
        tanh_m_one_button=Button(self, text='tanh^-1', width=5, command=tanh_m_one)
        tanh_m_one_button.grid(row=7, column=1)
        x_degree_of_ten_button=Button(self, text='10^x', width=5, command=x_degree_ten)
        x_degree_of_ten_button.grid(row=7, column=2)
        y_degree_root_of_x=Button(self, text='y√x', width=5, command=y_degree_root_of_x_f)
        y_degree_root_of_x.grid(row=7, column=3)
        abs_button=Button(self, text='abs', width=5, command=abs)
        abs_button.grid(row=4, column=8)
        mod_button=Button(self, text='mod', width=5, command=mod)
        mod_button.grid(row=5, column=8)
        equal_button=Button(self, text='=', width=5, command=equal)
        equal_button.grid(row=6, column=8)
        plus_button=Button(self, text='+', width=5, command=plus)
        plus_button.grid(row=7, column=7)
        minus_button=Button(self, text='-', width=5, command=minus)
        minus_button.grid(row=6, column=7)
        divide_button=Button(self, text='/', width=5, command=divide)
        divide_button.grid(row=4, column=7)
        multiply_button=Button(self, text='*', width=5, command=multiply)
        multiply_button.grid(row=5, column=7)
        plus_minus_on_button=Button(self, text='+/-', width=5, command=plus_minus)
        plus_minus_on_button.grid(row=7, column=6)
        dot_button=Button(self, text='.', width=5, command=dot)
        dot_button.grid(row=7, column=5)
        one_button=Button(self, text='1', width=5, command=number_one)
        one_button.grid(row=6, column=4)
        two_button=Button(self, text='2', width=5, command=number_two)
        two_button.grid(row=6, column=5)
        three_button=Button(self, text='3', width=5, command=number_three)
        three_button.grid(row=6, column=6)
        four_button=Button(self, text='4', width=5, command=number_four)
        four_button.grid(row=5, column=4)
        five_button=Button(self, text='5', width=5, command=number_five)
        five_button.grid(row=5, column=5)
        six_button=Button(self, text='6', width=5, command=number_six)
        six_button.grid(row=5, column=6)
        seven_button=Button(self, text='7', width=5, command=number_seven)
        seven_button.grid(row=4, column=4)
        eight_button=Button(self, text='8', width=5, command=number_eight)
        eight_button.grid(row=4, column=5)
        nine_button=Button(self, text='9', width=5, command=number_nine)
        nine_button.grid(row=4, column=6)
        zero_button=Button(self, text='0', width=5, command=number_zero)
        zero_button.grid(row=7, column=4)

        self.pack()
strs=''
window = Tk()
calculator0=Calculator()
window.mainloop()