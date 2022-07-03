from django.shortcuts import render
import pyrebase


config = {
    "apiKey": "AIzaSyDh3yo3N73gphUTESELvEebBWt9iR0-VLE",
    "authDomain": "shangkai-5444b.firebaseapp.com",
    "projectId": "shangkai-5444b",
    "storageBucket": "shangkai-5444b.appspot.com",
    "messagingSenderId": "335717800456",
    "appId": "1:335717800456:web:7d5c758e6d143f99ae4fbd",
    "measurementId": "G-PYKG8H9HSW",
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def signIn(request):
    return render(request, "welcome.html")
