import streamlit as st
import pandas as pd
import plotly.express as px

def pie_grap(df, value, nomes, titulo:str):   
    night_colors = ['rgb(56, 75, 126)', 'rgb(29, 45, 48)', 'rgb(3, 43, 44)'] 
    fig = px.pie(
        df,
        values=value,
        names = nomes,
        title=titulo,
        color_discrete_sequence=night_colors
    )    
    fig.update_traces(textposition='inside', textinfo='percent+label', textfont_size=15, textfont_color='darkblue')
    fig.update_layout(legend=dict(orientation="v", yanchor="bottom", y=0.65, xanchor="right", x=0.85))
    st.plotly_chart(fig)
