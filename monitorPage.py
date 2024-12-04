#core package
import streamlit as st

#EDA
import pandas as pd

#data viz
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

import plotly.express as px
import seaborn as sns
import altair as alt

#database fxn
from databaseFxn import view_all_data,view_unique_tasks

#main_fxn
def analyticsSectionFxn():
    #show all existing data from database
    result_all_data = view_all_data()
    all_data_df = pd.DataFrame(result_all_data,columns=['User','Task','Status','Due'])
    
    st.header('Existing Tasks')
    st.dataframe(all_data_df,use_container_width=True)


    with st.expander('User Stats'):
        # Calculate task counts per user
        all_data_user_df = all_data_df.groupby('User').size().reset_index(name='Task Count')

        # Altair bar chart
        user_chart = alt.Chart(all_data_user_df).mark_bar().encode(
            x=alt.X('User:N', title='User'),  # Nominal scale for User
            y=alt.Y('Task Count:Q', title='Task Count'),  # Quantitative scale for task counts
            color=alt.Color('User:N', legend=None),  # Optional: color each user differently
            tooltip=['User', 'Task Count']  # Tooltip to show counts when hovering
        )
        #display
        st.altair_chart(user_chart,use_container_width=True)


    with st.expander('Task Type Stats'):
        #plotly for pie chart
        df_pie = all_data_df['Status'].value_counts().to_frame()
        df_pie = df_pie.reset_index()
        df_pie.columns = ['Status','Counts']

        pie_fig = px.pie(data_frame=df_pie,names='Status',values='Counts')
        st.plotly_chart(figure_or_data=pie_fig,use_container_width=True)

if __name__ == '__main__':
    analyticsSectionFxn()