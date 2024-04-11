import streamlit as st
import pandas as pd
import plotly.express as px

def pie_grap(df, value, nomes, titulo:str):
    fig = px.pie(
        df,
        values=value,
        names = nomes,
        title=titulo,
        labels = nomes
    )     
    st.plotly_chart(fig)
