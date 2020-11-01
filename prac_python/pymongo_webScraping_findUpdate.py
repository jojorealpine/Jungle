from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle

target_movie = db.movies.find_one({'title':'매트릭스'})
target_star = target_movie['star']

movies = list(db.movies.find({'star':target_star}))

for movie in movies:
    print(movie['title'])

# 매트리스 영화 평점 0으로 만들기
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})

print(db.movies.find({'title':'매트리스'}))