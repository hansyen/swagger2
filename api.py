
from flask_restful import Resource, reqparse
from urllib import parse
from flask import request, jsonify
from flask_restful_swagger_2 import swagger, Schema

class GetModel(Schema):
    type = 'object'
    properties = {
        'id': {
            'type': 'string'
        },
        'account_name': {
            'type': 'string',
            'min_length': 1,
            'max_length': 30
        },
        'speak': {
            'type': 'string',
            'min_length': 1,
            'max_length': 100
        }
    }
    required = ['account_name', 'id', 'speak']

class PostModel(Schema):
    type = 'object'
    properties = {
        'id': {
            'type': 'string'
        },
        'account_name': {
            'type': 'string',
            'min_length': 1,
            'max_length': 30
        },
        'sport': {
            'type': 'string',
            'min_length': 1,
            'max_length': 60
        }
    }
    required = ['account_name', 'id', 'sport']

class ApiTestResource(Resource):
    @swagger.doc({
        'tags': ['User say something'],
        'description': 'Return what user say.',
        'parameters': [
            {
                'name': 'id',
                'description': 'User number',
                'in': 'path',
                'type': 'string'
            },
            {
                'name': 'account_name',
                'description': 'User name',
                'in': 'path',
                'type': 'string'
            },
            {
                'name': 'speak',
                'description': 'Say something',
                'in': 'path',
                'type': 'string'
            }
        ],
        'responses': {
            '200': {
                'description': 'Success',
                'schema': GetModel,
            },
            '400': {
                'description': 'Failed. Misunderstood Request.',
            },
            '404': {
                'description': 'Failed. Book request not found.',
            }
        }
    })
    def get(self):
        payload = dict(parse.parse_qsl(parse.urlsplit(request.url).query))
        try:
            number = payload['id']
            name = payload['account_name']
            say = payload['speak']
            result = {
                name:  say,
                'say': 'swagger'
            }

            result_use = {
                'id':number,
                'test': '1',
                'check_info': 'spiderman',
            }
            result_use["test"] = result

            return jsonify(result_use)
        except Exception as e:
            print('Error : ', e)
            return jsonify({'Warning': 'I can see dead people !'})

class ApiTestResourcePost(Resource):
    @swagger.doc({
        'tags': ['User play something'],
        'description': 'Return what user say.',
        'parameters': [
            {
                'name': 'id',
                'description': 'User number',
                'in': 'path',
                'type': 'string'
            },
            {
                'name': 'account_name',
                'description': 'User name',
                'in': 'path',
                'type': 'string'
            },
            {
                'name': 'sport',
                'description': 'play something',
                'in': 'path',
                'type': 'string'
            }
        ],
        'responses': {
            '200': {
                'description': 'Success',
                'schema': PostModel,
            },
            '400': {
                'description': 'Failed. Misunderstood Request.',
            },
            '404': {
                'description': 'Failed. Book request not found.',
            }
        }
    })
    def post(self):
        payload = dict(parse.parse_qsl(parse.urlsplit(request.url).query))
        try:
            number = payload['id']
            name = payload['account_name']
            play = payload['sport']
            result = {
                name: play,
                'swagger': 'gogogo!'
            }
            result_use = {
                'id': number,
                'test': '1',
                'check_info': 'superman',
            }
            result_use["test"] = result

            return jsonify(result_use)
        except Exception as e:
            print('Error : ', e)
            return jsonify({'Warning': 'I can see dead people !'})





