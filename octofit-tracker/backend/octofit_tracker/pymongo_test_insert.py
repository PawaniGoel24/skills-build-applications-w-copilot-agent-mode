import json
from pymongo import MongoClient

with open('octofit-tracker/backend/octofit_tracker/test_data.json') as f:
    data = json.load(f)

client = MongoClient('localhost', 27017)
db = client['octofit_db']

# Insert users
db.users.insert_many(data['users'])
# Insert teams
db.teams.insert_many(data['teams'])
# Insert activities
db.activity.insert_many(data['activity'])
# Insert leaderboard
db.leaderboard.insert_many(data['leaderboard'])
# Insert workouts
db.workouts.insert_many(data['workouts'])

print('Test data inserted using PyMongo.')
