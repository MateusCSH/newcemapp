import streamlit as st
import pandas as pd
import plotly.express as px

def pie_grap(df, value, nomes, titulo:str):
    label = nomes
    fig = px.pie(
        df,
        values=value,
        names = nomes,
        title=titulo,
        textinfo=label
    )     
    st.plotly_chart(fig)
