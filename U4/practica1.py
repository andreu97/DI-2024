from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QFormLayout,
    QLabel,
    QLineEdit,
    QSpinBox,
    QDoubleSpinBox,
    QVBoxLayout,
    QPushButton,
    QLabel
    
    
)


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout formulario")

        self.layout_formulario = QFormLayout()
        
        layout_login=QPushButton("Login")
        
        componente_principal = QWidget()
        componente_principal.setLayout(self.layout_formulario)
        
        self.setCentralWidget(componente_principal)
        
        self.label=QLabel("Usuario")
        self.label2=QLabel("Contraseña")
        
        self.usuari=QLineEdit()
        self.usuari.setPlaceholderText("Usuario")
        
        self.contra=QLineEdit()
        self.contra.setPlaceholderText("Contraseña")
        
        self.contra.setEchoMode(QLineEdit.EchoMode.Password)
        self.label_final=(QLabel())
        layout_login.clicked.connect(self.login) # type: ignore
        self.layout_formulario.addRow(self.label,self.usuari)
        self.layout_formulario.addRow(self.label2,self.contra)
        self.layout_formulario.addWidget(layout_login)
        self.layout_formulario.addWidget(self.label_final)
        self.label_final.setVisible(False)
    
    def login(self):
        
        self.label_final.setVisible(True)
        
        if(self.usuari.text()=="admin" and self.contra.text()=="admin"):
            self.label_final.setStyleSheet("color: green")
            self.label_final.setText("Usuario correcto")
        else:
            self.label_final.setStyleSheet("color: red")
            self.label_final.setText("Usuario incorrecto")

app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()

app.exec()
