import streamlit as st
import requests as req
from streamlit_lottie import st_lottie

st.set_page_config(page_title="The Data Processor AI",
                   page_icon="🚀", layout="wide"
                   )


def load_lottieurl(url):
    r = req.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local css


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("./style/style.css")


# --- ASSETS -- #
lottie_coding = load_lottieurl(
    "https://lottie.host/8feb2df2-0659-4603-8ae2-b42b40b832d4/nYJ7blGvxu.json")
lottie_cola = load_lottieurl(
    "https://lottie.host/726cc09d-84ee-4650-9eba-5b8d50bfa271/azHdrg5nqM.json")
lottie_cereal = load_lottieurl(
    "https://lottie.host/29515f58-9b07-4c15-be29-a670cb4d86dd/fzsh1V2crs.json")
lottie_retail = load_lottieurl(
    "https://lottie.host/6f68c090-12b0-45b3-89ed-1a6fa2979241/9le9ajiq8W.json")

# -- HEADER -- #
with st.container():
    st.subheader("Unlocking Business Potential with AI-Powered Insights. 🤖")
    st.title("Business Success Experts from the Future. 🚀")
    st.write("ransform your business landscape with The Data Processor.ai's enterprise AI solutions. Experience the precision of informed decision-making.")
    st.write("[Learn More >](https://thedataprocessor.ai/)")


# -- WHAT WE DO-- #
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What We Do")
        st.write("##")
        st.write(
            """
            Welcome to The Data Processor.ai, where we redefine the landscape of data-driven decision-making. 
              - Enterprise AI solutions is meticulously crafted to empower businesses with precision-driven insights. 
              - Analytics expertise to navigate your business strategies with unparalleled precision and confidence. 
              - Every decision you make is backed by the most relevant and advanced data analytics.
             
            """
        )

        st.write("[Learn More >](https://thedataprocessor.ai/)")
    with right_column:
        st_lottie(lottie_coding, speed=1, height=400, key="coding")

# -- OUR SERVICES --#
with st.container():
    st.write("---")
    st.header("Our Services")
    st.write("##")
    image_column_1, image_column_2, image_column_3 = st.columns(3)
    with image_column_1:
        st_lottie(lottie_cola, speed=1, height=200, key="cola")
    with image_column_2:
        st_lottie(lottie_cereal, speed=1, height=200, key="cereal")
    with image_column_3:
        st_lottie(lottie_retail, speed=1, height=200, key="retail")
    text_column_1, text_column_2, text_column_3 = st.columns(3)
    with text_column_1:
        st.write("---")
        st.header("Trade Promo Optimization")
        st.write("##")
        st.write("To optimize trade promotions, businesses can leverage data-driven processes to effectively manage promotional budgets, assess the impact of promotional efforts, and plan promotional activities. By analyzing historical data, market trends, and other relevant factors, trade promo optimization enables global enterprises to make informed decisions about promotional strategies, maximize return on investment, and drive sales growth.")
    with text_column_2:
        # --- DEMAND FORECASTING --- #
        with st.container():
            st.write("---")
            st.header("Demand Forecasting")
            st.write("##")
            st.write("Demand forecasting is a process that involves estimating the future demand for a product or service. It helps businesses make informed decisions about production, inventory management, and resource allocation. By analyzing historical data, market trends, and other relevant factors, demand forecasting enables businesses to anticipate customer demand and plan their operations accordingly.")
    with text_column_3:
        # --- RETAIL ANALYTICS --- #
        with st.container():
            st.write("---")
            st.header("Retail Analytics")
            st.write("##")
            st.write("Retail analytics is the process of providing analytical data on inventory levels, supply chain movement, consumer demand, sales, etc. that are crucial for making marketing, and procurement decisions. The analytics on supply chain movement and consumer demand help retailers make smarter decisions on how to optimize the supply chain and stocking of inventory, and the analytics on consumer demand can be used for optimizing pricing or markdown decisions, store layout, and product promotions.")

# -- CONTACT -- #
with st.container():
    st.write("---")
    st.header("Get In Touch!")
    st.write("##")
    st.write("We are always here to help you. Reach out to us anytime and we'll happily answer your questions.")

    contact_form = """
        <form action="https://formsubmit.co/info@thedataprocessor.ai" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
