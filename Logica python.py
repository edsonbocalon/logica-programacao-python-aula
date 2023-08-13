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

Convertendo tipo para inteiro

def verifica_se_pode_dirigir_sem_parametros():
 idade = input('Qual sua idade? ')
 idade = int(idade)
 if idade >= 18:
  print('Tem permisssão para dirigir')
 else:
  print('Não tem permissão para dirigir')

verifica_se_pode_dirigir_sem_parametros()