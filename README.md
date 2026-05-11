# Desafio 3 - Regras de Associação para Recomendação de Produtos

Sejam bem-vindos à terceira etapa do nosso programa! 🎉

Neste desafio, nosso foco é desenvolver um **modelo de recomendação** para os usuários, utilizando **regras de associação**, um dos algoritmos mais interessantes na identificação de padrões em dados.

---

## Objetivo

O objetivo principal deste desafio é **extrair padrões de consumo** e gerar insights para **combos de produtos** no segmento de vestuário. Como trainees da área de dados, vocês irão:

1. Analisar transações de clientes.
2. Aplicar algoritmos de regras de associação.
3. Gerar recomendações baseadas em padrões frequentes de consumo.

---

## Sobre Regras de Associação

Os **algoritmos de regras de associação** identificam padrões frequentes nos dados, auxiliando em diversas atividades:

- **Análise de cesta de pedidos:** identificar itens que são frequentemente comprados juntos.
- **Segmentação de clientes:** agrupar clientes com base em hábitos de consumo.
- **Detecção de fraudes:** reconhecer padrões anormais de comportamento em transações.

Apesar da sua versatilidade, esses algoritmos lidam com **problemas NP-Completos**, o que significa que encontrar a **solução ótima global** é computacionalmente inviável para grandes bases de dados. Por isso, utilizamos **heurísticas** que buscam soluções ótimas locais em tempo polinomial, como:

- **Apriori**
- **FP-Growth**
- **ECLAT**

---

## Dataset

Nesta etapa, os dados fornecidos representam transações de microempreendedores do **segmento de vestuário**. Cada registro corresponde a uma transação contendo uma lista de itens adquiridos pelo cliente.

> Dica: talvez seja interessante começar com um **suporte baixo (~0,5%)** e tratar os itens das transações, removendo marcas ou informações irrelevantes das descrições.

---

## Como usar este repositório

1. **Pré-processamento dos dados**: limpar e preparar os dados de transações.
2. **Aplicar algoritmo de regras de associação**: Apriori, FP-Growth ou ECLAT.
3. **Analisar resultados**: interpretar padrões frequentes e gerar insights para combos de produtos.

ps:
Como executar dende metrics.py

Para garantir que o script consiga localizar os arquivos de dados (`.csv`) corretamente, **é necessário executar o comando a partir da pasta raiz** do projeto.

No terminal, utilize o seguinte comando:

```bash
python src/dende_metrics.py
--- 

## Referências

- [Livro: Data Mining Concepts and Techniques - Han, Kamber, Pei](https://www.sciencedirect.com/book/9780123814791/data-mining-concepts-and-techniques)
- [Apriori Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Apriori_algorithm)
- [Apriori Algorithm - DataCamp](https://www.datacamp.com/tutorial/apriori-algorithm)
- [Apriori Algorithm - Medium](https://medium.com/@bernardo.costa/uma-introdu%C3%A7%C3%A3o-ao-algoritmo-apriori-60b11293aa5a)
- [FP-Growth Algorithm - Wikipedia](https://en.wikipedia.org/wiki/FP-growth_algorithm)
- [FP-Growth Algorithm - Medium](https://medium.com/image-processing-with-python/fp-growth-algorithm-in-data-mining-e1064accf6a3)
- [FP-Growth Algorithm - Medium](https://medium.com/@anilcogalan/fp-growth-algorithm-how-to-analyze-user-behavior-and-outrank-your-competitors-c39af08879db)
- [ECLAT](https://quality-life.medium.com/eclat-algorithm-in-machine-learning-fe07d33fcc5b)
- [ECLAT](https://medium.com/@gabrielreversi/association-rules-the-eclat-algorithm-96d47f32f992)
---
