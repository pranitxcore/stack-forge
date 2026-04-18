import streamlit as st
from logic import get_stack
st.title("StackForge")
st.subheader("Your personalised stack recommender")

st.markdown('### Tell us about you !')
#Inputs
interest = st.selectbox("Your Interest",['Web Dev','App Dev','AI','Data Science'])
goal=st.selectbox("Your Goal",['Job','Freelancing','Startup'])
experience=st.selectbox("Your Experience Level",['Beginner','Intermediate'])

#Button
if st.button("🚀 Recommend My Stack"):
    result = get_stack(interest, goal, experience)
    st.markdown('### 🔧 Your Recommended Stack')
    
    for tool in result:
        st.write("•", tool)
st.divider()
st.caption("Built by PraxCore | Less Talk. More Build.")