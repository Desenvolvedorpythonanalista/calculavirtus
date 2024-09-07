import streamlit as st

class Cliente:
    def __init__(self, tipo, perguntas_evitar, perguntas_certas, respostas, plano_acao):
        self.tipo = tipo
        self.perguntas_evitar = perguntas_evitar
        self.perguntas_certas = perguntas_certas
        self.respostas = respostas
        self.plano_acao = plano_acao

    def mostrar_dados_cliente(self):
        st.header(f"Cliente: {self.tipo}")

        st.subheader("Perguntas a evitar:")
        for pergunta in self.perguntas_evitar:
            st.write(f"- {pergunta}")

        st.subheader("Perguntas certas:")
        for pergunta in self.perguntas_certas:
            st.write(f"- {pergunta}")

        st.subheader("Abordagem Personalizada:")
        st.write(f"Para {self.tipo}, nossa abordagem se concentra em como você pode proteger e maximizar seu patrimônio. Aqui está como nossa solução pode ajudar:")
        st.write(f"1. **Proteção do Patrimônio**: Apresentamos estratégias eficazes para proteger seus bens contra riscos e imprevistos. Usamos ferramentas de blindagem patrimonial para garantir que seu patrimônio esteja seguro.")
        st.write(f"2. **Rentabilização com Imóveis e Aluguéis**: Mostramos como você pode aumentar a rentabilidade dos seus imóveis, seja por meio de investimentos estratégicos ou otimização da gestão de aluguéis.")
        st.write(f"3. **Qualidade de Vida**: Oferecemos soluções que melhoram sua qualidade de vida, seja por meio de gestão financeira eficiente, aumento de renda passiva ou melhoria na segurança.")
        st.write(f"4. **Dolarização do Patrimônio**: Explicamos como diversificar e dolarizar seu patrimônio para proteção adicional e crescimento global.")
        
        st.subheader("Plano de Ação:")
        for acao in self.plano_acao:
            st.write(f"- {acao}")

        st.subheader("Fechamento para Agendamento de Reunião:")
        st.write(f"Gostaríamos de discutir em detalhes como podemos personalizar essas soluções para atender às suas necessidades específicas. Agende uma reunião conosco para explorar as opções e começar a transformar seu patrimônio de maneira eficaz.")
        st.write(f"**Clique aqui para agendar sua reunião:** [Agendar Reunião](#)")

        st.markdown("---")  # Divisória entre os clientes

    def roteiro_argumentativo(self):
        st.subheader("Roteiro Argumentativo:")
        st.write(f"Para {self.tipo}, a abordagem deve focar em:")
        st.write(f"1. **Introdução**: Destacar a importância de proteger e otimizar o patrimônio.")
        st.write(f"2. **Necessidade**: Identificar as necessidades específicas do cliente.")
        st.write(f"3. **Solução**: Demonstrar como nossas soluções atendem a essas necessidades.")
        st.write(f"4. **Benefícios**: Enfatizar os benefícios de nossa abordagem.")
        st.write(f"5. **Chamada para Ação**: Convidar o cliente para uma reunião para discutir a implementação das soluções.")

# Dados dos clientes com planos de ação e roteiros argumentativos
clientes = [
    Cliente(
        "Donos de Imobiliárias",
        [
            "Quanto custa sua comissão?",
            "Por que devo confiar em você?",
            "Você tem experiência suficiente?",
            "Vocês já tiveram problemas com outros clientes?",
            "Vocês garantem o retorno do investimento?"
        ],
        [
            "Quais são os maiores desafios da sua imobiliária hoje?",
            "Você já pensou em maneiras de melhorar a visibilidade dos imóveis?",
            "Como você tem gerenciado suas propriedades de maior valor?",
            "Você tem interesse em aumentar a rentabilidade de seus imóveis?"
        ],
        [
            "Para donos de imobiliárias, nossas soluções ajudam a proteger seu patrimônio imobiliário contra riscos e aumentar a rentabilidade dos seus imóveis. Oferecemos estratégias de gestão otimizada e proteção contra imprevistos. Além disso, ajudamos a melhorar a visibilidade dos imóveis e aumentar a qualidade de vida ao otimizar a administração de aluguéis. Vamos mostrar como essas soluções podem ser personalizadas para suas necessidades específicas e como a dolarização pode trazer benefícios adicionais."
        ],
        [
            "Visite Feiras e Eventos Locais.",
            "Explore Escritórios de Imobiliárias.",
            "Participação em Grupos Locais.",
            "Ofereça Consultoria Personalizada.",
            "Realize Webinars Educacionais sobre Proteção Patrimonial."
        ]
    ),
    Cliente(
        "Diretores Executivos de Lojas de Consórcio Automotivo",
        [
            "Seu consórcio tem problemas de inadimplência?",
            "Como você lida com clientes insatisfeitos?",
            "Seu modelo de negócios é sustentável a longo prazo?",
            "Vocês já enfrentaram crises financeiras?",
            "Quanto tempo vai demorar para vermos retorno?"
        ],
        [
            "Como você tem incentivado seus clientes a aderirem ao consórcio?",
            "Você já pensou em estratégias para reduzir a inadimplência?",
            "Como podemos aumentar a confiança dos seus clientes no processo?",
            "Quais são os seus principais objetivos para o próximo trimestre?"
        ],
        [
            "Para diretores executivos de lojas de consórcio automotivo, oferecemos soluções para proteger e rentabilizar seu patrimônio. Abordamos a redução da inadimplência e a melhoria da confiança dos clientes. Nossas estratégias incluem otimização da gestão de consórcios e aumento da rentabilidade. Vamos explorar como essas soluções podem ser aplicadas especificamente à sua loja e como a dolarização do capital pode adicionar valor ao seu negócio."
        ],
        [
            "Visite Lojas de Consórcios e Concessionárias.",
            "Participe de Eventos do Setor Automotivo.",
            "Envolvimento em Associações Locais.",
            "Ofereça Consultoria Especializada.",
            "Realize Estudos de Caso sobre Rentabilidade."
        ]
    ),
    Cliente(
        "Representantes Comerciais de Concessionárias",
        [
            "Quanto você cobra por seus serviços?",
            "Você já teve problemas com concessionárias no passado?",
            "Como você garante a qualidade do seu serviço?",
            "Quais são seus maiores desafios?",
            "Por que eu deveria escolher você?"
        ],
        [
            "Quais são seus principais desafios de vendas?",
            "Como você tem impulsionado a performance das concessionárias?",
            "Quais são suas estratégias para atrair novos clientes?",
            "Como você mede o sucesso das suas campanhas?"
        ],
        [
            "Para representantes comerciais de concessionárias, nosso foco é em como nossas soluções podem melhorar a performance de vendas e atrair novos clientes. Ajudamos a otimizar as estratégias de marketing e aumentar a rentabilidade. Apresentamos casos de sucesso e estudos para demonstrar o valor de nossas soluções. Discutiremos em detalhes como personalizar essas soluções para suas necessidades e como a dolarização pode ser um diferencial competitivo."
        ],
        [
            "Visite Concessionárias e Agências.",
            "Participação em Eventos de Vendas.",
            "Networking em Eventos Locais.",
            "Ofereça Workshops sobre Proteção Patrimonial.",
            "Realize Análises Personalizadas de Performance."
        ]
    ),
    Cliente(
        "Promotores de Venda",
        [
            "Qual é o custo do seu serviço?",
            "Você já enfrentou problemas com promotores de vendas?",
            "Quais garantias você oferece?",
            "Como você mede o sucesso dos seus promotores?",
            "Qual é a sua experiência na área?"
        ],
        [
            "Como você atrai e motiva promotores de venda?",
            "Qual é o seu método para garantir a qualidade dos promotores?",
            "Como você avalia o desempenho e impacto dos promotores?",
            "Quais são os principais benefícios de trabalhar com seus promotores?"
        ],
        [
            "Para promotores de venda, oferecemos estratégias para atrair e motivar promotores qualificados. Nossa abordagem inclui métodos para garantir qualidade e avaliar o impacto dos promotores. Mostramos como isso pode melhorar a eficácia das campanhas e aumentar a rentabilidade. Discutiremos como adaptar essas soluções às suas necessidades específicas e explorar a dolarização do capital para maximizar resultados."
        ],
        [
            "Visite Eventos e Feiras de Vendas.",
            "Contato com Empresas de Promoção.",
            "Participação em Grupos Locais de Networking.",
            "Ofereça Seminários sobre Crescimento Patrimonial.",
            "Realize Análises de Impacto de Vendas."
        ]
    ),
    Cliente(
        "Administradores de Airbnb Brasileiros",
        [
            "Qual é a taxa de ocupação média dos seus imóveis?",
            "Como você lida com avaliações negativas?",
            "Quais são os maiores desafios que você enfrenta?",
            "Como você garante a qualidade dos imóveis?",
            "Você já enfrentou problemas de segurança?"
        ],
        [
            "Como você promove seus imóveis para aumentar a ocupação?",
            "Qual é a sua estratégia para lidar com avaliações e feedback?",
            "Como você melhora a experiência dos hóspedes?",
            "Quais são suas práticas para manter a qualidade e segurança dos imóveis?"
        ],
        [
            "Para administradores de Airbnb, nossa abordagem se concentra em estratégias para aumentar a ocupação e melhorar a experiência dos hóspedes. Oferecemos soluções para lidar com avaliações e garantir a segurança dos imóveis. Discutiremos como otimizar a gestão e a rentabilidade dos imóveis, além de explorar a dolarização como uma forma de proteção adicional."
        ],
        [
            "Participe de Eventos de Administradores de Airbnb.",
            "Visite Plataformas de Aluguel por Temporada.",
            "Networking em Comunidades Locais.",
            "Ofereça Consultoria sobre Proteção Patrimonial.",
            "Realize Webinars sobre Melhoria de Ocupação."
        ]
    ),
    Cliente(
        "Aposentados e Concursados",
        [
            "Qual é o retorno do seu investimento?",
            "Como você protege seu patrimônio?",
            "Qual é a sua experiência com planejamento financeiro?",
            "Quais são os maiores desafios financeiros que você enfrenta?",
            "Você já teve problemas com a gestão de investimentos?"
        ],
        [
            "Como você pode proteger e otimizar seu patrimônio no exterior?",
            "Quais são as melhores práticas para maximizar ganhos e economizar impostos?",
            "Como você pode dolarizar seu capital de forma global?",
            "Qual é a estratégia para manter a segurança tributária e reduzir riscos?"
        ],
        [
            "Para aposentados e concursados, nossa abordagem foca em proteger e otimizar o patrimônio, com ênfase em estratégias globais e economia de impostos. Explicamos como dolarizar seu capital e manter a segurança tributária. Utilizamos estudos de caso para ilustrar a eficácia das soluções. Discutiremos em detalhes como aplicar essas estratégias à sua situação específica e agendaremos uma reunião para explorar todas as opções."
        ],
        [
            "Organize Webinars sobre Planejamento Patrimonial.",
            "Realize Consultorias Personalizadas.",
            "Participação em Eventos de Aposentados e Concursados.",
            "Ofereça Estudos de Caso sobre Proteção Patrimonial.",
            "Desenvolva Material Educacional sobre Economia de Impostos."
        ]
    ),
    Cliente(
        "Donos de Frota de Caminhões",
        [
            "Qual é a taxa de sucesso na gestão de frotas?",
            "Como você lida com problemas de manutenção?",
            "Quais são os custos envolvidos?",
            "Como você garante a eficiência da frota?",
            "Você já teve problemas com regulamentações?"
        ],
        [
            "Como você gerencia a manutenção e operação da sua frota?",
            "Quais são as melhores práticas para manter a eficiência?",
            "Como você controla os custos e aumenta a rentabilidade?",
            "Quais são as soluções oferecidas para problemas comuns de frota?"
        ],
        [
            "Para donos de frota de caminhões, oferecemos soluções para otimizar a gestão e operação da frota, controlar custos e aumentar a rentabilidade. Nossas estratégias incluem melhores práticas para manutenção e eficiência. Utilizamos exemplos de sucesso para demonstrar o impacto positivo das soluções. Agende uma reunião para explorar como aplicar essas estratégias à sua frota e discutir a dolarização do capital como uma opção adicional."
        ],
        [
            "Visite Empresas de Transporte.",
            "Participação em Feiras de Transporte.",
            "Networking com Associações de Transporte.",
            "Ofereça Consultoria sobre Economia de Impostos.",
            "Desenvolva Estudos de Caso sobre Dolarização do Capital."
        ]
    ),
    Cliente(
        "Servidores de Autarquia",
        [
            "Qual é o custo para servidores?",
            "Como você garante a eficiência no setor público?",
            "Quais são os principais desafios que você enfrenta?",
            "Como você lida com a burocracia?",
            "Você tem experiência em trabalhar com autarquias?"
        ],
        [
            "Como você melhora a eficiência e redução de custos?",
            "Quais são as melhores práticas para gerenciar projetos públicos?",
            "Como você garante a conformidade com regulamentações?",
            "Quais são os serviços oferecidos para o setor público?"
        ],
        [
            "Para servidores de autarquias, nossa abordagem é focada em melhorar a eficiência e reduzir custos no setor público. Apresentamos práticas para gerenciar projetos e garantir a conformidade. Utilizamos estudos de caso para ilustrar como nossas soluções ajudam. Agendaremos uma reunião para adaptar essas soluções às suas necessidades e explorar a dolarização do capital como uma forma de proteção adicional."
        ],
        [
            "Participe de Eventos do Setor Público.",
            "Visite Associações de Servidores Públicos.",
            "Networking Local.",
            "Ofereça Consultoria sobre Segurança Tributária.",
            "Desenvolva Material Educacional sobre Planejamento Patrimonial."
        ]
    ),
    Cliente(
        "Vereadores",
        [
            "Qual é o impacto do seu serviço para a comunidade?",
            "Como você lida com questões políticas?",
            "Quais são os principais benefícios oferecidos?",
            "Como você garante a transparência?",
            "Você tem experiência em trabalhar com políticos?"
        ],
        [
            "Como você melhora a eficiência dos serviços comunitários?",
            "Quais são as melhores práticas para gestão política?",
            "Como você garante a conformidade e a transparência?",
            "Quais são os benefícios específicos para vereadores?"
        ],
        [
            "Para vereadores, a abordagem deve enfatizar a melhoria dos serviços comunitários e a gestão política eficiente. Apresentamos como nossas soluções melhoram a transparência e a conformidade, destacando benefícios específicos. Usamos exemplos de sucesso para mostrar o impacto positivo. Agendaremos uma reunião para discutir como aplicar essas soluções e explorar a dolarização como uma forma de maximizar resultados."
        ],
        [
            "Participação em Eventos Políticos.",
            "Conecte-se com Escritórios de Vereadores.",
            "Networking Político.",
            "Ofereça Consultoria sobre Economia de Impostos.",
            "Desenvolva Material Educacional sobre Proteção Patrimonial."
        ]
    ),
    Cliente(
        "Moradores de Residenciais de Alto Padrão",
        [
            "Qual é o custo dos seus serviços para residenciais de luxo?",
            "Como você garante a segurança dos imóveis?",
            "Quais são os principais benefícios oferecidos?",
            "Como você lida com questões de exclusividade?",
            "Você tem experiência com propriedades de alto padrão?"
        ],
        [
            "Como você melhora a proteção patrimonial?",
            "Quais são as melhores práticas para segurança e exclusividade?",
            "Como você oferece serviços personalizados para imóveis de luxo?",
            "Quais são os principais benefícios de trabalhar com você?"
        ],
        [
            "Para moradores de residenciais de alto padrão, nossa abordagem deve focar na proteção e valorização dos imóveis. Apresentamos soluções para segurança e exclusividade, utilizando estudos de caso e exemplos para ilustrar o valor agregado. Discutiremos como aplicar essas soluções às suas necessidades e como a dolarização pode adicionar valor ao seu patrimônio."
        ],
        [
            "Participação em Eventos em Residenciais de Luxo.",
            "Visite Imóveis de Luxo.",
            "Consultorias e Eventos Exclusivos.",
            "Ofereça Workshops sobre Proteção Patrimonial Global.",
            "Desenvolva Estudos de Caso sobre Dolarização do Capital."
        ]
    )
]

# Streamlit App
st.title("Ações de Prospecção")

# Seleciona o tipo de cliente
cliente_selecionado = st.selectbox(
    "Escolha o tipo de cliente:",
    [cliente.tipo for cliente in clientes]
)

# Exibe informações do cliente selecionado
for cliente in clientes:
    if cliente.tipo == cliente_selecionado:
        cliente.mostrar_dados_cliente()
        cliente.roteiro_argumentativo()
        break
