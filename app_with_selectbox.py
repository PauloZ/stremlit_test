import streamlit as st
# from streamlit_pdf_viewer import pdf_viewer

# tab1, tab2 = st.tabs(["image1", "image2"])

pdf_data1 = open("1.png", "rb").read()
pdf_data2 = open("2.png", "rb").read()


option = st.selectbox(
    "Select image",
    ("image 1", "image 2"),
)

# st.write("You selected:", option)
if option == "image 1":
    st.image(pdf_data1)
else:

    # pdf_viewer(pdf_data2)
    st.image(pdf_data2)
