import streamlit as st
import functions
todos = functions.get_todos()

st.subheader("This is my Todo App.")
st.write("This app is to increase your productivity.")
st.title("My Todo App")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")

