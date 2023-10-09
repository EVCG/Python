import sqlite3
conexao = sqlite3.connect("livraria.db")
cur = conexao.cursor()

# sql = '''insert into tb_cliente(cpf, nome, idade) values('000000000-00', 'Paula', 31)'''
sql = '''insert into tb_cliente(cpf, nome) values('111111111-11', 'Paula')'''
cur.execute(sql)
conexao.commit()
cur.close()
conexao.close()