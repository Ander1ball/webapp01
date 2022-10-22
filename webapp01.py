# myFirstStreamlitApp.py
#import the libraries
import streamlit as st
from PIL import Image

image =Image.open('repository-open-graph-template (2).png')

# Use st.title("Minecraft") para adicionar um TÍTULO ao seu Web app
st.title("Minecraft")

# Use st.subheader("por que o jogo é bom para pensar?") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("por que o jogo é bom pra pensar?")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("O jogo minecraft é famosso em multiplas plataformas de gaming ou plataformas de streming")

st.subheader("O jogo conhecido como o jogo quadrado teve o seu lançamento em 18 de novembro de 2011, onde foi notado muitas caracteristicas marcantes do jogo,como por exemplo, o fato dele ser totalmente quadrado em até mesmo em seus personagens.")
st.subheader("Seu personagens no inicio eram somente um o canonico Steve, mas em setembro de 2014 foi adicionada a personagem Alex.")

menu = ["Texto_Colunas",
        "Texto_Markdown",
        "Inserir_Figura"]
choice = st.sidebar.selectbox("Menu de Opções",menu)
st.sidebar.write("Texto Side Bar")
    
if choice == "Texto_Colunas":       
    st.subheader("Texto formatado em colunas")
    st.write("Veja a seguir uma opção de formatação em colunas")    
    cols01 = st.columns(2)    
    cols01[0].write('Texto da Coluna 01')
    cols01[1].write('Texto da Coluna 02')
elif choice == "Texto_Markdown":
    st.subheader("Texto Markdown")
    st.write("Veja a seguir opção de formatação de texto Markdown")
    st.markdown(
    """
    ## *Alguns sites referências*:    
    - [Streamlit: hello world](https://calmcode.io/streamlit/hello-world.html)
    - [:star: Streamlit emoji shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlitapp.com/)
    - [Layouts and Containers](https://docs.streamlit.io/library/api-reference/layout)
   
    ##### CRONOGRAMA
    DIA | CH HORÁRIA | CONTEÚDO
    :---------: | :------: | :-------:
    Dia 1 de 2 | ?h | ? a ?
    Dia 2 de 2 | ?h | ? a ?
    """
    )
elif choice == "Inserir_Figura":
    st.image(image01, width=800, caption='Rótulo da Imagem 01') 
    
