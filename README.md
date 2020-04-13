# twitter_app
Play with tweepy to get metrics from twitter and use flask for website

The twitter magic started with this Towardsdatascience post:[How to Scrape Tweets From Twitter](https://towardsdatascience.com/how-to-scrape-tweets-from-twitter-59287e20f0f1). 

That helps you to know a little bit about [Tweepy lib](https://github.com/tweepy/tweepy/blob/master/tweepy/api.py) and to create the account in the Twitter development Api. After that you can follow this two links [Twitter development - Getting started](https://developer.twitter.com/en/docs/basics/getting-started) and [Twitter development - Dashboard](https://developer.twitter.com/en/dashboard)

The tutorial for all the flask stuff is in this [meduim article](https://medium.com/better-programming/build-test-and-deploy-a-mini-flask-application-1d9ca6c45115)

You can find a notebook with some tweepy and some links to get data from twitter so you can show that magic in the app

Some other importants links to review are:
* Interactive Dashboards for Data Science:
[Creating an online dashboard in Python to analyse Facebook Stock Market Prices and Performance Metrics](https://towardsdatascience.com/interactive-dashboards-for-data-science-51aa038279e5)

* [Tweet analytics using NLP](https://towardsdatascience.com/tweet-analytics-using-nlp-f83b9f7f7349)

## Crear python envirnoment

First thing you need to do is create an environment:
```
virtualenv venv_twitter_app
```
After create the envirnoment, activate the envirnoment:
```
source venv_twitter_app/bin/activate
```
Then install some utils libs we are going to use in the notebooks and scripts:
```
pip install notebook
pip install tweepy
pip install matplotlib
pip install pandas
```

### Info to collect from a tweet:

* number of likes
* number of retweets
*  