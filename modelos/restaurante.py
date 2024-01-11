class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
     self._nome = nome.title()
     self._categoria = categoria.upper()
     self._ativo = False
     Restaurante.restaurantes.append(self)
    
    def __srt__(self):
       return f'{self._nome} | {self._categoria}'
    
    def status(self):   
       self._ativo = not self._ativo 
       
    @classmethod
    def listar_restaurantes(cls):
       print('| Lista de Restaurantes |\n')
       for restaurante in Restaurante.restaurantes:
          print(f'{restaurante._nome} | {restaurante._categoria} | {restaurante.ativo}')

    @property
    def ativo(self):
       return 'Em ação' if self._ativo else 'Em descanso' 

