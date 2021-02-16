class Contato: #Contato telefonico
    def __init__(self, codigo):
        self.codigo = codigo
        self.nome = None
        self.telefone = None
        self.email = None
        self.proximo = None
        self.anterior = None

    """        self.contatos Lista com os contatos / implantar Fase 2"""
    """        self.interesses Lista com os interesses / implantar Fase 3"""


#GETS
    def get_codigo(self):
        return self.codigo

    def get_nome(self):
        return self.nome

    def get_telefone(self):
        return self.telefone

    def get_email(self):
        return self.email


    def get_proximo(self):
        return self.proximo

    def get_anterior(self):
        return self.anterior

#SETS
    def set_codigo(self, codigo):
        self.codigo = codigo

    def set_nome(self, nome):
        self.nome = nome


    def set_telefone(self, telefone):
        self.telefone = telefone


    def set_email(self, email):
        self.email = email




    def set_proximo(self, contato):
        self.proximo = contato


    def set_anterior(self, contato):
        self.anterior = contato

"""     Implantar Fase 2
    def get_contatos(self):
        return self.contatos
"""

"""     Implantar Fase 3
    def get_interesses(self):
        return self.interesses
"""

"""     Implantar Fase 3
    def set_interesses(self, interesses):
        self.interesses = interesses
"""

"""     Implantar Fase 2
    def set_contatos(self, contatos):
        self.contatos = contatos
"""