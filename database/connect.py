from elasticsearch import Elasticsearch


CLOUD_URL = 'http://localhost:9200'
USER_NAME = 'elastic'
PASSWORD = 'mvsDWY3I'


client = Elasticsearch(CLOUD_URL, basic_auth=(USER_NAME, PASSWORD))

print(client.info())