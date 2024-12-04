#core package
import streamlit as st
import streamlit.components.v1 as stc


#APP_parts
from readPage import readPageRun
from postPage import taskSectionFxn
from monitorPage import analyticsSectionFxn

#utils
import time

#database
from databaseFxn import create_table

#######################################
#body

#header
HTML_BANNER = """
<div style="font-size:40px;font-weight:bolder;color: #F7F5FB;background-color:#6640C9;padding:10px;
border-radius:10px;border:10px solid #020008;text-align:center;">Task-List App
</div>
"""
stc.html(HTML_BANNER)
###########################################
def exclaimation():
    t=time.strftime('%H:%M:%S')
    hour=int(time.strftime('%H'))
    
    if(hour>=5 and hour<12):
        return "Good Morning"
    elif(hour>=12 and hour<17):
        return "Good Afternoon"
    elif(hour>=17 and hour<22):
        return "Good Evening"
    elif(hour>=22 and hour<=23):
        return f"it's {t} PM Already"
    else:
        return f"it's {t} AM Already"

def runHomePage():
    schoice = st.radio(label=":red[How to Use TaskList??]",options=['Read','Add Task','Edit Task','Delete Task','Analytics'],horizontal=True)
    if schoice == 'Read':
        st.markdown("## Read By :green[Task]")
        with st.expander("See"):
            st.image("images/ReadTask-01.png")
        st.markdown("## Read By :blue[User]")
        with st.expander("See"):
            st.image("images/ReadTask-02.png")
            
    elif schoice == 'Add Task':
        st.markdown("## Fill :grey[All Options]")
        with st.expander("See"):
            st.image("images/AddTask-01.png")
            st.image("images/AddTask-02.png")
            st.image("images/AddTask-03.png")
            
        st.markdown("## Click :blue[Add] button")
        with st.expander("See"):
            st.image("images/AddTask-04.png")
            st.image("images/AddTask-05.png")
    elif schoice == 'Edit Task':

        st.markdown("## Step 1: Edit :red[Required Options]")
        with st.expander("See"):
            st.image("images/EditTask-01.png")
            st.image("images/EditTask-02.png")
        st.markdown("## Step 2: Click :grey[Update Task] Button")
        with st.expander("See"):
            st.image("images/EditTask-03.png")

    elif schoice == 'Delete Task':
        st.markdown("## Step 1: :green[Choose Task] to delete")
        with st.expander("See"):
            st.image("images/DeleteTask-01.png")
        st.markdown("## Step 2: Confirm :blue[Checkbox] and :red[Delete]")
        with st.expander("See"):
            st.image("images/DeleteTask-02.png")
    elif schoice == 'Analytics':
        st.markdown("## :grey[User Analysis]")
        with st.expander("See"):
            st.image("images/Analytics-01.png")
        st.markdown("## :red[Progress] Wise Analysis")
        with st.expander("See"):
            st.image("images/Analytics-02.png")

###########################################
#main_fxn
def main():
    choice = st.sidebar.selectbox('Menu',['Home','Read','Post','Analytics','About'])
    create_table()
    if choice == 'Home':
        st.title("Welcome to :blue[Task-List App] 🐱")
        runHomePage()
        
    elif choice == 'Read':
        readPageRun()
    
    elif choice == 'Post':
        # st.title('Task List')
        taskSectionFxn()

    elif choice == 'Analytics':
        analyticsSectionFxn()

    else:
        #some issue in this
        #sommodhon = exclaimation()

        #so
        sommodhon = "How it's going?"
        st.markdown(f"""
        ## Hey Dude :green[{sommodhon}]
           + I am Kaushik
           + It's my Task-List App
           + This is made with Streamlit
        """)
if __name__ == '__main__':
    main()

# Using CSS Flexbox for layout
st.markdown("""
    <style>
    .footer {
        background-color: #2c2c2c;
        color: #f1f1f1;
        padding: 10px;
        text-align: center;
        position: relative;
        width: 100%;
        bottom: 0;
    }
    .content {
        min-height: calc(100vh - 100px);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    a {
        color: #64b5f6;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
    <div class="content">
        <div></div>
        <div class="footer">
            <p><b>Contact Us</b></p>
            <p>Ping me on GitHub: <a href="https://github.com/amiKaushik" target="_blank">https://github.com/amiKaushik</a></p>
        </div>
    </div>

""", unsafe_allow_html=True)
