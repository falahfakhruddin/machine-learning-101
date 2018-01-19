# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:14:53 2017

@author: falah.fakhruddin
"""

from pymongo import MongoClient
import pandas as pd

class DatabaseConnector():
    def playtennis():
        client = MongoClient()
        db = client.newdb
        collection = db.playtennis.find()
        df = pd.DataFrame(list(collection))
        del df['_id']
        print(df)
        target = df['play'].values.astype(str)
        del df['play']
        df = pd.get_dummies(df)
        features = df.iloc[:, :].values
        print(df)
        return [features, target]


    def iris():
        client = MongoClient()
        db = client.newdb
        collection = db.irisdataset.find()
        df = pd.DataFrame(list(collection))
        del df['_id']
        print(df)
        features = df.iloc[:, :-1].values.astype(float)
        target = df.iloc[:, -1].values.astype(str)
        return [features, target]

    client = MongoClient()
    db = client["newdb"]
    collection = db.sample.find()
    acol = list(collection)

import datetime
post = {"author": "Mike",
      "text": "My first blog post!",
      "tags": ["mongodb", "python", "pymongo"],
      "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert_one(post).inserted_id

new_posts = [{"author": "Mike",

              "text": "Another post!",
              "tags": ["bulk", "insert"],
              "date": datetime.datetime(2009, 11, 12, 11, 14)},
             {"author": "Eliot",
              "title": "MongoDB is fun",
              "text": "and pretty easy too!",
              "date": datetime.datetime(2009, 11, 10, 10, 45)}]
nsample = db.newcol
result = nsample.insert_many(new_posts).inserted_ids
