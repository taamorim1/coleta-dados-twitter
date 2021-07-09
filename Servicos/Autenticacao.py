import tweepy as tw

class Autenticacao:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret):
        self.api_key = api_key
        self.api_secret_key = api_secret_key
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.auth = {}

    def Autenticar(self):
        try:
            self.auth = tw.OAuthHandler(self.api_key, self.api_secret_key)
            self.auth.set_access_token(self.access_token, self.access_token_secret)
        except Exception as e:
            raise BaseException("Falha ao ao autenticar - " + str(e))

    def GetAutenticacao(self):
        if(self.auth == None):
            raise ValueError("Autenticação não realizada")
        return self.auth

