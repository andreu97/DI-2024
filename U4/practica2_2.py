import os
from PySide6.QtWidgets import QApplication, QMainWindow,QLineEdit,QToolBar,QPushButton,QDialog,QDialogButtonBox,QMessageBox,QTextEdit
from PySide6.QtGui import QAction, QKeySequence,QIcon


# Nuestra ventana principal hereda de QMainWindow
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor texto plano")
        
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Menu")
        
        self.editor=QTextEdit()
        self.setCentralWidget(self.editor)
        
        icono_guardar=os.path.join(os.path.dirname(__file__), "guardar_archivo.png")
        icono_abrir=os.path.join(os.path.dirname(__file__),"abrir_archivo.png")
        self.arxiu=os.path.join(os.path.dirname(__file__), "arxiu.txt")
        
        accion1 = QAction(QIcon(icono_abrir),"&Abrir archivo", self)
        accion2=QAction(QIcon(icono_guardar),"&Guardar archivo",self)
        accion3=QAction("Salir",self)
        
        accion1.setShortcut(QKeySequence("Ctrl+o"))
        accion2.setShortcut(QKeySequence("Ctrl+s"))  
        accion3.setShortcut(QKeySequence("Ctrl+p"))
        
        
        
        
        
        
        self.variable=True
        
        
        self.editor.textChanged.connect(self.vbFalse)
        accion1.triggered.connect(self.abrir_archivo)
        
        
        accion2.triggered.connect(self.guardar_archivo)
        accion3.triggered.connect(self.dialeg_cambis)
        
        menu.addAction(accion1)
        menu.addAction(accion2)
        
        
        barra_herramientas=QToolBar("Barra")
        barra_herramientas.addActions([accion1,accion2,accion3])
        self.addToolBar(barra_herramientas)
        
        self.jpgdata=""
        
    def vbTrue(self):
        self.variable=True
        
    def vbFalse(self):
        self.variable= False
        
        
    def dialeg_cambis(self):
        
        botonpulsado=QMessageBox.critical(self,"Texto no guardado","Vols guardar?",buttons=QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Open)
        if (botonpulsado==QMessageBox.Save):
            self.guardar_archivo()
            self.abrir_archivo()
            
        elif (botonpulsado==QMessageBox.Cancel):
           pass
            
        elif (botonpulsado==QMessageBox.Open):
            self.vbTrue()     
            self.abrir_archivo()
                  
            
        
    def abrir_archivo(self):
        if self.variable:
            f=open(self.arxiu,"r+")
            self.jpgdata=f.read()
            self.editor.setText(self.jpgdata)
            f.close()
            self.vbTrue()
        else:
            self.dialeg_cambis()
            
            
        
        

    def guardar_archivo(self):
        with open(self.arxiu,"w") as f:
            f.write(self.editor.toPlainText())
        f.close()
        print("guardar")
        
def tancar():
    app.quit()     
       
if __name__ == "__main__":
    app = QApplication([])
    ventana1 = VentanaPrincipal()
    ventana1.show()
    app.exec()
