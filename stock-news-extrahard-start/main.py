import requests
import datetime
import  smtplib

# # Get today's date
# today = datetime.date.today()
# print("Today is: ", today)
#
# # Yesterday date
# m_t = today - datetime.timedelta(days=1)
# print("Yesterday was: ", m_t)
#
# # Yesterday date
# m_y = today - datetime.timedelta(days=2)
# print("day before Yesterday was: ", m_y)
#
#
# STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
# api_key = "98K2IG317Y5DDDON"
#

# parameters = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK,
#     "apikey": api_key
# }
#
# response = requests.get("https://www.alphavantage.co/query", params=parameters)
# response.raise_for_status()
#
#
# data = response.json()
# print(data)
#
# today_stock = data["Time Series (Daily)"][f"{m_t}"]["4. close"]
# print(today_stock)
# yesterday_stock = data["Time Series (Daily)"][f"{m_y}"]["4. close"]
# print(yesterday_stock)


def get_articles():
    news_api = "40e81c9fd16e43aeb57e958b00ef9c7b"

    params = {
        "q": COMPANY_NAME,
        "apiKey": news_api

    }
    response = requests.get("https://newsapi.org/v2/everything", params=params)
    response.raise_for_status()

    data = response.json()
    # print(data)
    articles = data["articles"][:3]
    return articles


test_yes = 215.88

test_before_yes = 200.42

percentage_diff = (((test_yes - test_before_yes) * 100) / test_yes)
# print(percentage_diff, "%")

if percentage_diff > 5 or percentage_diff - 5:
    articles = get_articles()
    if percentage_diff > 0:
        emoji = "⬆️"
    else:
        emoji = "⬇️"  # Down arrow emoji

    for i in range(0, 3):
        articles_to_send = articles[i]
        print(type(emoji))
        # formatted_article = {f"Headline:{articles_to_send['title']} "}
        # print(formatted_article)
        title = articles_to_send["title"].replace("’", "")
        url = articles_to_send["url"]
        description = articles_to_send["description"].replace("[…]", "...").replace("’", "").replace("“", '"').replace("”", '"').encode('utf-8', 'ignore')
        print(description)
        # description = articles_to_send["description"].replace("[…]", "...")
        formatted_title = f"{emoji} {title}"
        my_email = "haricatest@gmail.com"
        password = "wyty qkaa xcym fvkt"
        #
        print(description)
        with smtplib.SMTP("smtp.gmail.com", 587) as connect:
            connect.starttls()  # make connection secure
            connect.login(user=my_email, password=password)
            # print("login success")
            connect.sendmail(from_addr=my_email,
                             to_addrs="aristidiszotka@gmail.com",
                             msg=f"Subject:{title}\n\n{description}\n{url}")
            print("email send")


# articles1 = articles[0]
# articles2 = articles[1]
# articles3 = articles[2]
#
# print(articles1)
# print(articles2)
# print(articles3)


# # STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

