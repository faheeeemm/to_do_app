import streamlit as st
from modules import functions

st.title("My To Do App!")
st.subheader("TO-DOs")

todos = functions.get_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new Todo here")