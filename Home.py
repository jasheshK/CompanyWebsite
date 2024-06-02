import streamlit as st
import pandas 

st.set_page_config(layout="wide")
st.header("The Best Company")   
content = '''The Best Company is a pioneering leader in the tech industry, dedicated to driving innovation and excellence through cutting-edge technology and transformative solutions. Our team consists of top talent in diverse roles, including Marketing Data Scientists who leverage data to optimize marketing strategies, Machine Learning Engineers who develop intelligent algorithms, Full Stack and Front End Developers who create seamless user experiences, Technical Consultants who provide expert guidance on complex technical issues, and Project Managers who ensure timely and successful project delivery. Together, we empower businesses to achieve their goals and maintain a competitive edge in an ever-evolving market.'''
st.info(content)

st.header("Our Team")

col1, col2, col3 = st.columns([1.5, 1.5, 1.5])

df = pandas.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])
with col2:
    for index, row in df[4:8].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])
with col3:
    for index, row in df[8:].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

