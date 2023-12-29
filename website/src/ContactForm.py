# ContactForm.py
import streamlit as st
import requests as req
from datetime import datetime

class ContactForm:
    def __init__(self):
        self.form_key = 'contact-form'

    def create_contact_form(self):
        with st.form(key=self.form_key, clear_on_submit=True):
            st.header("Get In Touch!")
            st.write("##")

            left_column, right_column = st.columns(2)
            with left_column:
                self.name = st.text_input("Your Name", key="name")
                self.email = st.text_input("Your Email", key="email")
                self.message = st.text_area("Your Message", key="message")

            with right_column:
                st.empty()

            # Return True if the form is submitted
            return st.form_submit_button('Send')

    def handle_form_submission(self):
        print(f"Name: {self.name}, Email: {self.email}, Message: {self.message}")
        response = req.post("https://formsubmit.co/info@thedataprocessor.ai", data={"name": self.name, "email": self.email, "message": self.message})
        print("response_status_code ", response.status_code)
        return response
