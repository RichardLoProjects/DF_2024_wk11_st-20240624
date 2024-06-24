import streamlit as st
import requests
import pandas as pd
import random




def get_jason(num):
    _url = f'https://pokeapi.co/api/v2/pokemon/{num}/'
    return requests.get(_url).json()

min_poke_num = 1
max_poke_num = 155
df = pd.DataFrame()
title_col, image_col = st.columns([4,1])
with title_col:
    st.title(':rainbow[Pokedex]')
with image_col:
    pokemon_pic = st.empty()
poke_number = st.slider(
    'label'
    , min_poke_num
    , max_poke_num
    , label_visibility='collapsed'
)
used_pokemon = {poke_number}

def extend_df(_num):
    _d = get_jason(_num)
    _p = {
        'Name': _d['name'].title()
        , 'Type': _d['types'][0]['type']['name'].title()
        , 'Height': _d['height']
        , 'Weight': _d['weight']
        , 'Health': _d['stats'][0]['base_stat']
        , 'Attack': _d['stats'][1]['base_stat']
        , 'Defense': _d['stats'][2]['base_stat']
        , 'Speed': _d['stats'][5]['base_stat']
    }
    return pd.DataFrame.from_dict([_p], orient='columns').set_index('Name')
data = get_jason(poke_number)
df = pd.concat([df, extend_df(poke_number)])
while len(used_pokemon) < 5:
    random_number = random.randint(min_poke_num, max_poke_num)
    if random_number not in used_pokemon:
        used_pokemon.add(random_number)
        df = pd.concat([df, extend_df(random_number)])


df_show = df.copy()
sort_col = st.radio('Sort by', options=list(df_show.columns))
df_show.sort_values(sort_col, ascending=True, inplace=True)

pokemon_pic.image(data['sprites']['front_default'])
st.table(df_show.head(5))
st.audio(requests.get(data['cries']['legacy']).content)


height_col, weight_col = st.columns(2)
with height_col:
    st.bar_chart(df.reset_index(), x='Name',y='Height',x_label='',color=(2,255,255,0.5))
with weight_col:
    st.bar_chart(df.reset_index(), x='Name',y='Weight',x_label='')


df_fight = df.copy().reset_index().iloc[0:2,:]
def calc_win(_fightdf):
    h1 = df_fight.iloc[0]["Health"]
    a1 = df_fight.iloc[0]["Attack"]
    d1 = df_fight.iloc[0]["Defense"]
    h2 = df_fight.iloc[1]["Health"]
    a2 = df_fight.iloc[1]["Attack"]
    d2 = df_fight.iloc[1]["Defense"]
    if h1 * (a2-d1) > h2 * (a1-d2):
        return df_fight.iloc[0]["Name"], df_fight.iloc[1]["Name"]
    else:
        return df_fight.iloc[1]["Name"], df_fight.iloc[0]["Name"]
st.write(f'I think that {calc_win(df_fight)[0]} will win vs {calc_win(df_fight)[1]} based on the health, attack, and defense stats.')















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


