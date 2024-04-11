import datetime as dt

from data import update_file
from news import get_news
from send_msg import send_message

json_data = update_file().get('Time Series (Daily)')

date_today = dt.datetime.now().date()
while True:  # finds the latest updated day from teh api
    if json_data.get(date_today.strftime("%Y-%m-%d")) is None:
        date_today = (date_today - dt.timedelta(1))
    else:
        break
date_yesterday = (date_today - dt.timedelta(1))

date_today = date_today.strftime("%Y-%m-%d")
date_yesterday = date_yesterday.strftime("%Y-%m-%d")

close = [float(json_data.get(date_today).get("4. close")), float(json_data.get(date_yesterday).get("4. close"))]
print(close)


def find_percentage(x: float, y: float) -> float:
    return ((x - y) / x) * 100


percentage_difference = find_percentage(close[0], close[1])

if abs(percentage_difference) > 5:
    news_list = get_news(3)
    news_list = [{"title": iter_dict.get("title"), "brief": iter_dict.get("description")} for iter_dict in news_list]
    send_message(news_list, "TSLA", percentage_difference, abs(percentage_difference) / percentage_difference + 1)
