import os
import pandas as pd
import yagmail
import streamlit as st
import re

from typing import Optional
from datetime import date
from dataclasses import dataclass


def send_email(user: str, password: str, recipient: str, subject: str, content: str, dry_run: Optional[bool] = False) -> None:
    if dry_run:
        message = f"Dry Run:\nSubject: {subject}\nTo: {recipient}\n{content}\n"
        return message 
    else:
        yag = yagmail.SMTP(user, password)
        yag.send(
            to=recipient,
            subject=subject,
            contents=content
        )
        return recipient

def create_email_content(template: str, row: pd.Series) -> str:
    # Extract variables from the template
    variables = re.findall(r'\{(\w+)\}', template)
    # Prepare a dictionary with variables and their values
    values = {var: str(row[var]).strip() if var in row else "{" + var + "}" for var in variables}

    # Interpolate variables in the template - in order for **syntax to work columns names cannot contain spaces
    return template.format(**values)

def main(dataframe, subject, user_input, dry_run: Optional[bool] = False) -> None:
    user = os.getenv('GMAIL_USER')
    password = os.getenv('GMAIL_PASSWORD')
    # UNCOMMENT TO OVERWRITE - DON'T FORGET TO REMOVE!
    user = ''
    password = ''
    
    dry_run_messages = []
    sent_emails = []

    for _, row in dataframe.iterrows():
        content = create_email_content(user_input, row)
        result = send_email(user, password, row['email'], subject, content, dry_run=dry_run)
        if dry_run:
            dry_run_messages.append(result)
        else:
            sent_emails.append(result)

    return dry_run_messages, sent_emails



################
# Streamlit UI
################
# Title of the application
st.title('Automated Email')

current_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(current_dir, "data")
csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]

# Create a select box for the CSV files
selected_csv_file = st.selectbox("Choose a CSV file from /data", csv_files)

# Read the selected CSV file into a dataframe
dataframe = pd.read_csv(f"{data_dir}/" + selected_csv_file)

# Select or upload csv to process
uploaded_file = st.file_uploader("Choose a CSV file", type='csv')
if uploaded_file is not None:
    selected_csv_file = uploaded_file
    dataframe = pd.read_csv(uploaded_file)

# Check for invalid characters/ missing cols in column names
invalid_headers = [col for col in dataframe.columns if '{' in col or '}' in col or ' ' in col]
if invalid_headers:
    st.warning(f"The following headers contain invalid characters ({{, }} or spaces): {', '.join(invalid_headers)}. Please correct them and try again.")
elif dataframe.isnull().any().any() or dataframe.applymap(lambda x: x == '').any().any():
    st.warning("The CSV file contains NaN or empty values. Please correct them and try again.")
elif 'email' not in dataframe.columns:
    st.warning("The CSV file must contain an 'email' column to send emails. Please include it and try again.")

# Show the first few rows of the dataframe
st.write(dataframe.head())

# Display available variables (column names)
st.write("Available variables for interpolation in email body:")
st.write(", ".join(dataframe.columns))


# Create a text input box
subject = st.text_input("Email Subject:")
user_input = st.text_area("Email Body:", '')

# Extract variables from the user_input
variables_in_email_body = set(re.findall(r'\{(\w+)\}', user_input))

# Check if all variables in the email body are in the CSV header
allowed_to_send = False
missing_variables = variables_in_email_body - set(dataframe.columns)
if missing_variables or user_input == '':
    allowed_to_send = False
    st.error(f"The following variables in the email body are not found in the CSV header: {', '.join(missing_variables)}. Please correct them and try again.")
else:
    allowed_to_send = True
# Add a checkbox for dry run
dry_run = st.checkbox("Dry Run (emails will not be sent)", value=True)


if st.button("Send Emails"):
    if allowed_to_send:
        dry_run_messages, sent_emails = main(dataframe, subject, user_input, dry_run=dry_run)
        if dry_run:
            st.subheader("Dry Run Output:")
            for message in dry_run_messages:
                st.text(message)
        else:
            st.subheader("Sent Emails:")
            for email in sent_emails:
                st.text(email)
