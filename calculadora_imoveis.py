import streamlit as st
import pandas as pd

# Configuração da interface do Streamlit
st.set_page_config(page_title="Calculadora de Imóvel", layout="wide")

def calcular_imovel(valor_inicial, valor_venda, obra, taxa_juros, entrada_percentual, numero_vendas, meses_pagar_ate_vender):
    
    # Definir o período do financiamento
    periodo_financiamento = 360  # 30 anos

    # Cálculo da taxa de juros mensal
    taxa_juros_mensal = taxa_juros / 100 / 12

    # Cálculo do valor da entrada
    valor_entrada = valor_inicial * (entrada_percentual / 100)

    # Cálculo do saldo devedor (antes Valor Total do Financiamento)
    saldo_devedor = valor_inicial - valor_entrada

    # Cálculo do valor total do financiamento (2x o valor do saldo devedor)
    valor_total_financiamento = saldo_devedor * 2

    # Calcular o valor da parcela mensal
    if taxa_juros_mensal > 0:
        valor_parcela = calcular_parcela(saldo_devedor, taxa_juros_mensal, periodo_financiamento)
    else:
        valor_parcela = saldo_devedor / periodo_financiamento

    # Calcular o custo total das parcelas do financiamento
    custo_total_parcelas = valor_parcela * periodo_financiamento

    # Calcular o número de parcelas pagas até vender
    parcelas_ate_vender = min(meses_pagar_ate_vender, periodo_financiamento)
    custo_total_parcelas_ate_vender = valor_parcela * parcelas_ate_vender

    # Cálculo do gasto total
    gasto_total = valor_inicial + obra + custo_total_parcelas_ate_vender

    # Cálculo do faturamento bruto
    faturamento_bruto = (valor_venda - gasto_total) * numero_vendas

    # Cálculo da margem de lucro de 30%
    margem_lucro = faturamento_bruto * 0.30

    # Percentual de aumento
    percentual_aumento = ((valor_venda - valor_inicial) / valor_inicial) * 100

    # Distribuição dos 70% do faturamento bruto
    despesas = faturamento_bruto * 0.70

    # Cálculo das despesas específicas
    investimento_proximo_imovel = despesas * 0.40
    material_audiovisual = despesas * 0.15

    # Distribuição das despesas fixas
    desp_fixas_total = despesas * 0.45
    social_media = desp_fixas_total * 0.10
    produtora_audiovisual = desp_fixas_total * 0.10
    gerente_comercial = desp_fixas_total * 0.10
    contador = desp_fixas_total * 0.10
    trafego_pago = desp_fixas_total * 0.10
    recursos_humanos = desp_fixas_total * 0.10
    ponto_comercial = desp_fixas_total * 0.10
    manutencao_paginas_web = desp_fixas_total * 0.10
    administrador = desp_fixas_total * 0.10
    advogado_empresarial = desp_fixas_total * 0.10

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
        'Valor de Compra do Apartamento': valor_inicial,
        'Gasto Total Atualizado': gasto_total,
        'Valor da Venda do Apartamento': valor_venda,
        'Faturamento Bruto': faturamento_bruto,
        'Margem de Lucro 30%': margem_lucro,
        'Percentual de Aumento no Preço de Venda': percentual_aumento,
        'Valor da Entrada': valor_entrada,
        'Saldo Devedor': saldo_devedor,
        'Valor Total do Financiamento': valor_total_financiamento,
        'Valor das Parcelas do Financiamento': valor_parcela,
        'Número de Meses que Prevê Pagar até Vender': parcelas_ate_vender,
        'Custo Total das Parcelas do Financiamento até Vender': custo_total_parcelas_ate_vender,
        'Despesas (70% do Faturamento Bruto)': despesas
    }

    despesas_detalhadas = {
        'Investimento para o Próximo Imóvel (40% das Despesas)': investimento_proximo_imovel,
        'Material Audiovisual (15% das Despesas)': material_audiovisual
    }

    return resultados, distrib_lucro_margem, despesas_detalhadas, social_media, produtora_audiovisual, gerente_comercial, contador, trafego_pago, recursos_humanos, ponto_comercial, manutencao_paginas_web, administrador, advogado_empresarial, investimentos_fixa_variavel, distribuicao_socios

def calcular_parcela(valor_total, taxa_juros_mensal, periodo_financiamento):
    """ Calcula o valor da parcela mensal usando a fórmula de financiamento """
    return valor_total * (taxa_juros_mensal * (1 + taxa_juros_mensal) ** periodo_financiamento) / ((1 + taxa_juros_mensal) ** periodo_financiamento - 1)

# Configuração da interface do Streamlit
st.title('Calculadora de Imóvel')

# Inputs
valor_inicial = st.number_input('Valor de Compra do Apartamento:', min_value=0.0, format="%.2f")
valor_venda = st.number_input('Valor da Venda do Apartamento:', min_value=0.0, format="%.2f")
obra = st.number_input('Valor da Obra:', min_value=0.0, format="%.2f")
taxa_juros = st.number_input('Taxa de Juros Anual (%):', min_value=0.0, format="%.2f")
entrada_percentual = st.slider('Percentual de Entrada (%):', min_value=0, max_value=100, value=20)
numero_vendas = st.number_input('Número de Vendas:', min_value=1, format="%d")
meses_pagar_ate_vender = st.number_input('Número de Meses que Prevê Pagar até Vender:', min_value=1, format="%d")

if st.button('Calcular Imóvel'):
    # Calcular resultados
    resultados, distrib_lucro_margem, despesas_detalhadas, social_media, produtora_audiovisual, gerente_comercial, contador, trafego_pago, recursos_humanos, ponto_comercial, manutencao_paginas_web, administrador, advogado_empresarial, investimentos_fixa_variavel, distribuicao_socios = calcular_imovel(valor_inicial, valor_venda, obra, taxa_juros, entrada_percentual, numero_vendas, meses_pagar_ate_vender)

    # Exibição dos resultados gerais
    st.subheader('Resultados Gerais')

    resultados_df = pd.DataFrame.from_dict({
        'Descrição': [
            'Gasto Total Atualizado',
            'Valor de Compra do Apartamento',
            'Valor da Venda do Apartamento',
            'Faturamento Bruto',
            'Margem de Lucro 30%',
            'Percentual de Aumento no Preço de Venda',
            'Valor da Entrada',
            'Saldo Devedor',
            'Valor Total do Financiamento',
            'Valor das Parcelas do Financiamento',
            'Número de Meses que Prevé Pagar até Vender',
            'Custo Total das Parcelas do Financiamento até Vender',
            'Despesas (70% do Faturamento Bruto)'
        ],
        'Valor': [
            f'R$ {resultados["Gasto Total Atualizado"]:,.2f}',
            f'R$ {resultados["Valor de Compra do Apartamento"]:,.2f}',
            f'R$ {resultados["Valor da Venda do Apartamento"]:,.2f}',
            f'R$ {resultados["Faturamento Bruto"]:,.2f}',
            f'R$ {resultados["Margem de Lucro 30%"]:,.2f}',
            f'{resultados["Percentual de Aumento no Preço de Venda"]:.2f}%',
            f'R$ {resultados["Valor da Entrada"]:,.2f}',
            f'R$ {resultados["Saldo Devedor"]:,.2f}',
            f'R$ {resultados["Valor Total do Financiamento"]:,.2f}',
            f'R$ {resultados["Valor das Parcelas do Financiamento"]:,.2f}',
            f'{resultados["Número de Meses que Prevê Pagar até Vender"]} meses',
            f'R$ {resultados["Custo Total das Parcelas do Financiamento até Vender"]:,.2f}',
            f'R$ {resultados["Despesas (70% do Faturamento Bruto)"]:,.2f}'
        ]
    })

    st.dataframe(resultados_df, use_container_width=True)

    # Exibição das despesas detalhadas
    st.subheader('Despesas Detalhadas')

    despesas_detalhadas_df = pd.DataFrame.from_dict({
        'Descrição': [
            'Investimento para o Próximo Imóvel (40% das Despesas)',
            'Material Audiovisual (15% das Despesas)'
        ],
        'Valor': [
            f'R$ {despesas_detalhadas["Investimento para o Próximo Imóvel (40% das Despesas)"]:,.2f}',
            f'R$ {despesas_detalhadas["Material Audiovisual (15% das Despesas)"]:,.2f}'
        ]
    })

    st.dataframe(despesas_detalhadas_df, use_container_width=True)

    # Exibição das despesas fixas
    st.subheader('Despesas Fixas (45% das Despesas)')

    caixa_df = pd.DataFrame.from_dict({
        'Descrição': [
            'Social Media',
            'Produtora Audiovisual',
            'Gerente Comercial',
            'Contador',
            'Tráfego Pago',
            'Recursos Humanos',
            'Ponto Comercial',
            'Manutenção Páginas Web',
            'Administrador',
            'Advogado Empresarial'
        ],
        'Valor': [
            f'R$ {social_media:,.2f}',
            f'R$ {produtora_audiovisual:,.2f}',
            f'R$ {gerente_comercial:,.2f}',
            f'R$ {contador:,.2f}',
            f'R$ {trafego_pago:,.2f}',
            f'R$ {recursos_humanos:,.2f}',
            f'R$ {ponto_comercial:,.2f}',
            f'R$ {manutencao_paginas_web:,.2f}',
            f'R$ {administrador:,.2f}',
            f'R$ {advogado_empresarial:,.2f}'
        ]
    })

    st.dataframe(caixa_df, use_container_width=True)

    # Exibição dos investimentos
    st.subheader('Investimentos da Margem de Lucro (50% para o Caixa da Empresa)')

    investimentos_df = pd.DataFrame.from_dict({
        'Descrição': [
            'Investimentos de Renda Fixa',
            'Investimentos de Renda Variável'
        ],
        'Valor': [
            f'R$ {investimentos_fixa_variavel["Investimentos de Renda Fixa"]:,.2f}',
            f'R$ {investimentos_fixa_variavel["Investimentos de Renda Variável"]:,.2f}'
        ]
    })

    st.dataframe(investimentos_df, use_container_width=True)

    # Exibição da distribuição para os sócios
    st.subheader('Distribuição da Margem de Lucro (50% distribuído)')

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
