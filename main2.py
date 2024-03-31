import pandas as pd
import streamlit as st
import plotly.express as px
from service.grap import grap_bar
from service.grapplotly import grap_plotly
from service.piegrap impor pie_grap


up = st.sidebar.file_uploader('Suba o arquivo', type='csv')

if up is not None:

    df = pd.read_csv(up, header=None, names=['Nome','Matricula','Tipo','Horas','Situação'], sep=',')

    name = st.sidebar.multiselect('Selecione os monitores:',
                                  options=sorted(df['Nome'].unique()),
                                  default=sorted(df['Nome'].unique()),
                                   placeholder = 'Selecione o arquivo')
    
    df_select = df.query(
        'Nome == @name'
    )
    #df_select = df[df['Nome']==name]

    op = st.selectbox('Opção:',
                ('Horas por Monitor','Horas por situação'),
                index=None,
                placeholder="Selecione a opção")

    st.write('Sua opção:', op)

    if op == 'Horas por Monitor':
        grap_bar(df_select,'Nome', 'Horas')
        grap_plotly(df_select, 'Horas', 'Nome')

        col1, col2 = st.columns(2)
        qtdhoras = int(df_select['Horas'].sum())
        maxhoras = int(df_select['Horas'].max())
        with col1:            
            st.metric('Horas acumuldas', qtdhoras,)
        with col2:
            st.metric('Hora máxima', maxhoras,)
            
             

    if op == 'Horas por situação':
        st.subheader('Gráfico de horas por utilização')
        grap_bar(df_select, 'Situação','Horas')
        grap_plotly(df_select, 'Horas','Situação')

        titulo = 'Gráfico de porcentagem - horas por situação'
        pie_grap(df_select, 'Horas', 'Situação', titulo)


    
    #df_select = df[df['Nome']==name]

else:
    st.warning('Para que consigamos mostrar o relatório necessita-se subir o arquivo')
    c = 'Browse files'
    st.caption(f'\nAo lado direito Clique em :blue[{c}] e selecione o arquivo desejado.')
    st.caption('O arquivo deve ser no formato :red[CSV]!')

