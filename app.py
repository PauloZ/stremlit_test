import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

#st.write("Hello world")


pdf_data1 = open("1.pdf", "rb").read()
pdf_data2 = open("2.pdf", "rb").read()
test_dic={}
test_dic["1"]=pdf_data1
test_dic["2"]=pdf_data2


x = st.slider('x', min_value=1, max_value=2)  # 👈 this is a widget
#st.write(x, 'squared is', x * x)
st.image(str(x)+".png", caption="loaded image"+str(x))
#displayPDF(str(x)+".pdf")
# pdf_viewer(str(x)+".pdf")
# pdf_viewer(test_dic[str(x)])
