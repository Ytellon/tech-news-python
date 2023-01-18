from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    title_found = search_news({"title": {"$regex": title, "$options": "i"}})
    result_list = []
    for title in title_found:
        result_list.append((title["title"], title["url"]))
    return result_list


# Requisito 7
def search_by_date(date):
    try:
        date_format = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        date_found = search_news(
            {"timestamp": {"$regex": date_format, "$options": "i"}}
        )
        result_list = []
        for news in date_found:
            result_list.append((news["title"], news["url"]))
        return result_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    tag_found = search_news({"tags": {"$regex": tag, "$options": "i"}})
    result_list = []
    for news in tag_found:
        result_list.append((news["title"], news["url"]))
    return result_list


# Requisito 9
def search_by_category(category):
    category_found = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    result_list = []
    for news in category_found:
        result_list.append((news["title"], news["url"]))
    return result_list
