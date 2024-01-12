from PySide6.QtWidgets import QApplication, QLabel, QWidget,QLineEdit

class Finestra(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("finestra")
        
        # Creem dues etiquetes amb el component com a parent
        self.input = QLineEdit( self)
        self.input.resize(50,30)
        self.input.setMaxLength(5)
        self.label2 = QLabel(self)
        self.label2.resize(50,30)
        self.input.textChanged.connect(self.label2.setText) # type: ignore
        # Necessitem moure la segona perquè no es solapi amb la primera
        self.label2.move(55, 0)

if __name__ == "__main__":
    app = QApplication([])
    finestra = Finestra()
    # Mostrem la finestra
    finestra.show()
    app.exec()
