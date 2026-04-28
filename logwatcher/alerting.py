import smtplib
from email.message import EmailMessage

def send_alert_email(ip):
    """
    Envoie une alerte mail lorsqu'une IP dépasse le seuil
    """
    sender_email = 
    receiver_email = 
    app_password = 

    msg = EmailMessage()
    msg["Subject"] = f"Alerte : activité suspecte détectée depuis {ip}"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(f"L'IP {ip} a dépassé le seuil autorisé de tentatives de connexion.")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)
        print("[MAIL] Alerte envoyée avec succès.")
