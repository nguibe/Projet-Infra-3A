import streamlit as st
import os

st.set_page_config(layout="wide", page_title ='FRIDGE & COOK', initial_sidebar_state='collapsed')
def display_html_in_streamlit(html_file_path):
    """Displays HTML content from a file in a Streamlit app.

    Args:
        html_file_path (str): The path to the HTML file.
    """
    try:
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=2000, width=1080, scrolling=True)
    except FileNotFoundError:
        st.error(f"Error: HTML file not found at {html_file_path}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Example usage (adjust the path as needed):
html_file_path = "Welcome_Page.html"
# # html_file_path = os.path.join(os.path.dirname(__file__), "Welcome page.html")

display_html_in_streamlit(html_file_path)

# # Check if the file exists before attempting to display it
# if os.path.exists(html_file_path):
#     display_html_in_streamlit(html_file_path)
# else:
#     st.error(f"The HTML file '{html_file_path}' does not exist. Please check the path.")