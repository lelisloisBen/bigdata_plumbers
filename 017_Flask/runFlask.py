from flask import Flask, request, jsonify, json
from googlesearch import search as MYSEARCH
from google import google as MYBESTSEARCH
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

myInfos = []

for info in MYSEARCH("python", tld="co.in", num=20, stop=20, pause=2):
    myInfos.append(info)


@app.route('/')
def hello_world():
    # return str(myInfos[::-1])
    return jsonify(myInfos)

@app.route('/test', methods=['GET','POST'])
def tester():
    return jsonify({
        "register": "success",
        "msg": myInfos
    })

@app.route('/SamirSearch', methods=['POST'])
def search():
    body = request.get_json()
    
    if request.method == 'POST':
        theWord = body['word']
        wordsList = []
        for info in MYSEARCH(theWord, tld="co.in", num=20, stop=20, pause=2):
            wordsList.append(info)
        
        return jsonify({
            'register': 'success',
            'msg': wordsList
        })
        # return jsonify(wordsList)
    return "Error coming along..."

@app.route('/search', methods=['POST'])
def searchComplex():
    body = request.get_json()
    
    if request.method == 'POST':
        theWord = body['word']

        myComplexSearchList = []

        for result in MYBESTSEARCH.search(theWord, 3):
            myComplexSearchList.append({
                "name": result.name,
                "link": result.link,
                "description": result.description
            })
        
        return jsonify({
            'server': 'success',
            'msg': myComplexSearchList
        })
    return "Error coming along..."

