import os
import pandas as pd
import yagmail
from typing import Optional
from datetime import date
from dataclasses import dataclass

SEASON = "Fall"
ORG_NAME = "" 
MENTOR_EMAIL_SUBJECT = f"[ACTION NEEDED] - Mentee assignments {SEASON} {date.today().year}"

ASSIGNMENTS_FILEPATH = "assignments.csv"
APPLICANTS_FILEPATH = "applications.csv"

def send_email(user: str, password: str, recipient: str, subject: str, content: str, dry_run: Optional[bool] = False) -> None:
    if dry_run:
        print(f"Dry Run: {subject}\nTo: {recipient}\n{content}\n")
    else:
        yag = yagmail.SMTP(user, password)
        yag.send(
            to=recipient,
            subject=subject,
            contents=content
        )

def create_email_content(template: str, name: str, linkedin_url: str, mentoring_track: str) -> str:
    return template.format(name=name, linkedin_url=linkedin_url, mentoring_track=mentoring_track)

def main(dry_run: Optional[bool] = False) -> None:
    df = pd.read_csv(APPLICANTS_FILEPATH)
    with open('template.html', 'r') as f:
        template = f.read()

    user = os.getenv('GMAIL_USER')
    password = os.getenv('GMAIL_PASSWORD')

    for index, row in df.iterrows():
        recipient = row['Email']
        name = row['Name']
        linkedin_url = row['LinkedIn URL']
        mentoring_track = row['Mentoring track']

        content = create_email_content(template, name, linkedin_url, mentoring_track)
        send_email(user, password, recipient, MENTOR_EMAIL_SUBJECT, content, dry_run=dry_run)

if __name__ == "__main__":
    dry_run = True  # Change to False to actually send emails
    main(dry_run=dry_run)
