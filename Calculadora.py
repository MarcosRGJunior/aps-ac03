from Divisao import Divisao
from Operacao import *
from Soma import Soma
from Subtracao import Subtracao
from Divisao  import Divisao


class Calculadora:
  @classmethod
  def calcular(self,valor1,valor2,operador):
    
    resultado = operador.executar(valor1,valor2)

    return resultado

