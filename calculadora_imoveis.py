import streamlit as st
import pandas as pd

# Configuração da interface do Streamlit
st.set_page_config(page_title="Calculadora de Imóvel", layout="wide")

def calcular_imovel(valor_inicial, valor_venda, obra, taxa_juros):
    # Definir o período do financiamento
    periodo_financiamento = 360  # 30 anos

    # Cálculo da taxa de juros mensal
    taxa_juros_mensal = taxa_juros / 100 / 12

    # Cálculo do valor total do financiamento
    valor_total_financiamento = valor_venda - valor_inicial

    # Calcular o valor da parcela mensal
    if taxa_juros_mensal > 0:
        valor_parcela = calcular_parcela(valor_total_financiamento, taxa_juros_mensal, periodo_financiamento)
    else:
        valor_parcela = valor_total_financiamento / periodo_financiamento

    # Cálculo dos custos
    entrada_leilao = valor_inicial * 0.05
    entrada_reforma = obra * 0.20
    gasto_total = entrada_leilao + obra + entrada_reforma + valor_total_financiamento

    # Cálculo do lucro real e presumido
    lucro_antes_dos_custos = valor_venda - valor_inicial
    lucro_real = lucro_antes_dos_custos - gasto_total

    # Cálculo de impostos para Lucro Real
    imposto_real = lucro_real * (0.15 + 0.09)  # 15% IRPJ + 9% CSLL
    lucro_real -= imposto_real

    # Cálculo de impostos para Lucro Presumido
    receita_bruta_presumida = valor_venda - valor_inicial
    base_presumida = receita_bruta_presumida * 0.08  # Presumido 8%
    imposto_presumido = base_presumida * (0.08 + 0.12)  # 8% IRPJ + 12% CSLL
    lucro_presumido = receita_bruta_presumida - imposto_presumido

    # Percentual de aumento
    percentual_aumento = ((valor_venda - valor_inicial) / valor_inicial) * 100

    # Distribuição do lucro
    distribucao_real = {
        '70% para o caixa da empresa': lucro_real * 0.70,
        '30% distribuído': lucro_real * 0.30
    }
    distribuicao_presumida = {
        '70% para o caixa da empresa': lucro_presumido * 0.70,
        '30% distribuído': lucro_presumido * 0.30
    }

    resultados = {
        'Gasto Total': gasto_total,
        'Lucro Real': lucro_real,
        'Lucro Presumido': lucro_presumido,
        'Percentual de Aumento': percentual_aumento,
        'Valor Total do Financiamento': valor_total_financiamento,
        'Valor das Parcelas do Financiamento': valor_parcela
    }
    
    return resultados, distribucao_real, distribuicao_presumida

def calcular_parcela(valor_total, taxa_juros_mensal, periodo_financiamento):
    """ Calcula o valor da parcela mensal usando a fórmula de financiamento """
    return valor_total * (taxa_juros_mensal * (1 + taxa_juros_mensal) ** periodo_financiamento) / ((1 + taxa_juros_mensal) ** periodo_financiamento - 1)

# Configuração da interface do Streamlit
st.title('Calculadora de Imóvel')

# Inputs
valor_inicial = st.number_input('Valor do apartamento inicial:', min_value=0.0, format="%.2f")
valor_venda = st.number_input('Valor da venda do apartamento:', min_value=0.0, format="%.2f")
obra = st.number_input('Valor da obra:', min_value=0.0, format="%.2f")
taxa_juros = st.number_input('Taxa de juros anual (%):', min_value=0.0, format="%.2f")

if st.button('Calcular Imóvel'):
    # Calcular resultados
    resultados, distribuicao_real, distribuicao_presumida = calcular_imovel(valor_inicial, valor_venda, obra, taxa_juros)
    
    # Exibição dos resultados
    st.subheader('Resultados Gerais')
    
    # Tabela de resultados principais
    resultados_df = pd.DataFrame.from_dict({
        'Descrição': [
            'Gasto Total Atualizado',
            'Lucro Real',
            'Lucro Presumido',
            'Percentual de Aumento no Preço de Venda',
            'Valor Total do Financiamento',
            'Valor das Parcelas do Financiamento'
        ],
        'Valor': [
            f'R$ {resultados["Gasto Total"]:,.2f}',
            f'R$ {resultados["Lucro Real"]:,.2f}',
            f'R$ {resultados["Lucro Presumido"]:,.2f}',
            f'{resultados["Percentual de Aumento"]:.2f}%',
            f'R$ {resultados["Valor Total do Financiamento"]:,.2f}',
            f'R$ {resultados["Valor das Parcelas do Financiamento"]:,.2f}'
        ]
    })

    st.dataframe(resultados_df, use_container_width=True)

    # Tabela de distribuição do lucro real
    distribuicao_real_df = pd.DataFrame.from_dict({
        'Descrição': [
            '70% para o caixa da empresa',
            '30% distribuído'
        ],
        'Valor': [
            f'R$ {distribuicao_real["70% para o caixa da empresa"]:,.2f}',
            f'R$ {distribuicao_real["30% distribuído"]:,.2f}'
        ]
    })
    
    st.subheader('Distribuição do Lucro Real')
    st.dataframe(distribuicao_real_df, use_container_width=True)

    # Tabela de distribuição do lucro presumido
    distribuicao_presumida_df = pd.DataFrame.from_dict({
        'Descrição': [
            '70% para o caixa da empresa',
            '30% distribuído'
        ],
        'Valor': [
            f'R$ {distribuicao_presumida["70% para o caixa da empresa"]:,.2f}',
            f'R$ {distribuicao_presumida["30% distribuído"]:,.2f}'
        ]
    })
    
    st.subheader('Distribuição do Lucro Presumido')
    st.dataframe(distribuicao_presumida_df, use_container_width=True)

    # Cálculo de valores distribuídos aos sócios
    valor_distribuido_real = distribuicao_real['30% distribuído']
    valor_distribuido_presumido = distribuicao_presumida['30% distribuído']

    # Definição das tabelas para distribuição aos sócios
    distribuicao_socios_real_df = pd.DataFrame.from_dict({
        'Descrição': [
            'Distribuição Real aos Sócios (50% do valor distribuído)',
            'Cada sócio recebe (dividido por 2)'
        ],
        'Valor': [
            f'R$ {valor_distribuido_real * 0.50:,.2f}',
            f'R$ {valor_distribuido_real * 0.50 / 2:,.2f}'
        ]
    })

    distribuicao_socios_presumida_df = pd.DataFrame.from_dict({
        'Descrição': [
            'Distribuição Presumida aos Sócios (50% do valor distribuído)',
            'Cada sócio recebe (dividido por 2)'
        ],
        'Valor': [
            f'R$ {valor_distribuido_presumido * 0.50:,.2f}',
            f'R$ {valor_distribuido_presumido * 0.50 / 2:,.2f}'
        ]
    })

    st.subheader('Distribuição Real aos Sócios')
    st.dataframe(distribuicao_socios_real_df, use_container_width=True)

    st.subheader('Distribuição Presumida aos Sócios')
    st.dataframe(distribuicao_socios_presumida_df, use_container_width=True)
