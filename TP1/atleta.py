class Atleta:
    def __init__(self,id,index,dataEMD,primeiro_nome,ultimo_nome,idade,genero,morada,modalidade,clube,email,federado,resultado):
        self.id = id
        self.index = index
        self.dataEMD = dataEMD
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.idade = idade
        self.genero = genero
        self.morada = morada
        self.modalidade = modalidade
        self.clube = clube
        self.email = email
        self.federado = federado
        self.resultado = resultado

    def __str__(self) -> str:
        return "ID: {id} -- Index: {index} -- Nome: {nome} -- Idade: {idade} -- Genero: {genero} -- Modalidade: {modalidade} -- Resultado: {resultado}".format(id=self.id,index=self.index,nome=self.primeiro_nome,idade=self.idade,genero=self.genero,modalidade=self.modalidade,resultado=self.resultado)