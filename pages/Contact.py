import streamlit as st

st.header("Contact Me")

from send_email import sendemail

with st.form(key = "my_forms"):
    user_email = st.text_input("Please enter your Email")
    topic = st.selectbox("What topic do you want to discuss?", [" ", "Job Inquires", "Project Proposals", "Others"], key="option1")
    message = st.text_area("Your message here")

    

    message = message + '\n' + user_email +'\n' + topic
    button = st.form_submit_button("Submit")
    if button:
        sendemail(message)
        st.info("Your emial was send successfully")