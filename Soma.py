from Operacao import *

class Soma(Operacao):
  @classmethod
  def executar(self,valor1,valor2):
    resultado = valor1 + valor2
    return resultado