import streamlit as st
import pandas as pd
import requests
import numpy as np
# Pokemon by name
my_title = st.empty()
pokemon_number = st.slider("Give me a num from 1 to 155: ", 1, 155)
url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}/'

response = requests.get(url).json()

pokemon_name = response['name']
my_title.title(f"{pokemon_name} info")
pokemon_ability = response['abilities']
weight = response['weight']
height = response['height']
base_exp = response['base_experience']
pokemon_sprite = response['sprites']
col0, col1, col2, col3, col4 = st.columns(5)

col0.write('image')
col1.write("Abilities")
col2.write("Base experience")
col3.write("Weight")
col4.write("Height")

ability_items = {}

for i in pokemon_ability: 
    ability_items[i['ability']['name']] = i['ability']['url']

with col0: 
    st.image(pokemon_sprite['front_default'])
with col1: 
    st.write(ability_items)
with col2: 
    st.write(base_exp)
with col3: 
    st.write(weight)
with col4: 
    st.write(height)



ability_choice = st.selectbox("Select an ability", ability_items)

url2 = ability_items[ability_choice]

ability_doc = requests.get(url2).json()


ability_effect = ability_doc['effect_entries']

st.write(ability_effect[:])


data = base_exp, height, weight

st.bar_chart(data, x_label = ['Base experience', 'Height', 'Weight'])
