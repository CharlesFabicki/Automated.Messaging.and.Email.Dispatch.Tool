# Auto Sending Motivation Code to Your Friends

This Python script sends a daily motivational quote to a designated email address. It retrieves motivational quotes from a text file, selects a random quote, and emails it to the specified recipient using Gmail's SMTP server.

## Getting Started

### Prerequisites

- You need to have Python installed on your system.
- Make sure you have a Gmail account to send emails from.
- Create a text file named `quotes for motivation script.txt` in the same directory as your script. Add motivational quotes, one per line, to this file.

### Installation

1. Clone this repository or copy the provided script to your local machine.

2. Open the script `auto_send_motivation.py` in a text editor.

3. Replace the following placeholders with your own credentials:
   - `my_email`: Your Gmail email address
   - `my_password`: Your Gmail account's app password (generate one for this script)

4. Customize the recipient's email address in the `to_addrs` field within the `connection.sendmail` function.

5. Run the script using the command:

## Note

- The script will run daily and send a motivational quote to the specified email address.
- To generate a disposable email address for testing, you can use [temp-mail.org](https://temp-mail.org/en/) or similar services.

## Disclaimer

This script is intended for educational and personal use. Be cautious when handling email credentials and personal information. Make sure to comply with the terms of use of the email service provider. The author is not responsible for any misuse or unintended consequences of using this script.


