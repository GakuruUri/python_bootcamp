import os
import smtplib
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup


# Load environment variables
load_dotenv()

# Practice
# url = "https://appbrewery.github.io/instant_pot/"
# Live Site
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"


# ====================== Add Headers to the Request ===========================

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}



# A minimal header:

# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }


# Adding header to the request
response = requests.get(url, headers=header)


soup = BeautifulSoup(response.content, "html.parser")
# Check that you are hetting the actual amazon image
print(soup.prettify())

# find the html that contains the price
price = soup.find(class_="a-offscreen").get_text()

# remove the dollar sign from the price using split
price_without_currency = price.split("$")[1]

# convert to floating point number 
price_as_float = float(price_without_currency)
print(price_as_float)

# Get the product title
title = soup.find(id="productTitle").get_text().strip()
print(title)


# Set the price below which you would like to get a notification
BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    # Send email
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject: Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )










# Alternative send email function

    # sender_email = os.getenv("SENDER_EMAIL")
    # receiver_email = os.getenv("RECEIVER_EMAIL")
    # password = os.getenv("EMAIL_PASSWORD")

    # server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    # server.login(sender_email, password)

    # subject = "Price Alert!"
    # body = message

    # msg = f"Subject: {subject}\n\n{body}"

    # server.sendmail(sender_email, receiver_email, msg)

    # print("Email sent successfully!")

    # server.quit()