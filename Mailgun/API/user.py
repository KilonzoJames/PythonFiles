import os
from dotenv import load_dotenv
import requests

load_dotenv()

def send_simple_message(to, subject, body):
    domain = os.getenv("MAILGUN_DOMAIN")
    api_key = os.getenv("MAILGUN_API_KEY")

    if not domain or not api_key:
        raise ValueError("MAILGUN_DOMAIN and MAILGUN_API_KEY environmental variables are required.")

    response = requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={"from": f"Excited User <mailgun@{domain}>",
              "to": [to],
              "subject": subject,
              "text": f"Testing some Mailgun awesomeness {body}!"},
        timeout=80
    )

    # Check the status code of the response
    if response.status_code == 200:
        print("Email sent successfully!")
    else:
        print(f"Failed to send email. Status code: {response.status_code}")
        print(response.text)

    return response

# Assuming you have set the required environmental variables (MAILGUN_DOMAIN and MAILGUN_API_KEY)
recipient_email = "hebiv70395@taobudao.com"
email_subject = "Test Email"
email_body = "This is the body of the Mailgun email. Temp Mail"

# Call the function
responsefn = send_simple_message(recipient_email, email_subject, email_body)

# Optionally, you can check the response object for additional information
print("Response status code:", responsefn.status_code)
print("Response text:", responsefn.text)
