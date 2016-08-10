trakt_api_version = 2
client_id = "b62243ebed0a24da0d44377a0ac1d4cc51a0de77a8be36a0bcbf67ba2142026d"

# Translations
# url_translation = "/movies/" + id_imdb + "/translations/" + language
# language = "en"

c = http.client.HTTPConnection("api.trakt.tv", None)
headers = { "Content-type": "application/json",
            "trakt-api-version" : trakt_api_version ,
            "trakt-api-key" : client_id}
