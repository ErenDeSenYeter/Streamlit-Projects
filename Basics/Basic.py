import streamlit as st 

st.title("Streamlit App Title")
st.write("First Steps")
button1 = st.button("Click Me")

if button1: 
    st.write("This Special Text")

st.header("Checkbox Button ")


like = st.checkbox("Do you like this app ? ")

button2 = st.button('Submit')
if button2:
    if like :
        st.write('Yeah i like it too')
    else:
        st.write('Bad Taste you have!') 










