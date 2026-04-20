import streamlit as st
from logic import get_stack
st.title("StackForge")
st.subheader("Your personalised stack recommender")

st.markdown('### Tell us about you !')
#Inputs
interest = st.selectbox("Your Interest",['Web Dev','App Dev','AI','Data Science'])
goal=st.selectbox("Your Goal",['Job','Freelancing','Startup'])
experience=st.selectbox("Your Experience Level",['Beginner','Intermediate'])

if st.button("🚀 Recommend My Stack"):
    result = get_stack(interest, goal, experience)

    # Context header
    st.success(f"{interest} • {goal} • {experience}")

    st.markdown("### 🔧 Your Recommended Stack")

    # Grid layout
    cols = st.columns(2)

    for i, tool in enumerate(result):
        cols[i % 2].markdown(f"✅ **{tool}**")

    # Copy section
    st.markdown("### 📋 Copy Stack")
    stack_text = ", ".join(result)
    st.text_input("", stack_text)
    # st.code(stack_text, language="text")
