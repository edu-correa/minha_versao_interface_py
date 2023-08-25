import mysql.connector as ms

class conectar:
    def __init__(self):
        self.host = "localhost"
        self.bd = "bd_conway"
        self.password = "sptech"
        self.user = "aluno"
        self.cursor = self.iniciar(self.host, self.bd, self.password, self.user)
    
    def iniciar(self, vhost, vbd, vpassword, vuser):
        conexao = ms.connection(
            host=vhost,
            database=vbd,
            user=vuser,
            password=vpassword
        )
        return conexao
    
    def comando(self, email, senha):
        banc = self.iniciar(self.host, self.bd, self.password, self.user)
        exec = banc.cursor()

        exec.execute(f"SELECT * FROM usuario WHERE email = {email} and senha = {senha}")
        res = banc.commit()

        if res:
            return True
        else:
            return False