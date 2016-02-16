# -*- coding: utf-8 -*-
"""
    jQuery Example
    ~~~~~~~~~~~~~~

    A simple application that shows how Flask and jQuery get along.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from flask import Flask, jsonify, render_template, request, url_for
import os

import sys
import pymongo
import json
from bson import json_util

app = Flask(__name__)


### Create seed data

SEED_DATA = [
    {
        'decade': '1970s',
        'artist': 'Debby Boone',
        'song': 'You Light Up My Life',
        'weeksAtOne': 10
    },
    {
        'decade': '1980s',
        'artist': 'Olivia Newton-John',
        'song': 'Physical',
        'weeksAtOne': 10
    },
    {
        'decade': '1990s',
        'artist': 'Mariah Carey',
        'song': 'One Sweet Day',
        'weeksAtOne': 16
    }
]

@app.route('/song/<int:song_id>')
def get_song(song_id):
    response = {}
    songs = []
    model = {}
    
    client = pymongo.MongoClient()
    db = client['db']
    songs = db['songs']
    
    # Note that the insert method can take either an array or a single dict.

    #songs.insert(SEED_DATA)
    # Finally we run a query which returns all the hits that spent 10 or
    # more weeks at number 1.

    cursor = songs.find({'weeksAtOne': {'$gte': 10}}).sort('decade', 1)

    # for doc in cursor:
    #     songs.append ( doc['song'])
 
    
    json_docs = []
    for doc in cursor:
        json_doc = json.dumps(doc['song'], default=json_util.default)
        json_docs.append(json_doc)
        
   # client.close()
    try:
       
        model['songlist'] = json_docs
      
        response['request'] = model
        client.close()
        return jsonify(response)
    except os.error as err:
        sys.stderr.write("Can't list %s: %s\n" % (dir, err))
        #self.addstats("<dir>", "unlistable", 1)
        response['error'] = "Can't list %s: %s\n" % (dir, err)
        return jsonify(response)


@app.route('/customer/<int:customer_id>')
def show_customer2(customer_id):
    response = {}
    model = {}
    dir = os.getcwd()
   
    try:
        names = os.listdir(dir)
        # print (names)
        model['filelist'] = names
        model['newfilelist'] = names
        response['newData'] = model
        
        return jsonify(response)
    except os.error as err:
        sys.stderr.write("Can't list %s: %s\n" % (dir, err))
        #self.addstats("<dir>", "unlistable", 1)
        response['error'] = "Can't list %s: %s\n" % (dir, err)
        return jsonify(response)
 
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username
    
@app.route('/post/<int:customer_id>')
def show_customer(customer_id):
    response = {}
    links = ['www.gooogle.com','www.mci.com']
    
    #for collection in Domain.keys():
    links.append('www.beyonce.com')
    response['sites'] = links
    return jsonify(response)
    
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

# @app.route('/_subtract_numbers')
# def add_numbers():
#     """Subtract two numbers server side, ridiculous but well..."""
#     a = request.args.get('a', 0, type=int)
#     b = request.args.get('b', 0, type=int)
#     return jsonify(result=a - b)

# @app.route('/_multiply_numbers')
# def add_numbers():
#     """Subtract two numbers server side, ridiculous but well..."""
#     a = request.args.get('a', 0, type=int)
#     b = request.args.get('b', 0, type=int)
#     return jsonify(result=a * b)
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index2')
def index2():
    return render_template('index2.html')
    
if __name__ == '__main__':
    app.run(debug=True)
