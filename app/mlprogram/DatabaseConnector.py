# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:14:53 2017

@author: falah.fakhruddin
"""

from pymongo import MongoClient
import pandas as pd
import datetime
from .. import db



class DatabaseConnector():
    def get_collection(self, datafile='irisdataset', database='newdb'):  # get dataframe
        client = MongoClient()
        db = client[database]
        collection = db[datafile].find()
        df = pd.DataFrame(list(collection))
        del df['_id']
        return df

    def export_collection(self, jsonfile, collection, database='newdb'):  # upload json file into database
        client = MongoClient()
        db = client[database]
        upload = db[collection]
        return upload.insert_many(jsonfile).inserted_ids

    def check_collection(self, database="newdb"):
        client = MongoClient()
        db = client[database]
        collection = db.collection_names(include_system_collections=False)
        return collection

class SaveModel(db.Document):
    dataset = db.StringField(max_length=100, required=True)
    algorithm = db.StringField(max_length=100, required=True)
    preprocessing = db.DictField(max_length=50, required=True)
    model = db.ListField(max_length=50, required=True)
    create = db.DateTimeField(default=datetime.datetime.now)
    dummies = db.BooleanField(required=True)

class SavePrepocessing(db.Document):
    dataset = db.StringField(max_length=100, required=True)
    preprocessing = db.DictField(max_length=50, required=True)
    create = db.DateTimeField(default=datetime.datetime.now)
"""        
logout = {
    "topic" : ,
    "mapper" : {
        "-$type" : "&$logout",
        "-$api_key" : "#SIFTSCIENCE.apikey",
        "-$user_id" : "$.result.result.username",
    },
    "is_added" : False,
    "time_stamp" : datetime.datetime.utcnow(),
    "is_active" : False
}
"""
"""
class User(EmbeddedDocument):
    last_name = StringField(max_length=50)

class Poster(Document):
    title = StringField(max_length=120, required=True)
    author = EmbeddedDocumentField(User)
    tags = ListField(StringField(max_length=30))
    meta = {'allow_inheritance': True}

class TextPoster(Poster):
    content = StringField()

class ImagePoster(Poster):
    image_path = StringField()

class LinkPoster(Poster):
    link_url = StringField()
""
if __name__ == "__main__":
    ross = User(email='jm@example.com')
    ross.first_name = 'jose'
    ross.last_name = 'mourinho'
    ross.save()

    john = User(email='john@example.com')
    john.first_name = 'John'
    john.last_name = 'Lawley'
    john.save()

    query = Q(tags='mongodb')
    query_result = query.to_query(Poster)
    print(query_result)

    num_posts = Poster.objects(tags='mongodb')
    print(num_posts)

    post1 = TextPoster(title='MongoEngine very weird', author=john)
    post1.content = 'Took a look at MongoEngine today.'
    post1.tags = ['mongodb', 'mongoal', 'machine-learning']
    post1.save()

    # extract value from
    connect('MLdb')
    temp = SaveModel.objects(dataset="homeprice_FeatureSelection_DataCleaning2")
    for data in temp:
        prepo_dict =data.preprocessing
    value = prepo_dict["DataCleaning2"]

    value2 = [data.preprocessing["DataCleaning2"] for data in temp]
    model2 = [data.model for data in SaveModel.objects(algorithm="LogisticRegression")]

    post2 = LinkPoster(title='MongoEngine Documentation', author=ross)
    post2.link_url = 'http://docs.mongoengine.com/'
    post2.tags = ['mongoengine']
    post2.save()

    for piss in Poster.objects:
        print(piss.author)

    for post in Poster.objects:
        print(post.title)
        print('=' * len(post.title))

        if isinstance(post, TextPoster):
            print(post.content)

        if isinstance(post, LinkPoster):
            print('Link: {}'.format(post.link_url))

    post = Poster.objects(tags='mongodb')
    print(post.title)
"""
# import pickle
#
# binary = pickle.dumps(nn)
# export_file = {"Model": binary}
# binary_list = list()
# binary_list.append(binary)

# client = MongoClient()
# db = client['rawdb']
# collection = db['playtennis'].find()
# df = pd.DataFrame(list(collection))
# del df['_id']
