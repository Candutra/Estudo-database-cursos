# Sistema de Gerenciamento de Cursos

Este é um projeto de sistema de gerenciamento de cursos que utiliza um banco de dados para armazenar informações sobre os cursos, incluindo o nome do curso e sua carga horária. O sistema inclui três scripts em Python que interagem com o banco de dados e uma interface gráfica para cada script construída usando PyQt5.

## Funcionalidades

- **Cadastrar Cursos:** Permite adicionar novos cursos ao banco de dados, inserindo o nome do curso e sua carga horária.
- **Listar Cursos:** Exibe todos os cursos armazenados no banco de dados, mostrando o nome do curso e sua carga horária.
- **Alterar Cursos:** Permite alterar informações de cursos existentes, como o nome do curso ou sua carga horária.

## Tecnologias Utilizadas

- Python
- PyQt5
- MySql

 #### Arquivo de cadastro: cad_cursos.py
``` python
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
```
#### Arquivo para listar os cursos: listar cursos.py
``` python
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
```

#### Arquivo de atualização de curso: atualizar_cursos.py
``` python
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
```
