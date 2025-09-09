import streamlit as st

###FUNÇÕES
# 1º Função calcula IMC
# 2ª Categoria do IMC
def calcular_imc(peso,altura):
    return peso/altura**2

def categoria_imc(imc):
    if imc <= 18.5:
        return "Abaixo do peso."
    elif imc <= 24.9:
        return "Peso normal."
    elif imc <= 29.9:
        return "Sobrepeso."
    elif imc <= 34.9:
        return "Obesidade Grau 1"
    elif imc <= 39.9:
        return "Obesidade Grau 2"
    else:
        return "Obesidade Grau 3"



# ---------------------------
# Configuração da página
# ---------------------------
st.set_page_config(
    page_title="Calculadora de IMC",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------------------------
# Cabeçalho
# ---------------------------
st.title("⚖️ Calculadora de IMC")
st.caption("Template decorativo — funcionalidade será feita em sala 🚀")

st.divider()

# ---------------------------
# Área de Destaque
# ---------------------------
col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Sobre o IMC")
    st.markdown(
        """
        O **Índice de Massa Corporal (IMC)** é uma medida usada para avaliar
        se uma pessoa está dentro de uma faixa considerada saudável de peso
        em relação à altura.

        👉 Neste app, você poderá:
        - Inserir seu peso e altura  
        - Calcular automaticamente o IMC  
        - Ver em qual **categoria** você se encontra  
        """
    )
with col2:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/3103/3103446.png",
        caption="Ilustração IMC",
        use_column_width=True,
    )

st.divider()

# ---------------------------
# Espaço reservado para o formulário
# ---------------------------
st.markdown("## 📋 Área do formulário")

peso = st.number_input("Digite seu peso em kg: ",min_value=10.0,max_value=300.0)
altura = st.number_input("Digite sua altura em metros: ",min_value=1.0, max_value=3.0)

botao_imc = st.button("Calcular IMC")

### INTERAÇÕES ####
if botao_imc:
    imc = calcular_imc(peso,altura)
    categoria = categoria_imc(imc)
    st.divider()
    st.markdown("## 📊 Resultados")

    colA, colB = st.columns(2)
    colA.metric("IMC", f"{imc:.2f}")
    colB.metric("Categoria", categoria)

st.divider()

# ---------------------------
# Tabela de Classificação
# ---------------------------
st.markdown(
    """
    ### Classificação (adultos)
    | IMC (kg/m²) | Categoria      |
    |-------------|----------------|
    | < 18,5      | Abaixo do peso |
    | 18,5 – 24,9 | Peso normal    |
    | 25,0 – 29,9 | Sobrepeso      |
    | 30,0 – 34,9 | Obesidade I    |
    | 35,0 – 39,9 | Obesidade II   |
    | ≥ 40,0      | Obesidade III  |
    """
)

st.divider()
st.caption("© 2025 • Template IMC para prática em sala")

