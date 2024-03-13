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
    img_file_buffer = camera_input_live()

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
    st.write(data.loc[data['Team Number'] == int(team_query)].style.format(subset=['Team Number'],precision=0))

st.dataframe(data.style.format(subset=['Team Number'],precision=0),
    use_container_width=True,hide_index=True)
    