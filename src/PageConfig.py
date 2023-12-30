# PageConfig.py
import streamlit as st
from PIL import Image


class PageConfig:
    def __init__(self, page_title, page_icon_path, layout='wide'):
        self.page_title = page_title
        self.page_icon_path = page_icon_path
        self.layout = layout

    def configure_page(self):
        im = Image.open(self.page_icon_path)
        st.set_page_config(page_title=self.page_title, page_icon=im,
                           layout=self.layout, initial_sidebar_state='auto')
