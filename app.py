import streamlit as st
import pandas as pd

dic = {'cpf':str}
df = pd.read_csv(r'dataframe.csv',sep=';', dtype=dic)

st.set_page_config(layout='wide', page_title='CIP')

col_1, col_2, col_3 = st.columns(3)
with col_2:
    titulo = st.title('C.I.P')

with st.sidebar:
    cpfcnpj = st.text_input(
        label="CPF CLIENTE"
    )

if cpfcnpj != '':
    tabela_filtrada = df[df['cpf'] == cpfcnpj]
    st.dataframe(tabela_filtrada,use_container_width=True,hide_index=True)
else:
    st.info('Você deve procurar um CPF ou CNPJ')
