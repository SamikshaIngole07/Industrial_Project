
import getpass

from AI_mail_generator import generate_email
from Gmail_automation import send_mail

# Gmail details
sender_email = input("Enter your Gmail address: ")
app_password = getpass.getpass("Enter your Gmail App Password: ")

# Receiver details
receiver_email = input("Enter receiver email: ")
receiver_name = input("Enter receiver name: ")

# Sender name
sender_name = input("Enter your name: ")

# Project details
subject = input("Enter project subject: ")
instructions = input("What do you want to communicate? : ")

# Project folder path
file_path = input("Enter project folder path: ")

# Generate email
email = generate_email(
    subject,
    instructions,
    receiver_name,
    sender_name
)

# Display email
print("\n========== GENERATED EMAIL ==========")
print("To:", receiver_email)
print("Subject:", subject)
print("\n", email)
print("=====================================")

# Approval
choice = input("\nDo you want to send this email? (yes/no): ")

if choice.lower() == "yes":

    send_mail(
        sender_email,
        app_password,
        receiver_email,
        subject,
        email,
        file_path
    )

else:
    print("Email sending cancelled.")

