import streamlit as st
import pandas as pd

# Configuração da interface do Streamlit
st.set_page_config(page_title="Calculadora de Imóvel", layout="wide")

def calcular_imovel(valor_inicial, valor_venda, obra, taxa_juros, entrada_percentual, numero_vendas, meses_pagar_ate_vender, moeda):
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

    # Ajuste do valor de venda com base na valorização (sem considerar inflação e período de meses)
    if moeda == 'Dólar':
        valor_venda_ajustado = valor_venda
        simbolo_moeda = 'USD'
    elif moeda == 'Real':
        valor_venda_ajustado = valor_venda
        simbolo_moeda = 'R$'
    else:
        valor_venda_ajustado = valor_venda  # Caso não seja uma moeda reconhecida
        simbolo_moeda = 'R$'

    # Cálculo do faturamento bruto
    faturamento_bruto = (valor_venda_ajustado - gasto_total) * numero_vendas

    # Cálculo da margem de lucro de 30%
    margem_lucro = faturamento_bruto * 0.30

    # Percentual de aumento
    percentual_aumento = ((valor_venda_ajustado - valor_inicial) / valor_inicial) * 100

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
        'Valor da Venda do Apartamento Ajustado': valor_venda_ajustado,
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

    return resultados, distrib_lucro_margem, despesas_detalhadas, social_media, produtora_audiovisual, gerente_comercial, contador, trafego_pago, recursos_humanos, ponto_comercial, manutencao_paginas_web, administrador, advogado_empresarial, investimentos_fixa_variavel, distribuicao_socios, simbolo_moeda

def calcular_parcela(valor_total, taxa_juros_mensal, periodo_financiamento):
    """ Calcula o valor da parcela mensal usando a fórmula de financiamento """
    return valor_total * (taxa_juros_mensal * (1 + taxa_juros_mensal) ** periodo_financiamento) / ((1 + taxa_juros_mensal) ** periodo_financiamento - 1)

# Configuração da interface do Streamlit
st.title('Calculadora de Imóvel')

# Barra lateral para previsões
st.sidebar.header('Parâmetros de Valorização')
moeda = st.sidebar.selectbox('Moeda de Valorização:', ['Dólar', 'Real'])

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
    resultados, distrib_lucro_margem, despesas_detalhadas, social_media, produtora_audiovisual, gerente_comercial, contador, trafego_pago, recursos_humanos, ponto_comercial, manutencao_paginas_web, administrador, advogado_empresarial, investimentos_fixa_variavel, distribuicao_socios, simbolo_moeda = calcular_imovel(
        valor_inicial, valor_venda, obra, taxa_juros, entrada_percentual, numero_vendas, meses_pagar_ate_vender, moeda
    )

    # Função para formatar números
    def formatar_numero(valor):
        return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    
    # Exibição dos resultados
    st.subheader('Resultados')
    resultados_df = pd.DataFrame.from_dict({
        'Descrição': [
            'Valor de Compra do Apartamento',
            'Gasto Total Atualizado',
            'Valor da Venda do Apartamento Ajustado',
            'Faturamento Bruto',
            'Margem de Lucro 30%',
            'Percentual de Aumento no Preço de Venda',
            'Valor da Entrada',
            'Saldo Devedor',
            'Valor Total do Financiamento',
            'Valor das Parcelas do Financiamento',
            'Número de Meses que Prevê Pagar até Vender',
            'Custo Total das Parcelas do Financiamento até Vender',
            'Despesas (70% do Faturamento Bruto)'
        ],
        'Valor': [
            f"{simbolo_moeda} {formatar_numero(resultados['Valor de Compra do Apartamento'])}",
            f"{simbolo_moeda} {formatar_numero(resultados['Gasto Total Atualizado'])}",
            f"{simbolo_moeda} {formatar_numero(resultados['Valor da Venda do Apartamento Ajustado'])}",
            f"{simbolo_moeda} {formatar_numero(resultados['Faturamento Bruto'])}",
            f"{simbolo_moeda} {formatar_numero(resultados['Margem de Lucro 30%'])}",
            f"{formatar_numero(resultados['Percentual de Aumento no Preço de Venda'])}%",
            f"{simbolo_moeda} {formatar_numero(resultados['Valor da Entrada'])}",
            f"{simbolo_moeda} {formatar_numero(resultados['Saldo Devedor'])}",
            f"{simbolo_moeda} {formatar_numero(resultados['Valor Total do Financiamento'])}",
            f"{simbolo_moeda} {formatar_numero(resultados['Valor das Parcelas do Financiamento'])}",
            f"{resultados['Número de Meses que Prevê Pagar até Vender']:.0f}",
            f"{simbolo_moeda} {formatar_numero(resultados['Custo Total das Parcelas do Financiamento até Vender'])}",
            f"{simbolo_moeda} {formatar_numero(resultados['Despesas (70% do Faturamento Bruto)'])}"
        ]
    })
    st.dataframe(resultados_df)

    st.subheader('Distribuição da Margem de Lucro')
    st.write({
        '50% para o caixa da empresa': f"{simbolo_moeda} {formatar_numero(distrib_lucro_margem['50% para o caixa da empresa'])}",
        '50% distribuído': f"{simbolo_moeda} {formatar_numero(distrib_lucro_margem['50% distribuído'])}"
    })

    st.subheader('Despesas Detalhadas')
    st.write({
        'Investimento para o Próximo Imóvel (40% das Despesas)': f"{simbolo_moeda} {formatar_numero(despesas_detalhadas['Investimento para o Próximo Imóvel (40% das Despesas)'])}",
        'Material Audiovisual (15% das Despesas)': f"{simbolo_moeda} {formatar_numero(despesas_detalhadas['Material Audiovisual (15% das Despesas)'])}"
    })

    st.subheader('Despesas Fixas')
    st.write({
        'Social Media': f"{simbolo_moeda} {formatar_numero(social_media)}",
        'Produtora Audiovisual': f"{simbolo_moeda} {formatar_numero(produtora_audiovisual)}",
        'Gerente Comercial': f"{simbolo_moeda} {formatar_numero(gerente_comercial)}",
        'Contador': f"{simbolo_moeda} {formatar_numero(contador)}",
        'Tráfego Pago': f"{simbolo_moeda} {formatar_numero(trafego_pago)}",
        'Recursos Humanos': f"{simbolo_moeda} {formatar_numero(recursos_humanos)}",
        'Ponto Comercial': f"{simbolo_moeda} {formatar_numero(ponto_comercial)}",
        'Manutenção de Páginas Web': f"{simbolo_moeda} {formatar_numero(manutencao_paginas_web)}",
        'Administrador': f"{simbolo_moeda} {formatar_numero(administrador)}",
        'Advogado Empresarial': f"{simbolo_moeda} {formatar_numero(advogado_empresarial)}"
    })

    st.subheader('Investimentos do Caixa da Empresa')
    st.write({
        'Investimentos de Renda Fixa': f"{simbolo_moeda} {formatar_numero(investimentos_fixa_variavel['Investimentos de Renda Fixa'])}",
        'Investimentos de Renda Variável': f"{simbolo_moeda} {formatar_numero(investimentos_fixa_variavel['Investimentos de Renda Variável'])}"
    })

    st.subheader('Distribuição para Sócios')
    st.write({
        'Sócio 1': f"{simbolo_moeda} {formatar_numero(distribuicao_socios['Sócio 1'])}",
        'Sócio 2': f"{simbolo_moeda} {formatar_numero(distribuicao_socios['Sócio 2'])}"
    })
