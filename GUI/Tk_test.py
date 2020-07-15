from tkinter import *
import tkinter.messagebox as messagebox
from tkinter.messagebox import showerror, showinfo, showwarning
from functools import partial as pto
# 在GUI中，每个Button、Label、输入框等，都是一个Widget。
# Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
# pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # self.pack()
        self.grid(column=0, row=0, stick='nsew')
        self.createWidget()
        

    # 创建窗口小部件
    def createWidget(self):
        self.helloLabel = Label(self, text='一伤二十八')
        self.helloLabel.pack(fill=Y, expand=0)
        # self.helloLabel.grid(row=0)
        # 滑块，控制hellolabel的字体大小
        self.scale = Scale(self, from_=10, to=40, orient=HORIZONTAL, command=self.resize)
        self.scale.set(12)
        self.scale.pack(fill=X, expand=1)
        # self.scale.grid(row=1)

        self.nameInput = Entry(self)
        self.nameInput.pack(fill=X,expand=1, side=LEFT)
        # self.nameInput.grid(row=2)

        self.alertbutton = Button(self, text='Hello', command=self.greet)
        self.alertbutton.pack()
        # 网格型，2行
        # self.alertbutton.grid(row=2, column=1)

        self.quitButton = Button(self, text='Quit', bg='white', fg='red', command=self.quit)
        # 填充x轴可视界面
        self.quitButton.pack(fill=X, expand=0)
        # self.quitButton.grid(row=3)

    def resize(self, ev=None):
        self.helloLabel.config(font='Hevtica -%d bold'%self.scale.get())
    def greet(self):
        name = self.nameInput.get() or 'World'
        messagebox.showinfo("Message", 'Hello %s' % name)


class RoadSign(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createButton()

    def createButton(self):
        CRIT = 'crit'
        WARN = 'warn'
        REGU = 'regu'
        SIGNS = {
            'do not enter': CRIT,
            'railroad crossing': WARN,
            '55\nspeed limit': REGU,
            'wrong way': CRIT,
            'merging traffic': WARN,
            'one way': REGU,
        }
        critCB = lambda:showerror('Error', 'Error Button Pressed')
        warnCB = lambda:showwarning('Warning', 'Warning Button Pressed')
        infoCB = lambda:showinfo('Info', 'Info Button Pressed')
        self.quitButton = Button(self, text='Quit', bg='red', fg='white', command=self.quit)
        self.quitButton.pack()
        # 调用mybutton时，会调用Button类，并将self作为第一个参数传递
        mybutton = pto(Button, self)
        # 二阶偏函数，根据不同类型
        CritButton = pto(mybutton, command=critCB, bg='white', fg='red')
        WarnButton = pto(mybutton, command=warnCB, bg='blue')
        ReguButton = pto(mybutton, command=infoCB, bg='white' )

        for eachSign in SIGNS:
            signType = SIGNS[eachSign]
            cmd = '%sButton(text=%r%s).pack(fill=X, expand=1)'%(signType.title(), eachSign,
                '.upper()'if signType == CRIT else '.title()')
            eval(cmd)


if __name__ == "__main__":

    # app = Application()
    # app.master.title('Author')
    # app.master.columnconfigure(0, weight=1)
    # app.master.rowconfigure(0, weight=1)
    # app.master.geometry('400x300')
    # app.master.maxsize(800, 600)
    # app.mainloop()
    # 主界面
    # top = Tk('111')
    # quit = Button(top, text='quit', command=top.quit)
    # quit.pack()
    # mainloop()
    rs = RoadSign()
    rs.master.title('RoadSign')
    rs.mainloop()
