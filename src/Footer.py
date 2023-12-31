# footer.py

import streamlit as st
from streamlit_lottie import st_lottie
from src.Helper import Helper


class Footer:
    @staticmethod
    def show_footer():
        st.markdown(
            """
            <style>
                .footer {
                    padding: 20px;
                    background-color: #333;
                    color: #fff;
                    text-align: center;
                }

                .footer img {
                    width: 50px;  /* Adjust the width as needed */
                }

                .footer a {
                    color: #fff;
                    margin: 0 10px;
                    text-decoration: none;
                }

                .footer hr {
                    border-color: #555;  /* Set the border color for horizontal lines */
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<hr>", unsafe_allow_html=True)
        image_col, hyperlinks_col = st.columns([1, 5])
        with image_col:
            st.image("resources/logo.png", width=150, use_column_width=False)

        with hyperlinks_col:
            col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
            with col1:
                # AI Platform Section
                st.markdown("<p style='margin-bottom: 5px;'><b>AI Platform</b></p>", unsafe_allow_html=True)
                st.markdown('<a href="/ai-platform/overview" style="margin-bottom: 5px; display: block;">Overview</a>',
                            unsafe_allow_html=True)
                st.markdown('<a href="/ai-platform/features" style="margin-bottom: 5px; display: block;">Features</a>',
                            unsafe_allow_html=True)
                st.markdown('<a href="/ai-platform/co-pilot" style="margin-bottom: 5px; display: block;">Co-Pilot</a>',
                            unsafe_allow_html=True)
                st.markdown(
                    '<a href="/ai-platform/integrations" style="margin-bottom: 5px; display: block;">Integrations</a>',
                    unsafe_allow_html=True)
                st.markdown(
                    '<a href="/ai-platform/documentation" style="margin-bottom: 5px; display: block;">Documentation</a>',
                    unsafe_allow_html=True)
                st.markdown('<a href="/ai-platform/security" style="margin-bottom: 5px; display: block;">Security</a>',
                            unsafe_allow_html=True)


            with col2:
                # Use Cases Section
                st.markdown("<p style='margin-bottom: 5px;'><b>Use Cases</b></p>", unsafe_allow_html=True)
                st.markdown(
                    '<a href="/use-cases/generative-ai" style="margin-bottom: 5px; display: block;">Generative AI</a>',
                    unsafe_allow_html=True)
                st.markdown(
                    '<a href="/use-cases/market-intelligence" style="margin-bottom: 5px; display: block;">Market Intelligence</a>',
                    unsafe_allow_html=True)
                st.markdown(
                    '<a href="/use-cases/analytics-bi" style="margin-bottom: 5px; display: block;">Analytics & BI</a>',
                    unsafe_allow_html=True)
                st.markdown(
                    '<a href="/use-cases/automation" style="margin-bottom: 5px; display: block;">Automation</a>',
                    unsafe_allow_html=True)
                st.markdown(
                    '<a href="/use-cases/all-use-cases" style="margin-bottom: 5px; display: block;">All Use Cases</a>',
                    unsafe_allow_html=True)

            with col3:
                # Professional Services Section
                st.markdown("<p style='margin-bottom: 5px;'><b>Professional Services</b></p>", unsafe_allow_html=True)
                st.markdown(
                    '<a href="/professional-services/overview" style="margin-bottom: 5px; display: block;">Services Overview</a>',
                    unsafe_allow_html=True)
                st.markdown(
                    '<a href="/professional-services/ai-copilots" style="margin-bottom: 5px; display: block;">AI-Copilots</a>',
                    unsafe_allow_html=True)
                st.markdown(
                    '<a href="/professional-services/data-ai-strategy" style="margin-bottom: 5px; display: block;">Data & AI Strategy</a>',
                    unsafe_allow_html=True)
                st.markdown(
                    '<a href="/professional-services/low-code-development" style="margin-bottom: 5px; display: block;">Low Code App Development</a>',
                    unsafe_allow_html=True)

            with col4:
                # Expertise Section
                st.markdown("<p style='margin-bottom: 5px;'><b>Expertise</b></p>", unsafe_allow_html=True)
                st.markdown(
                    '<a href="/expertise/microsoft-azure" style="margin-bottom: 5px; display: block;">Microsoft Azure</a>',
                    unsafe_allow_html=True)
                st.markdown(
                    '<a href="/expertise/aws" style="margin-bottom: 5px; display: block;">Amazon Web Services</a>',
                    unsafe_allow_html=True)
                st.markdown(
                    '<a href="/expertise/google-cloud" style="margin-bottom: 5px; display: block;">Google Cloud Project</a>',
                    unsafe_allow_html=True)
                st.markdown(
                    '<a href="/expertise/power-bi" style="margin-bottom: 5px; display: block;">Microsoft Power BI</a>',
                    unsafe_allow_html=True)
                st.markdown('<a href="/expertise/streamlit" style="margin-bottom: 5px; display: block;">Streamlit</a>',
                            unsafe_allow_html=True)
                st.markdown(
                    '<a href="/expertise/databricks" style="margin-bottom: 5px; display: block;">Databricks</a>',
                    unsafe_allow_html=True)
                st.markdown('<a href="/expertise/snowflake" style="margin-bottom: 5px; display: block;">Snowflake</a>',
                            unsafe_allow_html=True)
                st.markdown(
                    '<a href="/expertise/all-expertise" style="margin-bottom: 5px; display: block;">See all</a>',
                    unsafe_allow_html=True)

            with col1:
                # Industries Section
                st.markdown("<p style='margin-bottom: 5px;'><b>Industries</b></p>", unsafe_allow_html=True)
                st.markdown(
                    '<a href="/industries/retail-fmcg" style="margin-bottom: 5px; display: block;">Retail & FMCG</a>',
                    unsafe_allow_html=True)
                st.markdown(
                    '<a href="/industries/banking-finance" style="margin-bottom: 5px; display: block;">Banking & Finance</a>',
                    unsafe_allow_html=True)
                st.markdown(
                    '<a href="/industries/healthcare" style="margin-bottom: 5px; display: block;">Healthcare</a>',
                    unsafe_allow_html=True)
                st.markdown(
                    '<a href="/industries/other-industries" style="margin-bottom: 5px; display: block;">Other Industries</a>',
                    unsafe_allow_html=True)

            with col2:
                # Training & Events Section
                st.markdown("<p style='margin-bottom: 5px;'><b>Training & Events</b></p>", unsafe_allow_html=True)
                st.markdown(
                    '<a href="/training-events/private-training" style="margin-bottom: 5px; display: block;">Private Training</a>',
                    unsafe_allow_html=True)
                st.markdown(
                    '<a href="/training-events/user-groups" style="margin-bottom: 5px; display: block;">User Groups</a>',
                    unsafe_allow_html=True)
                st.markdown('<a href="/training-events/events" style="margin-bottom: 5px; display: block;">Events</a>',
                            unsafe_allow_html=True)

            with col3:
                # Resources Section
                st.markdown("<p style='margin-bottom: 5px;'><b>Resources</b></p>", unsafe_allow_html=True)
                st.markdown(
                    '<a href="/resources/case-studies" style="margin-bottom: 5px; display: block;">Case Studies</a>',
                    unsafe_allow_html=True)
                st.markdown('<a href="/resources/updates" style="margin-bottom: 5px; display: block;">Updates</a>',
                            unsafe_allow_html=True)
                st.markdown(
                    '<a href="/resources/news-blogs" style="margin-bottom: 5px; display: block;">News & Blogs</a>',
                    unsafe_allow_html=True)

            with col4:
                # Company Section
                st.markdown("<p style='margin-bottom: 5px;'><b>Company</b></p>", unsafe_allow_html=True)
                st.markdown(
                    '<a href="/company/meet-the-team" style="margin-bottom: 5px; display: block;">Meet the Team</a>',
                    unsafe_allow_html=True)
                st.markdown('<a href="/company/careers" style="margin-bottom: 5px; display: block;">Careers</a>',
                            unsafe_allow_html=True)
                st.markdown('<a href="/company/contact-us" style="margin-bottom: 5px; display: block;">Contact Us</a>',
                            unsafe_allow_html=True)
                st.markdown('<a href="/company/support" style="margin-bottom: 5px; display: block;">Support</a>',
                            unsafe_allow_html=True)

        st.markdown(
            """
            <div style="display: flex; justify-content: center;">
                <a href="https://twitter.com/yourcompany" target="_blank"><img src="https://cdn4.iconfinder.com/data/icons/social-media-black-white-2/1227/X-1024.png" alt="Twitter" width="30"></a>
                <span style="margin: 0 10px;">|</span>
                <a href="https://linkedin.com/company/yourcompany" target="_blank"><img src="https://cdn3.iconfinder.com/data/icons/free-social-media-22/32/linkedin_social_media_logo-1024.png" alt="LinkedIn" width="30"></a>
                <span style="margin: 0 10px;">|</span>
                <a href="https://instagram.com/yourcompany" target="_blank"><img src="https://cdn2.iconfinder.com/data/icons/social-icons-33/128/Instagram-1024.png" alt="Instagram" width="30"></a>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<hr>", unsafe_allow_html=True)


        # Center-align the copyright information directly in the markdown
        st.markdown("<p style='text-align: center;'>&copy; 2024 Data Processor AI . All rights reserved.</p>",
                    unsafe_allow_html=True)

        # Provide links and content for "Terms of Use" and "Privacy Policy"
        st.markdown(
            "<p style='text-align: center;'><a href='/terms-of-use'>Terms of Use</a> | <a "
            "href='/privacy-policy'>Privacy Policy</a></p>",
            unsafe_allow_html=True)
