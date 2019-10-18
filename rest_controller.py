from __init__ import api

from api import ApiTestResource, ApiTestResourcePost

api.add_resource(ApiTestResource, '/ohya/api_test?id={id}&account_name={account_name}&speak={speak}', '/ohya/api_test')
api.add_resource(ApiTestResourcePost, '/ohya/api_test_post?id={id}&account_name={account_name}&sport={sport}', '/ohya/api_test_post')
