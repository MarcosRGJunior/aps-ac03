import unittest
from Calculadora import Calculadora
from Soma import Soma
from Subtracao import Subtracao
from Divisao import Divisao

class TesteCalculadora(unittest.TestCase):
  def TesteSoma(self):
    testeSoma = Calculadora.calcular(7,2,Soma)
    self.assertEqual(testeSoma, 9)

  def TesteSubtracao(self):
    testeSubtracao = Calculadora.calcular(1,2,Subtracao)
    self.assertEqual(testeSubtracao,-1)

  def TesteDivisao(self):
    testeDivisao = Calculadora.calcular(104,4,Divisao)
    self.assertEqual(testeDivisao,26)


if __name__ == "__main__":
  teste = TesteCalculadora()
  teste.TesteSoma()
  teste.TesteSubtracao()
  teste.TesteDivisao()

