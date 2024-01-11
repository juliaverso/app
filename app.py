import os

restaurantes = [{'nome':'Cabritim', 'categoria': 'Bar', 'ativo': False},
                {'nome': 'MacDonalds', 'categoria': 'FastFood', 'ativo': True}] 

def exibir_nome():
  print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ\n')

def exibir_opcoes():

 print('1.Cadastrar Restaurante')
 print('2.Listar Restaurantes')
 print('3.Ativar Restaurante')
 print('4.Sair\n')



def finalizar_app():
    os.system('cls')
    print('Não é um adeus, mas um até logo!')

def back():
    input('\n\nDigite uma tecla para voltar para o home.\n\n')
    main()

def opcao_invalida():
   print('Opção inválida\n')
   back()

def cadastrar_novo_restaurante():
  os.system('cls')
  print('| Cadastro de novos restaurantes | \n')
  nome_restaurante = input('Informe o nome do restaurante que deseja cadastrar:')
  categoria = input('Informe a categoria do restaurante {nome_restaurante}:')
  dados_do_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo':False}
  restaurantes.append(dados_do_restaurante)
  back()
   
def listar_restaurantes():
  os.system('cls')
  print('|Lista de Restaurantes|\n')

  for restaurante in restaurantes:
    nome_restaurante = restaurante['nome']
    categoria = restaurante['categoria']
    ativo = 'ativo' if restaurante['ativo'] else 'desativado'
    print(f'.{nome_restaurante} | {categoria} | {ativo}')
  
  back()

def status():
  os.system('cls')
  print('| Status |\n')
  nome_restaurante = input('Digite o nome do restaurante que deseja alterar status:')
  busca = False
  for restaurante in restaurantes:
    if nome_restaurante == restaurante['nome']:
     busca = True
     restaurante ['ativo'] = not restaurante['ativo']
  if not busca:
    print('O restaurante não foi encontrado, que pena!\n')


  back()


def escolher_opcao():
 try:

     opcao_escolhida = int(input('Escolha uma opção: ')) 

     if opcao_escolhida == 1: 
       cadastrar_novo_restaurante() 
     elif opcao_escolhida == 2:
       listar_restaurantes()
     elif opcao_escolhida == 3:
       status()
     elif opcao_escolhida == 4:
       finalizar_app()
     else:
       opcao_invalida() 
 except:  
  opcao_invalida() 
      
   

def main():
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
  