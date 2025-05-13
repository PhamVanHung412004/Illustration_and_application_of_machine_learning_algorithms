import streamlit as st

col1, col2, col3 = st.columns([1, 2, 1])  # Tạo 3 cột với tỉ lệ chiều rộng 1:2:1

with col1:
    st.write("Cột 1")

with col2:
    st.write("Cột 2 - lớn nhất")

with col3:
    st.write("Cột 3")
