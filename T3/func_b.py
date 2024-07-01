from main import*
import sqlite3
import sys

con=sqlite3.connect("tutorial.db")
cur=con.cursor()
dados_senha=cur.execute("SELECT senha from registro where nome='test2'")
for linha in dados_senha.fetchall():
        senhas=linha
con.commit()


senha_digitada=""
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)

def func_():
    print("testando")
def func_senha():
    print(str(ui.lineEdit_senha.text()))

def func_bLimpar():
     print("bLimpar clicado")
     ui.lineEdit_senha.setText("")
     ui.lineEdit_funcao.setText("")
     ui.lineEdit_nome.setText("")
def func_inicia_ui():
     global ui
     global app
     global Dialog
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


def func_b0():
     print("b0 clicado")
     global senha_digitada
     senha_digitada=senha_digitada+"0"
def func_b1():
     global senha_digitada
     print("b1 clicado")
     senha_digitada=senha_digitada+"1"
def func_b2():
     global senha_digitada
     print("b2 clicado")
     senha_digitada=senha_digitada+"2"
def func_b3():
     global senha_digitada
     print("b3 clicado")
     senha_digitada=senha_digitada+"3"
def func_b4():
     global senha_digitada
     print("b4 clicado")
     senha_digitada=senha_digitada+"4"
def func_b5():
     global senha_digitada
     print("b5 clicado")
     senha_digitada=senha_digitada+"5"
def func_b6():
     global senha_digitada
     print("b6 clicado")
     senha_digitada=senha_digitada+"6"
def func_b7():
     global senha_digitada
     print("b7 clicado")
     senha_digitada=senha_digitada+"7"
def func_b8():
     global senha_digitada
     print("b8 clicado")
     senha_digitada=senha_digitada+"8"
def func_b9():
     global senha_digitada
     print("b9 clicado")
     senha_digitada=senha_digitada+"9"

def func_bCadastrar():
     global senha_digitada
     global ui
     con=sqlite3.connect("tutorial.db")
     cur=con.cursor()
     teste = 'terroso'
     print("bCadastrar clicado")
     ui.label_senha.setText("Senha: "+ui.lineEdit_senha.text())
     ui.label_funcao.setText("Funcao: "+ui.lineEdit_funcao.text())
     ui.label_nome.setText("Nome: "+ui.lineEdit_nome.text())
     string_cadastro="INSERT into registro values "+"('"+ui.lineEdit_nome.text()+"','"+ui.lineEdit_senha.text()+"','"+ui.lineEdit_funcao.text()+"')"
     print("string cadastro é: "+string_cadastro)
     cur.execute(string_cadastro)
     con.commit()
     
     
     
def func_bApagar():
     global senha_digitada
     print("bApagar clicado")
     senha_digitada=""
def func_bEnter():
     global senha_digitada
     global dados_senha
     global senhas
     print("bEnter clicado")
     
     if senha_digitada==senhas[0]:
          print("senha correta")
     else: 
          print("Erro")
          print(senha_digitada+" diferente de "+senhas[0])


     

     

