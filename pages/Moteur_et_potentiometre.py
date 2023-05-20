import streamlit as st
import plotly.graph_objs as go
import paho.mqtt.client as mqtt
import sqlite3
import math

#-------configuration du broker------------
mqtt_broker = "test.mosquitto.org"
mqtt_port = 1883
mqtt_topic = "test/pwm"

#-------config client-----

mqtt_client = mqtt.Client()
mqtt_client.connect(mqtt_broker, mqtt_port)
#mqtt_client.subscribe("test/potar")



#data = []
#-----fonction acquisition des données du potentiometre----------
#def on_message(client,userdata,message):
 #   if message.topic == "test/potar" :
 #       new_data = message.payload.decode("utf-8")
 #       data.append(int(new_data))

 #------fonction envoi de massage-----------------   
def send_message(value):
    message = str(value)
    mqtt_client.publish(mqtt_topic, message)

st.title("Exemple d'application MQTT  avec STREAMLIT")

st.subheader("Commande d'un moteur à courant continu par PWM")
value = st.slider("Sélectionner une valeur",0,1023,20)
#envoyer=st.button("Envoyer")
#if envoyer:
send_message(value)
#    st.write("message envoyé",value)
   
#mqtt_client.on_message = on_message

#st.subheader("Exemple de graphique Plotly en temps réel")
#graph= st.empty()
while True:        
    mqtt_client.loop()
    
    #fig=go.Figure(data=[go.Scatter(y=data,mode='lines+markers')])
    #fig.update_layout(title="Exemple de graphique en chart avec une echelle fixe sur y", yaxis=dict(range=[0,4500]))
    #graph.plotly_chart(fig,use_container_width=True)