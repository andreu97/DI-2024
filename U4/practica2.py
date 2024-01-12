import os
from PySide6.QtWidgets import QApplication, QMainWindow,QLineEdit,QToolBar,QPushButton,QDialog
from PySide6.QtGui import QAction, QKeySequence,QIcon


# Nuestra ventana principal hereda de QMainWindow
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor texto plano")
        
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Menu")
        
        self.editor=QLineEdit()
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
        
        accion1.triggered.connect(self.abrir_archivo) 
        accion2.triggered.connect(self.guardar_archivo) 
        accion3.triggered.connect(tancar)
        
        menu.addAction(accion1)
        menu.addAction(accion2)
        
        
        barra_herramientas=QToolBar("Barra")
        barra_herramientas.addActions([accion1,accion2,accion3])
        self.addToolBar(barra_herramientas)
        
        self.jpgdata=""
        
    
        
    def abrir_archivo(self):
        
        with open(self.arxiu,"r+") as f:
            self.jpgdata=f.read()
            self.editor.setText(self.jpgdata)
        f.close()
        

    def guardar_archivo(self):
        with open(self.arxiu,"w") as f:
            f.write(self.editor.text())
        f.close()
        print("guardar")
        
def tancar(self):
    
    app.quit()        
if __name__ == "__main__":
    app = QApplication([])
    ventana1 = VentanaPrincipal()
    ventana1.show()
    app.exec()
