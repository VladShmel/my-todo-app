import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

def edit_todo():
    todo = st.session_state["new_todo"] + "\n"
    index = checkbox_list[0]
    todos[index] = (todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

st.text_input(label="Enter a new todo",
              placeholder="Add new todo...",
              label_visibility="hidden",
              key="new_todo")

button_add = st.button("Add")
button_complete = st.button("Complete")
button_edit = st.button("Edit")
checkbox_list=[]

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        checkbox_list.append(index)

if button_add:
    add_todo()
    st.experimental_rerun()

if button_complete:
    todos = [todo for index,todo in enumerate(todos) if index not in checkbox_list]
    functions.write_todos(todos)
    st.experimental_rerun()

if button_edit:
    try:
        edit_todo()
        st.experimental_rerun()
    except IndexError:
        print("OOPS")

# st.session_state