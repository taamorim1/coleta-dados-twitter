class Tweet:
    def __init__(self, tweet, data_postagem):
        self.tweet = tweet
        self.data_postagem = data_postagem

    def as_dict(self):
        return {'tweet': self.tweet, 'data_postagem': self.data_postagem}

    def TratarTweet(self, removerMencoes):
        if (removerMencoes):
            self.RemoverMencoes()
        self.RemoverNovaLinha()
        self.RemoverPontoVirgula()
        self.RemoverEspacoBranco()

    def RemoverNovaLinha(self):
        self.tweet = self.tweet.strip("\n")

    def RemoverEspacoBranco(self):
        self.tweet = self.tweet.rstrip()
        self.tweet = self.tweet.lstrip()

    def RemoverPontoVirgula(self):
        self.tweet = self.tweet.replace(";", "")

    def RemoverMencoes(self):
        qtdeMencoes = self.tweet.count("@")
        indexInicio = 0
        for i in range(0, qtdeMencoes):
            mencao = ""
            indexFim = 0
            indexInicio = self.tweet.find("@", indexInicio)
            if(indexInicio >= 0):
                indexFim = self.tweet.find(" ", indexInicio)

            if(indexInicio >= 0):
                mencao = self.tweet[indexInicio:indexFim]
            self.tweet = self.tweet.replace(mencao, "")

