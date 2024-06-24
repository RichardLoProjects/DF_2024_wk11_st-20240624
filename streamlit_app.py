import streamlit as st
import pandas as pd
import requests


title_col, image_col = st.columns(2)
with title_col:
    st.title(':rainbow[Pokedex]')
with image_col:
    pokemon_pic = st.empty()
poke_number = st.slider('label', 1,155, label_visibility='collapsed')
url = f'https://pokeapi.co/api/v2/pokemon/{poke_number}/'
data = requests.get(url).json()
pokemon = {
    'name': data['name']
    , 'height': data['height']
    , 'weight': data['weight']
    #, 'number_of_moves': len(data['moves'])
    , 'type': data['types'][0]['type']['name']
    , 'hp': data['stats'][0]['base_stat']
    , 'attack': data['stats'][1]['base_stat']
    , 'defense': data['stats'][2]['base_stat']
    , 'speed': data['stats'][5]['base_stat']
}

df = pd.DataFrame.from_dict([pokemon], orient='columns').set_index('name')
st.table(df)

pokemon_pic.image(data['sprites']['front_default'])
st.audio(requests.get(data['cries']['latest']).content)













_ = '''
my_title = st.empty()

st.title('user inputs')

user_choice = st.radio('Labif', options=[":rainbow[Comedy]", 'dog'])
st.write(f'you chose {user_choice}')

my_title.title(f'you picked {user_choice}')

sweets = st.slider(
    'gkflk'
    , 5
    , 20
    , step=5
)


col1, col2, col3 = st.columns(3)
col1.write('sgljhfg')
col2.write('sgljfwrhfg')
col3.write('sgljrtehfg')

with col2:
    st.write('rjwehf')
'''




_ = '''
st.title("Cookie Clicker")

if 'counter' not in st.session_state.keys():
    st.session_state['counter'] = 19342395725709045


if st.button("Click me for a cookie"):
    st.snow()
    st.session_state['counter'] += 1

st.write(f'You have {st.session_state["counter"]} cookies!')
'''


