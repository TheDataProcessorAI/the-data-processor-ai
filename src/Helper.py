import streamlit as st


class Helper:
    def __init__(self):
        pass

    @staticmethod
    def display_images_side_by_side(image_paths, image_size=10):  # Adjust the image_size as needed
        st.markdown(
            f"""
                <style>
                    .center {{
                        display: flex;
                        justify-content: center;
                    }}
                    .custom-column {{
                        max-width: {image_size}px;
                        margin-right: {30}px;
                    }}
                </style>
                """,
            unsafe_allow_html=True
        )

        st.markdown("<div class='center'>", unsafe_allow_html=True)

        # Display images in separate columns
        columns = st.columns(len(image_paths))
        for column, image_path in zip(columns, image_paths):
            column.image(image_path, width=image_size, use_column_width=True)

        st.markdown("</div>", unsafe_allow_html=True)
