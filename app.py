#qpy:quiet
#-*-coding:utf8;-*-
"""
This is a project which use SL4A UI Framework.
"""
import qpy
import androidhelper
import urllib.request as ur
import sudoku
from qsl4ahelper.fullscreenwrapper2 import *

droid = androidhelper.Android()
size = 9


class MainScreen(Layout):
    pointer = 0
    f = ""
    fcnc = ["." for i in range(size*size)]
    def __init__(self):
        mv = open("mainview.txt")
        super(MainScreen,self).__init__(mv.read(),"SL4AApp")
        mv.close()


    def on_show(self):
        self.views.but1.add_event(click_EventHandler(self.views.but1, self.butnum))
        self.views.but2.add_event(click_EventHandler(self.views.but2, self.butnum))
        self.views.but3.add_event(click_EventHandler(self.views.but3, self.butnum))
        self.views.but4.add_event(click_EventHandler(self.views.but4, self.butnum))
        self.views.but5.add_event(click_EventHandler(self.views.but5, self.butnum))
        self.views.but6.add_event(click_EventHandler(self.views.but6, self.butnum))
        self.views.but7.add_event(click_EventHandler(self.views.but7, self.butnum))
        self.views.but8.add_event(click_EventHandler(self.views.but8, self.butnum))
        self.views.but9.add_event(click_EventHandler(self.views.but9, self.butnum))
        self.views.chetnechet.add_event(click_EventHandler(self.views.chetnechet, self.chet))
        self.views.calculate.add_event(click_EventHandler(self.views.calculate, self.calculate))
        self.views.diag.add_event(click_EventHandler(self.views.diag, self.exit))
        
        for i in range(size):
            for j in range(size):
                exec('self.views.f' + str(i) + 'x' + str(j) + '.add_event(click_EventHandler(self.views.f' + str(i) + 'x' + str(j) + ', self.cell))')
        
        pass

    def on_close(self):
        pass

    def on_page(self):
        droid.makeToast("Load")
        self.orientation = 'horizontal'
        pass

    def load(self, view, dummy):
        droid = FullScreenWrapper2App.get_android_instance()
        droid.makeToast("Load")

        saved_logo = qpy.tmp+"/qpy.logo"
        ur.urlretrieve("https://www.qpython.org/static/img_logo.png", saved_logo)
        self.views.logo.src = "file://"+saved_logo

    def exit(self, view, dummy):
        droid = FullScreenWrapper2App.get_android_instance()
        droid.makeToast("Exit")
        FullScreenWrapper2App.close_layout()

    def butnum(self, view, dummy):
        if self.pointer != 0:
            if eval('self.views.'+self.pointer.id+'.text == self.views.'+view.id+'.text'):
                exec('self.views.'+self.pointer.id+'.text = ""')
            else:
                exec('self.views.'+self.pointer.id+'.text = self.views.'+view.id+'.text')
        
    def chet(self, view, dummy):
        if self.pointer != 0:
            y, x = self.pointer.id.split('f')[1].split('x')
            if self.fcnc[int(x) + int(y)*9] == "*":
                exec('self.views.'+self.pointer.id+'.background = "#ffffffff"')
                self.fcnc[int(x) + int(y)*9] = "."
            else:
                exec('self.views.'+self.pointer.id+'.background = "#ffEFC802"')
                self.fcnc[int(x) + int(y)*9] = "*"
        
        
    def calculate(self, view, dummy):
        exec('droid.makeToast(view.id)')
        self.f = ""
        for i in range(size):
            for j in range(size):
                simbol = eval('self.views.f'+str(i)+'x'+str(j)+'.text')
                if simbol != "":
                    self.f += simbol
                else:
                    self.f += "."
        comb = sudoku.combine(self.f, self.fcnc)
        sudoku.complect()
        solve = sudoku.solve(comb)
        for i in range(size):
            for j in range(size):
                exec('self.views.f'+str(i)+'x'+str(j)+'.text = str(solve[i][j])')
        
    def cell(self, view, dummy):
        self.pointer = view
        
    def diag(self, view, dummy):
        if sudoku.digon:
            sudoku.digon = False
            exec('self.views.'+view.id+'.background = "#ffff0000"')
        else:
            sudoku.digon = True
            exec('self.views.'+view.id+'.background = "#ff00ff00"')
        
        
if __name__ == '__main__':
    FullScreenWrapper2App.initialize(droid)
    FullScreenWrapper2App.show_layout(MainScreen())
    FullScreenWrapper2App.eventloop()
