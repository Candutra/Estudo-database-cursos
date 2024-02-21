import sys
import mysql.connector as mc

cx = mc.connect(
    host="127.0.0.1",
    port="6556",
    user="root",
    password="senac@123",
    database="Senac"
)

cursor = cx.cursor()

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

class CadCursos(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150,100,600,250)
        self.setWindowTitle("Cadastro de cursos")

        labelNomeCurso = QLabel("Nome do curso")
        self.editNomeCurso = QLineEdit()

        labelCargaHoras = QLabel("Carga Horaria do Curso")
        self.editCargaHoras = QLineEdit()

        btCadastro = QPushButton("Cadastrar Curso")

        self.labelMsg = QLabel("Esperando dados")

        layout = QVBoxLayout()
        layout.addWidget(labelNomeCurso)
        layout.addWidget(self.editNomeCurso)

        layout.addWidget(labelCargaHoras)
        layout.addWidget(self.editCargaHoras)

        layout.addWidget(btCadastro)
        btCadastro.clicked.connect(self.rgCurso)

        layout.addWidget(self.labelMsg)
        self.setLayout(layout)

    def rgCurso(self):
        cursor.execute("insert into tbcursos(nome_curso,carga_horaria)values(%s,%s)",
                       (self.editNomeCurso.text(),self.editCargaHoras.text()))
        cx.commit()
        self.labelMsg.setText("Curso Registrado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = CadCursos()
    tela.show()
    sys.exit(app.exec_())
