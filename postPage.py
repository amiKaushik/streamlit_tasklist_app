#core package
import streamlit as st

#utils
from datetime import datetime

#EDA
import pandas as pd

#database
from databaseFxn import add_data,edit_task_data,view_all_data,view_unique_tasks,get_task,delete_task
########################################

#show table
def show_table(title):
    # view_all_data() returns all existing todo work in our DATA BASE
    try:
        result_all_data = view_all_data()
        all_data_df2 = pd.DataFrame(result_all_data,columns=['User','Task','Status','Due'])
        
        with st.expander(f'{title}'):
            st.dataframe(all_data_df2,use_container_width=True)

    except Exception as e:
        st.error(f'Error Occurred: {e}')

######################################
def addTask():
    #input
    col1,col2 = st.columns(2)
    with col1:
        doer = st.text_input('User')
        task = st.text_area('Task')

    with col2:
        status = st.selectbox(label='Task Status',options=['To Do','Inprogress','Incomplete','Completed','Abandoned','Uncertain'])
        due = st.date_input('Task Due Date',min_value=datetime.now())
    
    #submit
    if doer and task and status and due:
        if st.checkbox('Confirm') and st.button('Add'):
            try:
                add_data(doer.lower().capitalize(),task.lower().capitalize(),status,due)
                st.success(f'Added "{task}" to Task')
                # st.write(task_inp)
                show_table(title='Updated Task List')

            except Exception as e:
                st.error(f'Error Occurred: {e}')

def editTask():
    show_table(title='Current Task List')
    list_of_task =[i[0] for i in view_unique_tasks()] 
    # i in view_unique_tasks means we are iterating through our data(to-do list)
    # i[0] is the first data of each to-do task i.e. TASK NAME
    
    select_task = st.selectbox(label='Task',options=list_of_task)
    
    #depending upon the task -name we fetch all elements of it as a LIST
    task_element_selected = get_task(select_task)
    # see st.image('Screenshot 2024-10-26 195809.png')
    
    if task_element_selected:
        task_element = task_element_selected[0]
        
        # for example do : st.write(type(task_element))
        # task_element is a tuple inside task_element_selected
        # task_element = ('Kaushik', 'Watch Attack on titan', 'To Do', '2025-02-14')
        
        task_user = task_element[0]      #1st element of task_element
        task_name = task_element[1]
        task_status = task_element[2]
        task_due_date = task_element[3]

        # Convert task_due_date from string to datetime.date
        task_due_date = datetime.strptime(task_due_date, "%Y-%m-%d").date()

        col1,col2 = st.columns(2)
        with col1:
            edited_doer = st.text_input(label='Edit Task Doer',value=task_user).lower().capitalize()
            edited_task = st.text_area(label='Edit Task',value=task_name).lower().capitalize()
    
        with col2:
            edited_status = st.selectbox(label='Edit Task Status', options=['To Do', 'Inprogress', 'Incomplete', 'Completed', 'Abandoned', 'Uncertain'], index=['To Do', 'Inprogress', 'Incomplete', 'Completed', 'Abandoned', 'Uncertain'].index(task_status))
            edited_due = st.date_input(label='Edit Task Due Date',value=task_due_date)
    
        #update
        if st.button('Update Task'):
            # Check that the fields are not empty after stripping whitespace
            # strip() method used to remove extra white spaces
            if edited_doer.strip() and edited_task.strip() and edited_status and edited_due:
                try:
                    #edit in database
                    edit_task_data(edited_doer, edited_task, edited_status, edited_due, task_user, task_name, task_status, task_due_date)

                    st.success(f'Task "{edited_task}" updated successfully.')
                    show_table(title='Updated Task List')

                except Exception as e:
                    st.error(f'Error occurred: {e}')
            else:
                st.warning('Please fill in all fields.')


def deleteTask():
    #show existing Tasks from database in table/dataframe
    show_table(title='Existing Tasks')
    list_of_task = [i[0] for i in view_unique_tasks()]

    select_task = st.selectbox(label='Select Task',options=list_of_task)
    if st.checkbox('Confirm'):
        if st.warning(f'Are you sure to Delete "{select_task}" From Task List') and st.button('Delete'):
            
            try:
                delete_task(select_task)
                st.info('Task Deleted from Task List')
            except Exception as e:
                st.error(f'Error Occurred: {e}')
            #show updated database
            show_table(title='Updated Task List')

#######################################
#main_fxn
def taskSectionFxn():
    #st.subheader('meow')
    choice = st.sidebar.selectbox('SubMenu',['Add Task','Edit Task','Delete Task'])

    if choice == 'Add Task':
        st.header(':green[Add Task]')
        addTask()

    elif choice == 'Edit Task':
        st.subheader('Edit Task')
        editTask()

    elif choice == 'Delete Task':
        st.subheader('Delete Task')
        deleteTask()

if __name__ == '__main__':
    taskSectionFxn()