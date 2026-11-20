
import ollama

def generate_email(subject, explanation, receiver_name, sender_name):

    prompt = f"""
    You are an intelligent email writing assistant.

    Project Subject: {subject}

    Project Explanation: {explanation}

    Receiver Name: {receiver_name}
    Sender Name: {sender_name}

    Instructions:
    1. Automatically decide the appropriate tone.
    2. Use professional or informal language
       depending on the situation.
    3. Start with a suitable greeting using
       the receiver's name.
    4. Explain the purpose of the email.
    5. End with a suitable closing and sender's name.
    6. Do not invent project details.
    7. Return only the email body.
    8. Do not repeat the greeting or email content.
    9. Do not include explanations about how the email was generated.
    10. Return only one complete, ready-to-send email. 
    """

    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]
