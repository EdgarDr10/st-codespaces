import streamlit as st

st.title("Hola worlds!")
st.write("This is a super cool Streamlit app.")


import streamlit as st

Valor = st.slider('Indica el valor ', 0, 10, 2)
st.write("este es mi valor = ", Valor)
st.write("este es mi valor + 10= ", Valor+10)

if Valor >5:
    print("mayor que 5")
else:
    print("menor que 5")