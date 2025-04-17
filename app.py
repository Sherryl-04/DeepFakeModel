import streamlit as st
import dashboard
import classifyPage

st.set_page_config(
    page_title="Detecting Image Manipulations",
    page_icon="🤖",
    layout="wide")

PAGES = {
    "Dashboard": dashboard,
    "Classify Image": classifyPage
}

st.sidebar.title("Detecting Image Manipulations")

st.sidebar.write("This is a tool that leverages the power of Deep Learning to distinguish Real images from the Manipulated images.")

st.sidebar.subheader('Navigation:')
selection = st.sidebar.radio("", list(PAGES.keys()))

page = PAGES[selection]

page.app()