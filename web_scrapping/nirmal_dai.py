import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.youtube.com/results?search_query=halsey")


print(response.text)


soup = BeautifulSoup(response.text, "html.parser")


# articles = soup.find_all("article")
# print(articles)
# name = soup.find("ytd-badge-supported-renderer", {"class": "style-scope ytd-video-renderer"})



divs = soup.find_all("h3", { "class" : "title-and-badge style-scope ytd-video-renderer"})
# print(divs)

# headers = soup.find_all("articles")
# print(divs)
# print(headers)

# with open("title_links.csv", "w") as csv_file:
#     csv_writer = writer(csv_file)
#     csv_writer.writerow(["title", "link"])



for div in divs:
    div_tag = div.find("title")
    title = div_tag.get_text()
    print(title)
#     url = (div_tag["href"])
#     # csv_writer.writerow([title, url])
#     print(title, url)


        # print(title, url)