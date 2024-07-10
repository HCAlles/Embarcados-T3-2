from func_b import *
     
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
    func_bEntrada_saida()
    func_inicia_ui()
    
    
    
