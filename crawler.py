from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawler.settings")
import django
django.setup()

from best_comment.models import Article


def comment_crawl():
    driver = webdriver.Chrome(
        '/Users/ton/OnedgeLee/OnedgeLeeTools/chromedriver')
    driver.implicitly_wait(3)
    driver.get(
        'https://m.sports.naver.com/kbaseball/news/index.nhn?isPhoto=N&type=popular')
    article_a = driver.find_elements_by_xpath(
        '//ul[@class="article_lst"]/li/a')
    article = list()

    for i in range(10):
        article.append({'href': article_a[i].get_attribute('href')})

    for i in range(10):
        driver.get(article[i]['href'])
        article[i]['title'] = (driver.find_element_by_class_name(
            'media_end_head_headline').text)
        upvotes = driver.find_elements_by_class_name('u_cbox_cnt_recomm')
        elupvote = upvotes[0]
        maxupvote = int(upvotes[0].text)
        for upvote in upvotes:
            if maxupvote <= int(upvote.text):
                maxupvote = int(upvote.text)
                elupvote = upvote
        bc = elupvote.find_element_by_xpath(
            './ancestor::div[@class="u_cbox_area"]')
        article[i]['writer'] = bc.find_element_by_class_name(
            'u_cbox_nick').text
        article[i]['comment'] = bc.find_element_by_class_name(
            'u_cbox_contents').text
        article[i]['upvote'] = maxupvote
        article[i]['downvote'] = int(
            bc.find_element_by_class_name('u_cbox_cnt_unrecomm').text)
    driver.close()
    return article


if __name__ == '__main__':
    articles = comment_crawl()
    for article in articles:
        Article(article_href=article['href'], article_title=article['title'], article_writer=article['writer'],
                article_comment=article['comment'], article_upvote=article['upvote'], article_downvote=article['downvote']).save()
