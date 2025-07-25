import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

tab1, tab2 = st.tabs(["pdf1", "pdf2"])

pdf_data1 = open("1.pdf", "rb").read()
pdf_data2 = open("2.pdf", "rb").read()
# test_dic={}

with tab1:
    st.header("image1")
    pdf_viewer(pdf_data1)

    # st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("image2")
    pdf_viewer(pdf_data2)
    # st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
