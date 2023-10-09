import sqlite3
database = "livraria.db"
conexao = sqlite3.connect("livraria.db")
cur = conexao.cursor()

sql = '''create table if not exists tb_cliente(
        cpf varchar(14) primary key,
        nome varchar(30) not null,
        idade varchar(3) not null
        )'''



print("QTD dados inseridos", cur.rowcount)
print("QTD Registros na base", cur.lastrowid)



cur.execute(sql)
# conexao.commit()
cur.close()
conexao.close()