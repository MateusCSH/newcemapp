import pandas as pd
import streamlit as st
import plotly.express as px
from service.grap import grap_bar
from service.grapplotly import grap_plotly
from service.piegrap import pie_grap


up = st.sidebar.file_uploader('Suba o arquivo', type='csv')

if up is not None:

    df = pd.read_csv(up, header=None, names=['Nome','Horas','Motivo'], sep=',')

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
        
        st.info('**INFORMAÇÕES GERAIS**')
        st.subheader('',divider='rainbow')
        
        col1, col2, col3 = st.columns(3)
        qtdhoras = float(df_select['Horas'].sum())
        maxhoras = int(df_select['Horas'].max())
        qtdmoni = len(df_select['Nome'].unique())

        st.subheader('',divider='rainbow')
        
        with col1:            
            st.metric('Horas acumuldas', qtdhoras,)
        with col2:
            st.metric('Hora máxima', maxhoras,)
        with col3:
            st.metric('Quantidade monitor', qtdmoni)
            
             

    if op == 'Horas por situação':

        graf_bar, info, pizza = st.tabs(['GRÁFICO DE BARRAS','INFORMAÇÕES','PIZZA'])

        with graf_bar:
            st.info('GRÁFICO DE BARRAS')
            st.subheader('Gráfico de horas por utilização')
            grap_bar(df_select, 'Motivo','Horas')
            grap_plotly(df_select, 'Horas','Motivo')

        with info:
            st.info('**INFORMAÇÕES GERAIS**')
            st.subheader('',divider='rainbow')
            col1, col2, col3, col4 = st.columns(4)
            reun = df_select[df_select['Motivo'] == 'Reunião']['Horas'].sum()
            monin = df_select[df_select['Motivo'] == 'Monitoria']['Horas'].sum()
            aula = df_select[df_select['Motivo'] == 'Aula']['Horas'].sum()
            estu = df_select[df_select['Motivo'] == 'Estudos']['Horas'].sum()
    
            st.subheader('',divider='rainbow')
            
            with col1:
                st.metric('Horas Reunião',reun,)
    
            with col2:
                st.metric('Horas monitoria', monin,)
    
            with col3:
                st.metric('Horas aula', aula)
    
            with col4:
                st.metric('Horas estudo', estu)
        with pizza:
            st.info('PORCENTAGEM POR SITUAÇÃO')
            titulo = 'Gráfico de porcentagem - horas por situação'
            pie_grap(df_select, 'Horas', 'Motivo', titulo)
        


    
    #df_select = df[df['Nome']==name]

else:
    st.warning('Para que consigamos mostrar o relatório necessita-se subir o arquivo')
    c = 'Browse files'
    st.caption(f'\nAo lado direito Clique em :blue[{c}] e selecione o arquivo desejado.')
    st.caption('O arquivo deve ser no formato :red[CSV]!')

