import pandas as pd
from itertools import combinations 

from dende_apriori import Apriori
#Importando a classe que giovanna criou

dados = pd.read_csv('transactions_cleaned.csv')
#Carregando os dados que antonio limpou

fase1 = Apriori(dados)
#Puxa o apriori

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

    suporte_combo = (dados[item_a] * dados[item_b]).mean()

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