# app.py
import streamlit as st
from src.PageConfig import PageConfig
from src.SectionsCreator import SectionsCreator
from src.ContactForm import ContactForm
import hydralit as hy
from src.JobApplicationForm import JobApplicationForm
import requests as req


def show_home_page():
    print("Creating Sections...")
    sections_creator = SectionsCreator()
    sections_creator.create_sections()


def show_contact_us_page():
    # Customize this function to display content for the Contact Us page
    col1, col2 = st.columns(2)
    with col1:
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

    with col2:
        # Google Map Location
        hy.markdown(
            """
            ## Google Map Location
            <iframe
                width="600"
                height="350"
                style="border:0"
                loading="lazy"
                allowfullscreen
                src="https://www.google.com/maps/place/SOBHA+Dream+Gardens+(Residential+Apartments+in+Thanisandra)/@13.0986671,77.6412999,15z/data=!4m6!3m5!1s0x3bae19261265aa95:0xcc6de8ac0fc6561f!8m2!3d13.0986671!4d77.6412999!16s%2Fg%2F11f7760crx?entry=ttu"
            ></iframe>
            """,
            unsafe_allow_html=True,
        )

        # Office Address with Styling
        hy.markdown(
            """
            ## Office Address
            <div style="font-weight: bold;">
                The Data Processor AI
            </div>
            <div style="font-style: italic; margin-top: 5px;">
                B-8032 SDG, North Bengaluru <br>
                Karnataka, India 560013
            </div>
            <div style="margin-top: 5px;">
                Email: info@thedataprocessor.ai<br>
                Phone: +91-8284-089-680
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Use JavaScript to scroll to the top
    st.markdown(
        """
        <script>
            window.scrollTo(0, 0);
        </script>
        """,
        unsafe_allow_html=True,
    )


def show_about_us_page():
    # Customize this function to display content for the About Us page
    # Vision and Mission of the Company
    st.title("About Us - The Data Processor AI")

    st.write(
        "At The Data Processor AI, we are on a mission to transform the way businesses leverage data for "
        "decision-making. Our vision is to be a pioneering force in the field of data analytics, providing "
        "state-of-the-art solutions that empower organizations to thrive in the digital age.")

    # Team and Expertise
    st.header("Our Expert Team")
    st.write(
        "Founded by a team of highly skilled engineers with over a decade of experience in working with Big Data "
        "Platforms, we bring a wealth of expertise to the table. Our team is passionate about pushing the boundaries "
        "of what is possible with data analytics and machine learning.")

    # Values
    st.header("Our Values")
    st.write("We are guided by a set of core values that define who we are and how we operate:")
    st.write("- **Innovation:** We embrace creativity and continually seek innovative solutions.")
    st.write("- **Precision:** Our commitment to precision ensures that our solutions are accurate and impactful.")
    st.write("- **Integrity:** We uphold the highest standards of integrity in all our interactions.")
    st.write(
        "- **Collaboration:** Collaboration is at the heart of our approach, both within our team and with our clients.")

    # Achievements
    st.header("Our Achievements")
    st.write(
        "Over the years, we have achieved significant milestones, including successful implementations of AI "
        "solutions for leading businesses across various industries. Our commitment to excellence has been recognized "
        "through awards and accolades.")

    # Display team or additional information about the company
    # ...


def show_careers_page():
    st.title("Careers at The Data Processor AI")

    st.write(
        "We are always looking for talented individuals to join our team. "
        "If you're passionate about our company, apply today!"
    )

    ###
    print("Creating Job Application Form...")
    job_application = JobApplicationForm()

    # Use the 'with' statement to encapsulate the form creation and submission logic
    if job_application.create_job_application_form():
        # Retrieve form input values
        job_application.handle_job_form_submission()






def main():
    print("Initializing PageConfig...")
    page_config = PageConfig("Data Processor AI", "resources/box.png")
    page_config.configure_page()

    app = hy.HydraApp(title='The Data Processor AI')
    if app is None:
        print("Error: 'app' is None. Check HydraApp initialization.")

    @app.addapp("Home ")
    def home():
        show_home_page()

    @app.addapp("About Us")
    def about_us():
        show_about_us_page()

    @app.addapp("Contact")
    def contact_us():
        show_contact_us_page()

    @app.addapp("Careers ")
    def career():
        show_careers_page()

    app.run()


if __name__ == "__main__":
    print("Starting the main function...")
    main()
