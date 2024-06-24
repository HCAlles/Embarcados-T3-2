from main import*
senha_digitada=""
senha="12345678"
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
def func_bLimpar():
     global senha_digitada
     print("bLimpar clicado")
     senha_digitada=""
def func_bCadastrar():
     global senha_digitada
     print("bCadastrar clicado")
def func_bApagar():
     global senha_digitada
     print("bApagar clicado")
     senha_digitada=""
def func_bEnter():
     global senha_digitada
     
     print("bEnter clicado")
     print(senha_digitada)
     if senha_digitada==senha:
          print("senha correta")
     else: 
          
          print("Erro")
          print(senha_digitada+" diferente de"+senha)

     

     

