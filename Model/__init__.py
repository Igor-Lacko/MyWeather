import swagger_client
from os import environ


#config object
config = swagger_client.Configuration()
config.api_key["key"] = environ["WEATHERAPICOMKEY"]

#api instance
api = swagger_client.APIsApi(swagger_client.ApiClient(config))




