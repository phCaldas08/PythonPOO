from Classes.Conta import Conta
import json

response = requests.get("http://jsonplaceholder.typicode.com/comments")
print(response.status_code)

class Pessoa():
    def __init__(self, nome, altura, idade):
        self.conta = Conta()
        self.__nome = nome
        self.__altura = altura
        self.__idade = idade
        self.__stringMsg = "Nome: {0} Idade: {1} Altura: {2}"

    def getStringPessoa(self):
        return self.__stringMsg.format(self.__nome, self.__idade, self.__altura)

listPessoa = []
while True:
    nome = input("Digite um nome: ")
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura"))

    p = Pessoa(nome, altura, idade)
    listPessoa.append(p)

    p.conta.Deposito(float(input("Informe o valor do deposito")))

    print(p.conta.GetSaldo())

    if(input("Continuar? [s/n]") == "n"):
        break

for __p in listPessoa:
    print(__p.getStringPessoa())

