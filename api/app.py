from flask import g, request, Flask
import random
import os

app = Flask(__name__)
expansions_txt = os.path.join(os.path.dirname(app.root_path), "expansions.txt")


@app.get("/api/random")
def random_name():
    return {"code": 0, "message": "success", "data": random.choice(g.choices)}


@app.get("/api/sample")
def random_sample():
    k = min(request.args.get("k", 7), len(g.choices))
    return {"code": 0, "message": "success", "data": random.sample(g.choices, k)}


@app.before_first_request
def load_expansions():
    with open(expansions_txt, "r") as f:
        g.choices = list(filter(None, f.read().splitlines()))
