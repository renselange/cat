

import streamlit as st

q = ['question_%d'%d for d in range(3)]

st.title('Counter Example')
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Increment')
decremnet = st.button('Decrement')

if increment:
    st.session_state.count = (st.session_state.count +1)%len(q)

if decrement:
    st.session_state.count = (st.session_state.count -1)%len(q)




st.write('Count = ', st.session_state.count)