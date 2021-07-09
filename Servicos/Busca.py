import tweepy as tw
from Modelos import Tweet

class Busca:
    def __init__(self, twApi):
        self.api = twApi

    def Buscar(self, query, qtdeItens, removerMencoes):
        try:
            tweets = tw.Cursor(self.api.search, q = query, tweet_mode="extended").items(qtdeItens)
            lTweets = []
            for t in tweets:
                modelo = Tweet.Tweet(t.full_text, t.created_at)
                modelo.TratarTweet(removerMencoes)
                lTweets.append(modelo)
            return lTweets
        except Exception as e:
            raise BaseException("Falha ao buscar tweets - " + str(e))
