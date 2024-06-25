from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_Dialog
from func_b import *
import sqlite3
senha_digitada=""
def func_():
    print("testando")
def func_senha():
    print(str(ui.lineEdit_senha.text()))

def func_bLimpar():
     print("bLimpar clicado")
     ui.lineEdit_senha.setText("")
     ui.lineEdit_funcao.setText("")
     ui.lineEdit_nome.setText("")
     
def func_bCadastrar():
     print("bCadastrar clicado")
     ui.label_senha.setText("Senha: "+ui.lineEdit_senha.text())
     ui.label_funcao.setText("Funcao: "+ui.lineEdit_funcao.text())
     ui.label_nome.setText("Nome: "+ui.lineEdit_nome.text())

     
if __name__ == "__main__":
    import sys
    '''cur.execute("CREATE TABLE registro(nome, senha, funcao)")
    
    
    print("Criou TABLE registro")
    cur.execute("""
    DROP TABLE registro
    """)
    
    ######  cria table
    cur.execute("""
        INSERT INTO registro VALUES
            ('test1','123','nada'),
            ('test2','456','nada2')
        """)
    ###### 
    
    senha=cur.execute("""
        SELECT senha FROM registro
        WHERE nome='test1'; """)
    #print("Dados: "+str(cur.execute("SELECT ")))
    
    data = [
    ("","",""),
    ("","",""),
    ("","",""),]
    #cur.executemany("INSERT INTO registro VALUES(?, ?, ?)", data)
    #cur.execute("DELETE FROM registro WHERE nome=test1")
    
    con.commit()
    '''

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.bCadastrar.clicked.connect(func_senha)
    ui.b0.clicked.connect(func_b0)
    ui.b1.clicked.connect(func_b1)
    ui.b2.clicked.connect(func_b2)
    ui.b3.clicked.connect(func_b3)
    ui.b4.clicked.connect(func_b4)
    ui.b5.clicked.connect(func_b5)
    ui.b6.clicked.connect(func_b6)
    ui.b7.clicked.connect(func_b7)
    ui.b8.clicked.connect(func_b8)
    ui.b9.clicked.connect(func_b9)
    
    ui.bApagar.clicked.connect(func_bApagar)
    ui.bCadastrar.clicked.connect(func_bCadastrar)
    ui.bEnter.clicked.connect(func_bEnter)
    ui.bLimpar.clicked.connect(func_bLimpar)
    
    
    
    Dialog.show()
    sys.exit(app.exec_())
