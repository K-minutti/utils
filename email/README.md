# Automated Email Sender

Script to send personalized emails to multiple recipients using a CSV file and a email body template. It features a Streamlit-based user interface that enables the selection of CSV files, input of email subject, and creation of **email body** content with variable interpolation. A dry-run option is also available to inspect the interpolated emails without actually sending them.

## Dependencies
- Python 3.9 or higher

#### Step 1: Install Dependencies
```bash
pip install streamlit pandas yagmail
```

#### Step 2: Environment Variables
Set the following environment variables:
- `GMAIL_USER`: Your Gmail username
- `GMAIL_PASSWORD`: Your Gmail password or App Password if 2FA is enabled

**Note** If you prefer, you can hardcode these credentials in the main() function within the main.py file instead of setting environment variables.


## Getting Started
#### Step 1: Prepare Your Data
1. Create a directory named `data` in the same directory as `main.py`.
2. Prepare a CSV file with the recipient's information, including email addresses, and place it in the "data" directory.

#### Step 2: Create an Email Body
Create an email body with placeholders, such as `{name}`, `{mentoring_track}`, etc., matching the CSV headers. Create the email body in a separate text or HTML file. When ready, copy and paste the email body into the input box in the Streamlit app.

#### Step 3: Run the Script
Navigate to the script's directory and run the following command:
```
streamlit run main.py
```
This will open a streamlit UI in your browser usually at http://localhost:8501/ open the link a browser

#### Step 4: Use the UI
1. Select your CSV file using the UI.
2. Input your email subject in the text box.
3. Paste your previously created email body into the large text box.
4. Check "Dry Run" if you want to preview the emails without sending them.
5. Click "Send Emails".

## Example
Given the following CSV at the path data/data.csv
| email            | mentor  | linkedIn_url  | mentoring_track | time_commitment |
|------------------|---------|---------------|-----------------|-----------------|
| min70@gmail.com    | Kevin   | https://url1  | Data Science            | 1-2             |
| min60@columbia.edu  | KevinCU | https://url2  | Grad School            | 5               |
| min70@gmail.com    | Other   | none          | Compilers            | 2-4             |

A valid email body would be - (if you include a variable that does not exist in the csv headers you will be warned)
```
Hello {mentor},

LinkedIn Profile: {linkedIn_url}

You chose the mentoring track: {mentoring_track}
```

And would generate the following email body for the first row
```
Hello Kevin,

LinkedIn Profile: https://url1

You chose the mentoring track: Data Science
```

## Notes
- **CSV Header Requirements:** CSV headers should be camelcase, snakecase, or any case without spaces.
- **Dry-Run Option:** Use the dry-run option in the UI to inspect the interpolated emails without actually sending them. This helps verify the email content before dispatching.
- **Data Directory:** Ensure that a directory named 'data' exists in the same directory as the script. Place your CSV files within this directory.

## Troubleshooting
- **Missing "email" Column:** Ensure that the CSV file contains an "email" column.
- **Invalid Headers:** Check that CSV headers do not contain invalid characters (`{`, `}`, or spaces).
- **Empty or NaN Values:** Verify that the CSV file does not contain NaN or empty values.
- **Email Sending Issues:** Make sure the Gmail credentials are correct and that "Less secure apps" are allowed in your Gmail account settings. If 2FA is enabled, use an App Password for `GMAIL_PASSWORD`.
