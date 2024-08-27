import os
import requests
import smtplib
from dotenv import load_dotenv
from bs4 import BeautifulSoup

# Load environment variables from .env file
load_dotenv()

# url = "https://appbrewery.github.io/instant_pot/"
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(url, headers=
{
"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Sec-Ch-Ua-Mobile": "?0",
"Sec-Ch-Ua-Platform": "\"Linux\"",
"Sec-Fetch-Site": "cross-site",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-User": "?1",
"Sec-Fetch-Dest": "document",
"Accept-Encoding": "gzip, deflate, br, zstd",
"Accept-Language":"en-US,en;q=0.9",
"priority":"u=o, i",

"Upgrade-Insecure-Requests": "1",

})
soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
# print(f"The current Instant Pot price is ${price}")

#Current price without the $ sign
price_without_dollar_sign = price[1:]
# print(f"The current Instant Pot price is {price_without_dollar_sign}")

# print the price as a floating point
price_as_float = float(price_without_dollar_sign)
print(f"The current Instant Pot price is: {price_as_float}\n")

# Send email address
# title = soup.find(id="productTitle").get_text().replace("\r\n", "").replace(" ", "")
title = soup.find(id="productTitle").get_text().replace(" ", "")
print(f"The product definition: \n {title}")


# set the price below which you would like to get a notification
BUY_PRICE = 100
if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"


    # # # Use environment variables

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login("Your Gmail Account", "Get App Password") 
        # connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject: Amazon Price Alert!\n\n{url}".encode("utf-8")
        )










# this is frudtrating








    # # Use environment variables
    # load_dotenv()
    # EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
    # EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

    # # Send email
    # with smtplib.SMTP(EMAIL_ADDRESS, port=587) as connection:
    #     connection.starttls()
    #     connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    #     connection.sendmail(
    #         from_addr=EMAIL_ADDRESS,
    #         to_addrs=EMAIL_ADDRESS,
    #         msg=f"Subject: Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
    #     )

    # print("Email sent successfully!")





    # with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    #     connection.starttls()
    #     result = connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    #     connection.sendmail(
    #         from_addr=EMAIL_ADDRESS,
    #         to_addrs=EMAIL_ADDRESS,
    #         msg=f"Subject: Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
    #     )