from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    title_found = search_news({"title": {"$regex": title, "$options": "i"}})
    result_list = []
    for title in title_found:
        result_list.append((title["title"], title["url"]))
    return result_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
