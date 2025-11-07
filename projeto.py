import sqlite3

banco = sqlite3.connect("hospital.db")

cursor = banco.cursor()

# 1) Selecionar todos os pacientes da cidade de São Paulo .
# cursor.execute("SELECT nome FROM pacientes WHERE cidade = 'São Paulo' ")
# 2) Listar o nome e diagnóstico dos pacientes com idade acima de 40 anos .
# cursor.execute("SELECT nome,diagnostico FROM pacientes WHERE idade >40 ")
# 3) Mostrar o nome e plano de saúde dos pacientes atendidos pelo plano Unimed .
# cursor.execute("SELECT nome,plano_saude FROM pacientes WHERE plano_saude ='Unimed'   ")
# 4) Selecionar os pacientes ordenados pelos dados de internação (mais antigo primeiro) .
# cursor.execute("SELECT nome FROM pacientes ORDER BY data_internacao ASC ")
# 5) Mostrar apenas os pacientes que tiveram diagnóstico de Fratura .
# cursor.execute("SELECT nome FROM pacientes WHERE diagnostico ='Fratura'    ")
# 6) Selecionar os pacientes que foram atendidos pelo Dr.
cursor.execute("SELECT nome, medico_responsavel FROM pacientes WHERE medico_responsavel ='Dr. João'")

print(cursor.fetchall()) 



