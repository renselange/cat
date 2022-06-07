import streamlit as st

#### plan:
#### store all item info in excel/csv sheet
#### when starting, cache this sheet ? why not a python dict?
#### select item from this sheet as might be used in this session => dict?
#### when item has been administered, remove from local structure
####



if "celsius" not in st.session_state:
    # set the initial default value of the slider widget
    st.session_state.celsius = -40
    st.session_state.fahrenheit = -40

if st.session_state.celsius > 0:
    st.slider(
        "Temperature in Celsius",
        min_value=-100.0,
        max_value=100.0,
        key="celsius"
    )

else: 
    st.slider(
        "Temperature in Fahrenheit",
        min_value=-100.0,
        max_value=100.0,
        key="fahrenheit"
    )

# This will get the value of the slider widget
st.write('%0.1fC => %0.1fF'%(st.session_state['celsius'],9*st.session_state['celsius']/5 + 32))
