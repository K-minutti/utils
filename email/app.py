import os
import pandas as pd
import streamlit as st

import email_auto

# Title of the application
st.title('Automated Email')

data_dir = "data"
# List all the .csv files in the /data directory
csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]

# Create a select box for the CSV files
selected_csv_file = st.selectbox("Choose a CSV file from /data", csv_files)

# Read the selected CSV file into a dataframe
dataframe = pd.read_csv(f"{data_dir}/" + selected_csv_file)

# Select or upload csv to process
uploaded_file = st.file_uploader("Choose a CSV file", type='csv')
if uploaded_file is not None:
    selected_csv_file = uploaded_file

if selected_csv_file is not None:
    # Convert the uploaded file to a Pandas dataframe
    dataframe = pd.read_csv(f"{data_dir}/" + selected_csv_file)
    # Show the first few rows of the dataframe
    st.write(dataframe.head())





# Create a text input box
subject = st.text_input("Email Subject:")
user_input = st.text_area("Email Body:", '')

# Display the user's input back to them
st.write(f'You entered: {user_input}')

dry_run = True  # Change to False to actually send emails
email_auto.main(dry_run=dry_run)