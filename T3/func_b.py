from main import*
import sqlite3
import sys
import random
import string

dados_senha=0
senhas=0
entrada=True
marcador_ID_senha=0
ID=""
ID_digitado=""
senha_digitada=""
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)


def func_transform_to_random_digits(input_string):
    random.seed(input_string)
    random_digits = ''.join(random.choices('0123456789', k=5))
    return str(random_digits)

def func_contains_non_digit_characters(input_string):
    for char in input_string:
        if not char.isdigit():
            return True
    return False
def func_bLimpar():
     print("bLimpar clicado")
     ui.lineEdit_senha.setText("")
     ui.lineEdit_funcao.setText("")
     ui.lineEdit_nome.setText("")
     ui.label_senha.setText("Senha: ")
     ui.label_nome.setText("Nome: ")
     ui.label_funcao.setText("Funcao: ")
     ui.label_ID.setText("Seu id é: ")
def func_inicia_ui():
     global ui
     global app
     global Dialog
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
     ui.bEntrada_saida.clicked.connect(func_bEntrada_saida)
     ui.bApagar.clicked.connect(func_bApagar)
     ui.bCadastrar.clicked.connect(func_bCadastrar)
     ui.bEnter.clicked.connect(func_bEnter)
     ui.bLimpar.clicked.connect(func_bLimpar)
     Dialog.show()
     sys.exit(app.exec_())
def func_atualiza_display(digito):
     global ui
     global senha_digitada
     global marcador_ID_senha
     global ID_digitado
     if marcador_ID_senha==1:# se False senha, se nao id
          senha_digitada=senha_digitada+digito
          ui.label_digite_a_senha.setText("Digite a senha: "+senha_digitada)
     else:
          ID_digitado=ID_digitado+digito
          ui.label_digite_o_ID.setText("Digite o ID: "+ID_digitado)
def func_b0():
     print("b0 clicado")
     func_atualiza_display("0")
def func_b1():
     print("b1 clicado")
     func_atualiza_display("1")
def func_b2(): 
     print("b2 clicado")
     func_atualiza_display("2")
def func_b3():
     print("b3 clicado")
     func_atualiza_display("3")
def func_b4():
     print("b4 clicado")
     func_atualiza_display("4")
def func_b5():
     print("b5 clicado")
     func_atualiza_display("5")
def func_b6():
     print("b6 clicado")
     func_atualiza_display("6")
def func_b7():
     print("b7 clicado")
     func_atualiza_display("7")
def func_b8():
     print("b8 clicado")
     func_atualiza_display("8")
def func_b9():
     print("b9 clicado")
     func_atualiza_display("9")

def func_bEntrada_saida():
     global entrada
     global ui
     entrada=not entrada
     if(entrada):
          ui.bEntrada_saida.setText("entrada")
     else: ui.bEntrada_saida.setText("saida")

def func_bCadastrar():
     global ui
     con=sqlite3.connect("tutorial.db")
     cur=con.cursor()
     print("bCadastrar clicado")
     ui.label_senha.setText("Senha: "+ui.lineEdit_senha.text())
     ui.label_funcao.setText("Funcao: "+ui.lineEdit_funcao.text())
     ui.label_nome.setText("Nome: "+ui.lineEdit_nome.text())
     ID_final=func_transform_to_random_digits(ui.lineEdit_nome.text())
     #ui.label_ID.setText("Registro  Seu ID é: "+ID_final)
     string_cadastro="INSERT into registro values "+"('"+ui.lineEdit_nome.text()+"','"+ui.lineEdit_senha.text()+"','"+ui.lineEdit_funcao.text()+"','"+ID_final+"')"
     print("string cadastro é: "+string_cadastro)
     
     if func_check_cadastro()==False:
          ui.label_ID.setText("Seu ID é: "+str(ID_final))
          cur.execute(string_cadastro)

     else:
          ui.label_ID.setText("Nome ou senha já existentes")


     print("func_check_cadastro() é: "+str(func_check_cadastro()))
     con.commit()
     
def func_check_cadastro():
     global ui
     s=ui.lineEdit_senha.text()
     con = sqlite3.connect('tutorial.db')
     cur = con.cursor()
     dados=cur.execute("""select * from registro""")
     dados=dados.fetchall()
     print(dados)
     contador=0 #conta quantos informações são repitidas
     for cont in dados:
          for i in range(0,3):
               match i:
                    case 0:
                         s=ui.lineEdit_nome.text()
                    case 1:
                         s=ui.lineEdit_senha.text()
                    case 2:
                         s=ui.lineEdit_funcao.text()
                    case _:
                         print("i fora do range")
               if cont[i]==s:#index de cont é as rows do banco de dados: nome,senha,funcao,ID
                    print("achou")
                    contador=1
               else:
                    print("não achou")
     con.close()           
     if contador==1:
               contador=0
               return True
     else:
               contador=0
               if not func_contains_non_digit_characters(ui.lineEdit_senha.text()):
                    return False     
               else:
                    print("Senha só pode ter numeros")
                    ui.label_senha.setText("Senha: senha só pode ter numeros")
               
def func_confere_ID_senha():######################################
     print("conferindo ID")   
     global ui
     global ID_digitado
     global senha_digitada
     con = sqlite3.connect('tutorial.db')
     cur = con.cursor()
     dados_ID=cur.execute("""select ID from registro""")
     dados_ID=dados_ID.fetchall()
     print(dados_ID)
     dados_senha=cur.execute("""select senha from registro""")
     dados_senha=dados_senha.fetchall()
     print(dados_senha)
     contador=0 #conta quantos informações são repitidas
     r=ID_digitado
     s=senha_digitada
     for cont in dados_ID:
          if cont[0]==r:
               print("achou_ID")
               for cont2 in dados_senha:
                    if cont2[0]==s:
                         print("achou senha")
                         return True
                    else:
                         print("não achou senha")
          else:
               print("não achou ID")
               print("cont: "+str(cont)+" diferente de r: "+str(r))
     con.close()
     print("retornando False porque não achou ID e senhas compativeis")           
     return False           
def func_bApagar():
     global senha_digitada
     global ID_digitado
     global marcador_ID_senha
     marcador_ID_senha=0
     senha_digitada=""
     ID_digitado=""
     ui.label_digite_a_senha.setText("Digite a senha: ")
     ui.label_digite_o_ID.setText("Digite o ID: ")
     ui.label_acesso.setText("Acesso:")
     
def func_bEnter():##########################################
     global ui
     global marcador_ID_senha
     print("bEnter clicado")
     if marcador_ID_senha==1:
          if func_confere_ID_senha():
               print("acesso autorizado")
               marcador_ID_senha=3
          else:
               print("acesso negado")
               marcador_ID_senha=2
     if  marcador_ID_senha==0:
          marcador_ID_senha+=1
     if marcador_ID_senha==2:
          func_bApagar()
          ui.label_acesso.setText("Acesso: Negado")
     if marcador_ID_senha==3:
          func_bApagar()
          ui.label_acesso.setText("Acesso: Autorizado")


     
               
     
          

     

     

