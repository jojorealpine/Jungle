from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
from pymongo import MongoClient

client = MongoClient('mongodb://test:test@13.124.220.19', 27017)
db = client.dbjungle

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    result = list(db.posts.find({}, {'_id': 0}))
    # 2. posts라는 키 값으로 영화정보 내려주기
    return jsonify({'result': 'success', 'posts': result})


## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
    # 1. 클라이언트로부터 데이터를 받기
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']
    # global cardID
    cardID=1
    cardID = cardID+1

    article = {'url': url_receive, 'comment': comment_receive, 'cardID': cardID}
    # 3. mongoDB에 데이터 넣기
    db.posts.insert_one(article)
    return jsonify({'result': 'success', 'msg': 'POST 연결되었습니다!'})

## API 역할을 하는 부분
@app.route('/delete', methods=['POST'])
def deleting():
    # 1. 클라이언트로부터 데이터를 받기
    # id_receive = request.form['cardId']
    title_receive = request.form['cardTitle']
    content_receive = request.form['cardContent']

    db.posts.delete_one({'url': title_receive, 'comment' : content_receive})
    return jsonify({'result': 'success', 'msg': '삭제 성공했습니다!'})

## API 역할을 하는 부분
@app.route('/update', methods=['POST'])
def updating():
    # 1. 클라이언트로부터 데이터를 받기
    # id_receive = request.form['cardId']
    btitle_receive = request.form['beforeCardTitle']
    bcontent_receive = request.form['beforeCardContent']
    atitle_receive = request.form['afterCardTitle']
    acontent_receive = request.form['afterCardContent']
    print("btitle_receive : "+btitle_receive)
    print("atitle_receive : "+atitle_receive)
    print("acontent_receive : "+acontent_receive)

    filter1 = {'url': btitle_receive}
    filter2 = {'url': atitle_receive}

    # Values to be updated.
    newvalue1 = {"$set": {'url': atitle_receive}}
    newvalue2 = {"$set": {'comment': acontent_receive}}

    # Using update_one() method for single
    # updation.
    db.posts.update_one(filter1, newvalue1)
    db.posts.update_one(filter2, newvalue2)
    return jsonify({'result': 'success', 'msg': '수정 성공했습니다!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
