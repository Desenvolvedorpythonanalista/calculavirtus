import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import locale

# Configura o locale para formato brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Funções para calcular rendimentos
def calcular_rendimento_renda_fixa(valor_investido, taxa_juros, tempo, aportes_mensais, taxa_inflacao):
    saldo_final = valor_investido
    for mes in range(tempo * 12):
        saldo_final = saldo_final * (1 + taxa_juros / 12) + aportes_mensais
    saldo_final_ajustado = saldo_final / (1 + taxa_inflacao) ** tempo
    return saldo_final_ajustado

def calcular_rendimento_renda_variavel(valor_investido, taxa_retorno, aportes_mensais, tempo):
    saldo_inicial = valor_investido
    rendimentos = []
    for mes in range(tempo * 12):
        saldo_inicial = (saldo_inicial + aportes_mensais) * (1 + taxa_retorno / 12)
        rendimentos.append(saldo_inicial)
    return rendimentos

# Título da aplicação
st.title("Calculadora de Investimentos Diversificados")

# Seção para investimento em Renda Fixa
st.header("Renda Fixa")
valor_fixa = st.number_input("Valor investido em Renda Fixa (R$):", min_value=0.0, step=100.0)
taxa_fixa = st.number_input("Taxa de Juros Anual (%):", min_value=0.0, max_value=100.0, step=0.1) / 100
tempo_fixa = st.number_input("Tempo de Investimento (anos):", min_value=1, step=1)
aportes_mensais_fixa = st.number_input("Aportes Mensais (R$):", min_value=0.0, step=100.0)
taxa_inflacao = st.number_input("Taxa de Inflação Anual (%):", min_value=0.0, max_value=100.0, step=0.1) / 100

# Seção para investimento em Renda Variável
st.header("Renda Variável")
valor_variavel = st.number_input("Valor investido em Renda Variável (R$):", min_value=0.0, step=100.0)
taxa_variavel = st.number_input("Taxa de Retorno Anual Esperada (%):", min_value=0.0, max_value=100.0, step=0.1) / 100
tempo_variavel = st.number_input("Tempo de Investimento (anos) para Renda Variável:", min_value=1, step=1)
aportes_mensais_variavel = st.number_input("Aportes Mensais em Renda Variável (R$):", min_value=0.0, step=100.0)

# Botão para calcular os rendimentos
if st.button("Calcular"):
    # Calcula o rendimento em renda fixa ajustado pela inflação
    if valor_fixa > 0:
        rendimentos_fixa = [calcular_rendimento_renda_fixa(valor_fixa, taxa_fixa, tempo_fixa, aportes_mensais_fixa, taxa_inflacao)]
    else:
        rendimentos_fixa = []

    # Calcula o rendimento em renda variável
    if valor_variavel > 0:
        rendimentos_variavel = calcular_rendimento_renda_variavel(valor_variavel, taxa_variavel, aportes_mensais_variavel, tempo_variavel)
    else:
        rendimentos_variavel = []

    # Define o comprimento máximo para o eixo X
    num_meses = max(len(rendimentos_fixa), len(rendimentos_variavel)) if isinstance(rendimentos_fixa, list) and isinstance(rendimentos_variavel, list) else 0

    # Ajusta as listas para terem o mesmo tamanho
    if len(rendimentos_fixa) == 0:
        rendimentos_fixa = [0] * num_meses
    else:
        rendimentos_fixa.extend([rendimentos_fixa[-1]] * (num_meses - len(rendimentos_fixa)))

    if len(rendimentos_variavel) == 0:
        rendimentos_variavel = [0] * num_meses
    else:
        rendimentos_variavel.extend([rendimentos_variavel[-1]] * (num_meses - len(rendimentos_variavel)))

    # Define os meses como eixo X
    meses = np.arange(1, num_meses + 1)

    # Plot gráfico de barras emparelhadas
    st.subheader("Comparação de Investimentos (Renda Fixa x Renda Variável)")
    plt.figure(figsize=(10, 5))

    largura_barras = 0.4  # Define a largura das colunas

    plt.bar(meses - largura_barras / 2, rendimentos_fixa, width=largura_barras, label="Renda Fixa", color='blue')
    plt.bar(meses + largura_barras / 2, rendimentos_variavel, width=largura_barras, label="Renda Variável", color='green')

    plt.title("Evolução dos Investimentos")
    plt.xlabel("Meses")
    plt.ylabel("Valor Acumulado (R$)")
    plt.legend()
    plt.grid(True)

    st.pyplot(plt)

    # Calcula resultados
    total_aportes_fixa = aportes_mensais_fixa * 12 * tempo_fixa
    total_aportes_variavel = aportes_mensais_variavel * 12 * tempo_variavel
    investimento_total = valor_fixa + valor_variavel + total_aportes_fixa + total_aportes_variavel
    retorno_fixa = rendimentos_fixa[-1] if rendimentos_fixa else 0.0
    retorno_variavel = rendimentos_variavel[-1] if rendimentos_variavel else 0.0
    patrimonio_total = retorno_fixa + retorno_variavel
    ganho_real = patrimonio_total - investimento_total

    # Cálculo da rentabilidade
    rentabilidade_total = patrimonio_total - investimento_total
    percentual_rentabilidade_investimento = (rentabilidade_total / investimento_total) * 100 if investimento_total > 0 else 0
    percentual_rentabilidade_patrimonio = (rentabilidade_total / patrimonio_total) * 100 if patrimonio_total > 0 else 0

    # Cálculo da renda mensal e anual com base no ganho real
    renda_mensal_real = ganho_real / (tempo_fixa * 12) if tempo_fixa > 0 else 0
    renda_anual_real = renda_mensal_real * 12

    # Cálculo da renda mensal e anual com base no patrimônio total
    renda_mensal_patrimonio = patrimonio_total / (tempo_fixa * 12) if tempo_fixa > 0 else 0
    renda_anual_patrimonio = renda_mensal_patrimonio * 12

    # Cálculo de ganhos diários
    ganho_diario_total = renda_mensal_real / 30
    ganho_diario_real = ganho_real / (tempo_fixa * 12 * 30) if (tempo_fixa * 12 * 30) > 0 else 0

    # Cálculo da rentabilidade mensal em porcentagem
    rentabilidade_mensal_fixa = ((retorno_fixa - valor_fixa - total_aportes_fixa) / (tempo_fixa * 12)) / (valor_fixa + total_aportes_fixa) * 100 if (valor_fixa + total_aportes_fixa) > 0 else 0
    rentabilidade_mensal_variavel = ((retorno_variavel - valor_variavel - total_aportes_variavel) / (tempo_variavel * 12)) / (valor_variavel + total_aportes_variavel) * 100 if (valor_variavel + total_aportes_variavel) > 0 else 0

    # Função para formatar valores como moeda
    def formatar_moeda(valor):
        return locale.currency(valor, grouping=True)

    # Exibe resultados detalhados em tabelas
    with st.expander("Investimento e Retorno Esperado"):
        st.write("**Investimento e Retorno Esperado**")
        st.write(f"Investimento Inicial: {formatar_moeda(valor_fixa + valor_variavel)}")
        st.write(f"Total em Aportes (Renda Fixa): {formatar_moeda(total_aportes_fixa)}")
        st.write(f"Total em Aportes (Renda Variável): {formatar_moeda(total_aportes_variavel)}")
        st.write(f"Investimento Total: {formatar_moeda(investimento_total)}")
        st.write(f"Retorno esperado em Renda Fixa: {formatar_moeda(retorno_fixa)}")
        st.write(f"Retorno esperado em Renda Variável: {formatar_moeda(retorno_variavel)}")

    with st.expander("Valorização de Patrimônio"):
        st.write("**Valorização de Patrimônio**")
        st.write(f"Patrimônio Total: {formatar_moeda(patrimonio_total)}")
        st.write(f"Ganho Real no período: {formatar_moeda(ganho_real)}")
        st.write(f"Valorização dos Investimentos: {percentual_rentabilidade_investimento:.2f}%")
        st.write(f"Valorização do Patrimônio: {percentual_rentabilidade_patrimonio:.2f}%")

    with st.expander("Proventos gerados com base no patrimônio"):
        st.write("**COM BASE NO PERÍODO ESCOLHIDO**")
        st.write(f"Proventos anuais depois do período: {formatar_moeda(renda_anual_patrimonio)}")
        st.write(f"Proventos mensais depois do período: {formatar_moeda(renda_mensal_patrimonio)}")

    with st.expander("Proventos com Base no Ganho Real (Com base no rendimento)"):
        st.write("**Proventos coom Base no Ganho Real ( RENDIMENTO )**")
        st.write(f"Proventos Anuais Reais depois do período: {formatar_moeda(renda_anual_real)}")
        st.write(f"Proventos Mensais Reais depois do período: {formatar_moeda(renda_mensal_real)}")
        st.write(f"Proventos Diários Reais depois do período: {formatar_moeda(ganho_diario_real)}")

    with st.expander("Rentabilidade Mensal"):
        st.write("**Rentabilidade Mensal**")
        st.write(f"Rentabilidade Mensal em Renda Fixa: {rentabilidade_mensal_fixa:.2f}%")
        st.write(f"Rentabilidade Mensal em Renda Variável: {rentabilidade_mensal_variavel:.2f}%")

    # Adicione mais análises e visualizações conforme necessário
