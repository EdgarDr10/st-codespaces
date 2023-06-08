import streamlit as st

st.title("Hola worlds!")
st.write("This is a super cool Streamlit app.")


import streamlit as st

Valor = st.sidebar.slider('Indica el valor ', 0, 10)
st.write("este es mi valor = ", Valor)
st.write("este es mi valor + 10= ", Valor+10)


agree = st.sidebar.checkbox('El valor es mayor que 5')

if Valor >5 and agree:
    st.write("mayor que 5")

import pandas as pd
data=pd.read_csv("big mac.csv")
st.write(data.head())


import streamlit as st

option = st.sidebar.selectbox(
    'Indicame el País',
    ('Argentina', 'Brazil'))


data_pais=data.loc[data['name']==option,:]
st.write(data_pais.head())

name_data=data['name'].unique().tolist()


option_lista= st.sidebar.selectbox(
    'Indicame el País de la lista',
    (name_data))

data_pais_1=data.loc[data['name']==option_lista,:]
st.write(data_pais_1.head())


st.line_chart(data_pais_1, x="date",y="dollar_price")

