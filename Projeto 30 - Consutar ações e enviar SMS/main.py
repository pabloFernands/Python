import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_KEY= ""
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

STOCK_API = "https://www.alphavantage.co/query"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "apikey": API_KEY,
}

response_stock = requests.get(STOCK_API, params=stock_params)
response_stock_json = response_stock.json()["Time Series (Daily)"]
print(response_stock_json)

#2. - Get the day before yesterday's closing stock price

contador = 0

stock_data_list = []
for day, close in response_stock_json["Time Series (Daily)"].items():
    day_close = close["4. close"]
    stock_data_list.append(day_close)
    contador += 1

    if contador >= 2:
        break

#print(stock_data_list)

#3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

stock_data_float = [float(valor) for valor in stock_data_list]
stock_difference = abs(stock_data_float[0] - stock_data_float[1])
#print(stock_difference)

#4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

close_yesterday = stock_data_float[0] * 0.05
close_before_yest = stock_data_float[1] * 0.05
if stock_difference > close_yesterday:
    print("Porcetagem maior que 5%.")
else:
    print("Porcentagem menor que 5%.")

#5. - If TODO4 percentage is greater than 5 then print("Get News").

NEWSAPI = "https://newsapi.org/v2/everything"
newsapi_key = ""

news_params = {
    "q": COMPANY_NAME,
    "sortBy": "relevancy",
    "pageSize": 3,
    "apiKey": newsapi_key,
}

news_response = requests.get(NEWSAPI, params=news_params)
news_response = news_response.json()

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

news_article = [article for article in news_response["articles"]]
news_list = []
#print(news_article[0]["title"])

for news in news_article:
    news_title = news["title"]
    news_description = news["description"]
    news_list.append(news_title)
    news_list.append(news_description)

#print(news_list)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#8. - Create a new list of the first 3 article's headline and description using list comprehension.

#9. - Send each article as a separate message via Twilio.

count_sms = 0

account_sid = ""
auth_token = os.getenv("owm_auth_token")

client = Client(account_sid, auth_token)
while count_sms < 3:
    news_sms = {
        "Title": news_list[0 + count_sms],
        "Description": news_list[1 + count_sms],
    }

    message = client.messages \
        .create(
        body = f"\nTitulo: {news_sms['Title']}\nDescricao: {news_sms['Description']}",
        from_ = "+12563339753",
        to = "+5521995981080"
        )
    count_sms += 1
    #print(news_sms)
    print(message.body)

#Optional Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

