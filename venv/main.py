from google.cloud import firestore

from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

#db = firestore.client()
database = firestore.client()
data = {'username': 'deelaka', 'password': '123456'}

#database.collection('users').documents('s325689').set(data)







