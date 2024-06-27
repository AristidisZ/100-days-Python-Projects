from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

section = soup.find_all(class_="titleline")
# print(section.getText())
# print(section.name)
# print(section.get("class"))
#
# print(section)
#
#
# for i in section:
#     # print(i.getText())
#     print(i.get("href"))


# articles = soup.find_all(class_='titleline')

# Find the <tr> tag with the class "athing"
tr_tag = soup.find_all('tr', class_='athing')
# print(tr_tag)

all_titles = []
all_links = []

for tag in tr_tag:
    a_tag = tag.find('span', class_='titleline').find("a")
    # print(a_tag)
    title = a_tag.getText()
    all_titles.append(title)
    # print(title)
    link = a_tag.get("href")
    all_links.append(link)

score = soup.find_all(class_="score")

all_scores = [score_tag.getText().split()[0] for score_tag in score]
print(all_titles)
print(all_links)
print(all_scores)

maximum_val = all_scores[0]
maximum_index = 0
i = 1
while i < len(all_scores):
    if all_scores[i] > maximum_val:
        maximum_val = all_scores[i]
        maximum_index = i
    i += 1
print(f"Maximum Value: {maximum_val}")
print(f"Maximum Index position: {maximum_index}")

print(all_titles[maximum_index], all_links[maximum_index], maximum_val)


#
#
# tr_tag = soup.find('tr', class_='athing')
# # Extract the ID, title, and href
# item_id = tr_tag.get("id")
# f_id = f"score_{item_id}"
# item_title = tr_tag.find('span', class_='titleline').find("a").getText()
# item_href = tr_tag.find('span', class_='titleline').find("a").get("href")
#
# score = soup.find_all(class_="score")
#
# for score_tag in score:
#     if score_tag.get("id") == f_id:
#         points = score_tag.getText()
#
#
#
# # print("ID:", item_id)
# print("Title:", item_title)
# print("Href:", item_href)
# print(points)


# print(section3.getText(), section3.get("href"))

# for articles_tag in articles:
#     tag_a = articles_tag.find("a")
#     score = soup.find('span', class_="score").get_text()
#     print(tag_a.getText(), tag_a.get("href"))
#

#
# section2 = soup.find('span', class_='titleline')
# score = soup.find('span', class_="score").get_text()
# # print(score)
# # print(section2)
# a_tag = section2.find('a')
# # print(a_tag)
# article_text = section2.get_text()
# print(article_text)
# article_link = a_tag.get('href')
# print(article_link)
# print(score)
