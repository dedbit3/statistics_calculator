import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton

#creation of app instance
app = QApplication(sys.argv)

#GUI creation

window = QWidget()
window.setWindowTitle("Stats Calculator")

#this sets x, y, width, height
window.setGeometry(700, 700, 580, 300)

#displaying messges in GUI
helloMsg = QLabel("<h1>Select the Following Calculations</h1>", parent=window)
helloMsg.move(100, 40)

#functions for handling actions
def clickT():
    Twindow = QWidget()
    Twindow.setWindowTitle("T-Statistic")

#button for different functions and menus
tButton = QPushButton(parent=window, text="T statistic")
tButton.move(80, 100)
tButton.clicked.connect(clickT)

#showing window
window.show()
sys.exit(app.exec())


