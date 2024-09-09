import os

from models.endereco import Endereco
from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.enums.ufs import UnidadeFederativa

os.system("clear")

pessoa_um = Pessoa(123, "zezão", "11/09/1969", "98999999", "zezão@gmail.com", Sexo.MASCULINO, Endereco("rua alameda", "123", "ali na esquina", "40.000-000", "salvador", UnidadeFederativa.BAHIA))
print(pessoa_um)