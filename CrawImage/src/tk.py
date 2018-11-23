#!-*-coding=utf-8-*-

from tkinter import *
import tkinter as tk
import os

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    on_hit = False
    hit_count = 0
    def hit_me(self):
        # global on_hit
        if self.on_hit == False:
            self.on_hit = True
            self.hit_count += 1
        else:
            self.on_hit = False
            self.hit_count += 1

        if self.hit_count == 1:
            self.stringVar.set("爱我")
        elif self.hit_count == 2:
            self.stringVar.set("还是爱我")
        elif self.hit_count == 3:
            self.stringVar.set("你逃不掉的！！！")
        elif self.hit_count == 4:
            self.stringVar.set("看见中间那个框了吗，给你个机会。。。")
            self.buttonVar.set("写嘛写嘛")

            self.e = Entry(self, show=None, 
                highlightcolor="blue", highlightthickness=2,
                fg="black", relief=SUNKEN)
            self.e.pack()

            self.sureButton = Button(self, text="点我确认", 
                width=15, height=2, command=self.sureAction)
            self.sureButton.pack()

            self.textInsert = Text(self, height=2)
            self.textInsert.pack()

            # if os.path.exists("aiwo.png"):
            #     self.photo = PhotoImage(file='aiwo.png')
                


    def sureAction(self):
        self.stringVar.set("不能反悔了啊！")
        var = self.e.get()
        var = "你输入什么都不管用的，对不起我也爱你！"
        self.textInsert.insert('end', var)
        self.e.delete(0, END)
        self.e.insert(END, "我爱你")
        self.e.pack()

    def createWidgets(self):

        self.stringVar = StringVar()
        self.stringVar.set("说你爱我")

        self.buttonVar = StringVar()
        self.buttonVar.set("点我")

        # self.helloLabel = Label(self, textvariable=self.stringVar, bg='orange',
        #     width=30, height=3)
        # self.helloLabel.pack()
        self.quitButton = Button(self, textvariable=self.buttonVar, 
            command=self.hit_me, width=30, height=3)
        self.quitButton.pack()

        image_path = "xiaomei.png"
        if os.path.exists(image_path):
            self.background = PhotoImage(file=image_path)
            self.backLabel = Label(self, textvariable=self.stringVar, 
                justify=CENTER, image=self.background,
                compound=CENTER, fg='red', font=("华文行楷", 30))
            self.backLabel.pack()
        else:
            self.backLabel = Label(self, textvariable=self.stringVar, 
                justify=CENTER, compound=CENTER, fg='red', font=("华文行楷", 30))
            self.backLabel.pack()
        
        # self.background.pack()

if __name__ == '__main__':

    app = Application()
    # 设置窗口标题:
    app.master.title('大哥 大哥，说你爱我！')
    app.master.geometry('1200x800')
    # 主消息循环:
    app.mainloop()










