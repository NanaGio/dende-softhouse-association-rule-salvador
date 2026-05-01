import re
import pandas as pd
from collections import Counter

class DendeDatasetClear:
    def __init__(self, df):
        self.df = df

    def _clear_products(self, df):
        df = self.df
        # o código abaixo remove os espaços em branco no início e no final da string, converte para minúsculas e remove caracteres especiais
        df["descricao_produtos"] = df["descricao_produtos"].str.strip().str.lower()
        # o código abaixo remove caracteres especiais
        df["descricao_produtos"] = df["descricao_produtos"].str.replace(r'[^\w\s]+', ' ', regex=True)
        self.df = df
        return self.df

    def preprocess_transactions(self, df):
        df = self._clearProducts(df)
        count = Counter()
        transactions = []
        stopwords = {
            "de",
            "com",
            "e",
            "c",
            "para",
            "a",
            "o",
            "da",
            "do",
            "em",
        }
        # O código abaixo percorre cada linha do DataFrame, limpa a descrição dos produtos e conta a frequência das palavras, removendo stopwords, palavras curtas, números puros e medidas técnicas.
        for _, row in df.iterrows():
            products = row["descricao_produtos"]
            transaction_id = row["id_transacao"]
            cleaned_transaction = []
            itens = str(products).split(";")

            for item in itens:
                words = item.split()

                filtered_words = []
                for word in words:
                    # Remove stopwords
                    if word in stopwords:
                        continue
                    
                    # 1. Remove palavras com 3 letras ou menos (ex: cm, x, fem)
                    # "kids" e "baby" ficam porque têm 4 letras
                    if len(word) <= 3:
                        continue
                    
                    # 2. Remove números puros
                    if word.isdigit():
                        continue
                    
                    # 3. Remove medidas puramente técnicas (ex: 10cm, 50cm)
                    if re.match(r"^\d+cm$", word):
                        continue
                    
                    filtered_words.append(word)
                    cleaned_transaction.append(word)

                count.update(filtered_words)
            # Remove palavras duplicadas na mesma transação
            cleaned_transaction = list(set(cleaned_transaction))
            # Adiciona a transação limpa à lista de transações
            transactions.append({
                "id_transacao": transaction_id,
                "transactions": cleaned_transaction
            })

        most_common = count.most_common(25)
        print("As 25 palavras mais comuns são:")
        for word, freq in most_common:
            print(f"{word}: {freq}")
        # print(transactions[:15])  # Exibe as primeiras 15 transações limpas

        # O código abaixo cria um DataFrame a partir da lista de transações limpas, onde cada linha representa
        # uma transação e as colunas são "id_transacao" e "transactions", onde "transactions" é uma string contendo
        # os produtos separados por ponto e vírgula.
        transactions_df = pd.DataFrame({
            "id_transacao": [
                transaction["id_transacao"]
                for transaction in transactions
            ],
            "transactions": [
                ";".join(transaction["transactions"])
                for transaction in transactions
            ]
        })

        transactions_df.to_csv(
            "transactions_cleaned.csv",
            index=False
        )

        return transactions_df


    
    