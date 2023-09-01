from banco import conectar
import math

class Insert(object):
    def __init__(self, email = "", senha = "", percCPU = 0, memoria = 0, freq = 0):
        self.idUsuario
        self.idTotem
        self.idEmpresa
        self.idAeroporto
        self.email = email
        self.senha = senha
        self.freq = 0
        self.memoria = 0
        self.percCPU = 0
        self.banco = conectar.iniciar(self)

    def consultar(self):
        bancovar = conectar.iniciar(self)
        self.banco = bancovar
        bancoexec = bancovar.cursor(buffered=True)
        resultado = []
        bancoexec.execute(f"SELECT * FROM Funcionario JOIN Empresa ON fkEmpresa = idEmpresa JOIN Totem ON fkEmpresa = idEmpresa WHERE emailFunc = '{self.email}' AND senhaFunc = '{self.senha}'")
        for linha in bancoexec:
          self.idUsuario = linha['idFuncinario']
          self.idTotem = linha['idTotem']
          self.idEmpresa = linha['idEmpresa']
          self.idAeroporto = linha['idAeroporto ']
          self.idUsuario = linha['emailFunc']
          for coisa in linha:
              resultado.append(coisa)

        
        res = bancovar.commit()

        if len(resultado) > 0:
            return "Dados existem"
        else:
            return "ERRO: Não encontrado"

    def inserirMetricas(self):
        
        execucao = self.banco.cursor()
        varPerc = "%"
        varMz = "Mhz"
      
        addFreq = "INSERT INTO metrica (valor, tipoValor) VALUES (%s, %s)"
        dataFreq = (float(self.freq), varMz)
        addPerc = "INSERT INTO metrica (valor, tipoValor) VALUES (%s, %s)"
        dataPerc = (float(self.percCPU), varPerc)
        addMemory = "INSERT INTO metrica (valor, tipoValor) VALUES (%s, %s)"
        dataMemory = (self.memoria, varPerc)

 
        execucao.execute(addFreq, dataFreq)
        self.banco.commit()
        execucao.execute(addPerc, dataPerc)
        self.banco.commit()
        execucao.execute(addMemory, dataMemory)
        self.banco.commit()

        return True
       
     
            
    