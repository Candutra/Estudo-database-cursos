import sys
import mysql.connector as mc
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QVBoxLayout, QPushButton

cx = mc.connect(
    host="127.0.0.1",
    port="6556",
    user="root",
    password="senac@123",
    database="Senac"
)

cursor = cx.cursor()

class AtualizarCursos(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(150,100,600,250)
        self.setWindowTitle("Clientes cadastrados")

        labelId = QLabel("ID do Cliente")
        self.editId = QLineEdit()

        labelNomeCurso = QLabel("Nome do curso")
        self.editNomeCurso = QLineEdit()

        labelCargaHoras = QLabel("Carga Horaria do Curso")
        self.editCargaHoras = QLineEdit()

        btCadastro = QPushButton("Cadastrar Curso")

        layout = QVBoxLayout()
        
        layout.addWidget(labelId)
        layout.addWidget(self.editId)

        layout.addWidget(labelNomeCurso)
        layout.addWidget(self.editNomeCurso)

        layout.addWidget(labelCargaHoras)
        layout.addWidget(self.editCargaHoras)

        layout.addWidget(btCadastro)
        btCadastro.clicked.connect(self.attcurso)

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

        layout.addWidget(tbcursos)
        self.setLayout(layout)

    def attcurso(self):
        if (self.editId.text()==""):
            print("Não é possivel atualizar sem o id do Cliente")
        
        elif(self.editNomeCurso.text()=="" and self.editCargaHoras.text()==""):
            print("Não é possivel atualizar se não houver dados")

        elif(self.editNomeCurso.text()!="" and self.editCargaHoras.text()==""):
            cursor.execute("update tbcursos set nome_cursos=%s where curso_id=%s",
                           (self.editNomeCurso.text(),self.editCargaHoras.text()))
            

        elif(self.editNomeCurso.text()=="" and self.editCargaHoras.text()!=""):
            cursor.execute("update tbcursos set carga_horaria=%s where curso_id=%s",
                           (self.editCargaHoras.text(),self.editId.text()))
        
        else:
             cursor.execute("update Clientes set nome_curso=%s, carga_horaria=%s where curso_id=%s",
                           (self.editNomeCurso.text(),self.editCargaHoras.text(),self.editId.text()))
             
        cx.commit()
        print("Todas as modificações foram realizadas")


if __name__=="__main__":
    app = QApplication(sys.argv)
    tela = AtualizarCursos()
    tela.show()
    sys.exit(app.exec_())