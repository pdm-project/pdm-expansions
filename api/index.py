import os
import random

from flask import Flask, request

app = Flask(__name__, static_folder=None)
expansions_txt = os.path.join(os.path.dirname(app.root_path), "expansions.txt")
with open(expansions_txt, "r") as f:
    CHOICES = list(filter(None, f.read().splitlines()))


@app.get("/api/random")
def random_name():
    return {"code": 0, "message": "success", "data": random.choice(CHOICES)}


@app.get("/api/sample")
def random_sample():
    k = min(int(request.args.get("k", 7)), len(CHOICES))
    return {"code": 0, "message": "success", "data": random.sample(CHOICES, k)}
