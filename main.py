import requests_oauthlib

CLIENT_ID = "ea81a30065b6e7c823568717327b2a1d7f6272ede48f0a3a528246c72d356c55"
CLIENT_SECRET = "fa625b412448b5d0e974f0c3db65e1a256d32c4a388ab6cd42065b7d43f78970"

authorization_base_url = "https://simkl.com/oauth/authorize"
token_url = "https://api.simkl.com/oauth/token"
redirect_uri = "https://jletallec.github.io/simkl"

session = requests_oauthlib.OAuth2Session(
    client_id=CLIENT_ID,
    redirect_uri=redirect_uri,
    scope=['repo', 'user'],
)

authorization_url, state = session.authorization_url(authorization_base_url)
print(authorization_url)

redirect_response = input('Paste the full redirect URL here:')
token = session.fetch_token(token_url, authorization_response=redirect_response, client_secret=CLIENT_SECRET)