from src.config.database import Database
from datetime import datetime

db = Database()


class Provider:
    def __init__(self, idOperadora: int, cnpj: str, razaoSocial: str, nomeFantasia: str | None, modalidade: str | None, rua: str, numero: str, complemento: str | None, bairro: str, cidade: str, uf: str, cep: str, ddd: str | None, tel: str | None, fax: str | None, email: str | None, representante: str, cargoRepresentante: str, regiao: int, dataRegistro: datetime):
        self.idOperadora = idOperadora
        self.cnpj = cnpj
        self.razaoSocial = razaoSocial
        self.nomeFantasia = nomeFantasia
        self.modalidade = modalidade
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep
        self.ddd = ddd
        self.tel = tel
        self.fax = fax
        self.email = email
        self.representante = representante
        self.cargoRepresentante = cargoRepresentante
        self.regiao = regiao
        self.dataRegistro = dataRegistro
    
    def to_dict(self):
        return {
            "idOperadora": self.idOperadora,
            "cnpj": self.cnpj,
            "razaoSocial": self.razaoSocial,
            "nomeFantasia": self.nomeFantasia,
            "modalidade": self.modalidade,
            "rua": self.rua,
            "numero": self.numero,
            "complemento": self.complemento,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "uf": self.uf,
            "cep": self.cep,
            "ddd": self.ddd,
            "tel": self.tel,
            "fax": self.fax,
            "email": self.email,
            "representante": self.representante,
            "cargoRepresentante": self.cargoRepresentante,
            "regiao": self.regiao,
            "dataRegistro": self.dataRegistro.isoformat(),
        }

        
class ProviderDAO:
    @staticmethod
    def findByName(name, page):
        ok, result = db.query(name=name, offset=page)
        if ok and len(result) != 0:
            return [Provider(*row) for row in result]
    