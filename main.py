import streamlit as st
import groq 
MODELOS = ['llama3-8b-8192', 'llama3-70b-8192','gemma2-9b-it']

#Configurar paguina
def configurar_pagina():
    st.set_page_config(page_title="Proyecto Final", page_icon = "🗿")
    st.title("Bienvenido sentite como en casa")

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

#llamar aL MODELO DE GROQ 
def obtener_respuesta_modelo(cliente, modelo, mensaje): # obtengo el mensaje del cliente 
    respuesta = cliente.chat.completions.create( # almaceno la respuesat del modelo
        model = modelo,
        messages = mensaje,
        stream = False, # esto nos permite devolver el mensaje de una ves y no en partes
    )
    return respuesta.choices[0].message.content # me devuelve le mensaje de la posicion 0 del cliente


#EJECUTAR FUNCIONES
def ejecutar_funciones():
    configurar_pagina()
    cliente = crear_cliente_groq()
    modelo = mostrar_sedebar()
    # print(modelo) ca muestro el modelo elegido en la terminal

    inicializar_estado_chat()    
    mensaje_usuario = obtener_mensaje_usuario()
    # print(mensaje_usuario) aca muestro el mensaje en la terminal

    obtener_mensajes_previos()

    if mensaje_usuario:
        agregar_mensajes_previos("user", mensaje_usuario) #guardo el quein lo envia y que envia
        mostrar_mensajes("user", mensaje_usuario) # aca muestro el mensaje en la interfas

        respuesta_contenido = obtener_respuesta_modelo(cliente, modelo, st.session_state.mensajes)

        agregar_mensajes_previos("assistant",respuesta_contenido)
        mostrar_mensajes("assistant",respuesta_contenido)
    
#EJECUTAR LA APP 
if __name__ == "__main__": #Condiciona al name que es una funcion de paiton que toma un valor string aca le estoy dando el valor del archivo principal llamado main
    ejecutar_funciones() #si el name es distinto a main no se ejecuta nada porque no estoy en el archivo principal

