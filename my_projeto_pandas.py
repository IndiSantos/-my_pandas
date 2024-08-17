import pandas as pd

# Simulação dos dados de estoque e vendas
dados_estoque = {
    'ID_Peca': [101, 102, 103, 104, 105],
    'Descricao': ['Filtro de Óleo', 'Pastilha de Freio', 'Bateria 60Ah', 'Pneu Aro 16', 'Amortecedor Dianteiro'],
    'Estoque_Atual': [5, 12, 0, 8, 3],
    'Estoque_Minimo': [3, 10, 2, 5, 2],
    'Vendas_Mensais': [20, 35, 15, 10, 25]
}

# Criando o DataFrame com os dados
df_estoque = pd.DataFrame(dados_estoque)

# Exibindo o DataFrame inicialprint("Dados Iniciais do Estoque:")
print(df_estoque)
print("\n")

# 1. Identificar as peças com estoque abaixo do mínimo recomendado
estoque_critico = df_estoque[df_estoque['Estoque_Atual'] < df_estoque['Estoque_Minimo']]
print("Peças com Estoque Abaixo do Mínimo:")
print(estoque_critico)
print("\n")

# 2. Identificar as peças com maior demanda (vendas mensais)
peças_mais_vendidas = df_estoque[df_estoque['Vendas_Mensais'] > df_estoque['Vendas_Mensais'].mean()]
print("Peças com Maior Demanda (acima da média):")
print(peças_mais_vendidas)
print("\n")

# 3. Sugerir reposição de estoque para peças críticas (com base em estoque e vendas)
df_estoque['Sugestao_Reposicao'] = df_estoque.apply(lambda row: 'Repor'if row['Estoque_Atual'] < row['Estoque_Minimo'] else'OK', axis=1)
print("Sugestão de Reposição de Estoque:")
print(df_estoque[['ID_Peca', 'Descricao', 'Estoque_Atual', 'Sugestao_Reposicao']])

# 4. Análise de disponibilidade e tempo de atendimento (simulação simples)# Considerando que menor estoque pode aumentar tempo de espera
df_estoque['Impacto_Tempo_Atendimento'] = df_estoque['Estoque_Atual'].apply(lambda x: 'Alto'if x < 3else'Baixo')
print("\nImpacto no Tempo de Atendimento (estimado):")
print(df_estoque[['ID_Peca', 'Descricao', 'Impacto_Tempo_Atendimento']])