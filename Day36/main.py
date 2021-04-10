import requests, os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

ALPHAVANTAGE = "8JUVZTTB5EDPXDSO"

NEW_API = '2335cc3d01264975a6a58d67ef5a60aa'


ALPHA_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"


alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHAVANTAGE

}





response = requests.get(url=ALPHA_URL, params=alpha_parameters)

response.raise_for_status()

data = response.json()["Time Series (Daily)"]
dataList = [value for (key,value) in data.items()]



## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


yesterdayData = dataList[0]
yesterdayClosing = yesterdayData["4. close"]

dayBeforeData = dataList[1]
dayBeforeClosing = dayBeforeData["4. close"]

differeces = (float(yesterdayClosing) - float(dayBeforeClosing))

if differeces > 0:
    upOrDown = "🔺"
else:
    upOrDown = "🔻"

percentage = round((differeces / float(yesterdayClosing)) * 100)

if percentage > 5:
    news_parameters = {
        "q": STOCK_NAME,
        "apiKey": NEW_API,
        "qInTitle": COMPANY_NAME
    }
    newsResponse = requests.get(url=NEWS_URL, params=news_parameters)

    articles = newsResponse.json()["articles"]

    topNews = articles[:3]


    
    twilio_account_sid = os.getenv('TWILIO_SID')
    twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    my_number = os.getenv('MY_NUMBER')

    client = Client(twilio_account_sid, twilio_auth_token)


    formattedNews = [f"{STOCK_NAME}: {upOrDown}{percentage}%\n Headlines: {article['title']}. \nBrief: {article['description']}" for article in topNews]


    for article in formattedNews:
        message = client.messages \
                    .create(
                        body=article,
                        from_='+13472271948',
                        to=f'{my_number}'
                    )
#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

