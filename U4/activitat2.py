from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton,QVBoxLayout
)


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout horitzontal")

        # Creem un layout vertical
        layout_horitzontal = QHBoxLayout()
        layout_vertical=QVBoxLayout()
        componente_principal = QWidget()
        componente_principal.setLayout(layout_horitzontal)
        
        self.setCentralWidget(componente_principal)
        layout_vertical.addWidget(QPushButton('V1'))
        layout_vertical.addWidget(QPushButton('V2'))
        layout_vertical.addWidget(QPushButton('V3'))
        layout_vertical.addWidget(QPushButton('V4'))
        layout_horitzontal.addLayout(layout_vertical)
        layout_horitzontal.addWidget(QPushButton('H1'))
        layout_horitzontal.addWidget(QPushButton('H2'))
        layout_horitzontal.addWidget(QPushButton('H3'))
        layout_horitzontal.addWidget(QPushButton('H4'))


app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()

app.exec()
