import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Câmbio Financeiro", layout="wide")
st.title("💱 Projeto de Câmbio Financeiro")
st.markdown("Demonstração de manipulação de preços de produtos em diferentes moedas.")

dados_cambio = {
    "Produto": ["Produto A", "Produto B", "Produto C"],
    "Preco USD": [100, 150, 200],
    "Preco EUR": [85, 125, 170],
    "Preco JPY": [10000, 15000, 20000],
}
taxas_base = {"USD": 1.0, "EUR": 1.2, "JPY": 0.009, "GBP": 1.4}

df = pd.DataFrame(dados_cambio)

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Dados & Taxas", "➕ Nova Moeda", "🔄 Conversão", "📈 Visualizações"
])

with tab1:
    col1, col2 = st.columns([3, 2])
    with col1:
        st.subheader("DataFrame de Preços")
        moedas_exibidas = ["Produto"] + [c for c in df.columns if c.startswith("Preco")]
        st.dataframe(df[moedas_exibidas], use_container_width=True)
    with col2:
        st.subheader("Taxas de Câmbio (1 USD → Moeda)")
        taxa_df = pd.DataFrame([
            {"Moeda": moeda, "Taxa": taxa}
            for moeda, taxa in taxas_base.items()
        ])
        st.dataframe(taxa_df, use_container_width=True, hide_index=True)
        st.caption("Multiplique o valor em USD pela taxa para obter o valor na moeda.")

    st.subheader("Função de Conversão")
    st.code(
        "def conversao_para_usd(preco, taxa):\n    return preco / taxa",
        language="python",
    )

with tab2:
    st.subheader("Adicionar Nova Moeda")
    with st.form("nova_moeda"):
        codigo = st.text_input("Código da moeda (ex: BRL, CAD, AUD)", max_chars=5).upper()
        taxa = st.number_input("Taxa de câmbio (1 USD = X da moeda)", min_value=0.0001, value=5.0, format="%.4f")
        base = st.selectbox("Converter a partir de:", [c for c in df.columns if c.startswith("Preco")])
        if st.form_submit_button("Adicionar Moeda"):
            if codigo and codigo not in [c.replace("Preco ", "") for c in df.columns if c.startswith("Preco")]:
                nome_coluna = f"Preco {codigo}"
                df[nome_coluna] = df[base].apply(lambda x: x * taxa)
                taxas_base[codigo] = taxa
                st.success(f"Moeda {codigo} adicionada com taxa {taxa}!")
                st.rerun()
            elif codigo:
                st.error("Essa moeda já existe!")
            else:
                st.error("Insira um código válido.")

    if len(df.columns) > 4:
        st.subheader("Moedas Adicionadas")
        cols_moeda = ["Produto"] + [c for c in df.columns if c.startswith("Preco")]
        st.dataframe(df[cols_moeda], use_container_width=True)

with tab3:
    st.subheader("Conversor de Valores")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        valor = st.number_input("Valor", min_value=0.0, value=100.0, step=10.0)
    with col_b:
        moeda_origem = st.selectbox("De", [c for c in df.columns if c.startswith("Preco")])
    with col_c:
        moeda_destino = st.selectbox("Para", [c for c in df.columns if c.startswith("Preco")])

    if moeda_origem and moeda_destino and st.button("Converter"):
        ticker_origem = moeda_origem.replace("Preco ", "")
        ticker_destino = moeda_destino.replace("Preco ", "")
        taxa_origem = taxas_base[ticker_origem]
        taxa_destino = taxas_base[ticker_destino]
        valor_usd = valor / taxa_origem if ticker_origem != "USD" else valor
        valor_convertido = valor_usd * taxa_destino
        st.success(f"{valor:.2f} {ticker_origem} = {valor_convertido:.2f} {ticker_destino}")
        st.caption(f"Passo 1: {valor:.2f} {ticker_origem} ÷ {taxa_origem} = {valor_usd:.4f} USD")
        st.caption(f"Passo 2: {valor_usd:.4f} USD × {taxa_destino} = {valor_convertido:.2f} {ticker_destino}")

    st.subheader("Comparação de Preços")
    cols_graf = ["Produto"] + [c for c in df.columns if c.startswith("Preco")]
    st.dataframe(df[cols_graf], use_container_width=True)

with tab4:
    st.subheader("Gráfico de Preços por Moeda")
    cols_preco = [c for c in df.columns if c.startswith("Preco")]
    if cols_preco:
        df_melt = df.melt(id_vars=["Produto"], value_vars=cols_preco,
                          var_name="Moeda", value_name="Preco")
        fig = px.bar(df_melt, x="Produto", y="Preco", color="Moeda",
                     barmode="group", title="Preços dos Produtos por Moeda")
        st.plotly_chart(fig, use_container_width=True)

        fig2 = px.line(df_melt, x="Moeda", y="Preco", color="Produto",
                       markers=True, title="Variação de Preços entre Moedas")
        st.plotly_chart(fig2, use_container_width=True)

st.divider()
st.caption("Projeto de Câmbio Financeiro — built with Streamlit + Pandas + Plotly")
