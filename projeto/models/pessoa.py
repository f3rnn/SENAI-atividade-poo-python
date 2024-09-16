from models.endereco import Endereco
from models.enums.sexo import Sexo

class Pessoa:
    def __init__(self, id: int, nome: str, dataNascimento: str, telefone: str, email: str, sexo: Sexo, endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.telefone = telefone
        self.email = email
        self.sexo = sexo
        self.endereco = endereco
    
    def __str__(self) -> str:
        return (
            f"\nid: {self.id}"
            f"\nnome: {self.nome}"
            f"\ndata de nascimento: {self.dataNascimento}"
            f"\ntelefone: {self.telefone}"
            f"\ne-mail: {self.email}"
            f"\nsexo: {self.sexo.texto}"
            f"\nsexo: {self.sexo.caracter}"
            f"\n---endereço---: {self.endereco}"
                )