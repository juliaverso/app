from avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
     self._nome = nome.title()
     self._categoria = categoria.upper()
     self._ativo = False
     self._avaliacao = []
     Restaurante.restaurantes.append(self)
    
    def __srt__(self):
       return f'{self._nome} | {self._categoria}'
    
    def status(self):   
       self._ativo = not self._ativo 
       
    @classmethod
    def listar_restaurantes(cls):
       print('| Lista de Restaurantes |\n')
       for restaurante in Restaurante.restaurantes:
          print(f'{restaurante._nome} | {restaurante._categoria} | {restaurante.media_avaliacoes} | {restaurante.ativo}')

    @property
    def ativo(self):
       return 'Em ação' if self._ativo else 'Em descanso' 
    
    def receber_avaliacao(self, cliente, nota):
      if 0< nota<= 5:
       avaliacao = Avaliacao(cliente, nota)
       self._avaliacao.append(avaliacao)

    @property 
    def media_avaliacoes(self):
       if not self._avaliacao:
          return '-'
       soma_das_notas = sum (avaliacao._nota for avaliacao in self._avaliacao)
       quantidade_de_notas = len(self._avaliacao)
       media = round(soma_das_notas/quantidade_de_notas, 1)
       return media

   
   
   

