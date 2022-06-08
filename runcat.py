import streamlit as st

#from random import random
#from pprint import pprint

#### plan:
#### store all item info in excel/csv sheet
#### when starting, cache this sheet ? why not a python dict?
#### select item from this sheet as might be used in this session => dict?
#### when item has been administered, remove from local structure
####

if not 'done' in st.session_state:

    st.session_state.done = False

    st.session_state.answers = [['Answer A correct','Answer B wrong','Answer C wrong','Answer D wrong']]

    st.session_state.questions = [('q1','What is the capital of the Netherlands?',['Amsterdam','Brussels','Westerlee','No clue'],0),
                                  ('q2','WHat is the capital of Europe?',['Paris','Rome','London','Europe has no capital'],3),
                                  ('q3','What is the capital of Canada?',['Montreal','Ottawa',"Vancouver",'New Found Land','Sioux Ste. Marie'],1)
                                  ]

    st.write(st.session_state.questions)


    st.session_state.ready     = [('What is the capital of the Netherlands',['Amsterdam','Brussels','Westerlee','No clue'])]


if not 'save_answers' in st.session_state:
    st.session_state.save_answers = {}


def pick_one(qid,question, options, answer_index,button='First click best answer, then press this button'):

    user_answer = st.radio(question, options=options,key=qid)

    if st.button(button, key=qid+'987654321'):

        is_correct = options.index(user_answer) == answer_index
        
        if "save_answers" in st.session_state: 
            st.session_state.save_answers[qid] = [qid,user_answer,options[answer_index],is_correct]
        return True, is_correct

    else:
        return False, None


pick_one('abc123','wassup? but that is too short - typically there is quite a bit of text here',['a','b','c','d'],3)


pick_one('pqr456','wassup? but that is too short - typically there is quite a bit of text here',['a','b','c','d'],0)

for k in st.session_state: 
    if k != 'save_answers': 
        st.write(k)
        del st.session_state[k]

st.session_state['save_answers']


