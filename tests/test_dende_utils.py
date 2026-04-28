import unittest
import pandas as pd
import io
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.dende_utils import DendeDatasetClear

class TestDendeDatasetClear(unittest.TestCase):

    def setUp(self):
        # Carregamos o dataset real
        dataset_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'vendas_dataset.csv'))
        self.df = pd.read_csv(dataset_path)
        
        # Instanciamos a classe que estamos testando
        self.cleaner = DendeDatasetClear(self.df)

    def test_clear_products(self):
        """
        Testa o método _clearProducts aplicando-o no dataset real e exibindo os resultados.
        """
        print("\n\n=== SAÍDA DO MÉTODO _clearProducts (Dataset Real) ===")
        print("Como os primeiros 5 registros eram antes:")
        print(self.df["descricao_produtos"].head(5).tolist())
        
        # Executa o método de limpeza
        cleaned_df = self.cleaner._clearProducts(self.df)
        
        print("\nComo os primeiros 5 registros ficaram depois:")
        print(cleaned_df["descricao_produtos"].head(5).tolist())
        print("======================================\n")

        # Verificamos se a coluna continua existindo e não está vazia após a limpeza
        self.assertTrue("descricao_produtos" in cleaned_df.columns)
        self.assertGreater(len(cleaned_df), 0)

    def test_preprocess_transactions(self):
        """
        Testa o método preprocessTransactions e captura o seu print para mostrar no terminal.
        """
        # Capturamos o que seria impresso no console
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Executa o método
        self.cleaner.preprocessTransactions(self.df)
        
        # Restaura a saída padrão do sistema
        sys.stdout = sys.__stdout__ 
        
        # Pegamos o texto que foi gerado pelo print()
        output = captured_output.getvalue()
        
        print("\n\n=== SAÍDA DO MÉTODO preprocessTransactions (Dataset Real) ===")
        print(output)
        print("======================================\n")

        # Verificamos apenas se a frase base apareceu no print, já que as palavras mudam de acordo com o CSV real
        self.assertIn("As 25 palavras mais comuns são:", output)

if __name__ == "__main__":
    unittest.main()
