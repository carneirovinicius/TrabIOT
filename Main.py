#!/usr/bin/env python
# coding: utf-8

# In[43]:


import paho.mqtt.client as mqtt
import os
import time
import random

temperatures = [28, 29, 30, 31]

def sendMessages():
    #Define o cliente MQTT
    client = mqtt.Client()

    # A aplicação Node Red está rodando localmente. Abrimos a conexo em mtqq://127.0.0.1:1883
    client.connect("localhost",1883,60)

    # Envia mensagem para o endereço
    while True:
        temperature = random.choice(temperatures)
        client.publish("iot", temperature)
        time.sleep(1)
        
    client.disconnect()

    # Fecha a conexao
if __name__ == "__main__":
    sendMessages()
    


# No computador, foi utilizado o Mosquitto para possibilitar o uso do protocolo mtqq.

# In[39]:


random.choice(temperatures)


# In[ ]:




