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

