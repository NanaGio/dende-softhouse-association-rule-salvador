import pandas as pd

itemset = pd.read_csv('../transactions_cleaned.csv')

class Apriori:
    def __init__(self, dataset):
        self.df = dataset

    def calcular_suporte(self, item):
        return self.df[item].mean()

    def obter_item_frequente(self, itemset):
        itemset = {}
        treshold = 0.05
        for item in self.df.columns:
            c1_unicos = item.value_counts()
            suporte_item = self.calcular_suporte(item)
            if suporte_item >= treshold:
                itemset[item] = suporte_item
            return itemset











