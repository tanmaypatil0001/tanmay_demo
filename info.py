import streamlit as st

name=st.text_input("Enter your name: ")
fathername=st.text_input("Enter your father name: ")
addr=st.text_input("Eneter Your text")
classdata=st.selectbox("Enter your Division: ",(1,2,3,4,5))
roll=st.text_input("Enter your roll number:")

button =st.button("Submit")
if button :
    st.markdown(f"""
                Name :{name}
                Father Name:{fathername}
                Address : {addr}
                Class :{classdata}
                Roll no :{roll}""")
    

