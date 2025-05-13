import streamlit as st
class Read_Image:
    def __init__(self,image:str):
        self.image:str = image

    def Read(self):
        st.image(self.image)





        