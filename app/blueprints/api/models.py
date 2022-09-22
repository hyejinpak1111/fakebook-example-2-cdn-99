from app import app
from flask import render_template

# @app.route('/')
# def home():
#     return 'Hello World'

# @app.route('/about')
# def about():
#     return 'About page'

# @app.route('/contact')
# def contact():
#     return ('Contact page')

# @app.route('/blog')
# def blog():
#     return ('Blog page')

# @app.route('/shop')
# def shop():
#     return ('Shop page')

# Routes that return JSON
user_data = { # Mock database data
    'lucasl': {
        'user_id' : 0,
        'name': 'Lucas',
        'favoriteColor': 'blue',
        'posts':[
            {
                'id': 0,
                'title': 'This is post 1',
                'body': 'This is the text for the post'
            },
             {
                'id': 1,
                'title': 'This is post 2',
                'body': 'This is the text for the post'
            },
             {
                'id': 2,
                'title': 'This is post 3',
                'body': 'This is the text for the post'
            },
        ]
    },
    'christophert':{
        'user_id':1,
        'name': 'Christopher',
        'favoriteColor':'orange',
        'posts':[
             {
                'id': 3,
                'title': 'This is post 4',
                'body': 'This is the text for the post'
            }, {
                'id': 4,
                'title': 'This is post 5',
                'body': 'This is the text for the post'
            }, {
                'id': 5,
                'title': 'This is post 6',
                'body': 'This is the text for the post'
            },
        ]
    },
    'joelc':{
        'user_id':2,
        'name':'Joel',
        'favoriteColor':'red',
        'posts': [
            {
                'id': 6,
                'title': 'This is post 7',
                'body': 'This is the text for the post'
            },
            {
                'id': 7,
                'title': 'This is post 8',
                'body': 'This is the text for the post'
            },
            {
                'id': 8,
                'title': 'This is post 9',
                'body': 'This is the text for the post'
            }
        ]
    }
}