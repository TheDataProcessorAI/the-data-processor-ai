# app.py
import streamlit as st
from src.PageConfig import PageConfig
from src.SectionsCreator import SectionsCreator
from src.ContactForm import ContactForm


def main():
    print("Initializing PageConfig...")
    page_config = PageConfig("Data Processor AI", "resources/box.png")
    page_config.configure_page()

    print("Creating Sections...")
    sections_creator = SectionsCreator()
    sections_creator.create_sections()

    print("Creating Contact Form...")
    contact_form = ContactForm()

    # Use the 'with' statement to encapsulate the form creation and submission logic
    if contact_form.create_contact_form():
        # Retrieve form input values
        response = contact_form.handle_form_submission()

        # Display success or error message based on the response
        if response.status_code == 200:
            st.success("Form submitted successfully!")
        else:
            st.error("Error submitting the form. Please try again.")


if __name__ == "__main__":
    print("Starting the main function...")
    main()
