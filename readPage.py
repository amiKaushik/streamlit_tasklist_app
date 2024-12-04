#core package
import streamlit as st

#EDA
import pandas as pd

#database
from databaseFxn import view_all_data,view_unique_user,view_unique_tasks,get_task,get_user

def readByTask(search_element):

    col1,col2 = st.columns(2)
    with col1:
        st.subheader('Selected Task')
        st.write(search_element)

    with col2:
        st.subheader('Details')
        try:
            task_elements_selected = get_task(search_element)    
            # st.write(task_elements_selected)
            if not task_elements_selected:
                st.write(f'No tasks found for user: {search_element}')
                return
            st.write(f'Task: :green[{search_element}]')

            st.markdown("---")  # Adds a separator between tasks
            for i, task_element in enumerate(task_elements_selected):
                st.write(f'User {i+1}: :red[{task_element[0]}]')
                st.text(f'Task Status: {task_element[2]}')
                st.text(f'Due Date: {task_element[3]}')
                st.markdown("---")  # Adds a separator between tasks


        except Exception as e:
            st.info(f'Error Occurred: {e}')

def readByUser(search_element):

    col1,col2 = st.columns(2)
    with col1:
        st.subheader('Selected User')
        st.subheader(f":green[{search_element}]")
    with col2:
        st.subheader('Task Details')
        try:
            task_elements_selected = get_user(search_element)    
            
            if not task_elements_selected:
                st.write(f'No tasks found for user: {search_element}')
                return
            #st.write(f'User: "{search_element}"')

            st.markdown("---")  # Adds a separator between tasks
            for i, task_element in enumerate(task_elements_selected):
                st.write(f'Task {i+1}: :red[{task_element[1]}]')
                st.text(f'Task Status: {task_element[2]}')
                st.text(f'Due Date: {task_element[3]}')
                st.markdown("---")  # Adds a separator between tasks

        except Exception as e:
            st.info(f'Error Occurred: {e}')


#main_fxn
def readPageRun():
    st.subheader('Read Existing Tasks')
    list_of_tasks = [i[0] for i in view_unique_tasks()]
    list_of_users = [i[0] for i in view_unique_user()]
    

    search_field = st.radio('Search By',['Task','User'])
    search_element = st.text_input(label='Search')
    if search_element:
        search_element_lower = search_element.lower().strip()  # Convert input to lowercase and strip extra spaces
    try:
        if st.button('Read'):
            # Case-insensitive, partial matching logic
            matching_tasks = [task for task in list_of_tasks if search_element_lower in task.lower()]
            matching_users = [user for user in list_of_users if search_element_lower in user.lower()]

            if search_field == 'Task':
                if matching_tasks:
                    for task in matching_tasks:
                        readByTask(task)  # Display tasks that match the partial search
        
                else:
                   st.warning(f'No tasks found matching "{search_element}"')

            elif search_field == 'User':
                if matching_users:
                    for user in matching_users:
                        readByUser(user)  # Display users that match the partial search
                else:
                    st.warning(f'No users found matching "{search_element}"')

    except Exception as e:
        st.info(f'Error Occurred: {e}')
    
    
if __name__ == '__main__':
    readPageRun()