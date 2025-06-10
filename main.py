import streamlit as st
import groq 
MODELOS = ['llama3-8b-8192', 'llama3-70b-8192','mixtral-8x7b-32768']

#Configurar paguina
def configurar_pagina():
    st.set_page_config(page_title="Boca", page_icon = "🗿")
    st.title("Bienvenido a mi casa")

#CREar un CLIENTE GROQ me permite conectar con api de groq aca el cliente somos nosotros
def crear_cliente_groq(): #almacena los modelos de IA
    groq_api_key = st.secrets["GROQ_API_KEY"] #aca guardo la api key que me dio groq lee la api key atraves de streamlit que busca en la carpeta donde yo guarde la key
    return groq.Groq(api_key = groq_api_key) #Es un estring poreso la variable se lapasamos con comillas en el secrets

#Mostrar LA BARRA LATERL
def mostrar_sedebar():
    st.sidebar.title("Elegi tu modelo de IA favorito")
    modelo = st.sidebar.selectbox("elegi tu modelo", MODELOS, index =0)
    st.write(f"**ELeguiste el modelo:** {modelo}")
    return modelo

#INICIALIZAR EL ESTADO DEL CHAT 
def inicializar_estado_chat():
    if "mensajes" not in st.session_state: # not in si no esta en
        st.session_state.mensajes = [] #Bariable especial permite Almacenar otras variables es una lista

#MOSTRAR LOS MESAJER PREVIOS  
def obtener_mensajes_previos():
    for mensaje in st.session_state.mensajes:
        with st.chat_message(mensaje["role"]): #Generas una cajita de mensajes y reconosco quien lo envio al poner rol
            st.markdown(mensaje["content"]) # Muestra una cajita visualmente y tiene el contenido del mensaje

#OBTENER MENSAJE USUARIO
def obtener_mensaje_usuario():
    return st.chat_input("Envia tu mensaje") #lugar donde el usuario o cliente va escribir su mensaje

#GUARDAR LOS MENSJES
def agregar_mensajes_previos(role, content):
    st.session_state.mensajes.append({"role": role, "content": content})#meto cada mensaje para que me mustro el contenido y el rol de quien lo mando porque antes estaba vacia

#MOSTRAR LOS MENSAJES EN PANTALLA
def mostrar_mensajes(role, content):
    with st.chat_message(role):
        st.markdown(content)

#CREACION DEL MODELO DE GROQ 


#EJECUTAR FUNCIONES
def ejecutar_funciones():
    configurar_pagina()
    cliente = crear_cliente_groq()
    modelo = mostrar_sedebar()
    print(modelo)
    inicializar_estado_chat()    
    mensajeusuario = obtener_mensaje_usuario()
    print(mensajeusuario)
    # obtener_mensajes_previos()    

#EJECUTAR LA APP 
if __name__ == "__main__": #Condiciona al name que es una funcion de paiton que toma un valor string aca le estoy dando el valor del archivo principal llamado main
    ejecutar_funciones() #si el name es distinto a main no se ejecuta nada porque no estoy en el archivo principal

