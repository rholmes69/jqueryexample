# -*- coding: utf-8 -*-
"""
    jQuery Example
    ~~~~~~~~~~~~~~

    A simple application that shows how Flask and jQuery get along.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from flask import Flask, jsonify, render_template, request, url_for
import pyodbc, unittest

import os

import sys
import pymongo
import json
import collections

from bson import json_util

app = Flask(__name__)

def get_db_connection():
    """Renders the home page, with a list of all polls."""
    cnx_str = 'DRIVER={SQL Server};SERVER=ustorwromeiq1;PORT=1433;DATABASE=dbrome;UID=romeuser;PWD=romeuser;TDS_Version=7.3;'
    conn = pyodbc.connect(cnx_str, autocommit=True)
    #cursor = conn.cursor()
    return conn

def get_rome_bpc_extract(dealId):
      rows = []
      try:
          conn = get_db_connection()
          cursor = conn.cursor()
          #print('Inserted 500 rows, IDENTITY VALUE: %s' % (row[0],))
          sql = 'exec romeuser.spS_SMT_OUTLOOKSOFT_EXTRACT_DEAL_EVENTS %s,-1, 1, -1,-1,NULL,NULL, 1,1,-1' % (dealId)
            #          x = 'apple'
            #y = 'lemon'
            #z = "The items in the basket are %s and %s" % (x,y)

          cursor.execute(sql)
        #   for row in cursor:
        #     print row

          cursor.nextset()

          for row in cursor:
              rows.append(row)
            #   print row
          
          return rows
      except(e):
          print e
          raise e
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

###############################################################################
# pseudocode:
        
    #create a new routine for extracting the tbd forecast budget events data into a filelist
    #add header record
    #dynamically name the file with the appropriate mont year format
    #copy the file to specific location designated in the config file 
    #send email to the appropriate team members

    # sql          : exec romeuser.spS_SMT_OUTLOOKSOFT_EXTRACT_DEAL_EVENTS_TDB -1,-1, 7, -1,-1,'1/1/2016','12/31/2016', 1, 5,-1  --HOB ROME MUSIC TDB FORECAST 
    # header record: OracleID,ROMEID,Company,Department,EventDate,Promoter,Talent,Venue,Data_Type,Account,Value,Deal_Status,DATASRC,RPTCURRENCY,TYPEOFEVENT


###############################################################################


@app.route('/romebpcetl/<int:deal_id>')
def get_rome_bpc_extract2(deal_id):
    response = {}
    model = {}
  
   
    try:
        extract_data = get_rome_bpc_extract(deal_id)
        #print (extract_data)
        
        # Convert query to row arrays
 
        # rowarray_list = []
        # for row in extract_data:
        #     t = (row[0],row[1])
        #     rowarray_list.append(t)
        
        # j = json.dumps(rowarray_list)
        # rowarrays_file = 'student_rowarrays.js'
        # f = open(rowarrays_file,'w')
        # print >> f, j
        
        # Convert query to objects of key-value pairs
        # OracleID	ROMEID	Company	Department	EventDate	(No column name)	Talent	Venue	Data_Type	Account	Value	Deal_Status	DATASRC	RptCurrency	TYPEOFEVENT
        # NULL	270270	C3161	D00038	2016.JAN16	STestagain	T14008	V03590	FCST	A40223.00	68014.00	Confirmed	ROME	LC	Rental O/O
        objects_list = []
        for row in extract_data:
            d = collections.OrderedDict()
            d['OracleID'] = row[0]
            d['ROMEID'] = row[1]
            d['Company'] = row[2]
            d['Department'] = row[3]
            d['EventDate'] = row[4]
            d['Talent'] = row[5]
            d['Data_Type'] = row[6]
            d['Account	Value'] = row[7]
            d['Deal_Status'] = row[8]
            # d['DATASRC'] = row[9]
            # d['RptCurrency'] = row[10]
            # d['TYPEOFEVENT'] = row[11]
            objects_list.append(d)
        
        print (objects_list)
        print (len(objects_list))
        j = json.dumps(objects_list)
        objects_file = 'student_objects.js'
        f = open(objects_file,'w')
        print >> f, j
        
        
        # json_docs = []
        # for doc in extract_data:
        #     print (doc[5])
            #print (json.dumps(doc , default=json_util.default)
            # print(json_doc)
            # json_docs.append(json_doc)
        
        model['data'] = objects_list
        response['request'] = model
        
        return jsonify(response)
    except os.error as err:
        sys.stderr.write("Can't list %s: %s\n" % (json_docs, err))
        #self.addstats("<dir>", "unlistable", 1)
        response['error'] = "Can't list %s: %s\n" % (json_docs, err)
        return jsonify(response)

 
 
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
