# Automated Email Sender

Script to send personalized emails to multiple recipients using a CSV file and a customizable email body template. It features a Streamlit-based user interface that enables the selection of CSV files, input of email subjects, and creation of **email body** content with variable interpolation. A dry-run option is also available to inspect the interpolated emails without actually sending them.

## Dependencies
- Python 3.9 or higher
- Streamlit
- Pandas
- yagmail

You can install these dependencies using the following commands:
```bash
pip install streamlit pandas yagmail
```
## Environment Variables
Make sure to set the following environment variables:
- `GMAIL_USER`: Your Gmail username
- `GMAIL_PASSWORD`: Your Gmail password or App Password if 2FA is enabled

**Note** If you don't want to set environment variables you can also hardcode the credentials in the main function on lines 54-55 within the main.py file.

## Notes
- **Running the Script:** Run the script with the command: `streamlit run main.py`
- **CSV Header Requirements:** CSV headers should be camelcase, snakecase, or any case without spaces.
- **Dry-Run Option:** Use the dry-run option in the UI to inspect the interpolated emails without actually sending them. This helps verify the email content before dispatching.
- **Data Directory:** Ensure that a directory named 'data' exists in the same directory as the script. Place your CSV files within this directory.


## Usage
1. Create a directory named 'data' in the same directory as `main.py`. (should already exist)
2. Prepare a CSV file with the recipient's information, including email addresses, and place it in the "data" directory.
3. Customize the email body with placeholders, such as `{name}`, `{mentoring_track}`, etc., matching the CSV headers. Create the email body in a separate text or HTML file. When ready, copy and paste the email body into the input box in the Streamlit app.
4. CD into the current directory and run the script with the command `streamlit run main.py`
4.1 This will open a streamlit UI in your browser usually at http://localhost:8501/
5. Select the CSV file, input the email subject and body, and click "Send Emails."
6. Use the dry-run option if you want to preview the emails before sending.


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

And would result in for the following email for the first row
```
Hello Kevin,

LinkedIn Profile: https://url1

You chose the mentoring track: Data Science
```

## Troubleshooting
- **Missing "Email" Column:** Ensure that the CSV file contains an "Email" column.
- **Invalid Headers:** Check that CSV headers do not contain invalid characters (`{`, `}`, or spaces).
- **Empty or NaN Values:** Verify that the CSV file does not contain NaN or empty values.
- **Email Sending Issues:** Make sure the Gmail credentials are correct and that "Less secure apps" are allowed in your Gmail account settings. If 2FA is enabled, use an App Password for `GMAIL_PASSWORD`.
