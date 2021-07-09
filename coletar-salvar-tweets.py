from Servicos import Autenticacao
from Servicos import Api
from Servicos import Busca
import pandas as pd

try:
    with open("Chaves.txt", "r") as tokens:
        api_key = tokens.readline().strip("\n")
        api_secret_key = tokens.readline().strip("\n")
        access_token = tokens.readline().strip("\n")
        access_token_secret = tokens.readline().strip("\n")

    obj_autenticacao = Autenticacao.Autenticacao(api_key, api_secret_key, access_token, access_token_secret)
    obj_autenticacao.Autenticar()
    auth = obj_autenticacao.GetAutenticacao()
    obj_api = Api.Api(auth)
    api = obj_api.GetApi()
    obj_busca = Busca.Busca(api)

    termos_busca = ["bolsonaro", "vittar"]
    tweets = []

    for termo in termos_busca:
        print("Termo:" + termo)
        t = obj_busca.Buscar(termo + "-filter:retweets", 100, True)
        tweets = tweets + t

    df = pd.DataFrame([x.as_dict() for x in tweets])
    df.to_csv(sep = ";", path_or_buf="dados-coletados-twitter.csv", index=False, encoding="utf_8")
    #print(df.head())

except Exception as e:
    print("Ocorreu um erro: " + str(e))