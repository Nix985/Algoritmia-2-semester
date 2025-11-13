#pyside6-uic mainwindow.ui > ui_mainwindow.py 
#se utiliza cada vez que vamos a editar la interfaz grafica que vemos con qt
from PySide6.QtWidgets import QMainWindow, QApplication
from mainwindow import MainWindow
import sys

app= QApplication()
window = MainWindow()
window.show()
#button = QPushButton('Hola')
# Se hace visible el botón
#button.show()
#Qt loop
sys.exit(app.exec())