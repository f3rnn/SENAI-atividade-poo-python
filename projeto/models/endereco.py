from models.enums.ufs import UnidadeFederativa

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, uf: UnidadeFederativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf
    
    def __str__(self) -> str:
        return (
            f"\nlogradouro: {self.logradouro}"
            f"\nnúmero: {self.numero}"
            f"\ncomplemento: {self.complemento}"
            f"\ncep: {self.cep}"
            f"\ncidade: {self.cidade}"
            f"\nuf: {self.uf.nome}"
            f"\nuf: {self.uf.sigla}"
            )