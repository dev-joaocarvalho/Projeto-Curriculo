import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="João Carvalho",
    page_icon="🙂",
    layout="centered",
    initial_sidebar_state="auto"
)

col1, col2 = st.columns([4, 1])
    
with col1:
    st.title("João Marcos Santos e Carvalho")
    st.write("Estudante de Ciência da Computação, com paixão por tecnologia, programação e análise de dados.")
        

        
    st.divider()
    st.subheader(":blue[PROJETOS]")
    st.write("**[Projeto Currículo](https://curriculo-joaocarvalho.streamlit.app/)** — _Projeto Python_")
    st.caption("Objetivo de criar esse currículo em um site usando a biblioteca Streamlit do Python. ")
    st.write("**Projeto Guia do Universitário** — _Projeto Integrador_")
    st.caption("Plataforma web para ajudar calouros com dicas sobre a faculdade e estudos.")


    st.divider()
    st.subheader(":blue[FORMAÇÃO]")
    st.write("Instituto de Educação Superior de Brasília (IESB), Asa Sul, DF")
    st.caption("Bacharelado em Ciência da Computação - Quarto semestre, com previsão de formatura em 2026.")

    st.divider()

    st.subheader(":blue[REDES]")

    button_col1, button_col2, button_col3, button_col4 = st.columns([1, 1, 1, 1])

    with button_col1:
        st.link_button("🐈‍⬛Github", "https://github.com/dev-joaocarvalho") 

    with button_col2:
        st.link_button("🌎LinkedIn", "https://www.linkedin.com/in/joaom-s-carvalho/")
          

with col2:
    st.caption("Brasília, DF, 73105-905")
    st.caption("**☎️ +55 61 98199-4401**")
    st.caption("**dev.joaocarvalho@gmail.com**")
    button_col1, button_col2 = st.columns([1, 1])
    with button_col1:
        st.link_button("🐈‍⬛Github", "https://github.com/dev-joaocarvalho") 
    with button_col2:
        st.link_button("🌎LinkedIn", "https://www.linkedin.com/in/joaom-s-carvalho/")
        
    st.divider()
    st.write(":blue[COMPETÊNCIAS]")
    st.caption("Programação: C, Java, Python.")
    st.caption("Análise de Dados: Excel, Python (Pandas, NumPy), SQL.")
    st.caption("Desenvolvimento Web: HTML, CSS, Streamlit.")
    st.caption("Ferramentas: Eclipse, Visual Studio Code, Spring Boot.")
    st.caption("Banco de dados: DBeaver.")
    st.caption("Sistemas Operacionais: Linux, Windows.")

    st.divider()
    st.write(":blue[PROJETOS VOLUNTÁRIOS]")
    st.caption("Monitoria em Tópicos de Matemática")
        
    st.divider()
    st.write(":blue[IDIOMAS]")
    st.caption("Inglês Intermediário.")

st.divider()
