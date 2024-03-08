import streamlit as st

from processing import process
from decoding import decode
from save import add

"""
# 2374 Pit Scouting Analyzer
___
"""

if 'camera_on' not in st.session_state:
    st.session_state.camera_on = False

def toggle_camera_on():
    st.session_state.camera_on = not st.session_state.camera_on

st.button("Toggle Camera", on_click=toggle_camera_on,use_container_width=True)

if st.session_state.camera_on:
    img_file_buffer = st.camera_input("Image of QR Code:")

    if img_file_buffer:
        st.image(img_file_buffer)
        process(img_file_buffer)
        decoded_str = decode()[0]
        st.write(decoded_str)
        add(decoded_str, 'backup.csv')
        
    