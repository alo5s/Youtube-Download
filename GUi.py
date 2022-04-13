from PySide6.QtWidgets import QApplication, QMainWindow, QLabel,QPushButton,QLineEdit
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
        Link = self.tio.text()
        YT=pytube.YouTube(Link)
        YT.streams.first().download()

        

if __name__=="__main__":
    app=QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())