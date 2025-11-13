# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(549, 524)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.destinoX_spinBox_4 = QSpinBox(self.groupBox)
        self.destinoX_spinBox_4.setObjectName(u"destinoX_spinBox_4")
        self.destinoX_spinBox_4.setMaximum(255)

        self.gridLayout.addWidget(self.destinoX_spinBox_4, 3, 2, 1, 1)

        self.verde_spinBox_8 = QSpinBox(self.groupBox)
        self.verde_spinBox_8.setObjectName(u"verde_spinBox_8")
        self.verde_spinBox_8.setMaximum(255)

        self.gridLayout.addWidget(self.verde_spinBox_8, 7, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 2)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 8, 0, 1, 2)

        self.destinoY_spinBox_5 = QSpinBox(self.groupBox)
        self.destinoY_spinBox_5.setObjectName(u"destinoY_spinBox_5")
        self.destinoY_spinBox_5.setMaximum(255)

        self.gridLayout.addWidget(self.destinoY_spinBox_5, 4, 2, 1, 1)

        self.id_spinBox = QSpinBox(self.groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")
        self.id_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.id_spinBox, 0, 2, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.azul_spinBox_9 = QSpinBox(self.groupBox)
        self.azul_spinBox_9.setObjectName(u"azul_spinBox_9")
        self.azul_spinBox_9.setMaximum(255)

        self.gridLayout.addWidget(self.azul_spinBox_9, 8, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 2)

        self.origenX_spinBox_2 = QSpinBox(self.groupBox)
        self.origenX_spinBox_2.setObjectName(u"origenX_spinBox_2")
        self.origenX_spinBox_2.setMaximum(255)

        self.gridLayout.addWidget(self.origenX_spinBox_2, 1, 2, 1, 1)

        self.origenY_spinBox_3 = QSpinBox(self.groupBox)
        self.origenY_spinBox_3.setObjectName(u"origenY_spinBox_3")
        self.origenY_spinBox_3.setMaximum(255)

        self.gridLayout.addWidget(self.origenY_spinBox_3, 2, 2, 1, 1)

        self.rojo_spinBox_7 = QSpinBox(self.groupBox)
        self.rojo_spinBox_7.setObjectName(u"rojo_spinBox_7")
        self.rojo_spinBox_7.setMaximum(255)

        self.gridLayout.addWidget(self.rojo_spinBox_7, 6, 2, 1, 1)

        self.mostrar_pushButton_2 = QPushButton(self.groupBox)
        self.mostrar_pushButton_2.setObjectName(u"mostrar_pushButton_2")

        self.gridLayout.addWidget(self.mostrar_pushButton_2, 12, 0, 1, 3)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 2)

        self.agregar_inicio_pushButton = QPushButton(self.groupBox)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.gridLayout.addWidget(self.agregar_inicio_pushButton, 10, 0, 1, 3)

        self.velocidad_spinBox_6 = QSpinBox(self.groupBox)
        self.velocidad_spinBox_6.setObjectName(u"velocidad_spinBox_6")
        self.velocidad_spinBox_6.setMaximum(255)

        self.gridLayout.addWidget(self.velocidad_spinBox_6, 5, 2, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 7, 0, 1, 2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 2)

        self.agregar_final_pushButton_2 = QPushButton(self.groupBox)
        self.agregar_final_pushButton_2.setObjectName(u"agregar_final_pushButton_2")

        self.gridLayout.addWidget(self.agregar_final_pushButton_2, 9, 0, 1, 3)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.salida = QPlainTextEdit(self.centralwidget)
        self.salida.setObjectName(u"salida")

        self.gridLayout_2.addWidget(self.salida, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 549, 33))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen X:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino X:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Azul:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Destino Y:", None))
        self.mostrar_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Rojo:", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Verde:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen Y:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.agregar_final_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

