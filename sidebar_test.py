import streamlit as st


pdf_data1 = open("1.png", "rb").read()
pdf_data2 = open("2.png", "rb").read()

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Select an image:",
    ("image 1", "image 2")
)

# Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )

if add_selectbox == "image 1":
    st.image(pdf_data1)
else:

    # pdf_viewer(pdf_data2)
    st.image(pdf_data2)
