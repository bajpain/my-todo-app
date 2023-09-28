import streamlit as st
import functions

filepath = 'files/todos.txt'
todos = functions.get_todos(filepath)


def add_todos():
    todo = st.session_state["new_todos"] + "\n"
    print(todo)
    todos.append(todo)
    functions.write_todos(filepath, todos)


st.title("My Todo App")

st.subheader("This my Todo App")
st.write("This app is to increase the productivity")



for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(filepath,todos)
        del st.session_state[todo]
        st.rerun()


st.session_state["new_todos"] = ""

st.text_input(label="", placeholder="Enter the todo...",
              on_change=add_todos, key="new_todos")

st.session_state