import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

tab1, tab2 = st.tabs(["image1", "image2"])

pdf_data1 = open("1.png", "rb").read()
pdf_data2 = open("2.png", "rb").read()
# test_dic={}

with tab1:
    st.header("image1")
    # pdf_viewer(pdf_data1)

    st.image(pdf_data1)
with tab2:
    st.header("image2")
    # pdf_viewer(pdf_data2)
    st.image(pdf_data2)
