import tweepy as tw
class Api:
    def __init__(self, autenticacao):
        self.autenticacao = autenticacao

    def GetApi(self):
        try:
            return tw.API(self.autenticacao)
        except Exception as ex:
            raise BaseException("Falha ao obter a API - " + str(ex))