from Class.contato import Contato
from Class.Interesse import Interesse

class Base:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        self.qinteresses = 0


    def cadastrar(self, nome, tel, email, codigo):
        if (codigo != None):
            Novo = Contato(codigo)
        else:
            codigo = self.tamanho+1
            Novo = Contato(codigo)
        Novo.set_nome(nome)
        Novo.set_telefone(tel)
        Novo.set_email(email)
        if (self.tamanho <= 0):
            self.inicio = self.fim = Novo #Se o tamanho for 0 independente do tamanho inserido, sera cadasatrado como primeiro
        else:
            if (codigo <= 1): #inserir inicio
                self.inicio.set_anterior(Novo)
                Novo.set_proximo(self.inicio)
                self.inicio = Novo
            if (codigo >= self.tamanho): #inserir fim
                self.fim.set_proximo(Novo)
                Novo.set_anterior(self.fim)
                self.fim = Novo
            else: #inserir em qualquer posicao
                antecessor = sucessor = self.inicio
                while (antecessor.get_codigo() != codigo-1):
                    antecessor = antecessor.get_proximo()
                sucessor = antecessor.get_proximo()
                Novo.set_proximo(sucessor)
                Novo.set_anterior(antecessor)
                sucessor.set_anterior(Novo)
                antecessor.set_proximo(Novo)
                antecessor = sucessor = None
                self.organizarcodigos()
        self.tamanho += 1

    def is_empty(self):
        if (self.tamanho == 0): return True
        return False

    def procurarnome (self, nome): #pesquisa nome
        temp = self.inicio
        if (self.is_empty()):
            return False
        while(temp != None):
            if (indice > self.tamanho): return False
            if (temp.nome == nome): return temp
            temp = temp.get_proximo()
        return False

    def procuraremail (self, email): #pesquisa nome
        temp = self.inicio
        if (self.is_empty()):
            return False
        while(temp != None):
            if (indice > self.tamanho): return False
            if (temp.email == email): return temp
            temp = temp.get_proximo()
        return False

    def procurarcodigo (self, codigo):#Procurar Codigo
        if (self.is_empty()):
            return False
        if (codigo >= self.tamanho):
            return self.fim
        if (codigo <= 1):
            return self.inicio
        else:
            temp = self.inicio
            while(codigo != temp.get_codigo()):
                temp = temp.get_proximo()
            return temp

    def printcontato (self, contato):
        print("Codigo: {}".format(contato.get_codigo()))
        print("Nome: {}".format(contato.get_nome()))
        print("Email: {}".format(contato.get_email()))
        print("Telefone: {}".format(contato.get_telefone()))

    def organizarcodigos (self):
        temp = self.inicio
        codigo = 1
        if (self.is_empty()):
            return False
        while (temp != None):
            temp.set_codigo(codigo)
            codigo += 1
            temp = temp.get_proximo()
        return True

    def exibirtodos (self):
        if (self.is_empty()):
            print('Lista vazia')
        temp = self.inicio
        while(temp != None):
            self.printcontato(temp)
            temp = temp.get_proximo()

    def excluir (self, codigo):
        if (self.is_empty()):
            return False
        if (codigo <= 1):
            if(self.tamanho==1):
                self.inicio = self.fim = None
                self.tamanho -=1
                return True
            temp = self.inicio.get_proximo()
            temp.set_anterior(None)
            self.inicio.set_proximo(None)
            self.inicio = temp
        if (codigo >= self.tamanho):
            if (self.tamanho==1):
                self.excluir(1)
                return True
            temp = self.fim.get_anterior()
            temp.set_proximo(None)
            self.fim.set_anterior(None)
            self.fim = temp
        else:
            temp = self.procurarcodigo(codigo)
            temp2 = temp.get_anterior()
            temp2.set_proximo(temp.get_proximo())
            temp2 = temp.get_proximo()
            temp2.set_anterior(temp.get_anterior())
            temp = None
            self.organizarcodigos()
        self.tamanho -= 1

    def editarnome (self, codigo, nome):
        if (self.is_empty()):
            return False
        if (codigo <= 1):
            self.inicio.set_nome(nome)
        if (codigo >= self.tamanho):
            self.fim.set_nome(nome)
        else:
            temp = self.inicio
            while(codigo != temp.get_codigo()):
                temp = temp.get_proximo()
            temp.set_nome(nome)
        return True

    def editaremail (self, codigo, email):
        if (self.is_empty()):
            return False
        if (codigo <= 1):
            self.inicio.set_email(email)
        if (codigo >= self.tamanho):
            self.fim.set_email(email)
        else:
            temp = self.inicio
            while(codigo != temp.get_codigo()):
                temp = temp.get_proximo()
            temp.set_email(email)
        return True

    def editartelefone (self, codigo, telefone):
        if (self.is_empty()):
            return False
        if (codigo <= 1):
            self.inicio.set_telefone(telefone)
        if (codigo >= self.tamanho):
            self.fim.set_telefone(telefone)
        else:
            temp = self.inicio
            while(codigo != temp.get_codigo()):
                temp = temp.get_proximo()
            temp.set_telefone(telefone)
        return True

#Interesses
class interesses:
    def __init__(self):
        self.iniciointer = None
        self.fiminter = None
        self.proxcodinter = 1

    def InserirInteresse (self, inter):
        Novo = Interesse(inter)
        Novo.set_codigo(self.proxcodinter)
        if (self.proxcodinter == 1):
            self.iniciointer = self.fiminter = Novo #Inicio do primeiro interesse
        else:#Se não, inserir fim
            self.fim.set_proximo(Novo)
            Novo.set_anterior(self.fim)
            self.fim = Novo
        self.proxcodinter += 1


    def LimparNaoUsados (self):
        temp = self.iniciointer
        while (temp != None):
            if (temp.get_quantidadeint() == 0):
                if (temp.get_codigo()==1):
                    self.iniciointer = temp.get_proximo()
                    self.iniciointer.set_anterior(None)
                    temp.set_proximo(None)
                    temp = None
                if (temp.get_proximo != None):
                    temp2 = temp.get_anterior()
                    temp2.set_proximo(temp.get_proximo())
                    temp2 = temp.get_proximo()
                    temp2.set_anterior(temp.get_anterior())
                    temp = None
                else:
                    temp = self.fiminter.get_anterior()
                    self.fiminter.set_anterior(None)
                    temp.set_proximo(None)
                    self.fiminter = temp
                self.proxcodinter -= 1
                self.organizarinteresses()
            temp = temp.get_proximo()


    def organizarinteresses (self):
        temp = self.iniciointer
        codigo = 1
        if (self.proxcodinter == 1):
            return False
        while (temp != None):
            temp.set_codigo(codigo)
            codigo += 1
            temp = temp.get_proximo()
        return True

    def exibirinteresses (self):
        if (self.is_empty()):
            print('Lista vazia')
        temp = self.inicio
        while(temp != None):
            self.printcontato(temp)
            temp = temp.get_proximo()

