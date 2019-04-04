import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("http://www.ekantipur.com/")


# print(response.text)


soup = BeautifulSoup(response.text, "html.parser")


# articles = soup.find_all("article")
# print(articles)
# name = soup.find("ytd-badge-supported-renderer", {"class": "style-scope ytd-video-renderer"})



divs = soup.find_all("div", {"class" : "display-news-title"})


# headers = soup.find_all("articles")
# print(divs)
# print(headers)

with open("title_links.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link"])



    for div in divs:
        div_tag = div.find("a")
        title = div_tag.get_text()
        url = (div_tag["href"])
        csv_writer.writerow([title, url])


        # print(title, url)