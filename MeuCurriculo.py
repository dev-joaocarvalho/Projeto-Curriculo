import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="João Carvalho",
    page_icon="🙂",
    layout="wide",
    initial_sidebar_state="auto"
)

col1, col2 = st.columns([4, 1])
    
with col1:
    st.title("João Marcos Santos e Carvalho")
    st.write("Estudante de Ciência da Computação, com paixão por tecnologia, programação e análise de dados.")
        

        
    st.divider()
    st.subheader(":blue[EXPERIÊNCIA ACADÊMICA E PROJETOS]")
    st.write("**Monitoria no departamento de Matemática**")
    st.caption("Desenvolvimento de didática e comunicação técnica clara para explicação de conceitos abstratos e resolução de problemas. ")
    st.write("**[Projeto Immunity Dashboard](https://immunity-dashboard.streamlit.app/)** — _Python e Streamlit_")
    st.caption("Desenvolvimento de aplicação web interativa para análise e visualização de dados de vacinação ")
    st.write("**Projeto Guia do Universitário** — _Projeto Integrador_")
    st.caption("Plataforma web para ajudar calouros com dicas sobre a faculdade e estudos.")


    st.divider()
    st.subheader(":blue[FORMAÇÃO]")
    st.write("Instituto de Educação Superior de Brasília (IESB), Asa Sul, DF")
    st.caption("Bacharelado em Ciência da Computação - Quarto semestre, com previsão de formatura em 2026.")

    st.divider()
          

with col2:
    st.caption("Brasília, DF, 73105-905")
    st.caption("**☎️ +55 61 98199-4401**")
    st.caption("**dev.joaocarvalho@gmail.com**")
    st.link_button("🐈‍⬛GitHub", "https://github.com/dev-joaocarvalho") 
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
    st.write(":blue[IDIOMAS]")
    st.caption("Português Nativo.")
    st.caption("Inglês Intermediário.")

st.divider()
