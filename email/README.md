# Email Automation with Python

This Python script sends personalized email messages to a list of recipients. It uses the `yagmail` library to send emails from a Gmail account and `pandas` to read recipient information from a CSV file.
Before running the script, replace 'data.csv' with your csv or excel file name, 'template.html' with your html template file and replace your-email@gmail.com and your-password with your actual Gmail email and password. You might need to allow less secure apps to access your Gmail account, which you can do in your account settings under "Security". Be aware that this could make your account less secure.
Remember to replace 'data.csv' with your csv or excel file name and 'template.html' with your html template file in the Python script.

This script allows you to do a dry run by setting the dry_run variable at the bottom of the script to True. In this mode, the script prints the emails that would be sent but doesn't actually send them. To actually send the emails, you would set dry_run to False. This should make it easy to test the script and verify the email content before actually sending the emails.

In your html template file, use {name}, {linkedin_url}, and {mentoring_track} to indicate where the 'Name', 'LinkedIn URL', and 'Mentoring track' should be placed in the email.

TODO: 
Update such that the only inputs are the following 
Subject
CVS 
Text - with {variables}



## Libraries Used

- `pandas`: Used to read and manage data from CSV files.
- `yagmail`: Simplifies sending emails through a Gmail account.

## How to Run the Script

1. Install the necessary Python libraries with pip:

    ```
    pip install pandas yagmail
    ```

2. Set the Gmail username and password as environment variables:

    ```
    export GMAIL_USER=your-email@gmail.com 
    export GMAIL_PASSWORD=your-password
    # or if you're on windows
    set GMAIL_USER=your-email@gmail.com 
    set GMAIL_PASSWORD=your-password
    ```

    Replace `your-email@gmail.com` and `your-password` with your actual Gmail email and password.

3. Update the 'data.csv' filename if your csv or excel file has a different name or is in a different directory.

4. Update 'template.html' with the name of your HTML template file, if it's different.

5. To do a dry run without actually sending emails, make sure the `dry_run` variable in the script is set to `True`. To actually send emails, set it to `False`.

6. Run the script:

    ```
    python email_auto.py
    ```

## Troubleshooting

1. If you encounter issues with logging in to your Gmail account, make sure you have enabled "Less secure app access" in your Google account settings. Note that this may pose a security risk and you might want to consider using a dedicated Gmail account for sending these emails.

2. If you get an error about a missing library, make sure you have installed all the necessary libraries with pip.

3. If you get an error about a missing file, make sure the CSV file and HTML template file are in the same directory as the script, or update the file paths in the script to match their actual locations.

4. If you get an error about the Gmail username or password not being set, make sure you have set them as environment variables as described in the "How to Run the Script" section.