import streamlit as st
import streamlit.components.v1 as components

x = 6  # 👈 this is a widget
st.write(x, 'squared is', x * x)


components.iframe("https://share.streamlit.io/vinothkumarjothilatentview/streamlitsample/main.py",width=1000, height=1000, scrolling=False)