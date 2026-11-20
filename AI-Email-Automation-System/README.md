# AI-Powered Email Automation System

## 1. Project Description

The **AI-Powered Email Automation System** is a Python-based application that automatically generates and sends emails using Artificial Intelligence.

It uses the **Ollama LLM (Llama 3.2:1B)** to generate professional or informal email content based on the user's input. The system sends emails through Gmail SMTP and allows users to attach Python (`.py`) and PDF (`.pdf`) files.

The main objective of this project is to reduce manual effort in writing emails and automate the email-sending process.

## 2. Features

- **AI-Based Email Generation:** Automatically generates email content using Ollama.
- **Automatic Tone Selection:** Selects a suitable formal or informal tone based on the given instructions.
- **User Input:** Accepts receiver details, sender details, subject, and communication instructions.
- **Email Preview:** Displays the generated email before sending.
- **User Confirmation:** Sends the email only after user approval.
- **File Attachments:** Supports attaching Python (`.py`) and PDF (`.pdf`) files.
- **Gmail Integration:** Sends emails using Gmail SMTP.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Ollama | Runs the local AI language model |
| Llama 3.2:1B | Generates email content |
| Gmail SMTP | Sends emails |
| VS Code | Development environment |

### Python Libraries

- `ollama` – Connects Python with the Ollama language model.
- `smtplib` – Sends emails using SMTP.
- `email` – Creates email messages and attachments.
- `pathlib` – Handles file and folder paths.
- `mimetypes` – Identifies attachment file types.

## 4. Project Structure

```text
AI-Email-Automation-System/
│
├── email_generator.py   # Generates email content using Ollama
├── email_sender.py      # Sends emails and attaches files
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── .gitignore           # Files excluded from GitHub
```

## 5. Installation

### Step 1: Clone the Repository

```bash
git clone <repository-url>
```

Navigate to the project folder:

```bash
cd Industrial-Projects/AI-Email-Automation-System
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Install Ollama

Download and install Ollama from:

https://ollama.com/

### Step 4: Download the AI Model

Open the terminal and run:

```bash
ollama pull llama3.2:1b
```

Make sure Ollama is running before executing the project.

### Step 5: Configure Gmail

To send emails using Gmail SMTP:

1. Enable 2-Step Verification in your Google Account.
2. Generate a Google App Password.
3. Configure the sender's Gmail address and App Password securely using environment variables.

**Important:** Never upload your Gmail App Password or other credentials to GitHub.

## 6. How to Run

Run the main Python file:

```bash
python main.py
```

Follow the instructions displayed in the terminal.

### Working Process

1. Enter the receiver's email address.
2. Enter the receiver's name and sender's name.
3. Enter the email subject.
4. Provide communication instructions.
5. Enter the project folder path containing files to attach.
6. The Ollama AI model generates the email content.
7. Review the generated email.
8. Confirm whether you want to send the email.
9. The system sends the email through Gmail SMTP.

## 7. Future Improvements

- Develop a graphical user interface (GUI).
- Support multiple email providers.
- Add support for more attachment file formats.
- Maintain email sending history.
- Add email scheduling functionality.
- Improve AI-generated email quality.

## 8. Author

**Samiksha Ingole**

BE – Artificial Intelligence and Machine Learning

AISSMS College of Engineering

---

*Developed using Python, Ollama, and Gmail SMTP.*
