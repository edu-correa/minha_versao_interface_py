import mysql.connector as ms

class conectar:
    def __init__(self):
        self.host = "localhost"
        self.bd = "bd_conway"
        self.password = "sptech"
        self.user = "aluno"
        self.iniciar(self.host, self.bd, self.password, self.user)
    
    def iniciar(self, vhost, vbd, vpassword, vuser):
        conexao = ms.connection(
            host=vhost,
            database=vbd,
            user=vuser,
            password=vpassword
        )
        return conexao.cursor()
    
    