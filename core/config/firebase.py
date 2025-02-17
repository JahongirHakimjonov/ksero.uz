import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("assets/resources/ksero.json")
firebase_admin.initialize_app(cred)
