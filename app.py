from shortlib.shortner import Shortner,MemoryRepo,RedisCacheRepository,PostgresRepo
from ADs import Stage
from flask import Flask,abort,redirect,request
import numpy as np
import psycopg2
import dotenv
import os

dotenv.load_dotenv()

conn = psycopg2.connect(f"dbname=tae user=postgres password={os.environ['DB_PASSWORD']}")
stage = Stage(conn=conn)
shortner = Shortner(PostgresRepo(conn=conn), "http://127.0.0.1:5000")

app = Flask(__name__)

@app.route("/add" , methods=["POST"])
def shorten():
    original = request.json["url"]
    owner_ID = int(request.json["owner"])
    owner_channel = request.json["channel"]
    lifetime = 3 * 24 * 60 * 60 * 1000
    new = shortner.shorten(original , owner_ID , owner_channel , lifetime)
    return {"new":new , "full_url":f"{shortner.base}/{new}"}

@app.route("/<url>")
def get(url):
    return redirect(shortner.get(url)[0])

# this route is temporarily. Stage functionality will be transfer to bot.py later
@app.route("/temp" , methods=["POST"])
def add():
    stage.create(request.json["url"] , request.json["eval"])
    return {"ok":True}

# this route is temporarily. Stage functionality will be transfer to bot.py later
@app.route("/recommend")
def score():
    stage_urls , result = stage.score(np.array([0 , 10] + [0] * 7))

    return stage_urls[result.argmax()][0]
