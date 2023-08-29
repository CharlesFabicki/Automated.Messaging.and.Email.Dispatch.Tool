# Birthday Email Sender

This Python script automates the process of sending birthday greetings via email to contacts whose birthdays match the current date. It reads birthday information from a CSV file and uses randomly selected letter templates to personalize the email content.

## Prerequisites

- Python 3.x
- pandas library (`pip install pandas`)
- smtplib library (built-in)
- email library (built-in)

## Setup

1. Clone or download this repository to your local machine.

2. You'll need a Gmail account and generate an [App Password](https://support.google.com/accounts/answer/185833?hl=en) for secure access. Replace the values of `my_email` and `my_password` in the script with your Gmail credentials.

3. Prepare the `birthdays_people_data.csv` file with the following columns: `name`, `email`, `day`, `month`, and `year`. Each row should contain the birthday details of a contact.

4. Create letter templates in the `letter_templates` folder (e.g., `letter_1.txt`, `letter_2.txt`, etc.) with placeholders `[NAME]` and `[YEARS]` that will be replaced with the contact's name and their age, respectively.

## Usage

1. Ensure you have the required libraries installed (pandas).

2. Run the script using the following command:

3. The script will compare the current date with the birthdays in the CSV file. If a match is found, a personalized email will be sent to the contact using a randomly selected letter template.

4. The script will also display the number of contacts for whom birthdays were processed and the number of contacts whose birthdays match the current date.

## Note

- The script currently supports Gmail's SMTP server. If you're using a different email service, you may need to modify the SMTP server and port accordingly.
- Ensure responsible and respectful handling of email sending, respecting recipients' privacy and consent.


---

Feel free to customize and enhance the script as needed. Happy birthday emailing! 🎉
