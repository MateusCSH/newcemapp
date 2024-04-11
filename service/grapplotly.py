
import pandas as pd
import plotly.express as px
import streamlit as st

def grap_plotly(df, eixo_x, eixo_y):
    fig = px.bar(
        df,
        x = eixo_x,
        y = eixo_y,
        orientation='h',
        title='<b>Gráfico de horas por monitor<b>',
        template='plotly_white'        
    )
    fig.update_traces(text=df[eixo_y], textposition='outside')

    st.plotly_chart(fig)
