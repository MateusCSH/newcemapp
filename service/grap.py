import streamlit as st
import pandas as pd
import plotly.express as px

def grap_bar(df, va, vb):
    st.bar_chart(df, x = va, y = vb)