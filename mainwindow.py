import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particula import Particula
from AdministradorParticulas import AdministradorParticulas


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.administradorparticulas= AdministradorParticulas()


        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar)
        self.ui.agregar_final_pushButton_2.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton_2.clicked.connect(self.click_mostrar)
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

    @Slot ()
    def click_agregar(self):
        id=self.ui.id_spinBox.value()
        origen_x=self.ui.origenX_spinBox_2.value()
        origen_y=self.ui.origenY_spinBox_3.value()
        destino_x=self.ui.destinoX_spinBox_4.value()
        destino_y=self.ui.destinoY_spinBox_5.value()
        velocidad=self.ui.velocidad_spinBox_6.value()
        rojo=self.ui.rojo_spinBox_7.value()
        verde=self.ui.verde_spinBox_8.value()
        azul=self.ui.azul_spinBox_9.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, rojo, verde, azul)
        self.administradorparticulas.agregar_final(particula)

    @Slot ()
    def click_agregar_inicio(self):
        id=self.ui.id_spinBox.value()
        origen_x=self.ui.origenX_spinBox_2.value()
        origen_y=self.ui.origenY_spinBox_3.value()
        destino_x=self.ui.destinoX_spinBox_4.value()
        destino_y=self.ui.destinoY_spinBox_5.value()
        velocidad=self.ui.velocidad_spinBox_6.value()
        rojo=self.ui.rojo_spinBox_7.value()
        verde=self.ui.verde_spinBox_8.value()
        azul=self.ui.azul_spinBox_9.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, rojo, verde, azul)
        self.administradorparticulas.agregar_inicio(particula)
    
    @Slot () 
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.administradorparticulas))
    
    @Slot ()
    def action_abrir_archivo(self):
        #print ("abrir")
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        self.administradorparticulas.abrir(ubicacion)
    
    """@Slot()
    def action_abrir_archivo(self):
        ubicacion, _ = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )
        if not ubicacion:
            print("No se seleccionó archivo")
            return

        resultado = self.administradorparticulas.abrir(ubicacion)
        print("Resultado abrir:", resultado)
        """

    @Slot ()
    def action_guardar_archivo(self):
        #print ("guardar")
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print (ubicacion)
        if self.administradorparticulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo" + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "NO se pudo guardar el archivo en " + ubicacion
            )



    

       

