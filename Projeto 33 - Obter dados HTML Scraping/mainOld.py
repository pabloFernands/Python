from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get("https://news.ycombinator.com/")
website_text = response.text

soup = BeautifulSoup(website_text, "html.parser")

articles = soup.find_all("span", class_="titleline")
articles_texts = []
articles_links = []

for article_tag in articles:
    find_href = article_tag.find("a")
    # print(find_href)
    text = find_href.getText()
    articles_texts.append(text)
    link = find_href.get("href")
    articles_links.append(link)

# print(articles_texts)
# print(articles_links)

articleUpvote = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]
#print(articleUpvote)

largest_number = max(articleUpvote)
largest_index = articleUpvote.index(largest_number)
print(articles_texts[largest_index], articles_links[largest_index])

