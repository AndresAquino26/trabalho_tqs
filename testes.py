# Testes

import unittest
import os
from funcoes import calcular_preco, validar_qtd_bilhetes

# TESTES CONSIDERANDO O CONTEÚDO DE SALA DE AULA - Bateria de testes 1
# INTERVALO (DADO DE ENTRADA - IDADE VÁLIDA)
# QUALQUER VALOR DE 0 - 130 (VÁLIDA) // ACIMA OU ABAIXO DISSO (INVÁLIDAS)

class TestIntervaloIdade(unittest.TestCase):
    """Testes para intervalo de idade"""
    
    def test_idade_valida(self):
        """PARTIÇÃO VÁLIDA: apenas 1 valor válido entre 0 e 130 (50 anos)"""
        self.assertEqual(calcular_preco(50), 30)
        
    def test_idade_invalida_abaixo(self):
        """PARTIÇÃO INVÁLIDA 1: apenas 1 valor abaixo (idade negativa)"""
        self.assertEqual(calcular_preco(-5), -1)
        
    def test_idade_invalida_acima(self):
        """PARTIÇÃO INVÁLIDA 2: apenas 1 valor acima (135 anos)"""
        self.assertEqual(calcular_preco(135), -1)



# TESTES CONSIDERANDO O CONTEÚDO DE SALA DE AULA - Bateria de testes 2
# QUANTIDADE - QUANTIDADE DE BILHETES
# 1 - 5 (VÁLIDA) // STRING, QUATRO VALORES (INVÁLIDAS)

class TestQuantidadeBilhetes(unittest.TestCase):
    """Testes para quantidade de bilhetes"""
    
    def test_quantidade_valida(self):
        """PARTIÇÃO VÁLIDA 1: recebe apenas 1 número qualquer entre 1 e 5"""
        self.assertTrue(validar_qtd_bilhetes(3))
    
    def test_quantidade_invalida_string(self):
        """PARTIÇÃO INVÁLIDA 1: recebe uma string"""
        with self.assertRaises(TypeError):
            validar_qtd_bilhetes("a") 
    
    def test_quantidade_invalida_multiplos_numeros(self):
        """PARTIÇÃO INVÁLIDA 2: recebe 4 números"""       
        with self.assertRaises(TypeError):
            self.assertFalse(validar_qtd_bilhetes("2 3 4 5"))




# TESTES CONSIDERANDO O CONTEÚDO DE SALA DE AULA - Bateria de testes 3
# CONJUNTO DETERMINADO DE VALORES - TESTANDO OS RANGES DE IDADE E SEUS RETORNOS EM FORMA DE PREÇO
# UMA IDADE PARA CADA RANGE (VÁLIDAS) // IDADE NEGATIVA (INVÁLIDA) E IDADE ACIMA DE 130 (INVÁLIDA)

class TestFaixasIdade(unittest.TestCase):
    """Testes para conjuntos de valores"""
    
    def test_faixa_crianca_valida(self):
        """PARTIÇÃO VÁLIDA 1: IDADE PRIMEIRO RANGE (0 A 12) (5 anos = R$ 10)"""
        self.assertEqual(calcular_preco(5), 10)
    
    def test_faixa_adulto_valida(self):
        """PARTIÇÃO VÁLIDA 2: IDADE SEGUNDO RANGE (13 A 59) (30 anos = R$ 30)"""
        self.assertEqual(calcular_preco(30), 30)
    
    def test_faixa_idoso_valida(self):
        """PARTIÇÃO VÁLIDA 3: IDADE TERCEIRO RANGE (60+) (65 anos = R$ 15)"""
        self.assertEqual(calcular_preco(65), 15)
    
    def test_idade_invalida_geral_abaixo(self):
        """PARTIÇÃO INVÁLIDA: IDADE NEGATIVA (-5 anos)"""
        self.assertEqual(calcular_preco(-5), -1)

    def test_idade_invalida_geral_acima(self):
        """PARTIÇÃO INVÁLIDA: IDADE ACIMA DO LIMITE PERMITIDO (150 anos)"""
        self.assertEqual(calcular_preco(150), -1)



# TESTES CONSIDERANDO O CONTEÚDO DE SALA DE AULA - Bateria de testes 4
# ANÁLISE DO VALOR LIMITE - INTERVALO (DADO DE ENTRADA - IDADE VÁLIDA)
# 0 E 130 (VÁLIDAS) // "0 - 1" e "130 + 1" (INVÁLIDAS) - Como visto em sala, pegaremos o valor mais próximo do limite inferior e superior p/ teste.

class TestIntervaloValorLimite(unittest.TestCase):
    """Testes para intervalo de idade"""
    
    def test_idade_valida_valor_limite_abaixo(self):
        """PARTIÇÃO VÁLIDA 1: limite inferior (0)"""
        self.assertEqual(calcular_preco(0), 10)

    def test_idade_valida_valor_limite_acima(self):
        """PARTIÇÃO VÁLIDA 2: limite superior (130)"""
        self.assertEqual(calcular_preco(130), 15) 
        
    def test_idade_invalida_valor_limite_abaixo(self):
        """PARTIÇÃO INVÁLIDA 1: (limite inferior - 1) = -1"""
        self.assertEqual(calcular_preco(-1), -1)
        
    def test_idade_invalida_valor_limite_acima(self):
        """PARTIÇÃO INVÁLIDA 2: (limite superior + 1) = 131"""
        self.assertEqual(calcular_preco(131), -1)



# TESTES CONSIDERANDO O CONTEÚDO DE SALA DE AULA - Bateria de testes 5
# ANÁLISE DO VALOR LIMITE - QUANTIDADE - QUANTIDADE DE BILHETES
# RECEBER APENAS UM VALOR ENTRE 1 E 5 INDICANDO A QTD DE BILHETES (VÁLIDA) // RECEBER NENHUM VALOR (limite - 1)
# ou RECEBER DOIS VALORES (limite + 1) (INVÁLIDAS) 

class TestQuantidadeBilhetesValorLimite(unittest.TestCase):
    """Testes para quantidade de bilhetes"""
    
    def test_quantidade_valida_valor_limite(self):
        """PARTIÇÃO VÁLIDA 1: recebe apenas 1 número qualquer entre 1 e 5"""
        self.assertTrue(validar_qtd_bilhetes(4))  
    
    def test_quantidade_invalida_vazio_valor_limite(self):
        """PARTIÇÃO INVÁLIDA 1: recebe 0 números (1-1 = 0 -> vazio)"""
        with self.assertRaises(TypeError):
            validar_qtd_bilhetes("") 
    
    def test_quantidade_invalida_dois_numeros_valor_limite(self):
        """PARTIÇÃO INVÁLIDA 2: recebe 2 números (1+1)"""
        with self.assertRaises(TypeError):
            self.assertFalse(validar_qtd_bilhetes("1 2")) 



if __name__ == '__main__':

    test_classes = [
        TestIntervaloIdade,
        TestQuantidadeBilhetes,
        TestFaixasIdade,
        TestIntervaloValorLimite,
        TestQuantidadeBilhetesValorLimite
    ]
    
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    for test_class in test_classes:
        suite.addTests(loader.loadTestsFromTestCase(test_class))
    
    runner = unittest.TextTestRunner(verbosity=0)
    
    print("\n=== EXECUÇÃO DE TESTES ===")
    result = runner.run(suite)
    print(f"\nRESUMO FINAL:")
    print(f"Total de baterias: 5")
    print(f"Total de testes: {result.testsRun}")
    print(f"Status: {'Nenhum teste falhou!' if result.wasSuccessful() else 'Algum teste falhou!'}")
