class Interesse: #Contato telefonico
    def __init__(self, inter):
        self.interesse = inter
        self.codigo = None
        self.proximo = None
        self.anterior = None
        self.quantidadeint = 0 #Quantidade de contatos que tem esse interesse

#Gets
    def get_interesse(self):
        return self.interesse

    def get_proximo(self):
        return self.proximo

    def get_anterior(self):
        return self.anterior

    def get_codigo (self):
        return self.codigo

    def get_quantidadeint (self):
        return self.quantidadeint
#Sets
    def set_interesse(self, inter):
        self.interesse = inter

    def set_proximo(self, proximo):
        self.proximo = proximo

    def set_anterior(self, anterior):
        self.anterior = anterior

    def set_codigo (self, codigo):
        self.codigo = codigo

    def set_quantidadeint (self, quandidade):
        self.quantidadeint = quandidade

    def add_quantidadeint (self):#ADD 1 na quantidade
        self.quantidadeint += 1

    def remove_quantidadeint (self): #Remove 1 na quantidade
        self.quantidadeint -= 1