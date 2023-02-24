import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api_key = "your api key"
news_api_key = "your api key"

account_sid = "your sid"
auth_token = "your auth token"

stock_params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "apikey": stock_api_key
    }

news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": news_api_key
    }

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yest_closing_price = float(data_list[0]["4. close"])
day_before_yest_closing_price = float(data_list[1]["4. close"])

price_difference = abs(yest_closing_price - day_before_yest_closing_price)
percentage_difference = (price_difference / yest_closing_price) * 100

if percentage_difference > 5:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"][:3]
    updown = None
    if yest_closing_price > day_before_yest_closing_price:
        updown = "🔺"
    else:
        updown = "🔻"
    for article in news_data:
        text_message = f'{STOCK}: {updown} {round(percentage_difference)}%\nHeadline:{article["title"]}\nBrief: {article["description"]}'

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=text_message,
            from_="your phone number",
            to="your phone number"
        )
