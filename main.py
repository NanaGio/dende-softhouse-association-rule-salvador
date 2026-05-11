import pandas as pd
from itertools import combinations 

from src.dende_utils import DendeDatasetClear
from src.dende_apriori import Apriori
#Importando as classes que a equipe criou

dados_brutos = pd.read_csv('vendas_dataset.csv')
#Carregando os dados brutos de vendas que a gente recebeu

limpeza = DendeDatasetClear(dados_brutos)
#Puxa a classe de limpeza de dados

dados_limpos = limpeza.preprocess_transactions(dados_brutos)
#Processa os dados, binariza e já salva o transactions_cleaned.csv

fase1 = Apriori(dados_limpos)
#Puxa o apriori com os dados limpos

itens_frequentes = fase1.obter_item_frequente()
#Puxa o dicionario de itens frequentes

nomes_das_roupas = list(itens_frequentes.keys())
#Pega os nomes das roupas aprovadas 

# remove o ID da transação antes de formar os pares
if 'id_transacao' in nomes_das_roupas:
    nomes_das_roupas.remove('id_transacao')

pares = list(combinations(nomes_das_roupas, 2))
#geramos combinações de 2 itens para calcular a métrica de interesse

combos = {}
#novo dicionario para guardar os pares e suas métricas

for par in pares:
    item_a = par[0]
    item_b = par[1] 

    suporte_combo = (dados_limpos[item_a] * dados_limpos[item_b]).mean()

    if suporte_combo >= 0.05:
        #Puxa o suporte individual de cada peça lá da Fase 1
        suporte_a = itens_frequentes[item_a]
        suporte_b = itens_frequentes[item_b]
        
        #COntas de confiança e Lift
        confianca = suporte_combo / suporte_a
        lift = confianca / suporte_b
        
        #Guarda tudo no dicionario arredondando para 4 casas decimais
        combos[par] = {
            'Suporte': round(float(suporte_combo), 4),
            'Confianca': round(float(confianca), 4),
            'Lift': round(float(lift), 4)
        }
        

print("combos interessantes para possivel campanha:", combos)
#Mostra o resultado final da execução no terminal