from flask import Flask
from newsapi import NewsApiClient
import json
from collections import Counter
import re
from flask import request

newsapi = NewsApiClient(api_key='YOUR-API-KEY')
application = Flask(__name__, static_url_path="/static")

def Home_page():
	return application.send_static_file('index.html')

application.add_url_rule('/', 'Google News', (lambda: Home_page()))

@application.route("/top_headlines")
def top_headlines():
	top_headline_news = newsapi.get_top_headlines(page_size=30)
	return json.dumps(top_headline_news)

def Remove_stopwords(articles):
	titles=[]
	for single_art in articles:
		start = single_art['title']
		new_start = re.sub(r'[^\w\s]','',start)
		titles +=new_start.split()
	stop_word=open("static/stopwords_en.txt","r")
	stop_words=stop_word.readlines()
	all_stop = []
	for word_ in stop_words:
		all_stop.append(word_.strip())
	newA = []
	for m in titles:
		if(m.lower() not in all_stop) and (m not in all_stop):
			newA.append(m)
	words=Counter(newA)
	return words.most_common(30)

@application.route("/word_cloud_title")
def word_cloud_headlines():
	word_cloud_headline_news = newsapi.get_top_headlines(page_size=30)
	word_cloud_headline_news=Remove_stopwords(word_cloud_headline_news["articles"])
	return json.dumps(word_cloud_headline_news)

@application.route("/cnn_news")
def Cnn_news():
	cnn_news = newsapi.get_top_headlines(sources='cnn',page_size=30)
	return json.dumps(cnn_news)

@application.route("/fox_news")
def Fox_news():
	fox_news = newsapi.get_top_headlines(sources='fox-news',page_size=30)
	return json.dumps(fox_news)

@application.route("/get_sources")
def Get_sources():
	category_ = request.args.get('category')
	sources=newsapi.get_sources(category=category_, country='us', language='en')
	return json.dumps(sources)

@application.route("/Search_Form")
def Search_Form():
	keyword = request.args.get('keyword')
	From = request.args.get('From')
	To = request.args.get('To')
	category = request.args.get('category')
	source = request.args.get('source')
	try:
		if source=="all":
			news = newsapi.get_everything(q=keyword,from_param=From,to=To,page_size=30,sort_by='publishedAt',language='en')
		else:
			news = newsapi.get_everything(q=keyword,sources=source,from_param=From,to=To,page_size=30,sort_by='publishedAt',language='en')	
		news=news['articles']
		news_1=[]
		for i in range(0,len(news)):
			if news[i]['author']!=None and news[i]['description']!=None and news[i]['url']!=None and news[i]['urlToImage']!=None and news[i]['title']!=None and news[i]['publishedAt']!=None and news[i]['source']['name']!=None and news[i]['author']!="" and news[i]['description']!="" and news[i]['url']!="" and news[i]['urlToImage']!="" and news[i]['title']!="" and news[i]['publishedAt']!="" and news[i]['source']['name']!="":
				news_1.append(news[i])
	except Exception as e:
		news_1={}
		news_1["error"]=e.exception["message"]
	return json.dumps(news_1)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    #application.debug = True
    application.run()