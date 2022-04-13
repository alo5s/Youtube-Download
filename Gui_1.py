from PySide6.QtWidgets import QApplication, QMainWindow, QLabel,QPushButton, QWidget, QLineEdit
import pytube
from PySide6.QtGui import QPixmap
import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,200)
        self.setWindowTitle("GUi")
        icon = QPixmap("icon/YouTube.svg")
        self.setWindowIcon(icon)
        self.setStyleSheet("background: #3C3838  ")

        label = QLabel(self)
        iman = QPixmap("icon/YouTube.png")
        label.setGeometry(30,20,100,100)
        label.setPixmap(iman)

        texto_label = QLabel("URL",self)
        texto_label.setGeometry(140,60,20,20)
        texto_label.setStyleSheet("font-size: 12px;""color: #FFFFFF ;")

        self.tio = QLineEdit(self)
        self.tio.setStyleSheet("background: #FFFFFF ;")
        self.tio.setGeometry(165,60,300,20)

        btn = QPushButton("Download",self)
        btn.setGeometry(240,100,100,50)
        btn.setStyleSheet("font-size: 20px;" "background: #3D94F6;")
        btn.clicked.connect(self.activa)
        
    def activa(self):
        self.ventana=ventana()
        self.ventana.show()
        Link = self.tio.text()
        asd=pytube.YouTube(Link)
        self.ventana.urm2.setText(asd.title)
        self.ventana.imag.setText(asd.thumbnail_url)
        




class ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(450,150)
        self.setStyleSheet("background: #3C3838  ")
        self.urm2 = QLabel(self)
        self.urm2.setStyleSheet("color: #FF0000;")
        self.urm2.setGeometry(165,60,300,20)
        self.btn1 = QPushButton("Download",self)
        self.btn1.setGeometry(240,100,100,50)
        self.imag = QLabel(self)
        self.imag.setStyleSheet("background: #FFFFFF;")
        self.imag.setGeometry(32,20,100,100)


        

    

  
        

if __name__=="__main__":
    app=QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())