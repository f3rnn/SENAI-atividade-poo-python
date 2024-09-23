import pytest
from projeto.models.pessoa import Pessoa
from projeto.models.endereco import Endereco
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.ufs import UnidadeFederativa

@pytest.fixture
def criar_pessoa():
    pessoa = Pessoa(12, "Haroldo", "05/05/1989", "9899-9999", "haroldo@gmail.com", Sexo.MASCULINO,
                    Endereco("alameda", "123", "ali", "40.000-000", "salvador", UnidadeFederativa.BAHIA))
    return pessoa

def teste_pessoa_atributo_nome(criar_pessoa):
    assert criar_pessoa.nome == "Haroldo"

def test_pessoa_atributo_idade(criar_pessoa):
    assert criar_pessoa.id == 12

def test_endereco_logradouro_de_pessoa(criar_pessoa):
    assert criar_pessoa.endereco.logradouro == "alameda"