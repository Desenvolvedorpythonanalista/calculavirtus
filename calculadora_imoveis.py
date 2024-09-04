import streamlit as st
import pandas as pd

# Configuração da interface do Streamlit
st.set_page_config(page_title="Calculadora de Imóvel", layout="wide")

def calcular_imovel(valor_inicial, valor_venda, obra, taxa_juros, entrada_percentual):
    # Definir o período do financiamento
    periodo_financiamento = 360  # 30 anos

    # Cálculo da taxa de juros mensal
    taxa_juros_mensal = taxa_juros / 100 / 12

    # Cálculo do valor da entrada
    valor_entrada = valor_inicial * (entrada_percentual / 100)

    # Cálculo do valor total do financiamento
    valor_total_financiamento = valor_inicial - valor_entrada

    # Calcular o valor da parcela mensal
    if taxa_juros_mensal > 0:
        valor_parcela = calcular_parcela(valor_total_financiamento, taxa_juros_mensal, periodo_financiamento)
    else:
        valor_parcela = valor_total_financiamento / periodo_financiamento

    # Cálculo do custo total
    gasto_total = valor_inicial + obra

    # Cálculo do faturamento bruto
    faturamento_bruto = valor_venda - gasto_total

    # Cálculo da margem de lucro de 30%
    margem_lucro = faturamento_bruto * 0.30

    # Cálculo do lucro real
    lucro_real = faturamento_bruto

    # Percentual de aumento
    percentual_aumento = ((valor_venda - valor_inicial) / valor_inicial) * 100

    # Distribuição dos 70% do faturamento bruto
    despesas = faturamento_bruto * 0.70
    investimento_proximo_imovel = despesas * 0.40
    trafego_pago = despesas * 0.15
    produtora_audiovisual = despesas * 0.075
    social_media = despesas * 0.075
    gerente_comercial = despesas * 0.075
    contador = despesas * 0.075
    material_audiovisual = despesas * 0.15

    # Distribuição das despesas fixas
    desp_fixas_total = despesas * 0.30
    recursos_humanos = desp_fixas_total * 0.20
    ponto_comercial = desp_fixas_total * 0.20
    manutencao_paginas_web = desp_fixas_total * 0.20
    administrador = desp_fixas_total * 0.20
    advogado_empresarial = desp_fixas_total * 0.20

    # Distribuição da margem de lucro
    distrib_lucro_margem = {
        '50% para o caixa da empresa': margem_lucro * 0.50,
        '50% distribuído': margem_lucro * 0.50
    }

    # Distribuição do caixa da empresa
    caixa_empresa = distrib_lucro_margem['50% para o caixa da empresa']
    investimentos_fixa_variavel = {
        'Investimentos de Renda Fixa': caixa_empresa * 0.50,
        'Investimentos de Renda Variável': caixa_empresa * 0.50
    }

    # Distribuição do valor distribuído
    valor_distribuido = distrib_lucro_margem['50% distribuído']
    distribuicao_socios = {
        'Sócio 1': valor_distribuido * 0.50,
        'Sócio 2': valor_distribuido * 0.50
    }

    resultados = {
        'Faturamento Bruto': faturamento_bruto,
        'Gasto Total Atualizado': gasto_total,
        'Margem de Lucro 30%': margem_lucro,
        'Lucro Real': lucro_real,
        'Percentual de Aumento no Preço de Venda': percentual_aumento,
        'Valor Total do Financiamento': valor_total_financiamento,
        'Valor das Parcelas do Financiamento': valor_parcela,
        'Custo Operacional': gasto_total,
        'Valor da Entrada': valor_entrada,
        'Despesas (70% do Faturamento Bruto)': despesas
    }

    return resultados, distrib_lucro_margem, investimento_proximo_imovel, trafego_pago, produtora_audiovisual, social_media, gerente_comercial, contador, material_audiovisual, recursos_humanos, ponto_comercial, manutencao_paginas_web, administrador, advogado_empresarial, investimentos_fixa_variavel, distribuicao_socios

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
entrada_percentual = st.slider('Percentual de Entrada (%):', min_value=0, max_value=100, value=20)

if st.button('Calcular Imóvel'):
    # Calcular resultados
    resultados, distrib_lucro_margem, investimento_proximo_imovel, trafego_pago, produtora_audiovisual, social_media, gerente_comercial, contador, material_audiovisual, recursos_humanos, ponto_comercial, manutencao_paginas_web, administrador, advogado_empresarial, investimentos_fixa_variavel, distribuicao_socios = calcular_imovel(valor_inicial, valor_venda, obra, taxa_juros, entrada_percentual)

    # Exibição dos resultados gerais
    st.subheader('Resultados Gerais')

    resultados_df = pd.DataFrame.from_dict({
        'Descrição': [
            'Faturamento Bruto',
            'Gasto Total Atualizado',
            'Margem de Lucro 30%',
            'Lucro Real',
            'Percentual de Aumento no Preço de Venda',
            'Valor Total do Financiamento',
            'Valor das Parcelas do Financiamento',
            'Custo Operacional',
            'Valor da Entrada',
            'Despesas (70% do Faturamento Bruto)'
        ],
        'Valor': [
            f'R$ {resultados["Faturamento Bruto"]:,.2f}',
            f'R$ {resultados["Gasto Total Atualizado"]:,.2f}',
            f'R$ {resultados["Margem de Lucro 30%"]:,.2f}',
            f'R$ {resultados["Lucro Real"]:,.2f}',
            f'{resultados["Percentual de Aumento no Preço de Venda"]:.2f}%',
            f'R$ {resultados["Valor Total do Financiamento"]:,.2f}',
            f'R$ {resultados["Valor das Parcelas do Financiamento"]:,.2f}',
            f'R$ {resultados["Custo Operacional"]:,.2f}',
            f'R$ {resultados["Valor da Entrada"]:,.2f}',
            f'R$ {resultados["Despesas (70% do Faturamento Bruto)"]:,.2f}'
        ]
    })

    st.dataframe(resultados_df, use_container_width=True)

    # Exibição das despesas
    st.subheader('Despesas (70% do Faturamento Bruto)')

    despesas_df = pd.DataFrame.from_dict({
        'Descrição': [
            'Investimento para o Próximo Imóvel (40% das Despesas)',
            'Tráfego Pago (15% das Despesas)',
            'Produtora Audiovisual (7,5% das Despesas)',
            'Social Media (7,5% das Despesas)',
            'Gerente Comercial (7,5% das Despesas)',
            'Contador (7,5% das Despesas)',
            'Material Audiovisual (15% das Despesas)'
        ],
        'Valor': [
            f'R$ {investimento_proximo_imovel:,.2f}',
            f'R$ {trafego_pago:,.2f}',
            f'R$ {produtora_audiovisual:,.2f}',
            f'R$ {social_media:,.2f}',
            f'R$ {gerente_comercial:,.2f}',
            f'R$ {contador:,.2f}',
            f'R$ {material_audiovisual:,.2f}'
        ]
    })

    st.dataframe(despesas_df, use_container_width=True)

    # Exibição das despesas fixas
    st.subheader('Despesas Fixas (30% das Despesas)')

    despesas_fixas_df = pd.DataFrame.from_dict({
        'Descrição': [
            'Recursos Humanos (20% das Despesas Fixas)',
            'Ponto Comercial (20% das Despesas Fixas)',
            'Manutenção Páginas Web (20% das Despesas Fixas)',
            'Administrador (20% das Despesas Fixas)',
            'Advogado Empresarial (20% das Despesas Fixas)'
        ],
        'Valor': [
            f'R$ {recursos_humanos:,.2f}',
            f'R$ {ponto_comercial:,.2f}',
            f'R$ {manutencao_paginas_web:,.2f}',
            f'R$ {administrador:,.2f}',
            f'R$ {advogado_empresarial:,.2f}'
        ]
    })

    st.dataframe(despesas_fixas_df, use_container_width=True)

    # Exibição da distribuição da margem de lucro
    st.subheader('Distribuição da Margem de Lucro')

    margem_lucro_df = pd.DataFrame.from_dict({
        'Descrição': [
            '50% para o Caixa da Empresa',
            '50% Distribuído entre Sócios'
        ],
        'Valor': [
            f'R$ {distrib_lucro_margem["50% para o caixa da empresa"]:,.2f}',
            f'R$ {distrib_lucro_margem["50% distribuído"]:,.2f}'
        ]
    })

    st.dataframe(margem_lucro_df, use_container_width=True)

    # Exibição dos investimentos do caixa da empresa
    st.subheader('Investimentos do Caixa da Empresa')

    investimentos_fixa_variavel_df = pd.DataFrame.from_dict({
        'Descrição': [
            'Investimentos de Renda Fixa',
            'Investimentos de Renda Variável'
        ],
        'Valor': [
            f'R$ {investimentos_fixa_variavel["Investimentos de Renda Fixa"]:,.2f}',
            f'R$ {investimentos_fixa_variavel["Investimentos de Renda Variável"]:,.2f}'
        ]
    })

    st.dataframe(investimentos_fixa_variavel_df, use_container_width=True)

    # Exibição da distribuição para os sócios
    st.subheader('Distribuição para os Sócios')

    distribuicao_socios_df = pd.DataFrame.from_dict({
        'Descrição': [
            'Sócio 1',
            'Sócio 2'
        ],
        'Valor': [
            f'R$ {distribuicao_socios["Sócio 1"]:,.2f}',
            f'R$ {distribuicao_socios["Sócio 2"]:,.2f}'
        ]
    })

    st.dataframe(distribuicao_socios_df, use_container_width=True)
