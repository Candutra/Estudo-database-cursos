import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
import mysql.connector as myc

cx = myc.connect(
    host="127.0.0.1",
    port="6556",
    user="root",
    password="senac@123",
    database="Senac"
)

cursor = cx.cursor()

class ExibirCursos(QWidget):
        def __init__(self):
            super().__init__()

            self.setGeometry(100,100,360,400)
            self.setWindowTitle("Cursos Registrados")
            

            tbcursos = QTableWidget(self)
            tbcursos.setColumnCount(3)
            tbcursos.setRowCount(15)
            headerLine=["curso_id","nome_curso","carga_horaria"]

            tbcursos.setHorizontalHeaderLabels(headerLine)
            cursor.execute("select * from tbcursos")
            lintb = 0
            for linha in cursor:
                tbcursos.setItem(lintb,0,QTableWidgetItem(str(linha[0])))
                tbcursos.setItem(lintb,1,QTableWidgetItem(str(linha[1])))
                tbcursos.setItem(lintb,2,QTableWidgetItem(str(linha[2])))
                lintb+=1

            layout = QVBoxLayout()
            layout.addWidget(tbcursos)
            self.setLayout(layout)

if __name__=="__main__":
    app = QApplication(sys.argv)
    tela = ExibirCursos()
    tela.show()
    sys.exit(app.exec_())          
            
