from flask import Flask,abort,redirect,request
from shortlib.shortner import Shortner,MemoryRepo,RedisCacheRepository,PostgresRepo
import dotenv
import os

dotenv.load_dotenv()

app = Flask(__name__)
shortner = Shortner(PostgresRepo(f"dbname=tae user=postgres password={os.environ['DB_PASSWORD']}")
                     , "http://127.0.0.1:5000")

@app.route("/shorten" , methods=["POST"])
def shorten():
    original = request.json["url"]
    new = shortner.shorten(original)
    return {"new":new , "full_url":f"{shortner.base}/{new}"}

@app.route("/<url>")
def get(url):
    return redirect(shortner.get(url)[0])