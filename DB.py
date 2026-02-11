import sqlite3


def get_connection():
    con=sqlite3.connect("./dados.db")
    con.row_factory=sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    return con

def init_DB():
    con = get_connection()
    cur = con.cursor()
    
    try:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS meses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mes INTEGER NOT NULL,
            ano INTEGER NOT NULL,
            status TEXT NOT NULL,
            criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(mes, ano)
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS categoria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL,
            criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS movimentacao (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mes_id INTEGER NOT NULL,
            categoria_id INTEGER NOT NULL,
            valor REAL NOT NULL,
            data DATE NOT NULL,
            descricao TEXT,
            criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (mes_id) REFERENCES mes(id),
            FOREIGN KEY (categoria_id) REFERENCES categoria(id)
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS resumo_mensal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mes_id INTEGER NOT NULL UNIQUE,
            total_entradas REAL,
            total_saidas REAL,
            total_investimento REAL,
            saldo REAL,
            criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (mes_id) REFERENCES meses(id)
        );
        """)
    except con.DatabaseError as erro:
        print("Erro ao inicializar o banco de dados:", erro)
    finally:
        if con:
            con.close()
    
    
def iniciar_meses():
    con=get_connection()
    cur=con.cursor()
    statusp='fechado'
    
    try:
        for x in range(1,13):
            cur.execute("""INSERT INTO meses (mes,ano,status) VALUES(?,?,?)""",(x,2026,statusp,))
            con.commit()
                        
    except Exception as e:
        print("ERRO:", e)
    
    finally:
        con.close()        

def fechar_meses():
    con=get_connection()
    cur=con.cursor()
    try:
        cur.execute("UPDATE meses SET status=? WHERE status=?",("fechado",'aberto'))        
        con.commit()
    except Exception as e:
        print(e,"ERRO") 
    finally:
        con.close()
       
def abrir_mes(mes,ano):
    con=get_connection()
    cur=con.cursor()
    #============FECHAR TODOS OS MESES PARA QUE SÓ HAJA 1 ABERTO==============#
    try:
        fechar_meses()
    except Exception as e:
        print("Erro ao fechar meses abertos", e) 
    
    try: 
        cur.execute("UPDATE meses SET status=? WHERE mes=? and ano=?", ('aberto',mes,ano))     
        con.commit()   
    except Exception as e:
        print(F"ERRO,{e}")
    finally:
        con.close
        
iniciar_meses()