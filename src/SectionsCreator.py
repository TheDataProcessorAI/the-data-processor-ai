# sections_creator.py
import streamlit as st
from streamlit_lottie import st_lottie
from src.AssetsLoader import AssetsLoader


def create_company_header():
    # -- HEADER -- #
    # insert logo stored in resources folder here
    st.subheader("Unlocking Business Potential with AI-Powered Insights.")


def create_generative_ai_section():
    # -- GENERATIVE AI CAPABILITIES -- #
    col1, col2 = st.columns(2)
    with col1:
        st.header("Generative AI Capabilities")
        st.write(
            "Explore our cutting-edge Generative AI capabilities that enable businesses to harness the power of artificial intelligence for creative and innovative solutions.")
        st.write("""
            - **Creative Content Generation:** Leverage our Generative AI models to create high-quality and engaging content, from images to text.
            - **Innovative Design Solutions:** Drive innovation in design with AI-generated concepts and prototypes.
            - **Personalized Recommendations:** Provide personalized recommendations to users based on their preferences and behavior.
            - **Automated Creative Processes:** Streamline creative workflows by automating repetitive tasks using Generative AI.
            - **Customized AI Models:** Develop custom Generative AI models tailored to your specific business needs.
        """)
    with col2:
        assets_loader = AssetsLoader()
        lottie_animations = assets_loader.load_assets()
        st_lottie(lottie_animations[4], speed=1, height=400)




class SectionsCreator:
    def __init__(self):
        pass

    def create_sections(self):
        assets_loader = AssetsLoader()
        lottie_animations = assets_loader.load_assets()
        create_company_header()

        create_generative_ai_section()
        self.create_what_we_do_section()
        self.create_our_services_section(lottie_animations)

    def create_what_we_do_section(self):
        st.header("What We Do")
        st.write("""
            Welcome to The Data Processor.ai, where we redefine the landscape of data-driven decision-making.
            - Enterprise AI solutions meticulously crafted to empower businesses with precision-driven insights.
            - Analytics expertise to navigate your business strategies with unparalleled precision and confidence.
            - Every decision you make is backed by the most relevant and advanced data analytics.
        """)

    def create_our_services_section(self, lottie_animations):
        # -- OUR SERVICES -- #
        st.header("Our Services")
        services_columns = st.columns(3)
        with services_columns[0]:
            st_lottie(lottie_animations[0], speed=1, height=200, key="cola")
            st.subheader("Trade Promo Optimization")
            st.write("""
                To optimize trade promotions, businesses can leverage data-driven processes to effectively manage promotional budgets, assess the impact of promotional efforts, and plan promotional activities. By analyzing historical data, market trends, and other relevant factors, trade promo optimization enables global enterprises to make informed decisions about promotional strategies, maximize return on investment, and drive sales growth.
            """)
        with services_columns[1]:
            st_lottie(lottie_animations[1], speed=1, height=200, key="cereal")
            st.subheader("Demand Forecasting")
            st.write("""
                Demand forecasting is a process that involves estimating the future demand for a product or service. It helps businesses make informed decisions about production, inventory management, and resource allocation. By analyzing historical data, market trends, and other relevant factors, demand forecasting enables businesses to anticipate customer demand and plan their operations accordingly.
            """)
        with services_columns[2]:
            st_lottie(lottie_animations[2], speed=1, height=200, key="retail")
            st.subheader("Retail Analytics")
            st.write("""
                Retail analytics is the process of providing analytical data on inventory levels, supply chain movement, consumer demand, sales, etc. that are crucial for making marketing, and procurement decisions. The analytics on supply chain movement and consumer demand help retailers make smarter decisions on how to optimize the supply chain and stocking of inventory, and the analytics on consumer demand can be used for optimizing pricing or markdown decisions, store layout, and product promotions.
            """)
