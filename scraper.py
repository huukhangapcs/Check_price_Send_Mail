import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://tiki.vn/payback-time-ngay-doi-no-p3608625.html?src=personalization"
header = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
page = requests.get(URL, headers=header)


def check_price():
    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
    title = soup2.find(id = 'product-name').get_text().strip()
    price = soup2.find(id = 'span-price').get_text().strip()
    reverse_price = price[:-5]
    print(title)
    print(reverse_price)
    if int(reverse_price) <300:
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('huukhangwm@gmail.com','wngwtxlteknnnvht')
    subject = 'Price fell down!'
    body = 'Check https://tiki.vn/payback-time-ngay-doi-no-p3608625.html?src=personalization'
    msg = f'Subject:{subject}\n\n{body}'
    server.sendmail(
        'huukhangwm@gmail.com',
        'huukhangvn@gmail.com',
        msg
    )
    print('Senttttttttttttttttttt')
    server.quit()