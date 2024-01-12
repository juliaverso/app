import os
from restaurante import Restaurante

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
  categoria_restaurante = input(f'Informe a categoria de {nome_restaurante}:')
  new_restaurant = Restaurante(nome_restaurante, categoria_restaurante) 
  back()
   


def escolher_opcao():
 try:

     opcao_escolhida = int(input('Escolha uma opção: ')) 

     if opcao_escolhida == 1: 
       cadastrar_novo_restaurante() 
     elif opcao_escolhida == 2:
       Restaurante.listar_restaurantes()
       back()
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
  