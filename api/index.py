import os
import random

from flask import Flask, g, request
from flask_cors import CORS

app = Flask(__name__, static_folder=None)
CORS(app)


def read_expansions(name):
    expansions_txt = os.path.join(os.path.dirname(app.root_path), name)
    with open(expansions_txt, "r") as f:
        return list(filter(None, f.read().splitlines()))


CHOICES = {
    "en": read_expansions("expansions.txt"),
    "zh": read_expansions("expansions-zh.txt"),
}


@app.before_request
def pick_choices():
    lang = request.args.get("lang", "en")
    g.choices = CHOICES[lang]


@app.get("/api/random")
def random_name():
    return {"code": 0, "message": "success", "data": random.choice(g.choices)}


@app.get("/api/sample")
def random_sample():
    k = min(int(request.args.get("k", 7)), len(g.choices))
    return {"code": 0, "message": "success", "data": random.sample(g.choices, k)}
