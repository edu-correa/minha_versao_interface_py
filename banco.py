import mysql.connector as ms

class conectar:
    def __init__(self):
        self.host = "localhost"
        self.bd = "bd_conway"
        self.password = "220807"
        self.user = "root"
        self.iniciar()
    
    def iniciar(self):
        conexao = ms.connect(
            host="localhost",
            user="aluno",
            password="sptech",
            database="bd_conway",
            port=3306
        )
        return conexao  