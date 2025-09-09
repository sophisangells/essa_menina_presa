import streamlit as st
import time

st.title("Calisthenics ")
st.caption("Só pega")

'Carregando seu nivel de habilidade'

# Add a placeholder
latest_iteration = st.empty()



# Add a selectbox to the sidebar:                        python -m streamlit run C:\Users\Aluno_Programador3\Desktop\I_LOVE_PASTAS\ProjectsStremlit\FirstProject.py

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'O QUE É CALISTENIA', 'Local de Treino')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.randn(15, 3), columns=(["A", "B", "C"]))
my_data_element = st.line_chart(df)

for tick in range(10):
    time.sleep(.5)
    add_df = pd.DataFrame(np.random.randn(1, 3), columns=(["A", "B", "C"]))
    my_data_element.add_rows(add_df)

st.button("Regenerate")

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Carregando o site {i+1}')
  bar.progress(i + 1)
  time.sleep(0.01)


