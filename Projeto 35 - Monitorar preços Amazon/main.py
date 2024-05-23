from bs4 import BeautifulSoup
import requests
import smtplib
import email.message
from email.message import Message

response = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
website_text = response.text

soup = BeautifulSoup(website_text, "html.parser")
item_value = soup.find_all(name="span", class_="a-price-whole")
print(item_value)
pot_price = [price.getText() for price in item_value][1]
print(pot_price)


def enviar_email():
    corpo_email = f"O valor da Panela de pressão elétrica Duo Plus 9 em 1 esta : {pot_price}\nCompre agora!"

    msg = Message()
    msg['Subject'] = "Panela em promoção"
    msg['From'] = 'XXX'
    msg['To'] = 'XXX'
    password = 'XXX'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    connection = smtplib.SMTP('smtp.gmail.com: 587')
    connection.starttls()
    # Login Credentials for sending the mail
    connection.login(msg['From'], password)
    connection.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()