import streamlit as st

#from random import random
#from pprint import pprint

#### plan:
#### store all item info in excel/csv sheet
#### when starting, cache this sheet ? why not a python dict?
#### select item from this sheet as might be used in this session => dict?
#### when item has been administered, remove from local structure
####


def do_cat(): return 0 # implement and we have real CAT

'# An item DB with three glorious questions'

if not 'done' in st.session_state:

    st.session_state.done = False

    st.session_state.questions = [('q1','What is the capital of the Netherlands?',['Amsterdam','Brussels','Westerlee','No clue'],0),
                                  ('q2','WHat is the capital of Europe?',['Paris','Rome','London','Europe has no capital'],3),
                                  ('q3','What is the capital of Canada?',['Montreal','Ottawa',"Vancouver",'New Found Land','Sioux Ste. Marie'],1)
                                  ]

    st.write(st.session_state.questions)
    st.session_state.ready     = []
    st.session_state.answers = {}
    st.session_state.save_answers = True


def pick_one(qid,question, options, answer_index,button='First click the best answer, then press this button'):

    user_answer = st.radio(question, options=options,key=qid)

    if st.button(button, key=qid+'987654321'):

        is_correct = options.index(user_answer) == answer_index
        
        if "save_answers" in st.session_state: 
            st.session_state.save_answers[qid] = [qid,user_answer,options[answer_index],is_correct]
        return True, is_correct

    else:
        return False, None


if not st.session_state.done:

    pick_this_one = do_cat() # all I have to do is to implement do_cat and we have REAL cat!!!!!

    qid,qtext,qchoices,qcorrect = st.session_state.questions.pop(pick_this_one) 

    administer =  pick_one(qid,qtext,qchoices,qcorrect)

    st.session_state.answers[qid] = administer

    st.session_state.done = len(st.session_state.answers) > 2


if st.session_state.done:

    '# and we are finished'

    st.write(st.session_state)


