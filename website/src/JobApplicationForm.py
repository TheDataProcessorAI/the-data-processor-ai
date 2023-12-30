# Job Application Form.py
import streamlit as st
import requests as req
from datetime import datetime


class JobApplicationForm:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.resume = None

    def create_job_application_form(self):
        try:
            # Job Application Form
            st.header("Job Application Form")

            self.name = st.text_input("Full Name", key="name")
            self.email = st.text_input("Email", key="email")

            st.write("Upload Resume:")
            self.resume = st.file_uploader("Choose a file", type=["pdf", "docx"])

            # Return True if the form creation is successful
            return True
        except Exception as e:
            # Handle any exceptions and return False
            st.error(f"Error creating job application form: {e}")
            return False

    def handle_job_form_submission(self):
        if st.button("Submit Application"):
            if self.validate_application():
                st.success("Application submitted successfully!")
                url = "https://formsubmit.co/info@thedataprocessor.ai"
                data = {
                    'name': self.name,
                    'email': self.email,
                }
                files = {'resume': (self.resume.name, self.resume, self.resume.type)}

                req.post(url, data=data, files=files)
            else:
                st.error("Please fill out all fields and upload a valid resume.")

    def validate_application(self):
        # Simple validation, you can add more checks if needed
        return self.name and self.email and self.resume
