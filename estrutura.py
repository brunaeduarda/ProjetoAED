from Class.BaseContatos import Base

'''
1.  Cada  contato  deve  possuir  os  itens:
1.1. um  Código  (obrigatório)                  ok
1.2. Nome  (obrigatório)                        ok
1.3. Telefone  (obrigatório)                    ok
1.4. e-mail  (obrigatório)                      ok
1.5. Lista  de  interesses  (#Item) 
1.6. Lista  de  contatos.

2.  Funçõesque  o  sistema  deve  possuir:
2.1.  Salvar  os  contatos  em  Arquivo  (por  ordem  alfabética)
2.2.  Buscar  contatos  por  nome  ou  e-mail  ok
2.3.  Buscar  contatos  por  item  de  interesse.
2.4. Organizar contatos por "contatos em comum"
        (ex.:  pega  dois  contatos  e  mostra  os  contatos  em  comum  na  rede  de  contatos)
2.5.  Mostrar  contatos  por  algum  outro  critérioescolhido  pelo  candidato,  entre  as  Informações  do  contato.

3.  Obrigatório  o  uso  de  estruturas  de  dados  mostrados  na  disciplina
3.1  Listas  ligadas  (fila,  lista,  pilha); (CADASTRO)
3.2  Árvores;
3.3  Grafos.
'''




'''
Menu

1- Cadastro ok
2- excluir ok
3- exibir contatos ok








'''



nome = 'victor'
tel = '99159407'
email = 'victor@email.com'
codigo = 1

nome2 = 'teste'
tel2 = 'teste'
email2 = 'teste@email.com'

base = Base()
base.cadastrar(nome,tel,email, 1)
base.cadastrar(nome,tel,email, 2)
base.cadastrar(nome,tel,email, 3)
base.cadastrar(nome2,tel2,email2, 2)
base.exibirtodos()
print('...')
base.excluir(3)
base.exibirtodos()