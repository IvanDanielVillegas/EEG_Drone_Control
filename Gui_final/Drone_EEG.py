import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "Gui_final.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def Actualizar_label_ojos(self,var_estado_switch):
        if var_estado_switch == 0:
            desc1 = "Cerrar el ojo izquierdo"
            desc2 = "para bajar el drone"
            self.label_desc_izq_alt.setText(desc1)
            self.label_desc_izq_fron.setText(desc2)
            desc3 = "Cerrar el ojo derecho"
            desc4 = "para elevar el drone"
            self.label_desc_der_alt.setText(desc3)
            self.label_desc_der_fron.setText(desc4)
        elif var_estado_switch == 1:
            desc1 = "Cerrar el ojo izquierdo"
            desc2 = "para que el drone retroceda"
            self.label_desc_izq_alt.setText(desc1)
            self.label_desc_izq_fron.setText(desc2)
            desc3 = "Cerrar el ojo derecho"
            desc4 = "para que el drone avance"
            self.label_desc_der_alt.setText(desc3)
            self.label_desc_der_fron.setText(desc4)
        else:
            desc1 = "Cerrar el ojo izquierdo para"
            desc2 = "que el drone valla a la izquierda"
            self.label_desc_izq_alt.setText(desc1)
            self.label_desc_izq_fron.setText(desc2)
            desc3 = "Cerrar el ojo derecho para"
            desc4 = "que el drone valla a la derecha"
            self.label_desc_der_alt.setText(desc3)
            self.label_desc_der_fron.setText(desc4)

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    Actualizar_label_ojos(self,var_estado_switch=0)
    sys.exit(app.exec_())
