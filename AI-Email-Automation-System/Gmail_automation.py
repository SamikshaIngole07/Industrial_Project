
import smtplib
from pathlib import Path
from email.message import EmailMessage
import mimetypes


def send_mail(sender_email, app_password, receiver_email,
              subject, body, folder_path=None):

    msg = EmailMessage()

    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(body)

    # Attach Python and PDF files
    if folder_path:

        folder = Path(folder_path)

        if not folder.is_dir():
            raise NotADirectoryError(
                "Please enter a valid folder path!"
            )

        # Find only Python and PDF files, including subfolders
        project_files = (
            list(folder.rglob("*.py")) +
            list(folder.rglob("*.pdf"))
        )

        if not project_files:
            raise FileNotFoundError(
                "No Python or PDF files found in this folder!"
            )

        for project_file in project_files:

            with open(project_file, "rb") as file:
                file_data = file.read()

            # Detect file type
            mime_type, encoding = mimetypes.guess_type(project_file)

            if mime_type is None:
                mime_type = "application/octet-stream"

            maintype, subtype = mime_type.split("/", 1)

            msg.add_attachment(
                file_data,
                maintype=maintype,
                subtype=subtype,
                filename=project_file.name
            )

            print("Attached:", project_file.name)

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

    print("\nEmail sent successfully!")

