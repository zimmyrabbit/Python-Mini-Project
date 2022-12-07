import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from pynput import mouse

ui_path = r'분자진단 RPA\test.ui'
form_class = uic.loadUiType(ui_path)[0]

class windowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.pushButton_click)

    def pushButton_click(self) :
        openMouseLisener()
        self.le_view.setText(f'{x1},{y1}')

def openMouseLisener() :
    with mouse.Listener( 
        on_click = setMouseLocation
        ) as listener:
        listener.join()
    

def setMouseLocation(x, y, button, pressed):
    if pressed:
        global x1
        global y1
        x1 = x
        y1 = y
        
    if not pressed :
        return False


if __name__ == '__main__' :
    app = QApplication(sys.argv)
    myWindow = windowClass()
    myWindow.show()
    app.exec_()
