import streamlit as st
from camera_input_live import camera_input_live

from processing import process
from decoding import decode
from file import add,read

"""
# 2374 Pit Scouting Analyzer
___
"""

if 'scanning' not in st.session_state:
    st.session_state.scanning = False

def toggle_camera_on():
    st.session_state.scanning = not st.session_state.scanning

st.button("Scan", on_click=toggle_camera_on,use_container_width=True)

if st.session_state.scanning:
    img_file_buffer = camera_input_live(debounce=2500)

    if img_file_buffer:
        st.image(img_file_buffer)
        process(img_file_buffer)
        decoded_tuple = decode()
        if len(decoded_tuple) > 0:
            decoded_str = decoded_tuple[0]
            st.write(decoded_str)
            add(decoded_str, 'backup.csv')
            st.session_state.scanning = False

data = read('backup.csv')

team_query = st.text_input("Search By Team Number")
if team_query and team_query.isdigit():
    st.data_editor(data.loc[data['Team Number'] == int(team_query)].drop(columns=['Team Number']),
             use_container_width=True,hide_index=True)

new_data = st.dataframe(data.astype('category'),
                          use_container_width=True,hide_index=True)

man_entry = st.text_input("Manual Entry")
st.button("Add",on_click=add,args=(man_entry,'backup.csv'),use_container_width=True)