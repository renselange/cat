import streamlit as st

from random import random

#### plan:
#### store all item info in excel/csv sheet
#### when starting, cache this sheet ? why not a python dict?
#### select item from this sheet as might be used in this session => dict?
#### when item has been administered, remove from local structure
####

def expand(x): return [x]

if not 'done' in st.session_state:

    st.session_state.done    = False
    st.session_state.unused  = [(0,[0,0]),(1,[0,-1,1]),(2,[0,0])]
    st.session_state.used    = []
    st.session_state.pending = []


if not st.session_state.done:

    if not st.session_state.pending:

# get either a starter item or the most informative item
        seq = int(random() * len(st.session_state.unused)) # randomly 
        st.session_state.pending = [st.session_state.unused.pop(seq)]

# pick the first item from the pending list, always
    if st.session_state.pending:
        first = st.session_state.pending.pop(0)
        st.write('Administer this item:',first)
        st.session_state.used.append(first)

        st.session_state.done = len(st.session_state.unused) == 0

    next_question = st.button('Press to continue ...')
    if next_question:
        st.write(st.session_state)


if st.session_state.done:
    'Thank you, you are done now'
    st.table(st.session_state.used)
  




