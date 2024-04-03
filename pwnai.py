import streamlit as st  # Import Streamlit library for creating interactive UI
import pandas as pd  # Import Pandas library for data manipulation
import time  # Import time library for simulating a task

st.set_page_config(layout="wide", page_title="PWNAI", page_icon=":robot_face:")  # Set page layout, title, and icon

@st.cache_data  # Cache the data loading function to improve performance
def load_data(csv_file):  # Define a function to load data from a CSV file
    data = pd.read_csv(csv_file)  # Read the CSV file and store the data in a DataFrame
    return data  # Return the DataFrame

# Load data from a remote CSV file
data = load_data('https://raw.githubusercontent.com/NoDataFound/PwnAI/main/assets/platforms/PWNAI_Services%20-%20Hosted.csv')

# Initialize or load session state for the scoreboard
if 'scoreboard' not in st.session_state:  # Check if the scoreboard is initialized in the session state
    st.session_state['scoreboard'] = {service: 0 for service in data['Service'].unique()}  # Initialize the scoreboard as a dictionary in the session state

# Load the sidebar image
sidebar_image_url = 'https://raw.githubusercontent.com/NoDataFound/PwnAI/main/assets/artwork/PWNAI_logo_main.png'
st.sidebar.image(sidebar_image_url, width=200, use_column_width='always')  # Display the sidebar image

# Allow the user to select services and enter a query
selected_services = st.sidebar.multiselect("Select services", options=data['Service'].unique())  # Let the user select services from a list
query = st.text_input("", placeholder="Enter your query here", label_visibility="hidden")  # Create a text input field for the query

# Display the welcome message and the hack button
col1, col2 = st.columns([3, 1])  # Create two columns for the welcome message and the hack button
with col1:
    st.code("""
            
            ░█▄█░▄▀▄░█░░▒█░░░▀█▀░▄▀▄░░░█▄█▒▄▀▄░▄▀▀░█▄▀
▒█▒█░▀▄▀░▀▄▀▄▀▒░░▒█▒░▀▄▀▒░▒█▒█░█▀█░▀▄▄░█▒█

- 𝚂𝚎𝚕𝚎𝚌𝚝 𝚂𝚎𝚛𝚟𝚒𝚌𝚎𝚜 𝚒𝚗 𝚜𝚒𝚍𝚎𝚋𝚊𝚛
- 𝙴𝚗𝚝𝚎𝚛 �������������������
