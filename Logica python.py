1+1

"Edson"

'Edson'

nome = 'Edson'

nome

idade = 37

idade

print(f'O mone é {nome} e sua idade é {idade} anos')

idade = 38

print(f'O mone é {nome} e sua idade é {idade} anos')

# Criando minha primeira função


def saudacao():
  nome = input ('Qual é o seu nome?  ')
  print(f'Olá {nome}')

saudacao()

def nome_completo():
 primeiro_nome = input('Qual seu primeiro nome? ')
 sobrenome = input('Qual seu sobrenome? ')
 nome_inteiro = primeiro_nome + ' ' + sobrenome
 print(nome_inteiro)

nome_completo()


# Parâmetros

nome = 'João'

def saudacao_com_parametros(nome_da_pessoa):
  print(f'olá {nome_da_pessoa}')

saudacao_com_parametros(nome)

# Condicional

idade = 20

def verifica_se_pode_dirigir(idade):
  if idade >= 18:
    print('Tem permissão para dirigir')
  else:
    print('Não tem permissão para dirigir')

verifica_se_pode_dirigir(idade)

def verifica_se_pode_dirigir_sem_parametros():
 idade = input('Qual sua idade? ')
 idade = int(idade)
 if idade >= 18:
  print('Tem permisssão para dirigir')
 else:
  print('Não tem permissão para dirigir')

verifica_se_pode_dirigir_sem_parametros()

# Convertendo tipo para inteiro

def verifica_se_pode_dirigir_sem_parametros():
 idade = input('Qual sua idade? ')
 idade = int(idade)
 if idade >= 18:
  print('Tem permisssão para dirigir')
 else:
  print('Não tem permissão para dirigir')

verifica_se_pode_dirigir_sem_parametros()

Lista

idade = 22
idade

type(idade)

nome = 'Edson'
type(nome)

idades = [18, 22, 15, 50]
type(idades)

idades[2]

idades = [18, 22, 15, 50]
#          0   1   2   3
#          0  -3  -2  -1

idades[1]

idades[0 : 3]

idades[1 : ]

idades[-1]

idades [-2]

# Laços e loops

idades

# for fora da função

def verifica_se_pode_dirigir(idade):
  if idade >= 18:
    print(f'{idade} anos de idade, TEM permissão para dirigir')
  else:
    print(f'{idade} anos de idade, NÃO TEM permissão para dirigir')

for idade in idades:
  verifica_se_pode_dirigir(idade)

def verifica_se_pode_dirigir(idades):
  for idade in idades:
    if idade >= 18:
      print(f'{idade} anos de idade, TEM permissão para dirigir')
    else:
      print(f'{idade} anos de idade, NÃO TEM permissão para dirigir')

verifica_se_pode_dirigir(idades)

# Boleano

idade = 18
idade >= 18

idade = 15
idade >= 18

permissoes = []
idades = [20, 14, 40]

def verifica_se_pode_dirigir(idades, permissoes):
  for idade in idades:
    if idade >= 18:
      permissoes.append(True)
    else:
      permissoes.append(False)

verifica_se_pode_dirigir(idades, permissoes)

permissoes

for permissao in permissoes:
  if permissao == True:
    print('Tem permissão para dirigir')
  else:
    print('Não tem permissão para dirigir')

# Tipos em uma lista

lista = ['Edson', 37, True, '18']

for elemento in lista:
  print(f'O elemento {elemento} é do tipo: ', type(elemento))

# Import

from random import randrange, seed
seed(10)

randrange (0, 11)

notas_matematica = []
for notas in range(8):
  notas_matematica.append(randrange(0, 11))
notas_matematica

len (notas_matematica)

# Matplotlib

import matplotlib.pyplot as plt

x = list(range(1, 9))
y = notas_matematica
plt.plot(x, y, marker='o')
plt.title('Notas de matemática')
plt.xlabel('Provas')
plt.ylabel('Notas')
plt.show()

notas_matematica

