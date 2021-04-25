from flask import Flask , jsonify
from flask_pymongo import PyMongo
import pymongo

class connect():
    def make_connection(self):
        try:
            
            client = pymongo.MongoClient("mongodb+srv://paviPOST:DBSOFTWAREDEVTEST@cluster0.knwvi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
            db = client.test #connection to the database
            
        except:
            return jsonify({"message" : "Error......while connecting to the DataBase"})

        return db



